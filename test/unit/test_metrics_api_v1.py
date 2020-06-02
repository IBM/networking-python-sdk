# -*- coding: utf-8 -*-
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

from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import pytest
import requests
import responses
from ibm_cloud_networking_services import MetricsApiV1

crn = 'testString'
zone_id = 'testString'

service = MetricsApiV1(
    authenticator=NoAuthAuthenticator(),
    crn=crn,
    zone_id=zone_id
    )

base_url = 'https://api.cis.cloud.ibm.com'
service.set_service_url(base_url)

##############################################################################
# Start of Service: Zone
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for analytics_dashboard
#-----------------------------------------------------------------------------
class TestAnalyticsDashboard():

    #--------------------------------------------------------
    # analytics_dashboard()
    #--------------------------------------------------------
    @responses.activate
    def test_analytics_dashboard_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/analytics/dashboard'
        mock_response = '{"query": {"since": "since", "until": "until"}, "result": {"totals": {"since": "since", "until": "until", "requests": {"all": 3, "cached": 6, "uncached": 8, "ssl": {"encrypted": 9, "unencrypted": 11}, "http_status": "unknown property type: http_status", "content_type": {"css": 3, "empty": 5, "html": 4, "javascript": 10, "jpeg": 4, "json": 4, "other": 5, "png": 3}, "country": "unknown property type: country", "ip_class": {"no_record": 9, "whitelist": 9}}, "bandwidth": {"all": 3, "cached": 6, "uncached": 8, "ssl": {"encrypted": 9, "unencrypted": 11}, "content_type": {"css": 3, "empty": 5, "html": 4, "javascript": 10, "jpeg": 4, "json": 4, "other": 5, "png": 3}, "country": "unknown property type: country"}, "threats": {"all": 3, "type": "unknown property type: type", "country": "unknown property type: country"}, "pageviews": {"all": 3, "search_engine": "unknown property type: search_engine"}, "uniques": {"all": 3}}, "timeseries": [{"since": "since", "until": "until", "requests": {"all": 3, "cached": 6, "uncached": 8, "ssl": {"encrypted": 9, "unencrypted": 11}, "http_status": "unknown property type: http_status", "content_type": {"css": 3, "empty": 5, "html": 4, "javascript": 10, "jpeg": 4, "json": 4, "other": 5, "png": 3}, "country": "unknown property type: country", "ip_class": {"no_record": 9, "whitelist": 9}}, "bandwidth": {"all": 3, "cached": 6, "uncached": 8, "ssl": {"encrypted": 9, "unencrypted": 11}, "content_type": {"css": 3, "empty": 5, "html": 4, "javascript": 10, "jpeg": 4, "json": 4, "other": 5, "png": 3}, "country": "unknown property type: country"}, "threats": {"all": 3, "type": "unknown property type: type", "country": "unknown property type: country"}, "pageviews": {"all": 3, "search_engine": "unknown property type: search_engine"}, "uniques": {"all": 3}}]}, "success": false, "messages": [["messages"]], "errors": [["errors"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        since = 'testString'
        until = 'testString'
        continuous = True

        # Invoke method
        response = service.analytics_dashboard(
            since=since,
            until=until,
            continuous=continuous
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'since={}'.format(since) in query_string
        assert 'until={}'.format(until) in query_string
        assert 'continuous={}'.format('true' if continuous else 'false') in query_string


    #--------------------------------------------------------
    # test_analytics_dashboard_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_analytics_dashboard_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/analytics/dashboard'
        mock_response = '{"query": {"since": "since", "until": "until"}, "result": {"totals": {"since": "since", "until": "until", "requests": {"all": 3, "cached": 6, "uncached": 8, "ssl": {"encrypted": 9, "unencrypted": 11}, "http_status": "unknown property type: http_status", "content_type": {"css": 3, "empty": 5, "html": 4, "javascript": 10, "jpeg": 4, "json": 4, "other": 5, "png": 3}, "country": "unknown property type: country", "ip_class": {"no_record": 9, "whitelist": 9}}, "bandwidth": {"all": 3, "cached": 6, "uncached": 8, "ssl": {"encrypted": 9, "unencrypted": 11}, "content_type": {"css": 3, "empty": 5, "html": 4, "javascript": 10, "jpeg": 4, "json": 4, "other": 5, "png": 3}, "country": "unknown property type: country"}, "threats": {"all": 3, "type": "unknown property type: type", "country": "unknown property type: country"}, "pageviews": {"all": 3, "search_engine": "unknown property type: search_engine"}, "uniques": {"all": 3}}, "timeseries": [{"since": "since", "until": "until", "requests": {"all": 3, "cached": 6, "uncached": 8, "ssl": {"encrypted": 9, "unencrypted": 11}, "http_status": "unknown property type: http_status", "content_type": {"css": 3, "empty": 5, "html": 4, "javascript": 10, "jpeg": 4, "json": 4, "other": 5, "png": 3}, "country": "unknown property type: country", "ip_class": {"no_record": 9, "whitelist": 9}}, "bandwidth": {"all": 3, "cached": 6, "uncached": 8, "ssl": {"encrypted": 9, "unencrypted": 11}, "content_type": {"css": 3, "empty": 5, "html": 4, "javascript": 10, "jpeg": 4, "json": 4, "other": 5, "png": 3}, "country": "unknown property type: country"}, "threats": {"all": 3, "type": "unknown property type: type", "country": "unknown property type: country"}, "pageviews": {"all": 3, "search_engine": "unknown property type: search_engine"}, "uniques": {"all": 3}}]}, "success": false, "messages": [["messages"]], "errors": [["errors"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.analytics_dashboard()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for analytics_by_colos
#-----------------------------------------------------------------------------
class TestAnalyticsByColos():

    #--------------------------------------------------------
    # analytics_by_colos()
    #--------------------------------------------------------
    @responses.activate
    def test_analytics_by_colos_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/analytics/colos'
        mock_response = '{"query": {"since": "since", "until": "until"}, "result": [{"colo_id": "colo_id", "totals": {"since": "since", "until": "until", "requests": {"all": 3, "cached": 6, "uncached": 8, "ssl": {"encrypted": 9, "unencrypted": 11}, "http_status": "unknown property type: http_status", "content_type": {"css": 3, "empty": 5, "html": 4, "javascript": 10, "jpeg": 4, "json": 4, "other": 5, "png": 3}, "country": "unknown property type: country", "ip_class": {"no_record": 9, "whitelist": 9}}, "bandwidth": {"all": 3, "cached": 6, "uncached": 8, "ssl": {"encrypted": 9, "unencrypted": 11}, "content_type": {"css": 3, "empty": 5, "html": 4, "javascript": 10, "jpeg": 4, "json": 4, "other": 5, "png": 3}, "country": "unknown property type: country"}, "threats": {"all": 3, "type": "unknown property type: type", "country": "unknown property type: country"}, "pageviews": {"all": 3, "search_engine": "unknown property type: search_engine"}, "uniques": {"all": 3}}, "timeseries": [{"since": "since", "until": "until", "requests": {"all": 3, "cached": 6, "uncached": 8, "ssl": {"encrypted": 9, "unencrypted": 11}, "http_status": "unknown property type: http_status", "content_type": {"css": 3, "empty": 5, "html": 4, "javascript": 10, "jpeg": 4, "json": 4, "other": 5, "png": 3}, "country": "unknown property type: country", "ip_class": {"no_record": 9, "whitelist": 9}}, "bandwidth": {"all": 3, "cached": 6, "uncached": 8, "ssl": {"encrypted": 9, "unencrypted": 11}, "content_type": {"css": 3, "empty": 5, "html": 4, "javascript": 10, "jpeg": 4, "json": 4, "other": 5, "png": 3}, "country": "unknown property type: country"}, "threats": {"all": 3, "type": "unknown property type: type", "country": "unknown property type: country"}, "pageviews": {"all": 3, "search_engine": "unknown property type: search_engine"}, "uniques": {"all": 3}}]}], "success": false, "messages": ["messages"], "errors": [["errors"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        since = 'testString'
        until = 'testString'
        continuous = True

        # Invoke method
        response = service.analytics_by_colos(
            since=since,
            until=until,
            continuous=continuous
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'since={}'.format(since) in query_string
        assert 'until={}'.format(until) in query_string
        assert 'continuous={}'.format('true' if continuous else 'false') in query_string


    #--------------------------------------------------------
    # test_analytics_by_colos_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_analytics_by_colos_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/analytics/colos'
        mock_response = '{"query": {"since": "since", "until": "until"}, "result": [{"colo_id": "colo_id", "totals": {"since": "since", "until": "until", "requests": {"all": 3, "cached": 6, "uncached": 8, "ssl": {"encrypted": 9, "unencrypted": 11}, "http_status": "unknown property type: http_status", "content_type": {"css": 3, "empty": 5, "html": 4, "javascript": 10, "jpeg": 4, "json": 4, "other": 5, "png": 3}, "country": "unknown property type: country", "ip_class": {"no_record": 9, "whitelist": 9}}, "bandwidth": {"all": 3, "cached": 6, "uncached": 8, "ssl": {"encrypted": 9, "unencrypted": 11}, "content_type": {"css": 3, "empty": 5, "html": 4, "javascript": 10, "jpeg": 4, "json": 4, "other": 5, "png": 3}, "country": "unknown property type: country"}, "threats": {"all": 3, "type": "unknown property type: type", "country": "unknown property type: country"}, "pageviews": {"all": 3, "search_engine": "unknown property type: search_engine"}, "uniques": {"all": 3}}, "timeseries": [{"since": "since", "until": "until", "requests": {"all": 3, "cached": 6, "uncached": 8, "ssl": {"encrypted": 9, "unencrypted": 11}, "http_status": "unknown property type: http_status", "content_type": {"css": 3, "empty": 5, "html": 4, "javascript": 10, "jpeg": 4, "json": 4, "other": 5, "png": 3}, "country": "unknown property type: country", "ip_class": {"no_record": 9, "whitelist": 9}}, "bandwidth": {"all": 3, "cached": 6, "uncached": 8, "ssl": {"encrypted": 9, "unencrypted": 11}, "content_type": {"css": 3, "empty": 5, "html": 4, "javascript": 10, "jpeg": 4, "json": 4, "other": 5, "png": 3}, "country": "unknown property type: country"}, "threats": {"all": 3, "type": "unknown property type: type", "country": "unknown property type: country"}, "pageviews": {"all": 3, "search_engine": "unknown property type: search_engine"}, "uniques": {"all": 3}}]}], "success": false, "messages": ["messages"], "errors": [["errors"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.analytics_by_colos()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: Zone
##############################################################################

##############################################################################
# Start of Service: DNS
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for dns_analytics
#-----------------------------------------------------------------------------
class TestDnsAnalytics():

    #--------------------------------------------------------
    # dns_analytics()
    #--------------------------------------------------------
    @responses.activate
    def test_dns_analytics_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/dns_analytics/report'
        mock_response = '{"query": "unknown property type: query", "result": {"data": "unknown property type: data", "totals": "unknown property type: totals", "min": "unknown property type: min", "max": "unknown property type: max"}, "success": false, "messages": ["messages"], "errors": [["errors"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        dimensions = ['testString']
        metrics = ['testString']
        since = 'testString'
        until = 'testString'
        sort = ['testString']
        filters = 'testString'
        limit = 38

        # Invoke method
        response = service.dns_analytics(
            dimensions,
            metrics,
            since,
            until,
            sort=sort,
            filters=filters,
            limit=limit
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'dimensions={}'.format(','.join(dimensions)) in query_string
        assert 'metrics={}'.format(','.join(metrics)) in query_string
        assert 'since={}'.format(since) in query_string
        assert 'until={}'.format(until) in query_string
        assert 'sort={}'.format(','.join(sort)) in query_string
        assert 'filters={}'.format(filters) in query_string
        assert 'limit={}'.format(limit) in query_string


    #--------------------------------------------------------
    # test_dns_analytics_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_dns_analytics_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/dns_analytics/report'
        mock_response = '{"query": "unknown property type: query", "result": {"data": "unknown property type: data", "totals": "unknown property type: totals", "min": "unknown property type: min", "max": "unknown property type: max"}, "success": false, "messages": ["messages"], "errors": [["errors"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        dimensions = ['testString']
        metrics = ['testString']
        since = 'testString'
        until = 'testString'

        # Invoke method
        response = service.dns_analytics(
            dimensions,
            metrics,
            since,
            until
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'dimensions={}'.format(','.join(dimensions)) in query_string
        assert 'metrics={}'.format(','.join(metrics)) in query_string
        assert 'since={}'.format(since) in query_string
        assert 'until={}'.format(until) in query_string


#-----------------------------------------------------------------------------
# Test Class for dns_analytics_by_time
#-----------------------------------------------------------------------------
class TestDnsAnalyticsByTime():

    #--------------------------------------------------------
    # dns_analytics_by_time()
    #--------------------------------------------------------
    @responses.activate
    def test_dns_analytics_by_time_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/dns_analytics/report/bytime'
        mock_response = '{"query": "unknown property type: query", "result": {"data": "unknown property type: data", "totals": "unknown property type: totals", "min": "unknown property type: min", "max": "unknown property type: max"}, "success": false, "messages": ["messages"], "errors": [["errors"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        dimensions = ['testString']
        metrics = ['testString']
        since = 'testString'
        until = 'testString'
        sort = ['testString']
        filters = 'testString'
        limit = 38

        # Invoke method
        response = service.dns_analytics_by_time(
            dimensions=dimensions,
            metrics=metrics,
            since=since,
            until=until,
            sort=sort,
            filters=filters,
            limit=limit
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'dimensions={}'.format(','.join(dimensions)) in query_string
        assert 'metrics={}'.format(','.join(metrics)) in query_string
        assert 'since={}'.format(since) in query_string
        assert 'until={}'.format(until) in query_string
        assert 'sort={}'.format(','.join(sort)) in query_string
        assert 'filters={}'.format(filters) in query_string
        assert 'limit={}'.format(limit) in query_string


    #--------------------------------------------------------
    # test_dns_analytics_by_time_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_dns_analytics_by_time_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/dns_analytics/report/bytime'
        mock_response = '{"query": "unknown property type: query", "result": {"data": "unknown property type: data", "totals": "unknown property type: totals", "min": "unknown property type: min", "max": "unknown property type: max"}, "success": false, "messages": ["messages"], "errors": [["errors"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.dns_analytics_by_time()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: DNS
##############################################################################

