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
from ibm_cloud_networking_services.dns_zones_v1 import *


service = DnsZonesV1(
    authenticator=NoAuthAuthenticator()
    )

base_url = 'https://api.dns-svcs.cloud.ibm.com/v1'
service.set_service_url(base_url)

##############################################################################
# Start of Service: DNSZones
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_dnszones
#-----------------------------------------------------------------------------
class TestListDnszones():

    #--------------------------------------------------------
    # list_dnszones()
    #--------------------------------------------------------
    @responses.activate
    def test_list_dnszones_all_params(self):
        # Set up mock
        url = base_url + '/instances/testString/dnszones'
        mock_response = '{"dnszones": [{"id": "example.com:2d0f862b-67cc-41f3-b6a2-59860d0aa90e", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "instance_id": "1407a753-a93f-4bb0-9784-bcfc269ee1b3", "name": "example.com", "description": "The DNS zone is used for VPCs in us-east region", "state": "pending_network_add", "label": "us-east"}], "offset": 0, "limit": 10, "total_count": 10, "first": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?limit=10"}, "next": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=1&limit=10"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        x_correlation_id = 'testString'
        offset = 38
        limit = 38
        vpc_id = 'testString'

        # Invoke method
        response = service.list_dnszones(
            instance_id,
            x_correlation_id=x_correlation_id,
            offset=offset,
            limit=limit,
            vpc_id=vpc_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'offset={}'.format(offset) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'vpc_id={}'.format(vpc_id) in query_string


    #--------------------------------------------------------
    # test_list_dnszones_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_dnszones_required_params(self):
        # Set up mock
        url = base_url + '/instances/testString/dnszones'
        mock_response = '{"dnszones": [{"id": "example.com:2d0f862b-67cc-41f3-b6a2-59860d0aa90e", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "instance_id": "1407a753-a93f-4bb0-9784-bcfc269ee1b3", "name": "example.com", "description": "The DNS zone is used for VPCs in us-east region", "state": "pending_network_add", "label": "us-east"}], "offset": 0, "limit": 10, "total_count": 10, "first": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?limit=10"}, "next": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=1&limit=10"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = service.list_dnszones(
            instance_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for create_dnszone
#-----------------------------------------------------------------------------
class TestCreateDnszone():

    #--------------------------------------------------------
    # create_dnszone()
    #--------------------------------------------------------
    @responses.activate
    def test_create_dnszone_all_params(self):
        # Set up mock
        url = base_url + '/instances/testString/dnszones'
        mock_response = '{"id": "example.com:2d0f862b-67cc-41f3-b6a2-59860d0aa90e", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "instance_id": "1407a753-a93f-4bb0-9784-bcfc269ee1b3", "name": "example.com", "description": "The DNS zone is used for VPCs in us-east region", "state": "pending_network_add", "label": "us-east"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        name = 'example.com'
        description = 'The DNS zone is used for VPCs in us-east region'
        label = 'us-east'
        x_correlation_id = 'testString'

        # Invoke method
        response = service.create_dnszone(
            instance_id,
            name=name,
            description=description,
            label=label,
            x_correlation_id=x_correlation_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == name
        assert req_body['description'] == description
        assert req_body['label'] == label


    #--------------------------------------------------------
    # test_create_dnszone_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_dnszone_required_params(self):
        # Set up mock
        url = base_url + '/instances/testString/dnszones'
        mock_response = '{"id": "example.com:2d0f862b-67cc-41f3-b6a2-59860d0aa90e", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "instance_id": "1407a753-a93f-4bb0-9784-bcfc269ee1b3", "name": "example.com", "description": "The DNS zone is used for VPCs in us-east region", "state": "pending_network_add", "label": "us-east"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = service.create_dnszone(
            instance_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for delete_dnszone
#-----------------------------------------------------------------------------
class TestDeleteDnszone():

    #--------------------------------------------------------
    # delete_dnszone()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_dnszone_all_params(self):
        # Set up mock
        url = base_url + '/instances/testString/dnszones/testString'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = service.delete_dnszone(
            instance_id,
            dnszone_id,
            x_correlation_id=x_correlation_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    #--------------------------------------------------------
    # test_delete_dnszone_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_dnszone_required_params(self):
        # Set up mock
        url = base_url + '/instances/testString/dnszones/testString'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'

        # Invoke method
        response = service.delete_dnszone(
            instance_id,
            dnszone_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


#-----------------------------------------------------------------------------
# Test Class for get_dnszone
#-----------------------------------------------------------------------------
class TestGetDnszone():

    #--------------------------------------------------------
    # get_dnszone()
    #--------------------------------------------------------
    @responses.activate
    def test_get_dnszone_all_params(self):
        # Set up mock
        url = base_url + '/instances/testString/dnszones/testString'
        mock_response = '{"id": "example.com:2d0f862b-67cc-41f3-b6a2-59860d0aa90e", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "instance_id": "1407a753-a93f-4bb0-9784-bcfc269ee1b3", "name": "example.com", "description": "The DNS zone is used for VPCs in us-east region", "state": "pending_network_add", "label": "us-east"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = service.get_dnszone(
            instance_id,
            dnszone_id,
            x_correlation_id=x_correlation_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_dnszone_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_dnszone_required_params(self):
        # Set up mock
        url = base_url + '/instances/testString/dnszones/testString'
        mock_response = '{"id": "example.com:2d0f862b-67cc-41f3-b6a2-59860d0aa90e", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "instance_id": "1407a753-a93f-4bb0-9784-bcfc269ee1b3", "name": "example.com", "description": "The DNS zone is used for VPCs in us-east region", "state": "pending_network_add", "label": "us-east"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'

        # Invoke method
        response = service.get_dnszone(
            instance_id,
            dnszone_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for update_dnszone
#-----------------------------------------------------------------------------
class TestUpdateDnszone():

    #--------------------------------------------------------
    # update_dnszone()
    #--------------------------------------------------------
    @responses.activate
    def test_update_dnszone_all_params(self):
        # Set up mock
        url = base_url + '/instances/testString/dnszones/testString'
        mock_response = '{"id": "example.com:2d0f862b-67cc-41f3-b6a2-59860d0aa90e", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "instance_id": "1407a753-a93f-4bb0-9784-bcfc269ee1b3", "name": "example.com", "description": "The DNS zone is used for VPCs in us-east region", "state": "pending_network_add", "label": "us-east"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        description = 'The DNS zone is used for VPCs in us-east region'
        label = 'us-east'
        x_correlation_id = 'testString'

        # Invoke method
        response = service.update_dnszone(
            instance_id,
            dnszone_id,
            description=description,
            label=label,
            x_correlation_id=x_correlation_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['description'] == description
        assert req_body['label'] == label


    #--------------------------------------------------------
    # test_update_dnszone_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_dnszone_required_params(self):
        # Set up mock
        url = base_url + '/instances/testString/dnszones/testString'
        mock_response = '{"id": "example.com:2d0f862b-67cc-41f3-b6a2-59860d0aa90e", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "instance_id": "1407a753-a93f-4bb0-9784-bcfc269ee1b3", "name": "example.com", "description": "The DNS zone is used for VPCs in us-east region", "state": "pending_network_add", "label": "us-east"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'

        # Invoke method
        response = service.update_dnszone(
            instance_id,
            dnszone_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: DNSZones
##############################################################################

