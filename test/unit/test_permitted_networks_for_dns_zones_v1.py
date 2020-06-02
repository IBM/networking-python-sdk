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
import requests
import responses
from ibm_cloud_networking_services import *


service = PermittedNetworksForDnsZonesV1(
    authenticator=NoAuthAuthenticator()
    )

base_url = 'https://api.dns-svcs.cloud.ibm.com/v1'
service.set_service_url(base_url)

##############################################################################
# Start of Service: PermittedNetwork
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_permitted_networks
#-----------------------------------------------------------------------------
class TestListPermittedNetworks():

    #--------------------------------------------------------
    # list_permitted_networks()
    #--------------------------------------------------------
    @responses.activate
    def test_list_permitted_networks_all_params(self):
        # Set up mock
        url = base_url + '/instances/testString/dnszones/testString/permitted_networks'
        mock_response = '{"permitted_networks": [{"id": "fecd0173-3919-456b-b202-3029dfa1b0f7", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "permitted_network": [{"vpc_crn": "crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6"}], "type": "vpc", "state": "ACTIVE"}], "offset": 0, "limit": 10, "total_count": 200, "first": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:252926c6-7d0c-4d37-861a-1faca0041785/permitted_networks?limit=10"}, "next": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:252926c6-7d0c-4d37-861a-1faca0041785/permitted_networks?offset=1&limit=10"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        x_correlation_id = 'testString'
        offset = 'testString'
        limit = 'testString'

        # Invoke method
        response = service.list_permitted_networks(
            instance_id,
            dnszone_id,
            x_correlation_id=x_correlation_id,
            offset=offset,
            limit=limit
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'offset={}'.format(offset) in query_string
        assert 'limit={}'.format(limit) in query_string


    #--------------------------------------------------------
    # test_list_permitted_networks_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_permitted_networks_required_params(self):
        # Set up mock
        url = base_url + '/instances/testString/dnszones/testString/permitted_networks'
        mock_response = '{"permitted_networks": [{"id": "fecd0173-3919-456b-b202-3029dfa1b0f7", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "permitted_network": [{"vpc_crn": "crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6"}], "type": "vpc", "state": "ACTIVE"}], "offset": 0, "limit": 10, "total_count": 200, "first": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:252926c6-7d0c-4d37-861a-1faca0041785/permitted_networks?limit=10"}, "next": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:252926c6-7d0c-4d37-861a-1faca0041785/permitted_networks?offset=1&limit=10"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'

        # Invoke method
        response = service.list_permitted_networks(
            instance_id,
            dnszone_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for create_permitted_networks
#-----------------------------------------------------------------------------
class TestCreatePermittedNetworks():

    #--------------------------------------------------------
    # create_permitted_networks()
    #--------------------------------------------------------
    @responses.activate
    def test_create_permitted_networks_all_params(self):
        # Set up mock
        url = base_url + '/instances/testString/dnszones/testString/permitted_networks'
        mock_response = '{"id": "fecd0173-3919-456b-b202-3029dfa1b0f7", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "permitted_network": [{"vpc_crn": "crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6"}], "type": "vpc", "state": "ACTIVE"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a PermittedNetworkVpc model
        permitted_network_vpc_model =  {
            'vpc_crn': 'crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6'
        }

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        type = 'vpc'
        permitted_network = permitted_network_vpc_model
        x_correlation_id = 'testString'

        # Invoke method
        response = service.create_permitted_networks(
            instance_id,
            dnszone_id,
            type=type,
            permitted_network=permitted_network,
            x_correlation_id=x_correlation_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['type'] == type
        assert req_body['permitted_network'] == permitted_network


    #--------------------------------------------------------
    # test_create_permitted_networks_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_permitted_networks_required_params(self):
        # Set up mock
        url = base_url + '/instances/testString/dnszones/testString/permitted_networks'
        mock_response = '{"id": "fecd0173-3919-456b-b202-3029dfa1b0f7", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "permitted_network": [{"vpc_crn": "crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6"}], "type": "vpc", "state": "ACTIVE"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'

        # Invoke method
        response = service.create_permitted_networks(
            instance_id,
            dnszone_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for delete_permitted_network
#-----------------------------------------------------------------------------
class TestDeletePermittedNetwork():

    #--------------------------------------------------------
    # delete_permitted_network()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_permitted_network_all_params(self):
        # Set up mock
        url = base_url + '/instances/testString/dnszones/testString/permitted_networks/testString'
        mock_response = '{"id": "fecd0173-3919-456b-b202-3029dfa1b0f7", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "permitted_network": [{"vpc_crn": "crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6"}], "type": "vpc", "state": "ACTIVE"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        permitted_network_id = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = service.delete_permitted_network(
            instance_id,
            dnszone_id,
            permitted_network_id,
            x_correlation_id=x_correlation_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


    #--------------------------------------------------------
    # test_delete_permitted_network_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_permitted_network_required_params(self):
        # Set up mock
        url = base_url + '/instances/testString/dnszones/testString/permitted_networks/testString'
        mock_response = '{"id": "fecd0173-3919-456b-b202-3029dfa1b0f7", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "permitted_network": [{"vpc_crn": "crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6"}], "type": "vpc", "state": "ACTIVE"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        permitted_network_id = 'testString'

        # Invoke method
        response = service.delete_permitted_network(
            instance_id,
            dnszone_id,
            permitted_network_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


#-----------------------------------------------------------------------------
# Test Class for get_permitted_network
#-----------------------------------------------------------------------------
class TestGetPermittedNetwork():

    #--------------------------------------------------------
    # get_permitted_network()
    #--------------------------------------------------------
    @responses.activate
    def test_get_permitted_network_all_params(self):
        # Set up mock
        url = base_url + '/instances/testString/dnszones/testString/permitted_networks/testString'
        mock_response = '{"id": "fecd0173-3919-456b-b202-3029dfa1b0f7", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "permitted_network": [{"vpc_crn": "crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6"}], "type": "vpc", "state": "ACTIVE"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        permitted_network_id = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = service.get_permitted_network(
            instance_id,
            dnszone_id,
            permitted_network_id,
            x_correlation_id=x_correlation_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_permitted_network_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_permitted_network_required_params(self):
        # Set up mock
        url = base_url + '/instances/testString/dnszones/testString/permitted_networks/testString'
        mock_response = '{"id": "fecd0173-3919-456b-b202-3029dfa1b0f7", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "permitted_network": [{"vpc_crn": "crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6"}], "type": "vpc", "state": "ACTIVE"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        permitted_network_id = 'testString'

        # Invoke method
        response = service.get_permitted_network(
            instance_id,
            dnszone_id,
            permitted_network_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: PermittedNetwork
##############################################################################

