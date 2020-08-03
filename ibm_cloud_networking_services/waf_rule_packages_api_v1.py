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
This document describes CIS WAF Rule Packages API.
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

class WafRulePackagesApiV1(BaseService):
    """The WAF Rule Packages API V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.cis.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'waf_rule_packages_api'

    @classmethod
    def new_instance(cls,
                     crn: str,
                     zone_id: str,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'WafRulePackagesApiV1':
        """
        Return a new client for the WAF Rule Packages API service using the
               specified parameters and external configuration.

        :param str crn: cloud resource name.

        :param str zone_id: zone id.
        """
        if crn is None:
            raise ValueError('crn must be provided')
        if zone_id is None:
            raise ValueError('zone_id must be provided')

        authenticator = get_authenticator_from_environment(service_name)
        service = cls(
            crn,
            zone_id,
            authenticator
            )
        service.configure_service(service_name)
        return service

    def __init__(self,
                 crn: str,
                 zone_id: str,
                 authenticator: Authenticator = None,
                ) -> None:
        """
        Construct a new client for the WAF Rule Packages API service.

        :param str crn: cloud resource name.

        :param str zone_id: zone id.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/master/README.md
               about initializing the authenticator of your choice.
        """
        if crn is None:
            raise ValueError('crn must be provided')
        if zone_id is None:
            raise ValueError('zone_id must be provided')

        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)
        self.crn = crn
        self.zone_id = zone_id


    #########################
    # WAF Rule Packages
    #########################


    def list_waf_packages(self,
        *,
        name: str = None,
        page: int = None,
        per_page: int = None,
        order: str = None,
        direction: str = None,
        match: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List all WAF rule packages.

        Get firewall packages for a zone.

        :param str name: (optional) Name of the firewall package.
        :param int page: (optional) Page number of paginated results.
        :param int per_page: (optional) Number of packages per page.
        :param str order: (optional) Field to order packages by.
        :param str direction: (optional) Direction to order packages.
        :param str match: (optional) Whether to match all search requirements or at
               least one (any).
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `WafPackagesResponse` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_waf_packages')
        headers.update(sdk_headers)

        params = {
            'name': name,
            'page': page,
            'per_page': per_page,
            'order': order,
            'direction': direction,
            'match': match
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/firewall/waf/packages'.format(
            *self.encode_path_vars(self.crn, self.zone_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def get_waf_package(self,
        package_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get WAF rule package.

        Get information about a single firewall package.

        :param str package_id: Package ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `WafPackageResponse` object
        """

        if package_id is None:
            raise ValueError('package_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_waf_package')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/firewall/waf/packages/{2}'.format(
            *self.encode_path_vars(self.crn, self.zone_id, package_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_waf_package(self,
        package_id: str,
        *,
        sensitivity: str = None,
        action_mode: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Change WAF rule package package.

        Change the sensitivity and action for an anomaly detection type WAF rule package.

        :param str package_id: Package ID.
        :param str sensitivity: (optional) The sensitivity of the firewall package.
        :param str action_mode: (optional) The default action that will be taken
               for rules under the firewall package.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `WafPackageResponse` object
        """

        if package_id is None:
            raise ValueError('package_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_waf_package')
        headers.update(sdk_headers)

        data = {
            'sensitivity': sensitivity,
            'action_mode': action_mode
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/firewall/waf/packages/{2}'.format(
            *self.encode_path_vars(self.crn, self.zone_id, package_id))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


class ListWafPackagesEnums:
    """
    Enums for list_waf_packages parameters.
    """

    class Direction(str, Enum):
        """
        Direction to order packages.
        """
        DESC = 'desc'
        ASC = 'asc'
    class Match(str, Enum):
        """
        Whether to match all search requirements or at least one (any).
        """
        ALL = 'all'
        ANY = 'any'


##############################################################################
# Models
##############################################################################


class WafPackageResponseResult():
    """
    Container for response information.

    :attr str id: (optional) ID.
    :attr str name: (optional) Name.
    :attr str description: (optional) Description.
    :attr str detection_mode: (optional) Detection mode.
    :attr str zone_id: (optional) Value.
    :attr str status: (optional) Value.
    :attr str sensitivity: (optional) Value.
    :attr str action_mode: (optional) Value.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 name: str = None,
                 description: str = None,
                 detection_mode: str = None,
                 zone_id: str = None,
                 status: str = None,
                 sensitivity: str = None,
                 action_mode: str = None) -> None:
        """
        Initialize a WafPackageResponseResult object.

        :param str id: (optional) ID.
        :param str name: (optional) Name.
        :param str description: (optional) Description.
        :param str detection_mode: (optional) Detection mode.
        :param str zone_id: (optional) Value.
        :param str status: (optional) Value.
        :param str sensitivity: (optional) Value.
        :param str action_mode: (optional) Value.
        """
        self.id = id
        self.name = name
        self.description = description
        self.detection_mode = detection_mode
        self.zone_id = zone_id
        self.status = status
        self.sensitivity = sensitivity
        self.action_mode = action_mode

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'WafPackageResponseResult':
        """Initialize a WafPackageResponseResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'detection_mode' in _dict:
            args['detection_mode'] = _dict.get('detection_mode')
        if 'zone_id' in _dict:
            args['zone_id'] = _dict.get('zone_id')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'sensitivity' in _dict:
            args['sensitivity'] = _dict.get('sensitivity')
        if 'action_mode' in _dict:
            args['action_mode'] = _dict.get('action_mode')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WafPackageResponseResult object from a json dictionary."""
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
        if hasattr(self, 'detection_mode') and self.detection_mode is not None:
            _dict['detection_mode'] = self.detection_mode
        if hasattr(self, 'zone_id') and self.zone_id is not None:
            _dict['zone_id'] = self.zone_id
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'sensitivity') and self.sensitivity is not None:
            _dict['sensitivity'] = self.sensitivity
        if hasattr(self, 'action_mode') and self.action_mode is not None:
            _dict['action_mode'] = self.action_mode
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this WafPackageResponseResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'WafPackageResponseResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'WafPackageResponseResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class WafPackagesResponseResultInfo():
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
        Initialize a WafPackagesResponseResultInfo object.

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
    def from_dict(cls, _dict: Dict) -> 'WafPackagesResponseResultInfo':
        """Initialize a WafPackagesResponseResultInfo object from a json dictionary."""
        args = {}
        if 'page' in _dict:
            args['page'] = _dict.get('page')
        else:
            raise ValueError('Required property \'page\' not present in WafPackagesResponseResultInfo JSON')
        if 'per_page' in _dict:
            args['per_page'] = _dict.get('per_page')
        else:
            raise ValueError('Required property \'per_page\' not present in WafPackagesResponseResultInfo JSON')
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        else:
            raise ValueError('Required property \'count\' not present in WafPackagesResponseResultInfo JSON')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        else:
            raise ValueError('Required property \'total_count\' not present in WafPackagesResponseResultInfo JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WafPackagesResponseResultInfo object from a json dictionary."""
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
        """Return a `str` version of this WafPackagesResponseResultInfo object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'WafPackagesResponseResultInfo') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'WafPackagesResponseResultInfo') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class WafPackagesResponseResultItem():
    """
    WafPackagesResponseResultItem.

    :attr str id: (optional) ID.
    :attr str name: (optional) Name.
    :attr str description: (optional) Description.
    :attr str detection_mode: (optional) Detection mode.
    :attr str zone_id: (optional) Value.
    :attr str status: (optional) Value.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 name: str = None,
                 description: str = None,
                 detection_mode: str = None,
                 zone_id: str = None,
                 status: str = None) -> None:
        """
        Initialize a WafPackagesResponseResultItem object.

        :param str id: (optional) ID.
        :param str name: (optional) Name.
        :param str description: (optional) Description.
        :param str detection_mode: (optional) Detection mode.
        :param str zone_id: (optional) Value.
        :param str status: (optional) Value.
        """
        self.id = id
        self.name = name
        self.description = description
        self.detection_mode = detection_mode
        self.zone_id = zone_id
        self.status = status

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'WafPackagesResponseResultItem':
        """Initialize a WafPackagesResponseResultItem object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'detection_mode' in _dict:
            args['detection_mode'] = _dict.get('detection_mode')
        if 'zone_id' in _dict:
            args['zone_id'] = _dict.get('zone_id')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WafPackagesResponseResultItem object from a json dictionary."""
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
        if hasattr(self, 'detection_mode') and self.detection_mode is not None:
            _dict['detection_mode'] = self.detection_mode
        if hasattr(self, 'zone_id') and self.zone_id is not None:
            _dict['zone_id'] = self.zone_id
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this WafPackagesResponseResultItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'WafPackagesResponseResultItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'WafPackagesResponseResultItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class WafPackageResponse():
    """
    waf package response.

    :attr bool success: Was operation successful.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    :attr WafPackageResponseResult result: Container for response information.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: 'WafPackageResponseResult') -> None:
        """
        Initialize a WafPackageResponse object.

        :param bool success: Was operation successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        :param WafPackageResponseResult result: Container for response information.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'WafPackageResponse':
        """Initialize a WafPackageResponse object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in WafPackageResponse JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in WafPackageResponse JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in WafPackageResponse JSON')
        if 'result' in _dict:
            args['result'] = WafPackageResponseResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in WafPackageResponse JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WafPackageResponse object from a json dictionary."""
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
        """Return a `str` version of this WafPackageResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'WafPackageResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'WafPackageResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class WafPackagesResponse():
    """
    waf packages response.

    :attr bool success: Was operation successful.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    :attr List[WafPackagesResponseResultItem] result: Container for response
          information.
    :attr WafPackagesResponseResultInfo result_info: Statistics of results.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: List['WafPackagesResponseResultItem'],
                 result_info: 'WafPackagesResponseResultInfo') -> None:
        """
        Initialize a WafPackagesResponse object.

        :param bool success: Was operation successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        :param List[WafPackagesResponseResultItem] result: Container for response
               information.
        :param WafPackagesResponseResultInfo result_info: Statistics of results.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result
        self.result_info = result_info

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'WafPackagesResponse':
        """Initialize a WafPackagesResponse object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in WafPackagesResponse JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in WafPackagesResponse JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in WafPackagesResponse JSON')
        if 'result' in _dict:
            args['result'] = [WafPackagesResponseResultItem.from_dict(x) for x in _dict.get('result')]
        else:
            raise ValueError('Required property \'result\' not present in WafPackagesResponse JSON')
        if 'result_info' in _dict:
            args['result_info'] = WafPackagesResponseResultInfo.from_dict(_dict.get('result_info'))
        else:
            raise ValueError('Required property \'result_info\' not present in WafPackagesResponse JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WafPackagesResponse object from a json dictionary."""
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
        """Return a `str` version of this WafPackagesResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'WafPackagesResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'WafPackagesResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
