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
import responses
from ibm_cloud_networking_services.global_load_balancer_monitor_v1 import *

crn = 'testString'

service = GlobalLoadBalancerMonitorV1(
    authenticator=NoAuthAuthenticator(),
    crn=crn
    )

base_url = 'https://api.cis.cloud.ibm.com'
service.set_service_url(base_url)

##############################################################################
# Start of Service: GlobalLoadBalancerMonitor
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_all_load_balancer_monitors
#-----------------------------------------------------------------------------
class TestListAllLoadBalancerMonitors():

    #--------------------------------------------------------
    # list_all_load_balancer_monitors()
    #--------------------------------------------------------
    @responses.activate
    def test_list_all_load_balancer_monitors_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/load_balancers/monitors'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "type": "http", "description": "Login page monitor", "method": "GET", "port": 8080, "path": "/", "timeout": 5, "retries": 2, "interval": 60, "expected_body": "alive", "expected_codes": "2xx", "follow_redirects": true, "allow_insecure": true}], "result_info": {"page": 1, "per_page": 20, "count": 1, "total_count": 2000}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_all_load_balancer_monitors()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_list_all_load_balancer_monitors_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_all_load_balancer_monitors_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/load_balancers/monitors'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "type": "http", "description": "Login page monitor", "method": "GET", "port": 8080, "path": "/", "timeout": 5, "retries": 2, "interval": 60, "expected_body": "alive", "expected_codes": "2xx", "follow_redirects": true, "allow_insecure": true}], "result_info": {"page": 1, "per_page": 20, "count": 1, "total_count": 2000}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_all_load_balancer_monitors()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for create_load_balancer_monitor
#-----------------------------------------------------------------------------
class TestCreateLoadBalancerMonitor():

    #--------------------------------------------------------
    # create_load_balancer_monitor()
    #--------------------------------------------------------
    @responses.activate
    def test_create_load_balancer_monitor_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/load_balancers/monitors'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "type": "http", "description": "Login page monitor", "method": "GET", "port": 8080, "path": "/", "timeout": 5, "retries": 2, "interval": 60, "expected_body": "alive", "expected_codes": "2xx", "follow_redirects": true, "allow_insecure": true}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        expected_codes = '2xx'
        type = 'http'
        description = 'Login page monitor'
        method = 'GET'
        port = 8080
        path = '/'
        timeout = 5
        retries = 2
        interval = 60
        follow_redirects = True
        expected_body = 'alive'
        allow_insecure = True

        # Invoke method
        response = service.create_load_balancer_monitor(
            expected_codes=expected_codes,
            type=type,
            description=description,
            method=method,
            port=port,
            path=path,
            timeout=timeout,
            retries=retries,
            interval=interval,
            follow_redirects=follow_redirects,
            expected_body=expected_body,
            allow_insecure=allow_insecure,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['expected_codes'] == expected_codes
        assert req_body['type'] == type
        assert req_body['description'] == description
        assert req_body['method'] == method
        assert req_body['port'] == port
        assert req_body['path'] == path
        assert req_body['timeout'] == timeout
        assert req_body['retries'] == retries
        assert req_body['interval'] == interval
        assert req_body['follow_redirects'] == follow_redirects
        assert req_body['expected_body'] == expected_body
        assert req_body['allow_insecure'] == allow_insecure


    #--------------------------------------------------------
    # test_create_load_balancer_monitor_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_load_balancer_monitor_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/load_balancers/monitors'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "type": "http", "description": "Login page monitor", "method": "GET", "port": 8080, "path": "/", "timeout": 5, "retries": 2, "interval": 60, "expected_body": "alive", "expected_codes": "2xx", "follow_redirects": true, "allow_insecure": true}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.create_load_balancer_monitor()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for edit_load_balancer_monitor
#-----------------------------------------------------------------------------
class TestEditLoadBalancerMonitor():

    #--------------------------------------------------------
    # edit_load_balancer_monitor()
    #--------------------------------------------------------
    @responses.activate
    def test_edit_load_balancer_monitor_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/load_balancers/monitors/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "type": "http", "description": "Login page monitor", "method": "GET", "port": 8080, "path": "/", "timeout": 5, "retries": 2, "interval": 60, "expected_body": "alive", "expected_codes": "2xx", "follow_redirects": true, "allow_insecure": true}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        monitor_identifier = 'testString'
        expected_codes = '2xx'
        type = 'http'
        description = 'Login page monitor'
        method = 'GET'
        port = 8080
        path = '/'
        timeout = 5
        retries = 2
        interval = 60
        follow_redirects = True
        expected_body = 'alive'
        allow_insecure = True

        # Invoke method
        response = service.edit_load_balancer_monitor(
            monitor_identifier,
            expected_codes=expected_codes,
            type=type,
            description=description,
            method=method,
            port=port,
            path=path,
            timeout=timeout,
            retries=retries,
            interval=interval,
            follow_redirects=follow_redirects,
            expected_body=expected_body,
            allow_insecure=allow_insecure,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['expected_codes'] == expected_codes
        assert req_body['type'] == type
        assert req_body['description'] == description
        assert req_body['method'] == method
        assert req_body['port'] == port
        assert req_body['path'] == path
        assert req_body['timeout'] == timeout
        assert req_body['retries'] == retries
        assert req_body['interval'] == interval
        assert req_body['follow_redirects'] == follow_redirects
        assert req_body['expected_body'] == expected_body
        assert req_body['allow_insecure'] == allow_insecure


    #--------------------------------------------------------
    # test_edit_load_balancer_monitor_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_edit_load_balancer_monitor_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/load_balancers/monitors/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "type": "http", "description": "Login page monitor", "method": "GET", "port": 8080, "path": "/", "timeout": 5, "retries": 2, "interval": 60, "expected_body": "alive", "expected_codes": "2xx", "follow_redirects": true, "allow_insecure": true}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        monitor_identifier = 'testString'

        # Invoke method
        response = service.edit_load_balancer_monitor(
            monitor_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for delete_load_balancer_monitor
#-----------------------------------------------------------------------------
class TestDeleteLoadBalancerMonitor():

    #--------------------------------------------------------
    # delete_load_balancer_monitor()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_load_balancer_monitor_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/load_balancers/monitors/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        monitor_identifier = 'testString'

        # Invoke method
        response = service.delete_load_balancer_monitor(
            monitor_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_delete_load_balancer_monitor_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_load_balancer_monitor_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/load_balancers/monitors/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        monitor_identifier = 'testString'

        # Invoke method
        response = service.delete_load_balancer_monitor(
            monitor_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for get_load_balancer_monitor
#-----------------------------------------------------------------------------
class TestGetLoadBalancerMonitor():

    #--------------------------------------------------------
    # get_load_balancer_monitor()
    #--------------------------------------------------------
    @responses.activate
    def test_get_load_balancer_monitor_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/load_balancers/monitors/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "type": "http", "description": "Login page monitor", "method": "GET", "port": 8080, "path": "/", "timeout": 5, "retries": 2, "interval": 60, "expected_body": "alive", "expected_codes": "2xx", "follow_redirects": true, "allow_insecure": true}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        monitor_identifier = 'testString'

        # Invoke method
        response = service.get_load_balancer_monitor(
            monitor_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_load_balancer_monitor_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_load_balancer_monitor_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/load_balancers/monitors/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "type": "http", "description": "Login page monitor", "method": "GET", "port": 8080, "path": "/", "timeout": 5, "retries": 2, "interval": 60, "expected_body": "alive", "expected_codes": "2xx", "follow_redirects": true, "allow_insecure": true}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        monitor_identifier = 'testString'

        # Invoke method
        response = service.get_load_balancer_monitor(
            monitor_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: GlobalLoadBalancerMonitor
##############################################################################

