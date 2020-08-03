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
import io
import json
import pytest
import re
import responses
import tempfile
from ibm_cloud_networking_services.dns_record_bulk_v1 import *

crn = 'testString'
zone_identifier = 'testString'

service = DnsRecordBulkV1(
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
# Test Class for get_dns_records_bulk
#-----------------------------------------------------------------------------
class TestGetDnsRecordsBulk():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_dns_records_bulk()
    #--------------------------------------------------------
    @responses.activate
    def test_get_dns_records_bulk_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/dns_records_bulk')
        mock_response = '"unknown property type: operation_response"'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='text/plain; charset=utf-8',
                      status=200)

        # Invoke method
        response = service.get_dns_records_bulk()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_dns_records_bulk_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_dns_records_bulk_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/dns_records_bulk')
        mock_response = '"unknown property type: operation_response"'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='text/plain; charset=utf-8',
                      status=200)

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_dns_records_bulk(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for post_dns_records_bulk
#-----------------------------------------------------------------------------
class TestPostDnsRecordsBulk():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # post_dns_records_bulk()
    #--------------------------------------------------------
    @responses.activate
    def test_post_dns_records_bulk_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/dns_records_bulk')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [{"code": 4, "message": "message"}], "result": {"recs_added": 5, "total_records_parsed": 5}, "timing": {"start_time": "2014-03-01T12:20:00Z", "end_time": "2014-03-01T12:20:01Z", "process_time": 1}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        file = io.BytesIO(b'This is a mock file.').getvalue()
        file_content_type = 'testString'

        # Invoke method
        response = service.post_dns_records_bulk(
            file=file,
            file_content_type=file_content_type,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_post_dns_records_bulk_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_post_dns_records_bulk_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/dns_records_bulk')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [{"code": 4, "message": "message"}], "result": {"recs_added": 5, "total_records_parsed": 5}, "timing": {"start_time": "2014-03-01T12:20:00Z", "end_time": "2014-03-01T12:20:01Z", "process_time": 1}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.post_dns_records_bulk()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_post_dns_records_bulk_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_post_dns_records_bulk_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/dns_records_bulk')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [{"code": 4, "message": "message"}], "result": {"recs_added": 5, "total_records_parsed": 5}, "timing": {"start_time": "2014-03-01T12:20:00Z", "end_time": "2014-03-01T12:20:01Z", "process_time": 1}}'
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
                service.post_dns_records_bulk(**req_copy)



# endregion
##############################################################################
# End of Service: DNSRecords
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
#-----------------------------------------------------------------------------
# Test Class for DnsRecordsObjectMessagesItem
#-----------------------------------------------------------------------------
class TestDnsRecordsObjectMessagesItem():

    #--------------------------------------------------------
    # Test serialization/deserialization for DnsRecordsObjectMessagesItem
    #--------------------------------------------------------
    def test_dns_records_object_messages_item_serialization(self):

        # Construct a json representation of a DnsRecordsObjectMessagesItem model
        dns_records_object_messages_item_model_json = {}
        dns_records_object_messages_item_model_json['code'] = 38
        dns_records_object_messages_item_model_json['message'] = 'testString'

        # Construct a model instance of DnsRecordsObjectMessagesItem by calling from_dict on the json representation
        dns_records_object_messages_item_model = DnsRecordsObjectMessagesItem.from_dict(dns_records_object_messages_item_model_json)
        assert dns_records_object_messages_item_model != False

        # Construct a model instance of DnsRecordsObjectMessagesItem by calling from_dict on the json representation
        dns_records_object_messages_item_model_dict = DnsRecordsObjectMessagesItem.from_dict(dns_records_object_messages_item_model_json).__dict__
        dns_records_object_messages_item_model2 = DnsRecordsObjectMessagesItem(**dns_records_object_messages_item_model_dict)

        # Verify the model instances are equivalent
        assert dns_records_object_messages_item_model == dns_records_object_messages_item_model2

        # Convert model instance back to dict and verify no loss of data
        dns_records_object_messages_item_model_json2 = dns_records_object_messages_item_model.to_dict()
        assert dns_records_object_messages_item_model_json2 == dns_records_object_messages_item_model_json

#-----------------------------------------------------------------------------
# Test Class for DnsRecordsObjectResult
#-----------------------------------------------------------------------------
class TestDnsRecordsObjectResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for DnsRecordsObjectResult
    #--------------------------------------------------------
    def test_dns_records_object_result_serialization(self):

        # Construct a json representation of a DnsRecordsObjectResult model
        dns_records_object_result_model_json = {}
        dns_records_object_result_model_json['recs_added'] = 5
        dns_records_object_result_model_json['total_records_parsed'] = 5

        # Construct a model instance of DnsRecordsObjectResult by calling from_dict on the json representation
        dns_records_object_result_model = DnsRecordsObjectResult.from_dict(dns_records_object_result_model_json)
        assert dns_records_object_result_model != False

        # Construct a model instance of DnsRecordsObjectResult by calling from_dict on the json representation
        dns_records_object_result_model_dict = DnsRecordsObjectResult.from_dict(dns_records_object_result_model_json).__dict__
        dns_records_object_result_model2 = DnsRecordsObjectResult(**dns_records_object_result_model_dict)

        # Verify the model instances are equivalent
        assert dns_records_object_result_model == dns_records_object_result_model2

        # Convert model instance back to dict and verify no loss of data
        dns_records_object_result_model_json2 = dns_records_object_result_model.to_dict()
        assert dns_records_object_result_model_json2 == dns_records_object_result_model_json

#-----------------------------------------------------------------------------
# Test Class for DnsRecordsObjectTiming
#-----------------------------------------------------------------------------
class TestDnsRecordsObjectTiming():

    #--------------------------------------------------------
    # Test serialization/deserialization for DnsRecordsObjectTiming
    #--------------------------------------------------------
    def test_dns_records_object_timing_serialization(self):

        # Construct a json representation of a DnsRecordsObjectTiming model
        dns_records_object_timing_model_json = {}
        dns_records_object_timing_model_json['start_time'] = '2014-03-01T12:20:00Z'
        dns_records_object_timing_model_json['end_time'] = '2014-03-01T12:20:01Z'
        dns_records_object_timing_model_json['process_time'] = 1

        # Construct a model instance of DnsRecordsObjectTiming by calling from_dict on the json representation
        dns_records_object_timing_model = DnsRecordsObjectTiming.from_dict(dns_records_object_timing_model_json)
        assert dns_records_object_timing_model != False

        # Construct a model instance of DnsRecordsObjectTiming by calling from_dict on the json representation
        dns_records_object_timing_model_dict = DnsRecordsObjectTiming.from_dict(dns_records_object_timing_model_json).__dict__
        dns_records_object_timing_model2 = DnsRecordsObjectTiming(**dns_records_object_timing_model_dict)

        # Verify the model instances are equivalent
        assert dns_records_object_timing_model == dns_records_object_timing_model2

        # Convert model instance back to dict and verify no loss of data
        dns_records_object_timing_model_json2 = dns_records_object_timing_model.to_dict()
        assert dns_records_object_timing_model_json2 == dns_records_object_timing_model_json

#-----------------------------------------------------------------------------
# Test Class for DnsRecordsObject
#-----------------------------------------------------------------------------
class TestDnsRecordsObject():

    #--------------------------------------------------------
    # Test serialization/deserialization for DnsRecordsObject
    #--------------------------------------------------------
    def test_dns_records_object_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        dns_records_object_messages_item_model = {} # DnsRecordsObjectMessagesItem
        dns_records_object_messages_item_model['code'] = 38
        dns_records_object_messages_item_model['message'] = 'testString'

        dns_records_object_result_model = {} # DnsRecordsObjectResult
        dns_records_object_result_model['recs_added'] = 5
        dns_records_object_result_model['total_records_parsed'] = 5

        dns_records_object_timing_model = {} # DnsRecordsObjectTiming
        dns_records_object_timing_model['start_time'] = '2014-03-01T12:20:00Z'
        dns_records_object_timing_model['end_time'] = '2014-03-01T12:20:01Z'
        dns_records_object_timing_model['process_time'] = 1

        # Construct a json representation of a DnsRecordsObject model
        dns_records_object_model_json = {}
        dns_records_object_model_json['success'] = True
        dns_records_object_model_json['errors'] = [['testString']]
        dns_records_object_model_json['messages'] = [dns_records_object_messages_item_model]
        dns_records_object_model_json['result'] = dns_records_object_result_model
        dns_records_object_model_json['timing'] = dns_records_object_timing_model

        # Construct a model instance of DnsRecordsObject by calling from_dict on the json representation
        dns_records_object_model = DnsRecordsObject.from_dict(dns_records_object_model_json)
        assert dns_records_object_model != False

        # Construct a model instance of DnsRecordsObject by calling from_dict on the json representation
        dns_records_object_model_dict = DnsRecordsObject.from_dict(dns_records_object_model_json).__dict__
        dns_records_object_model2 = DnsRecordsObject(**dns_records_object_model_dict)

        # Verify the model instances are equivalent
        assert dns_records_object_model == dns_records_object_model2

        # Convert model instance back to dict and verify no loss of data
        dns_records_object_model_json2 = dns_records_object_model.to_dict()
        assert dns_records_object_model_json2 == dns_records_object_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
