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
from ibm_cloud_networking_services import CisIpApiV1


service = CisIpApiV1(
    authenticator=NoAuthAuthenticator()
    )

base_url = 'https://api.cis.cloud.ibm.com'
service.set_service_url(base_url)

##############################################################################
# Start of Service: IP
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_ips
#-----------------------------------------------------------------------------
class TestListIps():

    #--------------------------------------------------------
    # list_ips()
    #--------------------------------------------------------
    @responses.activate
    def test_list_ips_all_params(self):
        # Set up mock
        url = base_url + '/v1/ips'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"ipv4_cidrs": ["180.15.128.0/20"], "ipv6_cidrs": ["2400:cb00::/32"]}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_ips()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_list_ips_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_ips_required_params(self):
        # Set up mock
        url = base_url + '/v1/ips'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"ipv4_cidrs": ["180.15.128.0/20"], "ipv6_cidrs": ["2400:cb00::/32"]}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_ips()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: IP
##############################################################################

