# coding: utf-8

# (C) Copyright IBM Corp. 2021.
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

# IBM OpenAPI SDK Code Generator Version: 3.29.1-b338fb38-20210313-010605
 
"""
Filters
"""

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

class FiltersV1(BaseService):
    """The Filters V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.cis.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'filters'

    @classmethod
    def new_instance(cls,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'FiltersV1':
        """
        Return a new client for the Filters service using the specified parameters
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
        Construct a new client for the Filters service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/master/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)


    #########################
    # Filters
    #########################


    def list_all_filters(self,
        x_auth_user_token: str,
        crn: str,
        zone_identifier: str,
        **kwargs
    ) -> DetailedResponse:
        """
        List all filters for a zone.

        List all filters for a zone.

        :param str x_auth_user_token: IBM Cloud user IAM token.
        :param str crn: Full url-encoded cloud resource name (CRN) of resource
               instance.
        :param str zone_identifier: Zone identifier of the zone for which filters
               are listed.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListFiltersResp` object
        """

        if x_auth_user_token is None:
            raise ValueError('x_auth_user_token must be provided')
        if crn is None:
            raise ValueError('crn must be provided')
        if zone_identifier is None:
            raise ValueError('zone_identifier must be provided')
        headers = {
            'X-Auth-User-Token': x_auth_user_token
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_all_filters')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(crn, zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/filters'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def create_filter(self,
        x_auth_user_token: str,
        crn: str,
        zone_identifier: str,
        *,
        filter_input: List['FilterInput'] = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create filters for a zone.

        Create new filters for a given zone under a service instance.

        :param str x_auth_user_token: IBM Cloud user IAM token.
        :param str crn: Full url-encoded cloud resource name (CRN) of resource
               instance.
        :param str zone_identifier: Zone identifier of the zone for which filters
               are created.
        :param List[FilterInput] filter_input: (optional) Json objects which are
               used to create filters.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `FiltersResp` object
        """

        if x_auth_user_token is None:
            raise ValueError('x_auth_user_token must be provided')
        if crn is None:
            raise ValueError('crn must be provided')
        if zone_identifier is None:
            raise ValueError('zone_identifier must be provided')
        if filter_input is not None:
            filter_input = [convert_model(x) for x in filter_input]
        headers = {
            'X-Auth-User-Token': x_auth_user_token
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_filter')
        headers.update(sdk_headers)

        data = json.dumps(filter_input)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(crn, zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/filters'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def update_filters(self,
        x_auth_user_token: str,
        crn: str,
        zone_identifier: str,
        *,
        filter_update_input: List['FilterUpdateInput'] = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update filters.

        Update existing filters for a given zone under a given service instance.

        :param str x_auth_user_token: IBM Cloud user IAM token.
        :param str crn: Full crn of the service instance.
        :param str zone_identifier: Zone identifier (zone id).
        :param List[FilterUpdateInput] filter_update_input: (optional)
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `FiltersResp` object
        """

        if x_auth_user_token is None:
            raise ValueError('x_auth_user_token must be provided')
        if crn is None:
            raise ValueError('crn must be provided')
        if zone_identifier is None:
            raise ValueError('zone_identifier must be provided')
        if filter_update_input is not None:
            filter_update_input = [convert_model(x) for x in filter_update_input]
        headers = {
            'X-Auth-User-Token': x_auth_user_token
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_filters')
        headers.update(sdk_headers)

        data = json.dumps(filter_update_input)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(crn, zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/filters'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def delete_filters(self,
        x_auth_user_token: str,
        crn: str,
        zone_identifier: str,
        id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete filters.

        Delete filters by filter ids.

        :param str x_auth_user_token: IBM Cloud user IAM token.
        :param str crn: Full crn of the service instance.
        :param str zone_identifier: Identifier of zone whose filters are to be
               deleted.
        :param str id: ids of filters which will be deleted.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DeleteFiltersResp` object
        """

        if x_auth_user_token is None:
            raise ValueError('x_auth_user_token must be provided')
        if crn is None:
            raise ValueError('crn must be provided')
        if zone_identifier is None:
            raise ValueError('zone_identifier must be provided')
        if id is None:
            raise ValueError('id must be provided')
        headers = {
            'X-Auth-User-Token': x_auth_user_token
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_filters')
        headers.update(sdk_headers)

        params = {
            'id': id
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(crn, zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/filters'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def delete_filter(self,
        x_auth_user_token: str,
        crn: str,
        zone_identifier: str,
        filter_identifier: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete a filter.

        Delete a filter given its id.

        :param str x_auth_user_token: IBM Cloud user IAM token.
        :param str crn: Full crn of the service instance.
        :param str zone_identifier: Identifier of zone whose filter is to be
               deleted.
        :param str filter_identifier: Identifier of the filter to be deleted.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DeleteFilterResp` object
        """

        if x_auth_user_token is None:
            raise ValueError('x_auth_user_token must be provided')
        if crn is None:
            raise ValueError('crn must be provided')
        if zone_identifier is None:
            raise ValueError('zone_identifier must be provided')
        if filter_identifier is None:
            raise ValueError('filter_identifier must be provided')
        headers = {
            'X-Auth-User-Token': x_auth_user_token
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_filter')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier', 'filter_identifier']
        path_param_values = self.encode_path_vars(crn, zone_identifier, filter_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/filters/{filter_identifier}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_filter(self,
        x_auth_user_token: str,
        crn: str,
        zone_identifier: str,
        filter_identifier: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get filter details by id.

        Get the details of a filter for a given zone under a given service instance.

        :param str x_auth_user_token: IBM Cloud user IAM token.
        :param str crn: Full crn of the service instance.
        :param str zone_identifier: Zone identifier (zone id).
        :param str filter_identifier: Identifier of filter for the given zone.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `FilterResp` object
        """

        if x_auth_user_token is None:
            raise ValueError('x_auth_user_token must be provided')
        if crn is None:
            raise ValueError('crn must be provided')
        if zone_identifier is None:
            raise ValueError('zone_identifier must be provided')
        if filter_identifier is None:
            raise ValueError('filter_identifier must be provided')
        headers = {
            'X-Auth-User-Token': x_auth_user_token
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_filter')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier', 'filter_identifier']
        path_param_values = self.encode_path_vars(crn, zone_identifier, filter_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/filters/{filter_identifier}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_filter(self,
        x_auth_user_token: str,
        crn: str,
        zone_identifier: str,
        filter_identifier: str,
        *,
        id: str = None,
        expression: str = None,
        description: str = None,
        paused: bool = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update a filter.

        Update an existing filter for a given zone under a given service instance.

        :param str x_auth_user_token: IBM Cloud user IAM token.
        :param str crn: Full crn of the service instance.
        :param str zone_identifier: Zone identifier (zone id).
        :param str filter_identifier: Identifier of filter.
        :param str id: (optional) Identifier of the filter.
        :param str expression: (optional) A filter expression.
        :param str description: (optional) To briefly describe the filter.
        :param bool paused: (optional) Indicates if the filter is active.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `FilterResp` object
        """

        if x_auth_user_token is None:
            raise ValueError('x_auth_user_token must be provided')
        if crn is None:
            raise ValueError('crn must be provided')
        if zone_identifier is None:
            raise ValueError('zone_identifier must be provided')
        if filter_identifier is None:
            raise ValueError('filter_identifier must be provided')
        headers = {
            'X-Auth-User-Token': x_auth_user_token
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_filter')
        headers.update(sdk_headers)

        data = {
            'id': id,
            'expression': expression,
            'description': description,
            'paused': paused
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier', 'filter_identifier']
        path_param_values = self.encode_path_vars(crn, zone_identifier, filter_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/filters/{filter_identifier}'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


##############################################################################
# Models
##############################################################################


class DeleteFilterRespResult():
    """
    Container for response information.

    :attr str id: Identifier of the filter.
    """

    def __init__(self,
                 id: str) -> None:
        """
        Initialize a DeleteFilterRespResult object.

        :param str id: Identifier of the filter.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteFilterRespResult':
        """Initialize a DeleteFilterRespResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in DeleteFilterRespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteFilterRespResult object from a json dictionary."""
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
        """Return a `str` version of this DeleteFilterRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteFilterRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteFilterRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DeleteFiltersRespResultItem():
    """
    DeleteFiltersRespResultItem.

    :attr str id: Identifier of the filter.
    """

    def __init__(self,
                 id: str) -> None:
        """
        Initialize a DeleteFiltersRespResultItem object.

        :param str id: Identifier of the filter.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteFiltersRespResultItem':
        """Initialize a DeleteFiltersRespResultItem object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in DeleteFiltersRespResultItem JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteFiltersRespResultItem object from a json dictionary."""
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
        """Return a `str` version of this DeleteFiltersRespResultItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteFiltersRespResultItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteFiltersRespResultItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ListFiltersRespResultInfo():
    """
    Statistics of results.

    :attr int page: Page number.
    :attr int per_page: Number of results per page.
    :attr int count: Number of results.
    :attr int total_count: Total number of results.
    """

    def __init__(self,
                 page: int,
                 per_page: int,
                 count: int,
                 total_count: int) -> None:
        """
        Initialize a ListFiltersRespResultInfo object.

        :param int page: Page number.
        :param int per_page: Number of results per page.
        :param int count: Number of results.
        :param int total_count: Total number of results.
        """
        self.page = page
        self.per_page = per_page
        self.count = count
        self.total_count = total_count

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListFiltersRespResultInfo':
        """Initialize a ListFiltersRespResultInfo object from a json dictionary."""
        args = {}
        if 'page' in _dict:
            args['page'] = _dict.get('page')
        else:
            raise ValueError('Required property \'page\' not present in ListFiltersRespResultInfo JSON')
        if 'per_page' in _dict:
            args['per_page'] = _dict.get('per_page')
        else:
            raise ValueError('Required property \'per_page\' not present in ListFiltersRespResultInfo JSON')
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        else:
            raise ValueError('Required property \'count\' not present in ListFiltersRespResultInfo JSON')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        else:
            raise ValueError('Required property \'total_count\' not present in ListFiltersRespResultInfo JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListFiltersRespResultInfo object from a json dictionary."""
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
        """Return a `str` version of this ListFiltersRespResultInfo object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListFiltersRespResultInfo') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListFiltersRespResultInfo') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DeleteFilterResp():
    """
    DeleteFilterResp.

    :attr bool success: Operation success flag.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    :attr DeleteFilterRespResult result: Container for response information.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: 'DeleteFilterRespResult') -> None:
        """
        Initialize a DeleteFilterResp object.

        :param bool success: Operation success flag.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        :param DeleteFilterRespResult result: Container for response information.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteFilterResp':
        """Initialize a DeleteFilterResp object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in DeleteFilterResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in DeleteFilterResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in DeleteFilterResp JSON')
        if 'result' in _dict:
            args['result'] = DeleteFilterRespResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in DeleteFilterResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteFilterResp object from a json dictionary."""
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
        """Return a `str` version of this DeleteFilterResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteFilterResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteFilterResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DeleteFiltersResp():
    """
    DeleteFiltersResp.

    :attr bool success: Operation success flag.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    :attr List[DeleteFiltersRespResultItem] result: Container for response
          information.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: List['DeleteFiltersRespResultItem']) -> None:
        """
        Initialize a DeleteFiltersResp object.

        :param bool success: Operation success flag.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        :param List[DeleteFiltersRespResultItem] result: Container for response
               information.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteFiltersResp':
        """Initialize a DeleteFiltersResp object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in DeleteFiltersResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in DeleteFiltersResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in DeleteFiltersResp JSON')
        if 'result' in _dict:
            args['result'] = [DeleteFiltersRespResultItem.from_dict(x) for x in _dict.get('result')]
        else:
            raise ValueError('Required property \'result\' not present in DeleteFiltersResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteFiltersResp object from a json dictionary."""
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
        """Return a `str` version of this DeleteFiltersResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteFiltersResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteFiltersResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class FilterInput():
    """
    Json objects which are used to create filters.

    :attr str expression: A filter expression.
    :attr bool paused: (optional) Indicates if the filter is active.
    :attr str description: (optional) To briefly describe the filter, omitted from
          object if empty.
    """

    def __init__(self,
                 expression: str,
                 *,
                 paused: bool = None,
                 description: str = None) -> None:
        """
        Initialize a FilterInput object.

        :param str expression: A filter expression.
        :param bool paused: (optional) Indicates if the filter is active.
        :param str description: (optional) To briefly describe the filter, omitted
               from object if empty.
        """
        self.expression = expression
        self.paused = paused
        self.description = description

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'FilterInput':
        """Initialize a FilterInput object from a json dictionary."""
        args = {}
        if 'expression' in _dict:
            args['expression'] = _dict.get('expression')
        else:
            raise ValueError('Required property \'expression\' not present in FilterInput JSON')
        if 'paused' in _dict:
            args['paused'] = _dict.get('paused')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FilterInput object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'expression') and self.expression is not None:
            _dict['expression'] = self.expression
        if hasattr(self, 'paused') and self.paused is not None:
            _dict['paused'] = self.paused
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this FilterInput object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'FilterInput') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'FilterInput') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class FilterObject():
    """
    FilterObject.

    :attr str id: Identifier of the filter.
    :attr bool paused: Indicates if the filter is active.
    :attr str description: To briefly describe the filter, omitted from object if
          empty.
    :attr str expression: A filter expression.
    :attr str created_on: The creation date-time of the filter.
    :attr str modified_on: The modification date-time of the filter.
    """

    def __init__(self,
                 id: str,
                 paused: bool,
                 description: str,
                 expression: str,
                 created_on: str,
                 modified_on: str) -> None:
        """
        Initialize a FilterObject object.

        :param str id: Identifier of the filter.
        :param bool paused: Indicates if the filter is active.
        :param str description: To briefly describe the filter, omitted from object
               if empty.
        :param str expression: A filter expression.
        :param str created_on: The creation date-time of the filter.
        :param str modified_on: The modification date-time of the filter.
        """
        self.id = id
        self.paused = paused
        self.description = description
        self.expression = expression
        self.created_on = created_on
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'FilterObject':
        """Initialize a FilterObject object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in FilterObject JSON')
        if 'paused' in _dict:
            args['paused'] = _dict.get('paused')
        else:
            raise ValueError('Required property \'paused\' not present in FilterObject JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        else:
            raise ValueError('Required property \'description\' not present in FilterObject JSON')
        if 'expression' in _dict:
            args['expression'] = _dict.get('expression')
        else:
            raise ValueError('Required property \'expression\' not present in FilterObject JSON')
        if 'created_on' in _dict:
            args['created_on'] = _dict.get('created_on')
        else:
            raise ValueError('Required property \'created_on\' not present in FilterObject JSON')
        if 'modified_on' in _dict:
            args['modified_on'] = _dict.get('modified_on')
        else:
            raise ValueError('Required property \'modified_on\' not present in FilterObject JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FilterObject object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'paused') and self.paused is not None:
            _dict['paused'] = self.paused
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'expression') and self.expression is not None:
            _dict['expression'] = self.expression
        if hasattr(self, 'created_on') and self.created_on is not None:
            _dict['created_on'] = self.created_on
        if hasattr(self, 'modified_on') and self.modified_on is not None:
            _dict['modified_on'] = self.modified_on
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this FilterObject object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'FilterObject') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'FilterObject') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class FilterResp():
    """
    FilterResp.

    :attr bool success: Operation success flag.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    :attr FilterObject result:
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: 'FilterObject') -> None:
        """
        Initialize a FilterResp object.

        :param bool success: Operation success flag.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        :param FilterObject result:
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'FilterResp':
        """Initialize a FilterResp object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in FilterResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in FilterResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in FilterResp JSON')
        if 'result' in _dict:
            args['result'] = FilterObject.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in FilterResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FilterResp object from a json dictionary."""
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
        """Return a `str` version of this FilterResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'FilterResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'FilterResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class FilterUpdateInput():
    """
    FilterUpdateInput.

    :attr str id: Identifier of the filter.
    :attr str expression: A filter expression.
    :attr str description: (optional) To briefly describe the filter.
    :attr bool paused: (optional) Indicates if the filter is active.
    """

    def __init__(self,
                 id: str,
                 expression: str,
                 *,
                 description: str = None,
                 paused: bool = None) -> None:
        """
        Initialize a FilterUpdateInput object.

        :param str id: Identifier of the filter.
        :param str expression: A filter expression.
        :param str description: (optional) To briefly describe the filter.
        :param bool paused: (optional) Indicates if the filter is active.
        """
        self.id = id
        self.expression = expression
        self.description = description
        self.paused = paused

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'FilterUpdateInput':
        """Initialize a FilterUpdateInput object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in FilterUpdateInput JSON')
        if 'expression' in _dict:
            args['expression'] = _dict.get('expression')
        else:
            raise ValueError('Required property \'expression\' not present in FilterUpdateInput JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'paused' in _dict:
            args['paused'] = _dict.get('paused')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FilterUpdateInput object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'expression') and self.expression is not None:
            _dict['expression'] = self.expression
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'paused') and self.paused is not None:
            _dict['paused'] = self.paused
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this FilterUpdateInput object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'FilterUpdateInput') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'FilterUpdateInput') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class FiltersResp():
    """
    FiltersResp.

    :attr bool success: Operation success flag.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    :attr List[FilterObject] result: Container for response information.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: List['FilterObject']) -> None:
        """
        Initialize a FiltersResp object.

        :param bool success: Operation success flag.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        :param List[FilterObject] result: Container for response information.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'FiltersResp':
        """Initialize a FiltersResp object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in FiltersResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in FiltersResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in FiltersResp JSON')
        if 'result' in _dict:
            args['result'] = [FilterObject.from_dict(x) for x in _dict.get('result')]
        else:
            raise ValueError('Required property \'result\' not present in FiltersResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FiltersResp object from a json dictionary."""
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
        """Return a `str` version of this FiltersResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'FiltersResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'FiltersResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ListFiltersResp():
    """
    ListFiltersResp.

    :attr bool success: Operation success flag.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    :attr List[FilterObject] result: Container for response information.
    :attr ListFiltersRespResultInfo result_info: Statistics of results.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: List['FilterObject'],
                 result_info: 'ListFiltersRespResultInfo') -> None:
        """
        Initialize a ListFiltersResp object.

        :param bool success: Operation success flag.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        :param List[FilterObject] result: Container for response information.
        :param ListFiltersRespResultInfo result_info: Statistics of results.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result
        self.result_info = result_info

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListFiltersResp':
        """Initialize a ListFiltersResp object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in ListFiltersResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in ListFiltersResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in ListFiltersResp JSON')
        if 'result' in _dict:
            args['result'] = [FilterObject.from_dict(x) for x in _dict.get('result')]
        else:
            raise ValueError('Required property \'result\' not present in ListFiltersResp JSON')
        if 'result_info' in _dict:
            args['result_info'] = ListFiltersRespResultInfo.from_dict(_dict.get('result_info'))
        else:
            raise ValueError('Required property \'result_info\' not present in ListFiltersResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListFiltersResp object from a json dictionary."""
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
        """Return a `str` version of this ListFiltersResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListFiltersResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListFiltersResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
