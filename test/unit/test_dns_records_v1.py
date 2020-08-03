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
import requests
import responses
from ibm_cloud_networking_services.dns_records_v1 import *

crn = 'testString'
zone_identifier = 'testString'

service = DnsRecordsV1(
    authenticator=NoAuthAuthenticator(),
    crn=crn,
    zone_identifier=zone_identifier
    )

base_url = 'https://api.cis.cloud.ibm.com'
service.set_service_url(base_url)

##############################################################################
# Start of Service: DNSRecords
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_all_dns_records
#-----------------------------------------------------------------------------
class TestListAllDnsRecords():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # list_all_dns_records()
    #--------------------------------------------------------
    @responses.activate
    def test_list_all_dns_records_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/dns_records')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "host-1.test-example.com", "type": "A", "content": "169.154.10.10", "zone_id": "023e105f4ecef8ad9ca31a8372d0c353", "zone_name": "test-example.com", "proxiable": true, "proxied": false, "ttl": 120, "priority": 5, "data": {"anyKey": "anyValue"}}], "result_info": {"page": 1, "per_page": 20, "count": 1, "total_count": 2000}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        type = 'testString'
        name = 'host1.test-example.com'
        content = '1.2.3.4'
        page = 38
        per_page = 5
        order = 'type'
        direction = 'asc'
        match = 'any'

        # Invoke method
        response = service.list_all_dns_records(
            type=type,
            name=name,
            content=content,
            page=page,
            per_page=per_page,
            order=order,
            direction=direction,
            match=match,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'type={}'.format(type) in query_string
        assert 'name={}'.format(name) in query_string
        assert 'content={}'.format(content) in query_string
        assert 'page={}'.format(page) in query_string
        assert 'per_page={}'.format(per_page) in query_string
        assert 'order={}'.format(order) in query_string
        assert 'direction={}'.format(direction) in query_string
        assert 'match={}'.format(match) in query_string


    #--------------------------------------------------------
    # test_list_all_dns_records_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_all_dns_records_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/dns_records')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "host-1.test-example.com", "type": "A", "content": "169.154.10.10", "zone_id": "023e105f4ecef8ad9ca31a8372d0c353", "zone_name": "test-example.com", "proxiable": true, "proxied": false, "ttl": 120, "priority": 5, "data": {"anyKey": "anyValue"}}], "result_info": {"page": 1, "per_page": 20, "count": 1, "total_count": 2000}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_all_dns_records()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_list_all_dns_records_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_list_all_dns_records_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/dns_records')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "host-1.test-example.com", "type": "A", "content": "169.154.10.10", "zone_id": "023e105f4ecef8ad9ca31a8372d0c353", "zone_name": "test-example.com", "proxiable": true, "proxied": false, "ttl": 120, "priority": 5, "data": {"anyKey": "anyValue"}}], "result_info": {"page": 1, "per_page": 20, "count": 1, "total_count": 2000}}'
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
                service.list_all_dns_records(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for create_dns_record
#-----------------------------------------------------------------------------
class TestCreateDnsRecord():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # create_dns_record()
    #--------------------------------------------------------
    @responses.activate
    def test_create_dns_record_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/dns_records')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "host-1.test-example.com", "type": "A", "content": "169.154.10.10", "zone_id": "023e105f4ecef8ad9ca31a8372d0c353", "zone_name": "test-example.com", "proxiable": true, "proxied": false, "ttl": 120, "priority": 5, "data": {"anyKey": "anyValue"}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        type = 'A'
        name = 'host-1.test-example.com'
        content = '1.2.3.4'
        priority = 5
        data = { 'foo': 'bar' }

        # Invoke method
        response = service.create_dns_record(
            type=type,
            name=name,
            content=content,
            priority=priority,
            data=data,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['type'] == 'A'
        assert req_body['name'] == 'host-1.test-example.com'
        assert req_body['content'] == '1.2.3.4'
        assert req_body['priority'] == 5
        assert req_body['data'] == { 'foo': 'bar' }


    #--------------------------------------------------------
    # test_create_dns_record_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_dns_record_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/dns_records')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "host-1.test-example.com", "type": "A", "content": "169.154.10.10", "zone_id": "023e105f4ecef8ad9ca31a8372d0c353", "zone_name": "test-example.com", "proxiable": true, "proxied": false, "ttl": 120, "priority": 5, "data": {"anyKey": "anyValue"}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.create_dns_record()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_create_dns_record_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_create_dns_record_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/dns_records')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "host-1.test-example.com", "type": "A", "content": "169.154.10.10", "zone_id": "023e105f4ecef8ad9ca31a8372d0c353", "zone_name": "test-example.com", "proxiable": true, "proxied": false, "ttl": 120, "priority": 5, "data": {"anyKey": "anyValue"}}}'
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
                service.create_dns_record(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for delete_dns_record
#-----------------------------------------------------------------------------
class TestDeleteDnsRecord():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # delete_dns_record()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_dns_record_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/dns_records/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        dnsrecord_identifier = 'testString'

        # Invoke method
        response = service.delete_dns_record(
            dnsrecord_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_delete_dns_record_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_dns_record_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/dns_records/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        dnsrecord_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "dnsrecord_identifier": dnsrecord_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_dns_record(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_dns_record
#-----------------------------------------------------------------------------
class TestGetDnsRecord():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_dns_record()
    #--------------------------------------------------------
    @responses.activate
    def test_get_dns_record_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/dns_records/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "host-1.test-example.com", "type": "A", "content": "169.154.10.10", "zone_id": "023e105f4ecef8ad9ca31a8372d0c353", "zone_name": "test-example.com", "proxiable": true, "proxied": false, "ttl": 120, "priority": 5, "data": {"anyKey": "anyValue"}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        dnsrecord_identifier = 'testString'

        # Invoke method
        response = service.get_dns_record(
            dnsrecord_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_dns_record_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_dns_record_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/dns_records/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "host-1.test-example.com", "type": "A", "content": "169.154.10.10", "zone_id": "023e105f4ecef8ad9ca31a8372d0c353", "zone_name": "test-example.com", "proxiable": true, "proxied": false, "ttl": 120, "priority": 5, "data": {"anyKey": "anyValue"}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        dnsrecord_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "dnsrecord_identifier": dnsrecord_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_dns_record(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_dns_record
#-----------------------------------------------------------------------------
class TestUpdateDnsRecord():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_dns_record()
    #--------------------------------------------------------
    @responses.activate
    def test_update_dns_record_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/dns_records/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "host-1.test-example.com", "type": "A", "content": "169.154.10.10", "zone_id": "023e105f4ecef8ad9ca31a8372d0c353", "zone_name": "test-example.com", "proxiable": true, "proxied": false, "ttl": 120, "priority": 5, "data": {"anyKey": "anyValue"}}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        dnsrecord_identifier = 'testString'
        type = 'A'
        name = 'host-1.test-example.com'
        content = '1.2.3.4'
        priority = 5
        proxied = False
        data = { 'foo': 'bar' }

        # Invoke method
        response = service.update_dns_record(
            dnsrecord_identifier,
            type=type,
            name=name,
            content=content,
            priority=priority,
            proxied=proxied,
            data=data,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['type'] == 'A'
        assert req_body['name'] == 'host-1.test-example.com'
        assert req_body['content'] == '1.2.3.4'
        assert req_body['priority'] == 5
        assert req_body['proxied'] == False
        assert req_body['data'] == { 'foo': 'bar' }


    #--------------------------------------------------------
    # test_update_dns_record_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_dns_record_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/dns_records/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "host-1.test-example.com", "type": "A", "content": "169.154.10.10", "zone_id": "023e105f4ecef8ad9ca31a8372d0c353", "zone_name": "test-example.com", "proxiable": true, "proxied": false, "ttl": 120, "priority": 5, "data": {"anyKey": "anyValue"}}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        dnsrecord_identifier = 'testString'

        # Invoke method
        response = service.update_dns_record(
            dnsrecord_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_dns_record_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_dns_record_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/dns_records/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "host-1.test-example.com", "type": "A", "content": "169.154.10.10", "zone_id": "023e105f4ecef8ad9ca31a8372d0c353", "zone_name": "test-example.com", "proxiable": true, "proxied": false, "ttl": 120, "priority": 5, "data": {"anyKey": "anyValue"}}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        dnsrecord_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "dnsrecord_identifier": dnsrecord_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.update_dns_record(**req_copy)



# endregion
##############################################################################
# End of Service: DNSRecords
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
#-----------------------------------------------------------------------------
# Test Class for DeleteDnsrecordRespResult
#-----------------------------------------------------------------------------
class TestDeleteDnsrecordRespResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for DeleteDnsrecordRespResult
    #--------------------------------------------------------
    def test_delete_dnsrecord_resp_result_serialization(self):

        # Construct a json representation of a DeleteDnsrecordRespResult model
        delete_dnsrecord_resp_result_model_json = {}
        delete_dnsrecord_resp_result_model_json['id'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'

        # Construct a model instance of DeleteDnsrecordRespResult by calling from_dict on the json representation
        delete_dnsrecord_resp_result_model = DeleteDnsrecordRespResult.from_dict(delete_dnsrecord_resp_result_model_json)
        assert delete_dnsrecord_resp_result_model != False

        # Construct a model instance of DeleteDnsrecordRespResult by calling from_dict on the json representation
        delete_dnsrecord_resp_result_model_dict = DeleteDnsrecordRespResult.from_dict(delete_dnsrecord_resp_result_model_json).__dict__
        delete_dnsrecord_resp_result_model2 = DeleteDnsrecordRespResult(**delete_dnsrecord_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert delete_dnsrecord_resp_result_model == delete_dnsrecord_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        delete_dnsrecord_resp_result_model_json2 = delete_dnsrecord_resp_result_model.to_dict()
        assert delete_dnsrecord_resp_result_model_json2 == delete_dnsrecord_resp_result_model_json

#-----------------------------------------------------------------------------
# Test Class for DeleteDnsrecordResp
#-----------------------------------------------------------------------------
class TestDeleteDnsrecordResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for DeleteDnsrecordResp
    #--------------------------------------------------------
    def test_delete_dnsrecord_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        delete_dnsrecord_resp_result_model = {} # DeleteDnsrecordRespResult
        delete_dnsrecord_resp_result_model['id'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'

        # Construct a json representation of a DeleteDnsrecordResp model
        delete_dnsrecord_resp_model_json = {}
        delete_dnsrecord_resp_model_json['success'] = True
        delete_dnsrecord_resp_model_json['errors'] = [['testString']]
        delete_dnsrecord_resp_model_json['messages'] = [['testString']]
        delete_dnsrecord_resp_model_json['result'] = delete_dnsrecord_resp_result_model

        # Construct a model instance of DeleteDnsrecordResp by calling from_dict on the json representation
        delete_dnsrecord_resp_model = DeleteDnsrecordResp.from_dict(delete_dnsrecord_resp_model_json)
        assert delete_dnsrecord_resp_model != False

        # Construct a model instance of DeleteDnsrecordResp by calling from_dict on the json representation
        delete_dnsrecord_resp_model_dict = DeleteDnsrecordResp.from_dict(delete_dnsrecord_resp_model_json).__dict__
        delete_dnsrecord_resp_model2 = DeleteDnsrecordResp(**delete_dnsrecord_resp_model_dict)

        # Verify the model instances are equivalent
        assert delete_dnsrecord_resp_model == delete_dnsrecord_resp_model2

        # Convert model instance back to dict and verify no loss of data
        delete_dnsrecord_resp_model_json2 = delete_dnsrecord_resp_model.to_dict()
        assert delete_dnsrecord_resp_model_json2 == delete_dnsrecord_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for DnsrecordDetails
#-----------------------------------------------------------------------------
class TestDnsrecordDetails():

    #--------------------------------------------------------
    # Test serialization/deserialization for DnsrecordDetails
    #--------------------------------------------------------
    def test_dnsrecord_details_serialization(self):

        # Construct a json representation of a DnsrecordDetails model
        dnsrecord_details_model_json = {}
        dnsrecord_details_model_json['id'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'
        dnsrecord_details_model_json['created_on'] = '2014-01-01T05:20:00.12345Z'
        dnsrecord_details_model_json['modified_on'] = '2014-01-01T05:20:00.12345Z'
        dnsrecord_details_model_json['name'] = 'host-1.test-example.com'
        dnsrecord_details_model_json['type'] = 'A'
        dnsrecord_details_model_json['content'] = '169.154.10.10'
        dnsrecord_details_model_json['zone_id'] = '023e105f4ecef8ad9ca31a8372d0c353'
        dnsrecord_details_model_json['zone_name'] = 'test-example.com'
        dnsrecord_details_model_json['proxiable'] = True
        dnsrecord_details_model_json['proxied'] = False
        dnsrecord_details_model_json['ttl'] = 120
        dnsrecord_details_model_json['priority'] = 5
        dnsrecord_details_model_json['data'] = { 'foo': 'bar' }

        # Construct a model instance of DnsrecordDetails by calling from_dict on the json representation
        dnsrecord_details_model = DnsrecordDetails.from_dict(dnsrecord_details_model_json)
        assert dnsrecord_details_model != False

        # Construct a model instance of DnsrecordDetails by calling from_dict on the json representation
        dnsrecord_details_model_dict = DnsrecordDetails.from_dict(dnsrecord_details_model_json).__dict__
        dnsrecord_details_model2 = DnsrecordDetails(**dnsrecord_details_model_dict)

        # Verify the model instances are equivalent
        assert dnsrecord_details_model == dnsrecord_details_model2

        # Convert model instance back to dict and verify no loss of data
        dnsrecord_details_model_json2 = dnsrecord_details_model.to_dict()
        assert dnsrecord_details_model_json2 == dnsrecord_details_model_json

#-----------------------------------------------------------------------------
# Test Class for DnsrecordResp
#-----------------------------------------------------------------------------
class TestDnsrecordResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for DnsrecordResp
    #--------------------------------------------------------
    def test_dnsrecord_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        dnsrecord_details_model = {} # DnsrecordDetails
        dnsrecord_details_model['id'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'
        dnsrecord_details_model['created_on'] = '2014-01-01T05:20:00.12345Z'
        dnsrecord_details_model['modified_on'] = '2014-01-01T05:20:00.12345Z'
        dnsrecord_details_model['name'] = 'host-1.test-example.com'
        dnsrecord_details_model['type'] = 'A'
        dnsrecord_details_model['content'] = '169.154.10.10'
        dnsrecord_details_model['zone_id'] = '023e105f4ecef8ad9ca31a8372d0c353'
        dnsrecord_details_model['zone_name'] = 'test-example.com'
        dnsrecord_details_model['proxiable'] = True
        dnsrecord_details_model['proxied'] = False
        dnsrecord_details_model['ttl'] = 120
        dnsrecord_details_model['priority'] = 5
        dnsrecord_details_model['data'] = { 'foo': 'bar' }

        # Construct a json representation of a DnsrecordResp model
        dnsrecord_resp_model_json = {}
        dnsrecord_resp_model_json['success'] = True
        dnsrecord_resp_model_json['errors'] = [['testString']]
        dnsrecord_resp_model_json['messages'] = [['testString']]
        dnsrecord_resp_model_json['result'] = dnsrecord_details_model

        # Construct a model instance of DnsrecordResp by calling from_dict on the json representation
        dnsrecord_resp_model = DnsrecordResp.from_dict(dnsrecord_resp_model_json)
        assert dnsrecord_resp_model != False

        # Construct a model instance of DnsrecordResp by calling from_dict on the json representation
        dnsrecord_resp_model_dict = DnsrecordResp.from_dict(dnsrecord_resp_model_json).__dict__
        dnsrecord_resp_model2 = DnsrecordResp(**dnsrecord_resp_model_dict)

        # Verify the model instances are equivalent
        assert dnsrecord_resp_model == dnsrecord_resp_model2

        # Convert model instance back to dict and verify no loss of data
        dnsrecord_resp_model_json2 = dnsrecord_resp_model.to_dict()
        assert dnsrecord_resp_model_json2 == dnsrecord_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for ListDnsrecordsResp
#-----------------------------------------------------------------------------
class TestListDnsrecordsResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for ListDnsrecordsResp
    #--------------------------------------------------------
    def test_list_dnsrecords_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        dnsrecord_details_model = {} # DnsrecordDetails
        dnsrecord_details_model['id'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'
        dnsrecord_details_model['created_on'] = '2014-01-01T05:20:00.12345Z'
        dnsrecord_details_model['modified_on'] = '2014-01-01T05:20:00.12345Z'
        dnsrecord_details_model['name'] = 'host-1.test-example.com'
        dnsrecord_details_model['type'] = 'A'
        dnsrecord_details_model['content'] = '169.154.10.10'
        dnsrecord_details_model['zone_id'] = '023e105f4ecef8ad9ca31a8372d0c353'
        dnsrecord_details_model['zone_name'] = 'test-example.com'
        dnsrecord_details_model['proxiable'] = True
        dnsrecord_details_model['proxied'] = False
        dnsrecord_details_model['ttl'] = 120
        dnsrecord_details_model['priority'] = 5
        dnsrecord_details_model['data'] = { 'foo': 'bar' }

        result_info_model = {} # ResultInfo
        result_info_model['page'] = 1
        result_info_model['per_page'] = 20
        result_info_model['count'] = 1
        result_info_model['total_count'] = 2000

        # Construct a json representation of a ListDnsrecordsResp model
        list_dnsrecords_resp_model_json = {}
        list_dnsrecords_resp_model_json['success'] = True
        list_dnsrecords_resp_model_json['errors'] = [['testString']]
        list_dnsrecords_resp_model_json['messages'] = [['testString']]
        list_dnsrecords_resp_model_json['result'] = [dnsrecord_details_model]
        list_dnsrecords_resp_model_json['result_info'] = result_info_model

        # Construct a model instance of ListDnsrecordsResp by calling from_dict on the json representation
        list_dnsrecords_resp_model = ListDnsrecordsResp.from_dict(list_dnsrecords_resp_model_json)
        assert list_dnsrecords_resp_model != False

        # Construct a model instance of ListDnsrecordsResp by calling from_dict on the json representation
        list_dnsrecords_resp_model_dict = ListDnsrecordsResp.from_dict(list_dnsrecords_resp_model_json).__dict__
        list_dnsrecords_resp_model2 = ListDnsrecordsResp(**list_dnsrecords_resp_model_dict)

        # Verify the model instances are equivalent
        assert list_dnsrecords_resp_model == list_dnsrecords_resp_model2

        # Convert model instance back to dict and verify no loss of data
        list_dnsrecords_resp_model_json2 = list_dnsrecords_resp_model.to_dict()
        assert list_dnsrecords_resp_model_json2 == list_dnsrecords_resp_model_json

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


# endregion
##############################################################################
# End of Model Tests
##############################################################################
