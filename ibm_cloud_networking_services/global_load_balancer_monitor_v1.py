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
Global Load Balancer Monitor
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

class GlobalLoadBalancerMonitorV1(BaseService):
    """The Global Load Balancer Monitor V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.cis.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'global_load_balancer_monitor'

    @classmethod
    def new_instance(cls,
                     crn: str,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'GlobalLoadBalancerMonitorV1':
        """
        Return a new client for the Global Load Balancer Monitor service using the
               specified parameters and external configuration.

        :param str crn: Full CRN of the service instance.
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
        Construct a new client for the Global Load Balancer Monitor service.

        :param str crn: Full CRN of the service instance.

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
    # Global Load Balancer Monitor
    #########################


    def list_all_load_balancer_monitors(self,
        **kwargs
    ) -> DetailedResponse:
        """
        List all load balancer monitors.

        List configured load balancer monitors for a user.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListMonitorResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_all_load_balancer_monitors')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/load_balancers/monitors'.format(
            *self.encode_path_vars(self.crn))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def create_load_balancer_monitor(self,
        *,
        expected_codes: str = None,
        type: str = None,
        description: str = None,
        method: str = None,
        port: int = None,
        path: str = None,
        timeout: int = None,
        retries: int = None,
        interval: int = None,
        follow_redirects: bool = None,
        expected_body: str = None,
        allow_insecure: bool = None,
        header: dict = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create load balancer monitor.

        Create a load balancer monitor for a given service instance.

        :param str expected_codes: (optional) expected codes.
        :param str type: (optional) http type.
        :param str description: (optional) login page monitor.
        :param str method: (optional) method.
        :param int port: (optional) port number.
        :param str path: (optional) path.
        :param int timeout: (optional) timeout count.
        :param int retries: (optional) retry count.
        :param int interval: (optional) interval.
        :param bool follow_redirects: (optional) follow redirects.
        :param str expected_body: (optional) expected body.
        :param bool allow_insecure: (optional) allow insecure.
        :param dict header: (optional) header.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `MonitorResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_load_balancer_monitor')
        headers.update(sdk_headers)

        data = {
            'expected_codes': expected_codes,
            'type': type,
            'description': description,
            'method': method,
            'port': port,
            'path': path,
            'timeout': timeout,
            'retries': retries,
            'interval': interval,
            'follow_redirects': follow_redirects,
            'expected_body': expected_body,
            'allow_insecure': allow_insecure,
            'header': header
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/load_balancers/monitors'.format(
            *self.encode_path_vars(self.crn))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def edit_load_balancer_monitor(self,
        monitor_identifier: str,
        *,
        expected_codes: str = None,
        type: str = None,
        description: str = None,
        method: str = None,
        port: int = None,
        path: str = None,
        timeout: int = None,
        retries: int = None,
        interval: int = None,
        follow_redirects: bool = None,
        expected_body: str = None,
        allow_insecure: bool = None,
        header: dict = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Edit load balancer monitor.

        Edit porperties of an existing load balancer monitor.

        :param str monitor_identifier: monitor identifier.
        :param str expected_codes: (optional) expected codes.
        :param str type: (optional) http type.
        :param str description: (optional) login page monitor.
        :param str method: (optional) method.
        :param int port: (optional) port number.
        :param str path: (optional) path.
        :param int timeout: (optional) timeout count.
        :param int retries: (optional) retry count.
        :param int interval: (optional) interval.
        :param bool follow_redirects: (optional) follow redirects.
        :param str expected_body: (optional) expected body.
        :param bool allow_insecure: (optional) allow insecure.
        :param dict header: (optional) header.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `MonitorResp` object
        """

        if monitor_identifier is None:
            raise ValueError('monitor_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='edit_load_balancer_monitor')
        headers.update(sdk_headers)

        data = {
            'expected_codes': expected_codes,
            'type': type,
            'description': description,
            'method': method,
            'port': port,
            'path': path,
            'timeout': timeout,
            'retries': retries,
            'interval': interval,
            'follow_redirects': follow_redirects,
            'expected_body': expected_body,
            'allow_insecure': allow_insecure,
            'header': header
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/load_balancers/monitors/{1}'.format(
            *self.encode_path_vars(self.crn, monitor_identifier))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def delete_load_balancer_monitor(self,
        monitor_identifier: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete load balancer monitor.

        Delete a load balancer monitor.

        :param str monitor_identifier: monitor identifier.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DeleteMonitorResp` object
        """

        if monitor_identifier is None:
            raise ValueError('monitor_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_load_balancer_monitor')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/load_balancers/monitors/{1}'.format(
            *self.encode_path_vars(self.crn, monitor_identifier))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_load_balancer_monitor(self,
        monitor_identifier: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get load balancer monitor.

        For a given service instance and load balancer monitor id, get the monitor
        details.

        :param str monitor_identifier: monitor identifier.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `MonitorResp` object
        """

        if monitor_identifier is None:
            raise ValueError('monitor_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_load_balancer_monitor')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/load_balancers/monitors/{1}'.format(
            *self.encode_path_vars(self.crn, monitor_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


##############################################################################
# Models
##############################################################################


class DeleteMonitorRespResult():
    """
    result.

    :attr str id: identifier.
    """

    def __init__(self,
                 id: str) -> None:
        """
        Initialize a DeleteMonitorRespResult object.

        :param str id: identifier.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteMonitorRespResult':
        """Initialize a DeleteMonitorRespResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in DeleteMonitorRespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteMonitorRespResult object from a json dictionary."""
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
        """Return a `str` version of this DeleteMonitorRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteMonitorRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteMonitorRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DeleteMonitorResp():
    """
    delete monitor response object.

    :attr bool success: success response.
    :attr List[List[str]] errors: errors.
    :attr List[List[str]] messages: messages.
    :attr DeleteMonitorRespResult result: result.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: 'DeleteMonitorRespResult') -> None:
        """
        Initialize a DeleteMonitorResp object.

        :param bool success: success response.
        :param List[List[str]] errors: errors.
        :param List[List[str]] messages: messages.
        :param DeleteMonitorRespResult result: result.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteMonitorResp':
        """Initialize a DeleteMonitorResp object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in DeleteMonitorResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in DeleteMonitorResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in DeleteMonitorResp JSON')
        if 'result' in _dict:
            args['result'] = DeleteMonitorRespResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in DeleteMonitorResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteMonitorResp object from a json dictionary."""
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
        """Return a `str` version of this DeleteMonitorResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteMonitorResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteMonitorResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ListMonitorResp():
    """
    monitor list response.

    :attr bool success: success response.
    :attr List[List[str]] errors: errors.
    :attr List[List[str]] messages: messages.
    :attr List[MonitorPack] result: result.
    :attr ResultInfo result_info: result information.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: List['MonitorPack'],
                 result_info: 'ResultInfo') -> None:
        """
        Initialize a ListMonitorResp object.

        :param bool success: success response.
        :param List[List[str]] errors: errors.
        :param List[List[str]] messages: messages.
        :param List[MonitorPack] result: result.
        :param ResultInfo result_info: result information.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result
        self.result_info = result_info

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListMonitorResp':
        """Initialize a ListMonitorResp object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in ListMonitorResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in ListMonitorResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in ListMonitorResp JSON')
        if 'result' in _dict:
            args['result'] = [MonitorPack.from_dict(x) for x in _dict.get('result')]
        else:
            raise ValueError('Required property \'result\' not present in ListMonitorResp JSON')
        if 'result_info' in _dict:
            args['result_info'] = ResultInfo.from_dict(_dict.get('result_info'))
        else:
            raise ValueError('Required property \'result_info\' not present in ListMonitorResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListMonitorResp object from a json dictionary."""
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
        """Return a `str` version of this ListMonitorResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListMonitorResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListMonitorResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class MonitorPack():
    """
    monitor package.

    :attr str id: (optional) identifier.
    :attr str created_on: (optional) created date.
    :attr str modified_on: (optional) modified date.
    :attr str type: (optional) type.
    :attr str description: (optional) login page.
    :attr str method: (optional) method name.
    :attr int port: (optional) port number.
    :attr str path: (optional) path.
    :attr int timeout: (optional) timeout count.
    :attr int retries: (optional) retries count.
    :attr int interval: (optional) interval.
    :attr str expected_body: expected body.
    :attr str expected_codes: expected codes.
    :attr bool follow_redirects: (optional) follow redirects.
    :attr bool allow_insecure: (optional) allow insecure.
    :attr dict header: (optional) header.
    """

    def __init__(self,
                 expected_body: str,
                 expected_codes: str,
                 *,
                 id: str = None,
                 created_on: str = None,
                 modified_on: str = None,
                 type: str = None,
                 description: str = None,
                 method: str = None,
                 port: int = None,
                 path: str = None,
                 timeout: int = None,
                 retries: int = None,
                 interval: int = None,
                 follow_redirects: bool = None,
                 allow_insecure: bool = None,
                 header: dict = None) -> None:
        """
        Initialize a MonitorPack object.

        :param str expected_body: expected body.
        :param str expected_codes: expected codes.
        :param str id: (optional) identifier.
        :param str created_on: (optional) created date.
        :param str modified_on: (optional) modified date.
        :param str type: (optional) type.
        :param str description: (optional) login page.
        :param str method: (optional) method name.
        :param int port: (optional) port number.
        :param str path: (optional) path.
        :param int timeout: (optional) timeout count.
        :param int retries: (optional) retries count.
        :param int interval: (optional) interval.
        :param bool follow_redirects: (optional) follow redirects.
        :param bool allow_insecure: (optional) allow insecure.
        :param dict header: (optional) header.
        """
        self.id = id
        self.created_on = created_on
        self.modified_on = modified_on
        self.type = type
        self.description = description
        self.method = method
        self.port = port
        self.path = path
        self.timeout = timeout
        self.retries = retries
        self.interval = interval
        self.expected_body = expected_body
        self.expected_codes = expected_codes
        self.follow_redirects = follow_redirects
        self.allow_insecure = allow_insecure
        self.header = header

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MonitorPack':
        """Initialize a MonitorPack object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'created_on' in _dict:
            args['created_on'] = _dict.get('created_on')
        if 'modified_on' in _dict:
            args['modified_on'] = _dict.get('modified_on')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'method' in _dict:
            args['method'] = _dict.get('method')
        if 'port' in _dict:
            args['port'] = _dict.get('port')
        if 'path' in _dict:
            args['path'] = _dict.get('path')
        if 'timeout' in _dict:
            args['timeout'] = _dict.get('timeout')
        if 'retries' in _dict:
            args['retries'] = _dict.get('retries')
        if 'interval' in _dict:
            args['interval'] = _dict.get('interval')
        if 'expected_body' in _dict:
            args['expected_body'] = _dict.get('expected_body')
        else:
            raise ValueError('Required property \'expected_body\' not present in MonitorPack JSON')
        if 'expected_codes' in _dict:
            args['expected_codes'] = _dict.get('expected_codes')
        else:
            raise ValueError('Required property \'expected_codes\' not present in MonitorPack JSON')
        if 'follow_redirects' in _dict:
            args['follow_redirects'] = _dict.get('follow_redirects')
        if 'allow_insecure' in _dict:
            args['allow_insecure'] = _dict.get('allow_insecure')
        if 'header' in _dict:
            args['header'] = _dict.get('header')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MonitorPack object from a json dictionary."""
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
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'method') and self.method is not None:
            _dict['method'] = self.method
        if hasattr(self, 'port') and self.port is not None:
            _dict['port'] = self.port
        if hasattr(self, 'path') and self.path is not None:
            _dict['path'] = self.path
        if hasattr(self, 'timeout') and self.timeout is not None:
            _dict['timeout'] = self.timeout
        if hasattr(self, 'retries') and self.retries is not None:
            _dict['retries'] = self.retries
        if hasattr(self, 'interval') and self.interval is not None:
            _dict['interval'] = self.interval
        if hasattr(self, 'expected_body') and self.expected_body is not None:
            _dict['expected_body'] = self.expected_body
        if hasattr(self, 'expected_codes') and self.expected_codes is not None:
            _dict['expected_codes'] = self.expected_codes
        if hasattr(self, 'follow_redirects') and self.follow_redirects is not None:
            _dict['follow_redirects'] = self.follow_redirects
        if hasattr(self, 'allow_insecure') and self.allow_insecure is not None:
            _dict['allow_insecure'] = self.allow_insecure
        if hasattr(self, 'header') and self.header is not None:
            _dict['header'] = self.header
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MonitorPack object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MonitorPack') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MonitorPack') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class MonitorResp():
    """
    monitor response.

    :attr bool success: success response.
    :attr List[List[str]] errors: errors.
    :attr List[List[str]] messages: messages.
    :attr MonitorPack result: monitor package.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: 'MonitorPack') -> None:
        """
        Initialize a MonitorResp object.

        :param bool success: success response.
        :param List[List[str]] errors: errors.
        :param List[List[str]] messages: messages.
        :param MonitorPack result: monitor package.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MonitorResp':
        """Initialize a MonitorResp object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in MonitorResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in MonitorResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in MonitorResp JSON')
        if 'result' in _dict:
            args['result'] = MonitorPack.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in MonitorResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MonitorResp object from a json dictionary."""
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
        """Return a `str` version of this MonitorResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MonitorResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MonitorResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ResultInfo():
    """
    result information.

    :attr int page: page number.
    :attr int per_page: per page number.
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

        :param int page: page number.
        :param int per_page: per page number.
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
