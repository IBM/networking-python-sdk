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
import re
import responses
from ibm_cloud_networking_services.cis_ip_api_v1 import *


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

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # list_ips()
    #--------------------------------------------------------
    @responses.activate
    def test_list_ips_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/ips')
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


##############################################################################
# Start of Model Tests
##############################################################################
# region
#-----------------------------------------------------------------------------
# Test Class for IpResponseResult
#-----------------------------------------------------------------------------
class TestIpResponseResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for IpResponseResult
    #--------------------------------------------------------
    def test_ip_response_result_serialization(self):

        # Construct a json representation of a IpResponseResult model
        ip_response_result_model_json = {}
        ip_response_result_model_json['ipv4_cidrs'] = ['180.15.128.0/20']
        ip_response_result_model_json['ipv6_cidrs'] = ['2400:cb00::/32']

        # Construct a model instance of IpResponseResult by calling from_dict on the json representation
        ip_response_result_model = IpResponseResult.from_dict(ip_response_result_model_json)
        assert ip_response_result_model != False

        # Construct a model instance of IpResponseResult by calling from_dict on the json representation
        ip_response_result_model_dict = IpResponseResult.from_dict(ip_response_result_model_json).__dict__
        ip_response_result_model2 = IpResponseResult(**ip_response_result_model_dict)

        # Verify the model instances are equivalent
        assert ip_response_result_model == ip_response_result_model2

        # Convert model instance back to dict and verify no loss of data
        ip_response_result_model_json2 = ip_response_result_model.to_dict()
        assert ip_response_result_model_json2 == ip_response_result_model_json

#-----------------------------------------------------------------------------
# Test Class for IpResponse
#-----------------------------------------------------------------------------
class TestIpResponse():

    #--------------------------------------------------------
    # Test serialization/deserialization for IpResponse
    #--------------------------------------------------------
    def test_ip_response_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        ip_response_result_model = {} # IpResponseResult
        ip_response_result_model['ipv4_cidrs'] = ['180.15.128.0/20']
        ip_response_result_model['ipv6_cidrs'] = ['2400:cb00::/32']

        # Construct a json representation of a IpResponse model
        ip_response_model_json = {}
        ip_response_model_json['success'] = True
        ip_response_model_json['errors'] = [['testString']]
        ip_response_model_json['messages'] = [['testString']]
        ip_response_model_json['result'] = ip_response_result_model

        # Construct a model instance of IpResponse by calling from_dict on the json representation
        ip_response_model = IpResponse.from_dict(ip_response_model_json)
        assert ip_response_model != False

        # Construct a model instance of IpResponse by calling from_dict on the json representation
        ip_response_model_dict = IpResponse.from_dict(ip_response_model_json).__dict__
        ip_response_model2 = IpResponse(**ip_response_model_dict)

        # Verify the model instances are equivalent
        assert ip_response_model == ip_response_model2

        # Convert model instance back to dict and verify no loss of data
        ip_response_model_json2 = ip_response_model.to_dict()
        assert ip_response_model_json2 == ip_response_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
