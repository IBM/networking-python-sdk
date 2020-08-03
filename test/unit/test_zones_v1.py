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
from ibm_cloud_networking_services.zones_v1 import *

crn = 'testString'

service = ZonesV1(
    authenticator=NoAuthAuthenticator(),
    crn=crn
    )

base_url = 'https://api.cis.cloud.ibm.com'
service.set_service_url(base_url)

##############################################################################
# Start of Service: CISZones
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_zones
#-----------------------------------------------------------------------------
class TestListZones():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # list_zones()
    #--------------------------------------------------------
    @responses.activate
    def test_list_zones_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones')
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
    # test_list_zones_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_list_zones_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "test-example.com", "original_registrar": "GoDaddy", "original_dnshost": "NameCheap", "status": "active", "paused": false, "original_name_servers": ["ns1.originaldnshost.com"], "name_servers": ["ns001.name.cloud.ibm.com"]}], "result_info": {"page": 1, "per_page": 20, "count": 1, "total_count": 2000}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.list_zones(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for create_zone
#-----------------------------------------------------------------------------
class TestCreateZone():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # create_zone()
    #--------------------------------------------------------
    @responses.activate
    def test_create_zone_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones')
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
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'test-example.com'


    #--------------------------------------------------------
    # test_create_zone_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_zone_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones')
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


    #--------------------------------------------------------
    # test_create_zone_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_create_zone_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "test-example.com", "original_registrar": "GoDaddy", "original_dnshost": "NameCheap", "status": "active", "paused": false, "original_name_servers": ["ns1.originaldnshost.com"], "name_servers": ["ns001.name.cloud.ibm.com"]}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.create_zone(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for delete_zone
#-----------------------------------------------------------------------------
class TestDeleteZone():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # delete_zone()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_zone_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString')
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
            zone_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_delete_zone_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_zone_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        zone_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "zone_identifier": zone_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_zone(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_zone
#-----------------------------------------------------------------------------
class TestGetZone():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_zone()
    #--------------------------------------------------------
    @responses.activate
    def test_get_zone_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString')
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
            zone_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_zone_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_zone_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "test-example.com", "original_registrar": "GoDaddy", "original_dnshost": "NameCheap", "status": "active", "paused": false, "original_name_servers": ["ns1.originaldnshost.com"], "name_servers": ["ns001.name.cloud.ibm.com"]}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        zone_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "zone_identifier": zone_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_zone(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_zone
#-----------------------------------------------------------------------------
class TestUpdateZone():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_zone()
    #--------------------------------------------------------
    @responses.activate
    def test_update_zone_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString')
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
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['paused'] == False


    #--------------------------------------------------------
    # test_update_zone_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_zone_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString')
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
            zone_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_zone_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_zone_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "test-example.com", "original_registrar": "GoDaddy", "original_dnshost": "NameCheap", "status": "active", "paused": false, "original_name_servers": ["ns1.originaldnshost.com"], "name_servers": ["ns001.name.cloud.ibm.com"]}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        zone_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "zone_identifier": zone_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.update_zone(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for zone_activation_check
#-----------------------------------------------------------------------------
class TestZoneActivationCheck():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # zone_activation_check()
    #--------------------------------------------------------
    @responses.activate
    def test_zone_activation_check_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/activation_check')
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
            zone_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_zone_activation_check_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_zone_activation_check_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/activation_check')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        zone_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "zone_identifier": zone_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.zone_activation_check(**req_copy)



# endregion
##############################################################################
# End of Service: CISZones
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
#-----------------------------------------------------------------------------
# Test Class for DeleteZoneRespResult
#-----------------------------------------------------------------------------
class TestDeleteZoneRespResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for DeleteZoneRespResult
    #--------------------------------------------------------
    def test_delete_zone_resp_result_serialization(self):

        # Construct a json representation of a DeleteZoneRespResult model
        delete_zone_resp_result_model_json = {}
        delete_zone_resp_result_model_json['id'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'

        # Construct a model instance of DeleteZoneRespResult by calling from_dict on the json representation
        delete_zone_resp_result_model = DeleteZoneRespResult.from_dict(delete_zone_resp_result_model_json)
        assert delete_zone_resp_result_model != False

        # Construct a model instance of DeleteZoneRespResult by calling from_dict on the json representation
        delete_zone_resp_result_model_dict = DeleteZoneRespResult.from_dict(delete_zone_resp_result_model_json).__dict__
        delete_zone_resp_result_model2 = DeleteZoneRespResult(**delete_zone_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert delete_zone_resp_result_model == delete_zone_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        delete_zone_resp_result_model_json2 = delete_zone_resp_result_model.to_dict()
        assert delete_zone_resp_result_model_json2 == delete_zone_resp_result_model_json

#-----------------------------------------------------------------------------
# Test Class for ZoneActivationcheckRespResult
#-----------------------------------------------------------------------------
class TestZoneActivationcheckRespResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for ZoneActivationcheckRespResult
    #--------------------------------------------------------
    def test_zone_activationcheck_resp_result_serialization(self):

        # Construct a json representation of a ZoneActivationcheckRespResult model
        zone_activationcheck_resp_result_model_json = {}
        zone_activationcheck_resp_result_model_json['id'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'

        # Construct a model instance of ZoneActivationcheckRespResult by calling from_dict on the json representation
        zone_activationcheck_resp_result_model = ZoneActivationcheckRespResult.from_dict(zone_activationcheck_resp_result_model_json)
        assert zone_activationcheck_resp_result_model != False

        # Construct a model instance of ZoneActivationcheckRespResult by calling from_dict on the json representation
        zone_activationcheck_resp_result_model_dict = ZoneActivationcheckRespResult.from_dict(zone_activationcheck_resp_result_model_json).__dict__
        zone_activationcheck_resp_result_model2 = ZoneActivationcheckRespResult(**zone_activationcheck_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert zone_activationcheck_resp_result_model == zone_activationcheck_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        zone_activationcheck_resp_result_model_json2 = zone_activationcheck_resp_result_model.to_dict()
        assert zone_activationcheck_resp_result_model_json2 == zone_activationcheck_resp_result_model_json

#-----------------------------------------------------------------------------
# Test Class for DeleteZoneResp
#-----------------------------------------------------------------------------
class TestDeleteZoneResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for DeleteZoneResp
    #--------------------------------------------------------
    def test_delete_zone_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        delete_zone_resp_result_model = {} # DeleteZoneRespResult
        delete_zone_resp_result_model['id'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'

        # Construct a json representation of a DeleteZoneResp model
        delete_zone_resp_model_json = {}
        delete_zone_resp_model_json['success'] = True
        delete_zone_resp_model_json['errors'] = [['testString']]
        delete_zone_resp_model_json['messages'] = [['testString']]
        delete_zone_resp_model_json['result'] = delete_zone_resp_result_model

        # Construct a model instance of DeleteZoneResp by calling from_dict on the json representation
        delete_zone_resp_model = DeleteZoneResp.from_dict(delete_zone_resp_model_json)
        assert delete_zone_resp_model != False

        # Construct a model instance of DeleteZoneResp by calling from_dict on the json representation
        delete_zone_resp_model_dict = DeleteZoneResp.from_dict(delete_zone_resp_model_json).__dict__
        delete_zone_resp_model2 = DeleteZoneResp(**delete_zone_resp_model_dict)

        # Verify the model instances are equivalent
        assert delete_zone_resp_model == delete_zone_resp_model2

        # Convert model instance back to dict and verify no loss of data
        delete_zone_resp_model_json2 = delete_zone_resp_model.to_dict()
        assert delete_zone_resp_model_json2 == delete_zone_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for ListZonesResp
#-----------------------------------------------------------------------------
class TestListZonesResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for ListZonesResp
    #--------------------------------------------------------
    def test_list_zones_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        result_info_model = {} # ResultInfo
        result_info_model['page'] = 1
        result_info_model['per_page'] = 20
        result_info_model['count'] = 1
        result_info_model['total_count'] = 2000

        zone_details_model = {} # ZoneDetails
        zone_details_model['id'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'
        zone_details_model['created_on'] = '2014-01-01T05:20:00.12345Z'
        zone_details_model['modified_on'] = '2014-01-01T05:20:00.12345Z'
        zone_details_model['name'] = 'test-example.com'
        zone_details_model['original_registrar'] = 'GoDaddy'
        zone_details_model['original_dnshost'] = 'NameCheap'
        zone_details_model['status'] = 'active'
        zone_details_model['paused'] = False
        zone_details_model['original_name_servers'] = ['ns1.originaldnshost.com']
        zone_details_model['name_servers'] = ['ns001.name.cloud.ibm.com']

        # Construct a json representation of a ListZonesResp model
        list_zones_resp_model_json = {}
        list_zones_resp_model_json['success'] = True
        list_zones_resp_model_json['errors'] = [['testString']]
        list_zones_resp_model_json['messages'] = [['testString']]
        list_zones_resp_model_json['result'] = [zone_details_model]
        list_zones_resp_model_json['result_info'] = result_info_model

        # Construct a model instance of ListZonesResp by calling from_dict on the json representation
        list_zones_resp_model = ListZonesResp.from_dict(list_zones_resp_model_json)
        assert list_zones_resp_model != False

        # Construct a model instance of ListZonesResp by calling from_dict on the json representation
        list_zones_resp_model_dict = ListZonesResp.from_dict(list_zones_resp_model_json).__dict__
        list_zones_resp_model2 = ListZonesResp(**list_zones_resp_model_dict)

        # Verify the model instances are equivalent
        assert list_zones_resp_model == list_zones_resp_model2

        # Convert model instance back to dict and verify no loss of data
        list_zones_resp_model_json2 = list_zones_resp_model.to_dict()
        assert list_zones_resp_model_json2 == list_zones_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for ResultInfo
#-----------------------------------------------------------------------------
class TestResultInfo():

    #--------------------------------------------------------
    # Test serialization/deserialization for ResultInfo
    #--------------------------------------------------------
    def test_result_info_serialization(self):

        # Construct a json representation of a ResultInfo model
        result_info_model_json = {}
        result_info_model_json['page'] = 1
        result_info_model_json['per_page'] = 20
        result_info_model_json['count'] = 1
        result_info_model_json['total_count'] = 2000

        # Construct a model instance of ResultInfo by calling from_dict on the json representation
        result_info_model = ResultInfo.from_dict(result_info_model_json)
        assert result_info_model != False

        # Construct a model instance of ResultInfo by calling from_dict on the json representation
        result_info_model_dict = ResultInfo.from_dict(result_info_model_json).__dict__
        result_info_model2 = ResultInfo(**result_info_model_dict)

        # Verify the model instances are equivalent
        assert result_info_model == result_info_model2

        # Convert model instance back to dict and verify no loss of data
        result_info_model_json2 = result_info_model.to_dict()
        assert result_info_model_json2 == result_info_model_json

#-----------------------------------------------------------------------------
# Test Class for ZoneActivationcheckResp
#-----------------------------------------------------------------------------
class TestZoneActivationcheckResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for ZoneActivationcheckResp
    #--------------------------------------------------------
    def test_zone_activationcheck_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        zone_activationcheck_resp_result_model = {} # ZoneActivationcheckRespResult
        zone_activationcheck_resp_result_model['id'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'

        # Construct a json representation of a ZoneActivationcheckResp model
        zone_activationcheck_resp_model_json = {}
        zone_activationcheck_resp_model_json['success'] = True
        zone_activationcheck_resp_model_json['errors'] = [['testString']]
        zone_activationcheck_resp_model_json['messages'] = [['testString']]
        zone_activationcheck_resp_model_json['result'] = zone_activationcheck_resp_result_model

        # Construct a model instance of ZoneActivationcheckResp by calling from_dict on the json representation
        zone_activationcheck_resp_model = ZoneActivationcheckResp.from_dict(zone_activationcheck_resp_model_json)
        assert zone_activationcheck_resp_model != False

        # Construct a model instance of ZoneActivationcheckResp by calling from_dict on the json representation
        zone_activationcheck_resp_model_dict = ZoneActivationcheckResp.from_dict(zone_activationcheck_resp_model_json).__dict__
        zone_activationcheck_resp_model2 = ZoneActivationcheckResp(**zone_activationcheck_resp_model_dict)

        # Verify the model instances are equivalent
        assert zone_activationcheck_resp_model == zone_activationcheck_resp_model2

        # Convert model instance back to dict and verify no loss of data
        zone_activationcheck_resp_model_json2 = zone_activationcheck_resp_model.to_dict()
        assert zone_activationcheck_resp_model_json2 == zone_activationcheck_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for ZoneDetails
#-----------------------------------------------------------------------------
class TestZoneDetails():

    #--------------------------------------------------------
    # Test serialization/deserialization for ZoneDetails
    #--------------------------------------------------------
    def test_zone_details_serialization(self):

        # Construct a json representation of a ZoneDetails model
        zone_details_model_json = {}
        zone_details_model_json['id'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'
        zone_details_model_json['created_on'] = '2014-01-01T05:20:00.12345Z'
        zone_details_model_json['modified_on'] = '2014-01-01T05:20:00.12345Z'
        zone_details_model_json['name'] = 'test-example.com'
        zone_details_model_json['original_registrar'] = 'GoDaddy'
        zone_details_model_json['original_dnshost'] = 'NameCheap'
        zone_details_model_json['status'] = 'active'
        zone_details_model_json['paused'] = False
        zone_details_model_json['original_name_servers'] = ['ns1.originaldnshost.com']
        zone_details_model_json['name_servers'] = ['ns001.name.cloud.ibm.com']

        # Construct a model instance of ZoneDetails by calling from_dict on the json representation
        zone_details_model = ZoneDetails.from_dict(zone_details_model_json)
        assert zone_details_model != False

        # Construct a model instance of ZoneDetails by calling from_dict on the json representation
        zone_details_model_dict = ZoneDetails.from_dict(zone_details_model_json).__dict__
        zone_details_model2 = ZoneDetails(**zone_details_model_dict)

        # Verify the model instances are equivalent
        assert zone_details_model == zone_details_model2

        # Convert model instance back to dict and verify no loss of data
        zone_details_model_json2 = zone_details_model.to_dict()
        assert zone_details_model_json2 == zone_details_model_json

#-----------------------------------------------------------------------------
# Test Class for ZoneResp
#-----------------------------------------------------------------------------
class TestZoneResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for ZoneResp
    #--------------------------------------------------------
    def test_zone_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        zone_details_model = {} # ZoneDetails
        zone_details_model['id'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'
        zone_details_model['created_on'] = '2014-01-01T05:20:00.12345Z'
        zone_details_model['modified_on'] = '2014-01-01T05:20:00.12345Z'
        zone_details_model['name'] = 'test-example.com'
        zone_details_model['original_registrar'] = 'GoDaddy'
        zone_details_model['original_dnshost'] = 'NameCheap'
        zone_details_model['status'] = 'active'
        zone_details_model['paused'] = False
        zone_details_model['original_name_servers'] = ['ns1.originaldnshost.com']
        zone_details_model['name_servers'] = ['ns001.name.cloud.ibm.com']

        # Construct a json representation of a ZoneResp model
        zone_resp_model_json = {}
        zone_resp_model_json['success'] = True
        zone_resp_model_json['errors'] = [['testString']]
        zone_resp_model_json['messages'] = [['testString']]
        zone_resp_model_json['result'] = zone_details_model

        # Construct a model instance of ZoneResp by calling from_dict on the json representation
        zone_resp_model = ZoneResp.from_dict(zone_resp_model_json)
        assert zone_resp_model != False

        # Construct a model instance of ZoneResp by calling from_dict on the json representation
        zone_resp_model_dict = ZoneResp.from_dict(zone_resp_model_json).__dict__
        zone_resp_model2 = ZoneResp(**zone_resp_model_dict)

        # Verify the model instances are equivalent
        assert zone_resp_model == zone_resp_model2

        # Convert model instance back to dict and verify no loss of data
        zone_resp_model_json2 = zone_resp_model.to_dict()
        assert zone_resp_model_json2 == zone_resp_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
