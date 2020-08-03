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
CIS Zones
"""

from typing import Dict, List
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################

class ZonesV1(BaseService):
    """The Zones V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.cis.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'zones'

    @classmethod
    def new_instance(cls,
                     crn: str,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'ZonesV1':
        """
        Return a new client for the Zones service using the specified parameters
               and external configuration.

        :param str crn: Full url-encoded CRN of the service instance.
        """
        if crn is None:
            raise ValueError('crn must be provided')

        authenticator = get_authenticator_from_environment(service_name)
        service = cls(
            crn,
            authenticator
            )
        service.configure_service(service_name)
        return service

    def __init__(self,
                 crn: str,
                 authenticator: Authenticator = None,
                ) -> None:
        """
        Construct a new client for the Zones service.

        :param str crn: Full url-encoded CRN of the service instance.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/master/README.md
               about initializing the authenticator of your choice.
        """
        if crn is None:
            raise ValueError('crn must be provided')

        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)
        self.crn = crn


    #########################
    # CIS Zones
    #########################


    def list_zones(self,
        **kwargs
    ) -> DetailedResponse:
        """
        List all zones.

        List all zones for a service instance.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListZonesResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_zones')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones'.format(
            *self.encode_path_vars(self.crn))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def create_zone(self,
        *,
        name: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create zone.

        Add a new zone for a given service instance.

        :param str name: (optional) name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ZoneResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_zone')
        headers.update(sdk_headers)

        data = {
            'name': name
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones'.format(
            *self.encode_path_vars(self.crn))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def delete_zone(self,
        zone_identifier: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete zone.

        Delete a zone given its id.

        :param str zone_identifier: Identifier of zone.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DeleteZoneResp` object
        """

        if zone_identifier is None:
            raise ValueError('zone_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_zone')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}'.format(
            *self.encode_path_vars(self.crn, zone_identifier))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_zone(self,
        zone_identifier: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get zone.

        Get the details of a zone for a given service instance and given zone id.

        :param str zone_identifier: Zone identifier.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ZoneResp` object
        """

        if zone_identifier is None:
            raise ValueError('zone_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_zone')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}'.format(
            *self.encode_path_vars(self.crn, zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_zone(self,
        zone_identifier: str,
        *,
        paused: bool = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update zone.

        Update the paused field of the zone.

        :param str zone_identifier: Zone identifier.
        :param bool paused: (optional) paused.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ZoneResp` object
        """

        if zone_identifier is None:
            raise ValueError('zone_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_zone')
        headers.update(sdk_headers)

        data = {
            'paused': paused
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}'.format(
            *self.encode_path_vars(self.crn, zone_identifier))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def zone_activation_check(self,
        zone_identifier: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Check zone.

        Perform activation check on zone for status.

        :param str zone_identifier: Identifier of zone.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ZoneActivationcheckResp` object
        """

        if zone_identifier is None:
            raise ValueError('zone_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='zone_activation_check')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/activation_check'.format(
            *self.encode_path_vars(self.crn, zone_identifier))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


##############################################################################
# Models
##############################################################################


class DeleteZoneRespResult():
    """
    result.

    :attr str id: id.
    """

    def __init__(self,
                 id: str) -> None:
        """
        Initialize a DeleteZoneRespResult object.

        :param str id: id.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteZoneRespResult':
        """Initialize a DeleteZoneRespResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in DeleteZoneRespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteZoneRespResult object from a json dictionary."""
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
        """Return a `str` version of this DeleteZoneRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteZoneRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteZoneRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ZoneActivationcheckRespResult():
    """
    result.

    :attr str id: id.
    """

    def __init__(self,
                 id: str) -> None:
        """
        Initialize a ZoneActivationcheckRespResult object.

        :param str id: id.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ZoneActivationcheckRespResult':
        """Initialize a ZoneActivationcheckRespResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in ZoneActivationcheckRespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ZoneActivationcheckRespResult object from a json dictionary."""
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
        """Return a `str` version of this ZoneActivationcheckRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ZoneActivationcheckRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ZoneActivationcheckRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DeleteZoneResp():
    """
    delete zone response.

    :attr bool success: success.
    :attr List[List[str]] errors: errors.
    :attr List[List[str]] messages: messages.
    :attr DeleteZoneRespResult result: result.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: 'DeleteZoneRespResult') -> None:
        """
        Initialize a DeleteZoneResp object.

        :param bool success: success.
        :param List[List[str]] errors: errors.
        :param List[List[str]] messages: messages.
        :param DeleteZoneRespResult result: result.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteZoneResp':
        """Initialize a DeleteZoneResp object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in DeleteZoneResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in DeleteZoneResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in DeleteZoneResp JSON')
        if 'result' in _dict:
            args['result'] = DeleteZoneRespResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in DeleteZoneResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteZoneResp object from a json dictionary."""
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
        """Return a `str` version of this DeleteZoneResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteZoneResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteZoneResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ListZonesResp():
    """
    list zones response.

    :attr bool success: success.
    :attr List[List[str]] errors: errors.
    :attr List[List[str]] messages: messages.
    :attr List[ZoneDetails] result: zone list.
    :attr ResultInfo result_info: result information.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: List['ZoneDetails'],
                 result_info: 'ResultInfo') -> None:
        """
        Initialize a ListZonesResp object.

        :param bool success: success.
        :param List[List[str]] errors: errors.
        :param List[List[str]] messages: messages.
        :param List[ZoneDetails] result: zone list.
        :param ResultInfo result_info: result information.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result
        self.result_info = result_info

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListZonesResp':
        """Initialize a ListZonesResp object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in ListZonesResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in ListZonesResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in ListZonesResp JSON')
        if 'result' in _dict:
            args['result'] = [ZoneDetails.from_dict(x) for x in _dict.get('result')]
        else:
            raise ValueError('Required property \'result\' not present in ListZonesResp JSON')
        if 'result_info' in _dict:
            args['result_info'] = ResultInfo.from_dict(_dict.get('result_info'))
        else:
            raise ValueError('Required property \'result_info\' not present in ListZonesResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListZonesResp object from a json dictionary."""
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
        """Return a `str` version of this ListZonesResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListZonesResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListZonesResp') -> bool:
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

class ZoneActivationcheckResp():
    """
    zone activation check response.

    :attr bool success: success.
    :attr List[List[str]] errors: errors.
    :attr List[List[str]] messages: messages.
    :attr ZoneActivationcheckRespResult result: result.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: 'ZoneActivationcheckRespResult') -> None:
        """
        Initialize a ZoneActivationcheckResp object.

        :param bool success: success.
        :param List[List[str]] errors: errors.
        :param List[List[str]] messages: messages.
        :param ZoneActivationcheckRespResult result: result.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ZoneActivationcheckResp':
        """Initialize a ZoneActivationcheckResp object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in ZoneActivationcheckResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in ZoneActivationcheckResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in ZoneActivationcheckResp JSON')
        if 'result' in _dict:
            args['result'] = ZoneActivationcheckRespResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in ZoneActivationcheckResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ZoneActivationcheckResp object from a json dictionary."""
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
        """Return a `str` version of this ZoneActivationcheckResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ZoneActivationcheckResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ZoneActivationcheckResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ZoneDetails():
    """
    zone details.

    :attr str id: (optional) id.
    :attr str created_on: (optional) created date.
    :attr str modified_on: (optional) modified date.
    :attr str name: (optional) name.
    :attr str original_registrar: (optional) original registrar.
    :attr str original_dnshost: (optional) orginal dns host.
    :attr str status: (optional) status.
    :attr bool paused: (optional) paused.
    :attr List[str] original_name_servers: (optional) orginal name servers.
    :attr List[str] name_servers: (optional) name servers.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 created_on: str = None,
                 modified_on: str = None,
                 name: str = None,
                 original_registrar: str = None,
                 original_dnshost: str = None,
                 status: str = None,
                 paused: bool = None,
                 original_name_servers: List[str] = None,
                 name_servers: List[str] = None) -> None:
        """
        Initialize a ZoneDetails object.

        :param str id: (optional) id.
        :param str created_on: (optional) created date.
        :param str modified_on: (optional) modified date.
        :param str name: (optional) name.
        :param str original_registrar: (optional) original registrar.
        :param str original_dnshost: (optional) orginal dns host.
        :param str status: (optional) status.
        :param bool paused: (optional) paused.
        :param List[str] original_name_servers: (optional) orginal name servers.
        :param List[str] name_servers: (optional) name servers.
        """
        self.id = id
        self.created_on = created_on
        self.modified_on = modified_on
        self.name = name
        self.original_registrar = original_registrar
        self.original_dnshost = original_dnshost
        self.status = status
        self.paused = paused
        self.original_name_servers = original_name_servers
        self.name_servers = name_servers

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ZoneDetails':
        """Initialize a ZoneDetails object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'created_on' in _dict:
            args['created_on'] = _dict.get('created_on')
        if 'modified_on' in _dict:
            args['modified_on'] = _dict.get('modified_on')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'original_registrar' in _dict:
            args['original_registrar'] = _dict.get('original_registrar')
        if 'original_dnshost' in _dict:
            args['original_dnshost'] = _dict.get('original_dnshost')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'paused' in _dict:
            args['paused'] = _dict.get('paused')
        if 'original_name_servers' in _dict:
            args['original_name_servers'] = _dict.get('original_name_servers')
        if 'name_servers' in _dict:
            args['name_servers'] = _dict.get('name_servers')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ZoneDetails object from a json dictionary."""
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
        if hasattr(self, 'original_registrar') and self.original_registrar is not None:
            _dict['original_registrar'] = self.original_registrar
        if hasattr(self, 'original_dnshost') and self.original_dnshost is not None:
            _dict['original_dnshost'] = self.original_dnshost
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'paused') and self.paused is not None:
            _dict['paused'] = self.paused
        if hasattr(self, 'original_name_servers') and self.original_name_servers is not None:
            _dict['original_name_servers'] = self.original_name_servers
        if hasattr(self, 'name_servers') and self.name_servers is not None:
            _dict['name_servers'] = self.name_servers
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ZoneDetails object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ZoneDetails') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ZoneDetails') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ZoneResp():
    """
    zone response.

    :attr bool success: success.
    :attr List[List[str]] errors: errors.
    :attr List[List[str]] messages: messages.
    :attr ZoneDetails result: zone details.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: 'ZoneDetails') -> None:
        """
        Initialize a ZoneResp object.

        :param bool success: success.
        :param List[List[str]] errors: errors.
        :param List[List[str]] messages: messages.
        :param ZoneDetails result: zone details.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ZoneResp':
        """Initialize a ZoneResp object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in ZoneResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in ZoneResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in ZoneResp JSON')
        if 'result' in _dict:
            args['result'] = ZoneDetails.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in ZoneResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ZoneResp object from a json dictionary."""
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
        """Return a `str` version of this ZoneResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ZoneResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ZoneResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
