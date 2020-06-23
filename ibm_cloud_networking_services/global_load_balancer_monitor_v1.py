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


    def list_all_load_balancer_monitors(self, **kwargs) -> DetailedResponse:
        """
        List all load balancer monitors.

        List configured load balancer monitors for a user.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListMonitorResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='list_all_load_balancer_monitors')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/load_balancers/monitors'.format(*self.encode_path_vars(self.crn))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def create_load_balancer_monitor(self, *, expected_codes: str = None, type: str = None, description: str = None, method: str = None, port: int = None, path: str = None, timeout: int = None, retries: int = None, interval: int = None, follow_redirects: bool = None, expected_body: str = None, allow_insecure: bool = None, **kwargs) -> DetailedResponse:
        """
        Create a load balancer monitor.

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
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `MonitorResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='create_load_balancer_monitor')
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
            'allow_insecure': allow_insecure
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/load_balancers/monitors'.format(*self.encode_path_vars(self.crn))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def edit_load_balancer_monitor(self, monitor_identifier: str, *, expected_codes: str = None, type: str = None, description: str = None, method: str = None, port: int = None, path: str = None, timeout: int = None, retries: int = None, interval: int = None, follow_redirects: bool = None, expected_body: str = None, allow_insecure: bool = None, **kwargs) -> DetailedResponse:
        """
        Edit a load balancer monitor.

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
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `MonitorResp` object
        """

        if monitor_identifier is None:
            raise ValueError('monitor_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='edit_load_balancer_monitor')
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
            'allow_insecure': allow_insecure
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/load_balancers/monitors/{1}'.format(*self.encode_path_vars(self.crn, monitor_identifier))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def delete_load_balancer_monitor(self, monitor_identifier: str, **kwargs) -> DetailedResponse:
        """
        Delete a load balancer monitor.

        Delete a load balancer monitor.

        :param str monitor_identifier: monitor identifier.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DeleteMonitorResp` object
        """

        if monitor_identifier is None:
            raise ValueError('monitor_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='delete_load_balancer_monitor')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/load_balancers/monitors/{1}'.format(*self.encode_path_vars(self.crn, monitor_identifier))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_load_balancer_monitor(self, monitor_identifier: str, **kwargs) -> DetailedResponse:
        """
        get a load balancer monitor.

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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_load_balancer_monitor')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/load_balancers/monitors/{1}'.format(*self.encode_path_vars(self.crn, monitor_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response

