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
This is the  Metrics API
"""

from typing import Dict, List
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_list

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################

class MetricsApiV1(BaseService):
    """The Metrics API V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.cis.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'metrics_api'

    @classmethod
    def new_instance(cls,
                     crn: str,
                     zone_id: str,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'MetricsApiV1':
        """
        Return a new client for the Metrics API service using the specified
               parameters and external configuration.

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
        Construct a new client for the Metrics API service.

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
    # Zone
    #########################


    def analytics_dashboard(self, *, since: str = None, until: str = None, continuous: bool = None, **kwargs) -> DetailedResponse:
        """
        Zone web traffic analytics dashboard.

        The dashboard view provides both `totals` and `timeseries` data for the given zone
        and time period across the entire network.

        :param str since: (optional) The (inclusive) beginning of the requested
               time frame. This value can be a negative integer representing the number of
               minutes in the past relative to time the request is made, or can be an
               absolute timestamp that conforms to RFC 3339. At this point in time, it
               cannot exceed a time in the past greater than one year.
        :param str until: (optional) The (exclusive) end of the requested time
               frame. This value can be a negative integer representing the number of
               minutes in the past relative to time the request is made, or can be an
               absolute timestamp that conforms to RFC 3339. If omitted, the time of the
               request is used.
        :param bool continuous: (optional) When set to `true`, and when `since` is
               a relative timestamp
               (i.e. a negative number, representing the number of seconds to look back),
               the API will move the requested time window backward, up to a bounded
               number of seconds, until it finds a complete, continuous region of data.
               This flag thus should only be `true` when trying to get the most recently
               arrived, but also completely aggregated, data. The API will also return
               data when `continuous` is `true` and when `until` is set, or when both
               `since` and `until` are absolute timestamps. However, due to the underlying
               behaviour of `continuous`=`true`, which regresses the time window if data
               is not available, the users must beware that with these parameters, the API
               response may not represent the requested time window. We thus advise
               against using both `continuous`=`true` and absolute timestamps.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Dashboard` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='analytics_dashboard')
        headers.update(sdk_headers)

        params = {
            'since': since,
            'until': until,
            'continuous': continuous
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/analytics/dashboard'.format(*self.encode_path_vars(self.crn, self.zone_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def analytics_by_colos(self, *, since: str = None, until: str = None, continuous: bool = None, **kwargs) -> DetailedResponse:
        """
        Zone web traffic analytics data by datacenter.

        This view provides a breakdown of analytics data by datacenter. This is available
        to Enterprise customers only.

        :param str since: (optional) The (inclusive) beginning of the requested
               time frame. This value can be a negative integer representing the number of
               minutes in the past relative to time the request is made, or can be an
               absolute timestamp that conforms to RFC 3339. At this point in time, it
               cannot exceed a time in the past greater than one year.
        :param str until: (optional) The (exclusive) end of the requested time
               frame. This value can be a negative integer representing the number of
               minutes in the past relative to time the request is made, or can be an
               absolute timestamp that conforms to RFC 3339. If omitted, the time of the
               request is used.
        :param bool continuous: (optional) When set to `true`, and when `since` is
               a relative timestamp
               (i.e. a negative number, representing the number of seconds to look back),
               the API will move the requested time window backward, up to a bounded
               number of seconds, until it finds a complete, continuous region of data.
               This flag thus should only be `true` when trying to get the most recently
               arrived, but also completely aggregated, data. The API will also return
               data when `continuous` is `true` and when `until` is set, or when both
               `since` and `until` are absolute timestamps. However, due to the underlying
               behaviour of `continuous`=`true`, which regresses the time window if data
               is not available, the users must beware that with these parameters, the API
               response may not represent the requested time window. We thus advise
               against using both `continuous`=`true` and absolute timestamps.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Colos` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='analytics_by_colos')
        headers.update(sdk_headers)

        params = {
            'since': since,
            'until': until,
            'continuous': continuous
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/analytics/colos'.format(*self.encode_path_vars(self.crn, self.zone_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    #########################
    # DNS
    #########################


    def dns_analytics(self, dimensions: List[str], metrics: List[str], since: str, until: str, *, sort: List[str] = None, filters: str = None, limit: int = None, **kwargs) -> DetailedResponse:
        """
        Zone DNS traffic analytics data.

        Retrieves a list of summarised aggregate metrics over a given time period.

        :param List[str] dimensions: Dimensions can be used to break down the data
               by given attributes.
        :param List[str] metrics: A metric is a numerical value that is based on an
               attribute of the data, for example a query count.
        :param str since: The (inclusive) beginning of the requested time frame.
               This value can be a negative integer representing the number of minutes in
               the past relative to time the request is made, or can be an absolute
               timestamp that conforms to RFC 3339. At this point in time, it cannot
               exceed a time in the past greater than one year.
        :param str until: The (exclusive) end of the requested time frame. This
               value can be a negative integer representing the number of minutes in the
               past relative to time the request is made, or can be an absolute timestamp
               that conforms to RFC 3339. If omitted, the time of the request is used.
        :param List[str] sort: (optional) Array of dimensions to sort by, each
               dimension may be prefixed by - (descending) or + (ascending).
        :param str filters: (optional) Segmentation filter in attribute operator
               value format.
        :param int limit: (optional) Limit number of returned metrics, default is
               100.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Report` object
        """

        if dimensions is None:
            raise ValueError('dimensions must be provided')
        if metrics is None:
            raise ValueError('metrics must be provided')
        if since is None:
            raise ValueError('since must be provided')
        if until is None:
            raise ValueError('until must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='dns_analytics')
        headers.update(sdk_headers)

        params = {
            'dimensions': convert_list(dimensions),
            'metrics': convert_list(metrics),
            'since': since,
            'until': until,
            'sort': convert_list(sort),
            'filters': filters,
            'limit': limit
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/dns_analytics/report'.format(*self.encode_path_vars(self.crn, self.zone_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def dns_analytics_by_time(self, *, dimensions: List[str] = None, metrics: List[str] = None, since: str = None, until: str = None, sort: List[str] = None, filters: str = None, limit: int = None, **kwargs) -> DetailedResponse:
        """
        Zone DNS traffic analytics data by time interval.

        Retrieves a list of aggregate metrics grouped by time interval.

        :param List[str] dimensions: (optional) Dimensions can be used to break
               down the data by given attributes.
        :param List[str] metrics: (optional) A metric is a numerical value that is
               based on an attribute of the data, for example a query count.
        :param str since: (optional) The (inclusive) beginning of the requested
               time frame. This value can be a negative integer representing the number of
               minutes in the past relative to time the request is made, or can be an
               absolute timestamp that conforms to RFC 3339. At this point in time, it
               cannot exceed a time in the past greater than one year.
        :param str until: (optional) The (exclusive) end of the requested time
               frame. This value can be a negative integer representing the number of
               minutes in the past relative to time the request is made, or can be an
               absolute timestamp that conforms to RFC 3339. If omitted, the time of the
               request is used.
        :param List[str] sort: (optional) Array of dimensions to sort by, each
               dimension may be prefixed by - (descending) or + (ascending).
        :param str filters: (optional) Segmentation filter in attribute operator
               value format.
        :param int limit: (optional) Limit number of returned metrics, default is
               100.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ReportByTime` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='dns_analytics_by_time')
        headers.update(sdk_headers)

        params = {
            'dimensions': convert_list(dimensions),
            'metrics': convert_list(metrics),
            'since': since,
            'until': until,
            'sort': convert_list(sort),
            'filters': filters,
            'limit': limit
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/dns_analytics/report/bytime'.format(*self.encode_path_vars(self.crn, self.zone_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

