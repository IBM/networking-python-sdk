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

from datetime import datetime, timezone
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import pytest
import responses
from ibm_cloud_networking_services import GlobalLoadBalancerEventsV1

crn = 'testString'

service = GlobalLoadBalancerEventsV1(
    authenticator=NoAuthAuthenticator(),
    crn=crn
    )

base_url = 'https://api.cis.cloud.ibm.com'
service.set_service_url(base_url)

##############################################################################
# Start of Service: GetLoadBalancerEvents
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_load_balancer_events
#-----------------------------------------------------------------------------
class TestGetLoadBalancerEvents():

    #--------------------------------------------------------
    # get_load_balancer_events()
    #--------------------------------------------------------
    @responses.activate
    def test_get_load_balancer_events_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/load_balancers/events'
        mock_response = '{"success": true, "result": [{"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "timestamp": "2019-01-01T12:00:00", "pool": [{"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "name": "some-pool", "healthy": true, "changed": true, "minimum_origins": 1}], "origins": [{"name": "f1aba936b94213e5b8dca0c0dbf1f9cc", "address": "1.2.3.4", "ip": "1.2.3.4", "enabled": true, "healthy": true, "failure_reason": "No failures", "changed": true}]}], "result_info": {"page": 1, "per_page": 20, "count": 1, "total_count": 2000}, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_load_balancer_events()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_load_balancer_events_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_load_balancer_events_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/load_balancers/events'
        mock_response = '{"success": true, "result": [{"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "timestamp": "2019-01-01T12:00:00", "pool": [{"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "name": "some-pool", "healthy": true, "changed": true, "minimum_origins": 1}], "origins": [{"name": "f1aba936b94213e5b8dca0c0dbf1f9cc", "address": "1.2.3.4", "ip": "1.2.3.4", "enabled": true, "healthy": true, "failure_reason": "No failures", "changed": true}]}], "result_info": {"page": 1, "per_page": 20, "count": 1, "total_count": 2000}, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_load_balancer_events()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: GetLoadBalancerEvents
##############################################################################

