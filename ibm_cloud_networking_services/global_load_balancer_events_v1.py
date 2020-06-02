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
Global Load Balancer Healthcheck Events
"""

from datetime import datetime
from typing import Dict, List
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import datetime_to_string, string_to_datetime

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################

class GlobalLoadBalancerEventsV1(BaseService):
    """The Global Load Balancer Events V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.cis.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'global_load_balancer_events'

    @classmethod
    def new_instance(cls,
                     crn: str,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'GlobalLoadBalancerEventsV1':
        """
        Return a new client for the Global Load Balancer Events service using the
               specified parameters and external configuration.

        :param str crn: Full url-encoded cloud resource name (CRN) of resource
               instance.
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
        Construct a new client for the Global Load Balancer Events service.

        :param str crn: Full url-encoded cloud resource name (CRN) of resource
               instance.

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
    # Get load balancer events
    #########################


    def get_load_balancer_events(self, **kwargs) -> DetailedResponse:
        """
        List all load balancer events.

        Get load balancer events for all origins.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListEventsResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_load_balancer_events')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/load_balancers/events'.format(*self.encode_path_vars(self.crn))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response

