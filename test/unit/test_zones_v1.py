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
from ibm_cloud_networking_services.zones_v1 import ZonesV1

crn = 'testString'

service = ZonesV1(
    authenticator=NoAuthAuthenticator(),
    crn=crn
    )

base_url = 'https://api.cis.cloud.ibm.com'
service.set_service_url(base_url)

##############################################################################
# Start of Service: ListAllZones
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_zones
#-----------------------------------------------------------------------------
class TestListZones():

    #--------------------------------------------------------
    # list_zones()
    #--------------------------------------------------------
    @responses.activate
    def test_list_zones_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "test-example.com", "original_registrar": "GoDaddy", "original_dnshost": "NameCheap", "status": "active", "paused": false, "original_name_servers": ["ns1.originaldnshost.com"], "name_servers": ["ns001.name.cloud.ibm.com"]}], "result_info": {"page": 1, "per_page": 20, "count": 1, "total_count": 2000}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_zones()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_list_zones_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_zones_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "test-example.com", "original_registrar": "GoDaddy", "original_dnshost": "NameCheap", "status": "active", "paused": false, "original_name_servers": ["ns1.originaldnshost.com"], "name_servers": ["ns001.name.cloud.ibm.com"]}], "result_info": {"page": 1, "per_page": 20, "count": 1, "total_count": 2000}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_zones()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: ListAllZones
##############################################################################

##############################################################################
# Start of Service: GetAZone
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_zone
#-----------------------------------------------------------------------------
class TestGetZone():

    #--------------------------------------------------------
    # get_zone()
    #--------------------------------------------------------
    @responses.activate
    def test_get_zone_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "test-example.com", "original_registrar": "GoDaddy", "original_dnshost": "NameCheap", "status": "active", "paused": false, "original_name_servers": ["ns1.originaldnshost.com"], "name_servers": ["ns001.name.cloud.ibm.com"]}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        zone_identifier = 'testString'

        # Invoke method
        response = service.get_zone(
            zone_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_zone_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_zone_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "test-example.com", "original_registrar": "GoDaddy", "original_dnshost": "NameCheap", "status": "active", "paused": false, "original_name_servers": ["ns1.originaldnshost.com"], "name_servers": ["ns001.name.cloud.ibm.com"]}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        zone_identifier = 'testString'

        # Invoke method
        response = service.get_zone(
            zone_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: GetAZone
##############################################################################

##############################################################################
# Start of Service: UpdateAZone
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for update_zone
#-----------------------------------------------------------------------------
class TestUpdateZone():

    #--------------------------------------------------------
    # update_zone()
    #--------------------------------------------------------
    @responses.activate
    def test_update_zone_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "test-example.com", "original_registrar": "GoDaddy", "original_dnshost": "NameCheap", "status": "active", "paused": false, "original_name_servers": ["ns1.originaldnshost.com"], "name_servers": ["ns001.name.cloud.ibm.com"]}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        zone_identifier = 'testString'
        paused = False

        # Invoke method
        response = service.update_zone(
            zone_identifier,
            paused=paused,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['paused'] == paused


    #--------------------------------------------------------
    # test_update_zone_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_zone_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "test-example.com", "original_registrar": "GoDaddy", "original_dnshost": "NameCheap", "status": "active", "paused": false, "original_name_servers": ["ns1.originaldnshost.com"], "name_servers": ["ns001.name.cloud.ibm.com"]}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        zone_identifier = 'testString'

        # Invoke method
        response = service.update_zone(
            zone_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: UpdateAZone
##############################################################################

##############################################################################
# Start of Service: ZoneActivationCheck
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for zone_activation_check
#-----------------------------------------------------------------------------
class TestZoneActivationCheck():

    #--------------------------------------------------------
    # zone_activation_check()
    #--------------------------------------------------------
    @responses.activate
    def test_zone_activation_check_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/activation_check'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        zone_identifier = 'testString'

        # Invoke method
        response = service.zone_activation_check(
            zone_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_zone_activation_check_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_zone_activation_check_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/activation_check'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        zone_identifier = 'testString'

        # Invoke method
        response = service.zone_activation_check(
            zone_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: ZoneActivationCheck
##############################################################################

##############################################################################
# Start of Service: CreateAZone
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for create_zone
#-----------------------------------------------------------------------------
class TestCreateZone():

    #--------------------------------------------------------
    # create_zone()
    #--------------------------------------------------------
    @responses.activate
    def test_create_zone_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "test-example.com", "original_registrar": "GoDaddy", "original_dnshost": "NameCheap", "status": "active", "paused": false, "original_name_servers": ["ns1.originaldnshost.com"], "name_servers": ["ns001.name.cloud.ibm.com"]}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        name = 'test-example.com'

        # Invoke method
        response = service.create_zone(
            name=name,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == name


    #--------------------------------------------------------
    # test_create_zone_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_zone_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "test-example.com", "original_registrar": "GoDaddy", "original_dnshost": "NameCheap", "status": "active", "paused": false, "original_name_servers": ["ns1.originaldnshost.com"], "name_servers": ["ns001.name.cloud.ibm.com"]}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.create_zone()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: CreateAZone
##############################################################################

##############################################################################
# Start of Service: DeleteAZone
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for delete_zone
#-----------------------------------------------------------------------------
class TestDeleteZone():

    #--------------------------------------------------------
    # delete_zone()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_zone_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        zone_identifier = 'testString'

        # Invoke method
        response = service.delete_zone(
            zone_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_delete_zone_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_zone_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        zone_identifier = 'testString'

        # Invoke method
        response = service.delete_zone(
            zone_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: DeleteAZone
##############################################################################

