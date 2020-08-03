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
from ibm_cloud_networking_services.resource_records_v1 import *


service = ResourceRecordsV1(
    authenticator=NoAuthAuthenticator()
    )

base_url = 'https://api.dns-svcs.cloud.ibm.com/v1'
service.set_service_url(base_url)

##############################################################################
# Start of Service: ResourceRecords
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_resource_records
#-----------------------------------------------------------------------------
class TestListResourceRecords():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # list_resource_records()
    #--------------------------------------------------------
    @responses.activate
    def test_list_resource_records_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/dnszones/testString/resource_records')
        mock_response = '{"resource_records": [{"id": "SRV:5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "name": "_sip._udp.test.example.com", "type": "SRV", "ttl": 120, "rdata": {"anyKey": "anyValue"}, "service": "_sip", "protocol": "udp"}], "offset": 0, "limit": 20, "total_count": 200, "first": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/resource_records?limit=20"}, "next": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/resource_records?offset=20&limit=20"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        x_correlation_id = 'testString'
        offset = 38
        limit = 38

        # Invoke method
        response = service.list_resource_records(
            instance_id,
            dnszone_id,
            x_correlation_id=x_correlation_id,
            offset=offset,
            limit=limit,
            headers={}
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
    # test_list_resource_records_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_resource_records_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/dnszones/testString/resource_records')
        mock_response = '{"resource_records": [{"id": "SRV:5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "name": "_sip._udp.test.example.com", "type": "SRV", "ttl": 120, "rdata": {"anyKey": "anyValue"}, "service": "_sip", "protocol": "udp"}], "offset": 0, "limit": 20, "total_count": 200, "first": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/resource_records?limit=20"}, "next": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/resource_records?offset=20&limit=20"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'

        # Invoke method
        response = service.list_resource_records(
            instance_id,
            dnszone_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_list_resource_records_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_list_resource_records_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/dnszones/testString/resource_records')
        mock_response = '{"resource_records": [{"id": "SRV:5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "name": "_sip._udp.test.example.com", "type": "SRV", "ttl": 120, "rdata": {"anyKey": "anyValue"}, "service": "_sip", "protocol": "udp"}], "offset": 0, "limit": 20, "total_count": 200, "first": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/resource_records?limit=20"}, "next": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/resource_records?offset=20&limit=20"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "dnszone_id": dnszone_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.list_resource_records(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for create_resource_record
#-----------------------------------------------------------------------------
class TestCreateResourceRecord():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # create_resource_record()
    #--------------------------------------------------------
    @responses.activate
    def test_create_resource_record_all_params(self):
        pytest.skip('service keyword is used. so, skipped test')
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/dnszones/testString/resource_records')
        mock_response = '{"id": "SRV:5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "name": "_sip._udp.test.example.com", "type": "SRV", "ttl": 120, "rdata": {"anyKey": "anyValue"}, "service": "_sip", "protocol": "udp"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a ResourceRecordInputRdataRdataARecord model
        resource_record_input_rdata_model = {}
        resource_record_input_rdata_model['ip'] = '10.110.201.214'

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        type = 'SRV'
        name = 'test.example.com'
        rdata = resource_record_input_rdata_model
        ttl = 120
        service = '_sip'
        protocol = 'udp'
        x_correlation_id = 'testString'

        # Invoke method
        response = service.create_resource_record(
            instance_id,
            dnszone_id,
            type=type,
            name=name,
            rdata=rdata,
            ttl=ttl,
            service=service,
            protocol=protocol,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['type'] == 'SRV'
        assert req_body['name'] == 'test.example.com'
        assert req_body['rdata'] == resource_record_input_rdata_model
        assert req_body['ttl'] == 120
        assert req_body['service'] == '_sip'
        assert req_body['protocol'] == 'udp'


    #--------------------------------------------------------
    # test_create_resource_record_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_resource_record_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/dnszones/testString/resource_records')
        mock_response = '{"id": "SRV:5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "name": "_sip._udp.test.example.com", "type": "SRV", "ttl": 120, "rdata": {"anyKey": "anyValue"}, "service": "_sip", "protocol": "udp"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'

        # Invoke method
        response = service.create_resource_record(
            instance_id,
            dnszone_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_create_resource_record_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_create_resource_record_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/dnszones/testString/resource_records')
        mock_response = '{"id": "SRV:5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "name": "_sip._udp.test.example.com", "type": "SRV", "ttl": 120, "rdata": {"anyKey": "anyValue"}, "service": "_sip", "protocol": "udp"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "dnszone_id": dnszone_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.create_resource_record(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for delete_resource_record
#-----------------------------------------------------------------------------
class TestDeleteResourceRecord():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # delete_resource_record()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_resource_record_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/dnszones/testString/resource_records/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        record_id = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = service.delete_resource_record(
            instance_id,
            dnszone_id,
            record_id,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    #--------------------------------------------------------
    # test_delete_resource_record_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_resource_record_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/dnszones/testString/resource_records/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        record_id = 'testString'

        # Invoke method
        response = service.delete_resource_record(
            instance_id,
            dnszone_id,
            record_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    #--------------------------------------------------------
    # test_delete_resource_record_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_resource_record_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/dnszones/testString/resource_records/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        record_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "dnszone_id": dnszone_id,
            "record_id": record_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_resource_record(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_resource_record
#-----------------------------------------------------------------------------
class TestGetResourceRecord():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_resource_record()
    #--------------------------------------------------------
    @responses.activate
    def test_get_resource_record_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/dnszones/testString/resource_records/testString')
        mock_response = '{"id": "SRV:5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "name": "_sip._udp.test.example.com", "type": "SRV", "ttl": 120, "rdata": {"anyKey": "anyValue"}, "service": "_sip", "protocol": "udp"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        record_id = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = service.get_resource_record(
            instance_id,
            dnszone_id,
            record_id,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_resource_record_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_resource_record_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/dnszones/testString/resource_records/testString')
        mock_response = '{"id": "SRV:5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "name": "_sip._udp.test.example.com", "type": "SRV", "ttl": 120, "rdata": {"anyKey": "anyValue"}, "service": "_sip", "protocol": "udp"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        record_id = 'testString'

        # Invoke method
        response = service.get_resource_record(
            instance_id,
            dnszone_id,
            record_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_resource_record_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_resource_record_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/dnszones/testString/resource_records/testString')
        mock_response = '{"id": "SRV:5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "name": "_sip._udp.test.example.com", "type": "SRV", "ttl": 120, "rdata": {"anyKey": "anyValue"}, "service": "_sip", "protocol": "udp"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        record_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "dnszone_id": dnszone_id,
            "record_id": record_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_resource_record(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_resource_record
#-----------------------------------------------------------------------------
class TestUpdateResourceRecord():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_resource_record()
    #--------------------------------------------------------
    @responses.activate
    def test_update_resource_record_all_params(self):
        pytest.skip('service keyword is used. so, skipped test')
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/dnszones/testString/resource_records/testString')
        mock_response = '{"id": "SRV:5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "name": "_sip._udp.test.example.com", "type": "SRV", "ttl": 120, "rdata": {"anyKey": "anyValue"}, "service": "_sip", "protocol": "udp"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a ResourceRecordUpdateInputRdataRdataARecord model
        resource_record_update_input_rdata_model = {}
        resource_record_update_input_rdata_model['ip'] = '10.110.201.214'

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        record_id = 'testString'
        name = 'test.example.com'
        rdata = resource_record_update_input_rdata_model
        ttl = 120
        service = '_sip'
        protocol = 'udp'
        x_correlation_id = 'testString'

        # Invoke method
        response = service.update_resource_record(
            instance_id,
            dnszone_id,
            record_id,
            name=name,
            rdata=rdata,
            ttl=ttl,
            service=service,
            protocol=protocol,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'test.example.com'
        assert req_body['rdata'] == resource_record_update_input_rdata_model
        assert req_body['ttl'] == 120
        assert req_body['service'] == '_sip'
        assert req_body['protocol'] == 'udp'


    #--------------------------------------------------------
    # test_update_resource_record_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_resource_record_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/dnszones/testString/resource_records/testString')
        mock_response = '{"id": "SRV:5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "name": "_sip._udp.test.example.com", "type": "SRV", "ttl": 120, "rdata": {"anyKey": "anyValue"}, "service": "_sip", "protocol": "udp"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        record_id = 'testString'

        # Invoke method
        response = service.update_resource_record(
            instance_id,
            dnszone_id,
            record_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_resource_record_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_resource_record_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/dnszones/testString/resource_records/testString')
        mock_response = '{"id": "SRV:5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "name": "_sip._udp.test.example.com", "type": "SRV", "ttl": 120, "rdata": {"anyKey": "anyValue"}, "service": "_sip", "protocol": "udp"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        record_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "dnszone_id": dnszone_id,
            "record_id": record_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.update_resource_record(**req_copy)



# endregion
##############################################################################
# End of Service: ResourceRecords
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
#-----------------------------------------------------------------------------
# Test Class for FirstHref
#-----------------------------------------------------------------------------
class TestFirstHref():

    #--------------------------------------------------------
    # Test serialization/deserialization for FirstHref
    #--------------------------------------------------------
    def test_first_href_serialization(self):

        # Construct a json representation of a FirstHref model
        first_href_model_json = {}
        first_href_model_json['href'] = 'https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/resource_records?limit=20'

        # Construct a model instance of FirstHref by calling from_dict on the json representation
        first_href_model = FirstHref.from_dict(first_href_model_json)
        assert first_href_model != False

        # Construct a model instance of FirstHref by calling from_dict on the json representation
        first_href_model_dict = FirstHref.from_dict(first_href_model_json).__dict__
        first_href_model2 = FirstHref(**first_href_model_dict)

        # Verify the model instances are equivalent
        assert first_href_model == first_href_model2

        # Convert model instance back to dict and verify no loss of data
        first_href_model_json2 = first_href_model.to_dict()
        assert first_href_model_json2 == first_href_model_json

#-----------------------------------------------------------------------------
# Test Class for ListResourceRecords
#-----------------------------------------------------------------------------
class TestListResourceRecords():

    #--------------------------------------------------------
    # Test serialization/deserialization for ListResourceRecords
    #--------------------------------------------------------
    def test_list_resource_records_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        first_href_model = {} # FirstHref
        first_href_model['href'] = 'https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/resource_records?limit=20'

        next_href_model = {} # NextHref
        next_href_model['href'] = 'https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/resource_records?offset=20&limit=20'

        resource_record_model = {} # ResourceRecord
        resource_record_model['id'] = 'SRV:5365b73c-ce6f-4d6f-ad9f-d9c131b26370'
        resource_record_model['created_on'] = '2019-01-01T05:20:00.12345Z'
        resource_record_model['modified_on'] = '2019-01-01T05:20:00.12345Z'
        resource_record_model['name'] = '_sip._udp.test.example.com'
        resource_record_model['type'] = 'SRV'
        resource_record_model['ttl'] = 120
        resource_record_model['rdata'] = { 'foo': 'bar' }
        resource_record_model['service'] = '_sip'
        resource_record_model['protocol'] = 'udp'

        # Construct a json representation of a ListResourceRecords model
        list_resource_records_model_json = {}
        list_resource_records_model_json['resource_records'] = [resource_record_model]
        list_resource_records_model_json['offset'] = 0
        list_resource_records_model_json['limit'] = 20
        list_resource_records_model_json['total_count'] = 200
        list_resource_records_model_json['first'] = first_href_model
        list_resource_records_model_json['next'] = next_href_model

        # Construct a model instance of ListResourceRecords by calling from_dict on the json representation
        list_resource_records_model = ListResourceRecords.from_dict(list_resource_records_model_json)
        assert list_resource_records_model != False

        # Construct a model instance of ListResourceRecords by calling from_dict on the json representation
        list_resource_records_model_dict = ListResourceRecords.from_dict(list_resource_records_model_json).__dict__
        list_resource_records_model2 = ListResourceRecords(**list_resource_records_model_dict)

        # Verify the model instances are equivalent
        assert list_resource_records_model == list_resource_records_model2

        # Convert model instance back to dict and verify no loss of data
        list_resource_records_model_json2 = list_resource_records_model.to_dict()
        assert list_resource_records_model_json2 == list_resource_records_model_json

#-----------------------------------------------------------------------------
# Test Class for NextHref
#-----------------------------------------------------------------------------
class TestNextHref():

    #--------------------------------------------------------
    # Test serialization/deserialization for NextHref
    #--------------------------------------------------------
    def test_next_href_serialization(self):

        # Construct a json representation of a NextHref model
        next_href_model_json = {}
        next_href_model_json['href'] = 'https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/resource_records?offset=20&limit=20'

        # Construct a model instance of NextHref by calling from_dict on the json representation
        next_href_model = NextHref.from_dict(next_href_model_json)
        assert next_href_model != False

        # Construct a model instance of NextHref by calling from_dict on the json representation
        next_href_model_dict = NextHref.from_dict(next_href_model_json).__dict__
        next_href_model2 = NextHref(**next_href_model_dict)

        # Verify the model instances are equivalent
        assert next_href_model == next_href_model2

        # Convert model instance back to dict and verify no loss of data
        next_href_model_json2 = next_href_model.to_dict()
        assert next_href_model_json2 == next_href_model_json

#-----------------------------------------------------------------------------
# Test Class for ResourceRecord
#-----------------------------------------------------------------------------
class TestResourceRecord():

    #--------------------------------------------------------
    # Test serialization/deserialization for ResourceRecord
    #--------------------------------------------------------
    def test_resource_record_serialization(self):

        # Construct a json representation of a ResourceRecord model
        resource_record_model_json = {}
        resource_record_model_json['id'] = 'SRV:5365b73c-ce6f-4d6f-ad9f-d9c131b26370'
        resource_record_model_json['created_on'] = '2019-01-01T05:20:00.12345Z'
        resource_record_model_json['modified_on'] = '2019-01-01T05:20:00.12345Z'
        resource_record_model_json['name'] = '_sip._udp.test.example.com'
        resource_record_model_json['type'] = 'SRV'
        resource_record_model_json['ttl'] = 120
        resource_record_model_json['rdata'] = { 'foo': 'bar' }
        resource_record_model_json['service'] = '_sip'
        resource_record_model_json['protocol'] = 'udp'

        # Construct a model instance of ResourceRecord by calling from_dict on the json representation
        resource_record_model = ResourceRecord.from_dict(resource_record_model_json)
        assert resource_record_model != False

        # Construct a model instance of ResourceRecord by calling from_dict on the json representation
        resource_record_model_dict = ResourceRecord.from_dict(resource_record_model_json).__dict__
        resource_record_model2 = ResourceRecord(**resource_record_model_dict)

        # Verify the model instances are equivalent
        assert resource_record_model == resource_record_model2

        # Convert model instance back to dict and verify no loss of data
        resource_record_model_json2 = resource_record_model.to_dict()
        assert resource_record_model_json2 == resource_record_model_json

#-----------------------------------------------------------------------------
# Test Class for ResourceRecordInputRdataRdataARecord
#-----------------------------------------------------------------------------
class TestResourceRecordInputRdataRdataARecord():

    #--------------------------------------------------------
    # Test serialization/deserialization for ResourceRecordInputRdataRdataARecord
    #--------------------------------------------------------
    def test_resource_record_input_rdata_rdata_a_record_serialization(self):

        # Construct a json representation of a ResourceRecordInputRdataRdataARecord model
        resource_record_input_rdata_rdata_a_record_model_json = {}
        resource_record_input_rdata_rdata_a_record_model_json['ip'] = '10.110.201.214'

        # Construct a model instance of ResourceRecordInputRdataRdataARecord by calling from_dict on the json representation
        resource_record_input_rdata_rdata_a_record_model = ResourceRecordInputRdataRdataARecord.from_dict(resource_record_input_rdata_rdata_a_record_model_json)
        assert resource_record_input_rdata_rdata_a_record_model != False

        # Construct a model instance of ResourceRecordInputRdataRdataARecord by calling from_dict on the json representation
        resource_record_input_rdata_rdata_a_record_model_dict = ResourceRecordInputRdataRdataARecord.from_dict(resource_record_input_rdata_rdata_a_record_model_json).__dict__
        resource_record_input_rdata_rdata_a_record_model2 = ResourceRecordInputRdataRdataARecord(**resource_record_input_rdata_rdata_a_record_model_dict)

        # Verify the model instances are equivalent
        assert resource_record_input_rdata_rdata_a_record_model == resource_record_input_rdata_rdata_a_record_model2

        # Convert model instance back to dict and verify no loss of data
        resource_record_input_rdata_rdata_a_record_model_json2 = resource_record_input_rdata_rdata_a_record_model.to_dict()
        assert resource_record_input_rdata_rdata_a_record_model_json2 == resource_record_input_rdata_rdata_a_record_model_json

#-----------------------------------------------------------------------------
# Test Class for ResourceRecordInputRdataRdataAaaaRecord
#-----------------------------------------------------------------------------
class TestResourceRecordInputRdataRdataAaaaRecord():

    #--------------------------------------------------------
    # Test serialization/deserialization for ResourceRecordInputRdataRdataAaaaRecord
    #--------------------------------------------------------
    def test_resource_record_input_rdata_rdata_aaaa_record_serialization(self):

        # Construct a json representation of a ResourceRecordInputRdataRdataAaaaRecord model
        resource_record_input_rdata_rdata_aaaa_record_model_json = {}
        resource_record_input_rdata_rdata_aaaa_record_model_json['ip'] = '2019::2019'

        # Construct a model instance of ResourceRecordInputRdataRdataAaaaRecord by calling from_dict on the json representation
        resource_record_input_rdata_rdata_aaaa_record_model = ResourceRecordInputRdataRdataAaaaRecord.from_dict(resource_record_input_rdata_rdata_aaaa_record_model_json)
        assert resource_record_input_rdata_rdata_aaaa_record_model != False

        # Construct a model instance of ResourceRecordInputRdataRdataAaaaRecord by calling from_dict on the json representation
        resource_record_input_rdata_rdata_aaaa_record_model_dict = ResourceRecordInputRdataRdataAaaaRecord.from_dict(resource_record_input_rdata_rdata_aaaa_record_model_json).__dict__
        resource_record_input_rdata_rdata_aaaa_record_model2 = ResourceRecordInputRdataRdataAaaaRecord(**resource_record_input_rdata_rdata_aaaa_record_model_dict)

        # Verify the model instances are equivalent
        assert resource_record_input_rdata_rdata_aaaa_record_model == resource_record_input_rdata_rdata_aaaa_record_model2

        # Convert model instance back to dict and verify no loss of data
        resource_record_input_rdata_rdata_aaaa_record_model_json2 = resource_record_input_rdata_rdata_aaaa_record_model.to_dict()
        assert resource_record_input_rdata_rdata_aaaa_record_model_json2 == resource_record_input_rdata_rdata_aaaa_record_model_json

#-----------------------------------------------------------------------------
# Test Class for ResourceRecordInputRdataRdataCnameRecord
#-----------------------------------------------------------------------------
class TestResourceRecordInputRdataRdataCnameRecord():

    #--------------------------------------------------------
    # Test serialization/deserialization for ResourceRecordInputRdataRdataCnameRecord
    #--------------------------------------------------------
    def test_resource_record_input_rdata_rdata_cname_record_serialization(self):

        # Construct a json representation of a ResourceRecordInputRdataRdataCnameRecord model
        resource_record_input_rdata_rdata_cname_record_model_json = {}
        resource_record_input_rdata_rdata_cname_record_model_json['cname'] = 'www.example.com'

        # Construct a model instance of ResourceRecordInputRdataRdataCnameRecord by calling from_dict on the json representation
        resource_record_input_rdata_rdata_cname_record_model = ResourceRecordInputRdataRdataCnameRecord.from_dict(resource_record_input_rdata_rdata_cname_record_model_json)
        assert resource_record_input_rdata_rdata_cname_record_model != False

        # Construct a model instance of ResourceRecordInputRdataRdataCnameRecord by calling from_dict on the json representation
        resource_record_input_rdata_rdata_cname_record_model_dict = ResourceRecordInputRdataRdataCnameRecord.from_dict(resource_record_input_rdata_rdata_cname_record_model_json).__dict__
        resource_record_input_rdata_rdata_cname_record_model2 = ResourceRecordInputRdataRdataCnameRecord(**resource_record_input_rdata_rdata_cname_record_model_dict)

        # Verify the model instances are equivalent
        assert resource_record_input_rdata_rdata_cname_record_model == resource_record_input_rdata_rdata_cname_record_model2

        # Convert model instance back to dict and verify no loss of data
        resource_record_input_rdata_rdata_cname_record_model_json2 = resource_record_input_rdata_rdata_cname_record_model.to_dict()
        assert resource_record_input_rdata_rdata_cname_record_model_json2 == resource_record_input_rdata_rdata_cname_record_model_json

#-----------------------------------------------------------------------------
# Test Class for ResourceRecordInputRdataRdataMxRecord
#-----------------------------------------------------------------------------
class TestResourceRecordInputRdataRdataMxRecord():

    #--------------------------------------------------------
    # Test serialization/deserialization for ResourceRecordInputRdataRdataMxRecord
    #--------------------------------------------------------
    def test_resource_record_input_rdata_rdata_mx_record_serialization(self):

        # Construct a json representation of a ResourceRecordInputRdataRdataMxRecord model
        resource_record_input_rdata_rdata_mx_record_model_json = {}
        resource_record_input_rdata_rdata_mx_record_model_json['exchange'] = 'mail.example.com'
        resource_record_input_rdata_rdata_mx_record_model_json['preference'] = 10

        # Construct a model instance of ResourceRecordInputRdataRdataMxRecord by calling from_dict on the json representation
        resource_record_input_rdata_rdata_mx_record_model = ResourceRecordInputRdataRdataMxRecord.from_dict(resource_record_input_rdata_rdata_mx_record_model_json)
        assert resource_record_input_rdata_rdata_mx_record_model != False

        # Construct a model instance of ResourceRecordInputRdataRdataMxRecord by calling from_dict on the json representation
        resource_record_input_rdata_rdata_mx_record_model_dict = ResourceRecordInputRdataRdataMxRecord.from_dict(resource_record_input_rdata_rdata_mx_record_model_json).__dict__
        resource_record_input_rdata_rdata_mx_record_model2 = ResourceRecordInputRdataRdataMxRecord(**resource_record_input_rdata_rdata_mx_record_model_dict)

        # Verify the model instances are equivalent
        assert resource_record_input_rdata_rdata_mx_record_model == resource_record_input_rdata_rdata_mx_record_model2

        # Convert model instance back to dict and verify no loss of data
        resource_record_input_rdata_rdata_mx_record_model_json2 = resource_record_input_rdata_rdata_mx_record_model.to_dict()
        assert resource_record_input_rdata_rdata_mx_record_model_json2 == resource_record_input_rdata_rdata_mx_record_model_json

#-----------------------------------------------------------------------------
# Test Class for ResourceRecordInputRdataRdataPtrRecord
#-----------------------------------------------------------------------------
class TestResourceRecordInputRdataRdataPtrRecord():

    #--------------------------------------------------------
    # Test serialization/deserialization for ResourceRecordInputRdataRdataPtrRecord
    #--------------------------------------------------------
    def test_resource_record_input_rdata_rdata_ptr_record_serialization(self):

        # Construct a json representation of a ResourceRecordInputRdataRdataPtrRecord model
        resource_record_input_rdata_rdata_ptr_record_model_json = {}
        resource_record_input_rdata_rdata_ptr_record_model_json['ptrdname'] = 'www.example.com'

        # Construct a model instance of ResourceRecordInputRdataRdataPtrRecord by calling from_dict on the json representation
        resource_record_input_rdata_rdata_ptr_record_model = ResourceRecordInputRdataRdataPtrRecord.from_dict(resource_record_input_rdata_rdata_ptr_record_model_json)
        assert resource_record_input_rdata_rdata_ptr_record_model != False

        # Construct a model instance of ResourceRecordInputRdataRdataPtrRecord by calling from_dict on the json representation
        resource_record_input_rdata_rdata_ptr_record_model_dict = ResourceRecordInputRdataRdataPtrRecord.from_dict(resource_record_input_rdata_rdata_ptr_record_model_json).__dict__
        resource_record_input_rdata_rdata_ptr_record_model2 = ResourceRecordInputRdataRdataPtrRecord(**resource_record_input_rdata_rdata_ptr_record_model_dict)

        # Verify the model instances are equivalent
        assert resource_record_input_rdata_rdata_ptr_record_model == resource_record_input_rdata_rdata_ptr_record_model2

        # Convert model instance back to dict and verify no loss of data
        resource_record_input_rdata_rdata_ptr_record_model_json2 = resource_record_input_rdata_rdata_ptr_record_model.to_dict()
        assert resource_record_input_rdata_rdata_ptr_record_model_json2 == resource_record_input_rdata_rdata_ptr_record_model_json

#-----------------------------------------------------------------------------
# Test Class for ResourceRecordInputRdataRdataSrvRecord
#-----------------------------------------------------------------------------
class TestResourceRecordInputRdataRdataSrvRecord():

    #--------------------------------------------------------
    # Test serialization/deserialization for ResourceRecordInputRdataRdataSrvRecord
    #--------------------------------------------------------
    def test_resource_record_input_rdata_rdata_srv_record_serialization(self):

        # Construct a json representation of a ResourceRecordInputRdataRdataSrvRecord model
        resource_record_input_rdata_rdata_srv_record_model_json = {}
        resource_record_input_rdata_rdata_srv_record_model_json['port'] = 80
        resource_record_input_rdata_rdata_srv_record_model_json['priority'] = 10
        resource_record_input_rdata_rdata_srv_record_model_json['target'] = 'www.example.com'
        resource_record_input_rdata_rdata_srv_record_model_json['weight'] = 10

        # Construct a model instance of ResourceRecordInputRdataRdataSrvRecord by calling from_dict on the json representation
        resource_record_input_rdata_rdata_srv_record_model = ResourceRecordInputRdataRdataSrvRecord.from_dict(resource_record_input_rdata_rdata_srv_record_model_json)
        assert resource_record_input_rdata_rdata_srv_record_model != False

        # Construct a model instance of ResourceRecordInputRdataRdataSrvRecord by calling from_dict on the json representation
        resource_record_input_rdata_rdata_srv_record_model_dict = ResourceRecordInputRdataRdataSrvRecord.from_dict(resource_record_input_rdata_rdata_srv_record_model_json).__dict__
        resource_record_input_rdata_rdata_srv_record_model2 = ResourceRecordInputRdataRdataSrvRecord(**resource_record_input_rdata_rdata_srv_record_model_dict)

        # Verify the model instances are equivalent
        assert resource_record_input_rdata_rdata_srv_record_model == resource_record_input_rdata_rdata_srv_record_model2

        # Convert model instance back to dict and verify no loss of data
        resource_record_input_rdata_rdata_srv_record_model_json2 = resource_record_input_rdata_rdata_srv_record_model.to_dict()
        assert resource_record_input_rdata_rdata_srv_record_model_json2 == resource_record_input_rdata_rdata_srv_record_model_json

#-----------------------------------------------------------------------------
# Test Class for ResourceRecordInputRdataRdataTxtRecord
#-----------------------------------------------------------------------------
class TestResourceRecordInputRdataRdataTxtRecord():

    #--------------------------------------------------------
    # Test serialization/deserialization for ResourceRecordInputRdataRdataTxtRecord
    #--------------------------------------------------------
    def test_resource_record_input_rdata_rdata_txt_record_serialization(self):

        # Construct a json representation of a ResourceRecordInputRdataRdataTxtRecord model
        resource_record_input_rdata_rdata_txt_record_model_json = {}
        resource_record_input_rdata_rdata_txt_record_model_json['text'] = 'This is a text record'

        # Construct a model instance of ResourceRecordInputRdataRdataTxtRecord by calling from_dict on the json representation
        resource_record_input_rdata_rdata_txt_record_model = ResourceRecordInputRdataRdataTxtRecord.from_dict(resource_record_input_rdata_rdata_txt_record_model_json)
        assert resource_record_input_rdata_rdata_txt_record_model != False

        # Construct a model instance of ResourceRecordInputRdataRdataTxtRecord by calling from_dict on the json representation
        resource_record_input_rdata_rdata_txt_record_model_dict = ResourceRecordInputRdataRdataTxtRecord.from_dict(resource_record_input_rdata_rdata_txt_record_model_json).__dict__
        resource_record_input_rdata_rdata_txt_record_model2 = ResourceRecordInputRdataRdataTxtRecord(**resource_record_input_rdata_rdata_txt_record_model_dict)

        # Verify the model instances are equivalent
        assert resource_record_input_rdata_rdata_txt_record_model == resource_record_input_rdata_rdata_txt_record_model2

        # Convert model instance back to dict and verify no loss of data
        resource_record_input_rdata_rdata_txt_record_model_json2 = resource_record_input_rdata_rdata_txt_record_model.to_dict()
        assert resource_record_input_rdata_rdata_txt_record_model_json2 == resource_record_input_rdata_rdata_txt_record_model_json

#-----------------------------------------------------------------------------
# Test Class for ResourceRecordUpdateInputRdataRdataARecord
#-----------------------------------------------------------------------------
class TestResourceRecordUpdateInputRdataRdataARecord():

    #--------------------------------------------------------
    # Test serialization/deserialization for ResourceRecordUpdateInputRdataRdataARecord
    #--------------------------------------------------------
    def test_resource_record_update_input_rdata_rdata_a_record_serialization(self):

        # Construct a json representation of a ResourceRecordUpdateInputRdataRdataARecord model
        resource_record_update_input_rdata_rdata_a_record_model_json = {}
        resource_record_update_input_rdata_rdata_a_record_model_json['ip'] = '10.110.201.214'

        # Construct a model instance of ResourceRecordUpdateInputRdataRdataARecord by calling from_dict on the json representation
        resource_record_update_input_rdata_rdata_a_record_model = ResourceRecordUpdateInputRdataRdataARecord.from_dict(resource_record_update_input_rdata_rdata_a_record_model_json)
        assert resource_record_update_input_rdata_rdata_a_record_model != False

        # Construct a model instance of ResourceRecordUpdateInputRdataRdataARecord by calling from_dict on the json representation
        resource_record_update_input_rdata_rdata_a_record_model_dict = ResourceRecordUpdateInputRdataRdataARecord.from_dict(resource_record_update_input_rdata_rdata_a_record_model_json).__dict__
        resource_record_update_input_rdata_rdata_a_record_model2 = ResourceRecordUpdateInputRdataRdataARecord(**resource_record_update_input_rdata_rdata_a_record_model_dict)

        # Verify the model instances are equivalent
        assert resource_record_update_input_rdata_rdata_a_record_model == resource_record_update_input_rdata_rdata_a_record_model2

        # Convert model instance back to dict and verify no loss of data
        resource_record_update_input_rdata_rdata_a_record_model_json2 = resource_record_update_input_rdata_rdata_a_record_model.to_dict()
        assert resource_record_update_input_rdata_rdata_a_record_model_json2 == resource_record_update_input_rdata_rdata_a_record_model_json

#-----------------------------------------------------------------------------
# Test Class for ResourceRecordUpdateInputRdataRdataAaaaRecord
#-----------------------------------------------------------------------------
class TestResourceRecordUpdateInputRdataRdataAaaaRecord():

    #--------------------------------------------------------
    # Test serialization/deserialization for ResourceRecordUpdateInputRdataRdataAaaaRecord
    #--------------------------------------------------------
    def test_resource_record_update_input_rdata_rdata_aaaa_record_serialization(self):

        # Construct a json representation of a ResourceRecordUpdateInputRdataRdataAaaaRecord model
        resource_record_update_input_rdata_rdata_aaaa_record_model_json = {}
        resource_record_update_input_rdata_rdata_aaaa_record_model_json['ip'] = '2019::2019'

        # Construct a model instance of ResourceRecordUpdateInputRdataRdataAaaaRecord by calling from_dict on the json representation
        resource_record_update_input_rdata_rdata_aaaa_record_model = ResourceRecordUpdateInputRdataRdataAaaaRecord.from_dict(resource_record_update_input_rdata_rdata_aaaa_record_model_json)
        assert resource_record_update_input_rdata_rdata_aaaa_record_model != False

        # Construct a model instance of ResourceRecordUpdateInputRdataRdataAaaaRecord by calling from_dict on the json representation
        resource_record_update_input_rdata_rdata_aaaa_record_model_dict = ResourceRecordUpdateInputRdataRdataAaaaRecord.from_dict(resource_record_update_input_rdata_rdata_aaaa_record_model_json).__dict__
        resource_record_update_input_rdata_rdata_aaaa_record_model2 = ResourceRecordUpdateInputRdataRdataAaaaRecord(**resource_record_update_input_rdata_rdata_aaaa_record_model_dict)

        # Verify the model instances are equivalent
        assert resource_record_update_input_rdata_rdata_aaaa_record_model == resource_record_update_input_rdata_rdata_aaaa_record_model2

        # Convert model instance back to dict and verify no loss of data
        resource_record_update_input_rdata_rdata_aaaa_record_model_json2 = resource_record_update_input_rdata_rdata_aaaa_record_model.to_dict()
        assert resource_record_update_input_rdata_rdata_aaaa_record_model_json2 == resource_record_update_input_rdata_rdata_aaaa_record_model_json

#-----------------------------------------------------------------------------
# Test Class for ResourceRecordUpdateInputRdataRdataCnameRecord
#-----------------------------------------------------------------------------
class TestResourceRecordUpdateInputRdataRdataCnameRecord():

    #--------------------------------------------------------
    # Test serialization/deserialization for ResourceRecordUpdateInputRdataRdataCnameRecord
    #--------------------------------------------------------
    def test_resource_record_update_input_rdata_rdata_cname_record_serialization(self):

        # Construct a json representation of a ResourceRecordUpdateInputRdataRdataCnameRecord model
        resource_record_update_input_rdata_rdata_cname_record_model_json = {}
        resource_record_update_input_rdata_rdata_cname_record_model_json['cname'] = 'www.example.com'

        # Construct a model instance of ResourceRecordUpdateInputRdataRdataCnameRecord by calling from_dict on the json representation
        resource_record_update_input_rdata_rdata_cname_record_model = ResourceRecordUpdateInputRdataRdataCnameRecord.from_dict(resource_record_update_input_rdata_rdata_cname_record_model_json)
        assert resource_record_update_input_rdata_rdata_cname_record_model != False

        # Construct a model instance of ResourceRecordUpdateInputRdataRdataCnameRecord by calling from_dict on the json representation
        resource_record_update_input_rdata_rdata_cname_record_model_dict = ResourceRecordUpdateInputRdataRdataCnameRecord.from_dict(resource_record_update_input_rdata_rdata_cname_record_model_json).__dict__
        resource_record_update_input_rdata_rdata_cname_record_model2 = ResourceRecordUpdateInputRdataRdataCnameRecord(**resource_record_update_input_rdata_rdata_cname_record_model_dict)

        # Verify the model instances are equivalent
        assert resource_record_update_input_rdata_rdata_cname_record_model == resource_record_update_input_rdata_rdata_cname_record_model2

        # Convert model instance back to dict and verify no loss of data
        resource_record_update_input_rdata_rdata_cname_record_model_json2 = resource_record_update_input_rdata_rdata_cname_record_model.to_dict()
        assert resource_record_update_input_rdata_rdata_cname_record_model_json2 == resource_record_update_input_rdata_rdata_cname_record_model_json

#-----------------------------------------------------------------------------
# Test Class for ResourceRecordUpdateInputRdataRdataMxRecord
#-----------------------------------------------------------------------------
class TestResourceRecordUpdateInputRdataRdataMxRecord():

    #--------------------------------------------------------
    # Test serialization/deserialization for ResourceRecordUpdateInputRdataRdataMxRecord
    #--------------------------------------------------------
    def test_resource_record_update_input_rdata_rdata_mx_record_serialization(self):

        # Construct a json representation of a ResourceRecordUpdateInputRdataRdataMxRecord model
        resource_record_update_input_rdata_rdata_mx_record_model_json = {}
        resource_record_update_input_rdata_rdata_mx_record_model_json['exchange'] = 'mail.example.com'
        resource_record_update_input_rdata_rdata_mx_record_model_json['preference'] = 10

        # Construct a model instance of ResourceRecordUpdateInputRdataRdataMxRecord by calling from_dict on the json representation
        resource_record_update_input_rdata_rdata_mx_record_model = ResourceRecordUpdateInputRdataRdataMxRecord.from_dict(resource_record_update_input_rdata_rdata_mx_record_model_json)
        assert resource_record_update_input_rdata_rdata_mx_record_model != False

        # Construct a model instance of ResourceRecordUpdateInputRdataRdataMxRecord by calling from_dict on the json representation
        resource_record_update_input_rdata_rdata_mx_record_model_dict = ResourceRecordUpdateInputRdataRdataMxRecord.from_dict(resource_record_update_input_rdata_rdata_mx_record_model_json).__dict__
        resource_record_update_input_rdata_rdata_mx_record_model2 = ResourceRecordUpdateInputRdataRdataMxRecord(**resource_record_update_input_rdata_rdata_mx_record_model_dict)

        # Verify the model instances are equivalent
        assert resource_record_update_input_rdata_rdata_mx_record_model == resource_record_update_input_rdata_rdata_mx_record_model2

        # Convert model instance back to dict and verify no loss of data
        resource_record_update_input_rdata_rdata_mx_record_model_json2 = resource_record_update_input_rdata_rdata_mx_record_model.to_dict()
        assert resource_record_update_input_rdata_rdata_mx_record_model_json2 == resource_record_update_input_rdata_rdata_mx_record_model_json

#-----------------------------------------------------------------------------
# Test Class for ResourceRecordUpdateInputRdataRdataPtrRecord
#-----------------------------------------------------------------------------
class TestResourceRecordUpdateInputRdataRdataPtrRecord():

    #--------------------------------------------------------
    # Test serialization/deserialization for ResourceRecordUpdateInputRdataRdataPtrRecord
    #--------------------------------------------------------
    def test_resource_record_update_input_rdata_rdata_ptr_record_serialization(self):

        # Construct a json representation of a ResourceRecordUpdateInputRdataRdataPtrRecord model
        resource_record_update_input_rdata_rdata_ptr_record_model_json = {}
        resource_record_update_input_rdata_rdata_ptr_record_model_json['ptrdname'] = 'www.example.com'

        # Construct a model instance of ResourceRecordUpdateInputRdataRdataPtrRecord by calling from_dict on the json representation
        resource_record_update_input_rdata_rdata_ptr_record_model = ResourceRecordUpdateInputRdataRdataPtrRecord.from_dict(resource_record_update_input_rdata_rdata_ptr_record_model_json)
        assert resource_record_update_input_rdata_rdata_ptr_record_model != False

        # Construct a model instance of ResourceRecordUpdateInputRdataRdataPtrRecord by calling from_dict on the json representation
        resource_record_update_input_rdata_rdata_ptr_record_model_dict = ResourceRecordUpdateInputRdataRdataPtrRecord.from_dict(resource_record_update_input_rdata_rdata_ptr_record_model_json).__dict__
        resource_record_update_input_rdata_rdata_ptr_record_model2 = ResourceRecordUpdateInputRdataRdataPtrRecord(**resource_record_update_input_rdata_rdata_ptr_record_model_dict)

        # Verify the model instances are equivalent
        assert resource_record_update_input_rdata_rdata_ptr_record_model == resource_record_update_input_rdata_rdata_ptr_record_model2

        # Convert model instance back to dict and verify no loss of data
        resource_record_update_input_rdata_rdata_ptr_record_model_json2 = resource_record_update_input_rdata_rdata_ptr_record_model.to_dict()
        assert resource_record_update_input_rdata_rdata_ptr_record_model_json2 == resource_record_update_input_rdata_rdata_ptr_record_model_json

#-----------------------------------------------------------------------------
# Test Class for ResourceRecordUpdateInputRdataRdataSrvRecord
#-----------------------------------------------------------------------------
class TestResourceRecordUpdateInputRdataRdataSrvRecord():

    #--------------------------------------------------------
    # Test serialization/deserialization for ResourceRecordUpdateInputRdataRdataSrvRecord
    #--------------------------------------------------------
    def test_resource_record_update_input_rdata_rdata_srv_record_serialization(self):

        # Construct a json representation of a ResourceRecordUpdateInputRdataRdataSrvRecord model
        resource_record_update_input_rdata_rdata_srv_record_model_json = {}
        resource_record_update_input_rdata_rdata_srv_record_model_json['port'] = 80
        resource_record_update_input_rdata_rdata_srv_record_model_json['priority'] = 10
        resource_record_update_input_rdata_rdata_srv_record_model_json['target'] = 'www.example.com'
        resource_record_update_input_rdata_rdata_srv_record_model_json['weight'] = 10

        # Construct a model instance of ResourceRecordUpdateInputRdataRdataSrvRecord by calling from_dict on the json representation
        resource_record_update_input_rdata_rdata_srv_record_model = ResourceRecordUpdateInputRdataRdataSrvRecord.from_dict(resource_record_update_input_rdata_rdata_srv_record_model_json)
        assert resource_record_update_input_rdata_rdata_srv_record_model != False

        # Construct a model instance of ResourceRecordUpdateInputRdataRdataSrvRecord by calling from_dict on the json representation
        resource_record_update_input_rdata_rdata_srv_record_model_dict = ResourceRecordUpdateInputRdataRdataSrvRecord.from_dict(resource_record_update_input_rdata_rdata_srv_record_model_json).__dict__
        resource_record_update_input_rdata_rdata_srv_record_model2 = ResourceRecordUpdateInputRdataRdataSrvRecord(**resource_record_update_input_rdata_rdata_srv_record_model_dict)

        # Verify the model instances are equivalent
        assert resource_record_update_input_rdata_rdata_srv_record_model == resource_record_update_input_rdata_rdata_srv_record_model2

        # Convert model instance back to dict and verify no loss of data
        resource_record_update_input_rdata_rdata_srv_record_model_json2 = resource_record_update_input_rdata_rdata_srv_record_model.to_dict()
        assert resource_record_update_input_rdata_rdata_srv_record_model_json2 == resource_record_update_input_rdata_rdata_srv_record_model_json

#-----------------------------------------------------------------------------
# Test Class for ResourceRecordUpdateInputRdataRdataTxtRecord
#-----------------------------------------------------------------------------
class TestResourceRecordUpdateInputRdataRdataTxtRecord():

    #--------------------------------------------------------
    # Test serialization/deserialization for ResourceRecordUpdateInputRdataRdataTxtRecord
    #--------------------------------------------------------
    def test_resource_record_update_input_rdata_rdata_txt_record_serialization(self):

        # Construct a json representation of a ResourceRecordUpdateInputRdataRdataTxtRecord model
        resource_record_update_input_rdata_rdata_txt_record_model_json = {}
        resource_record_update_input_rdata_rdata_txt_record_model_json['text'] = 'This is a text record'

        # Construct a model instance of ResourceRecordUpdateInputRdataRdataTxtRecord by calling from_dict on the json representation
        resource_record_update_input_rdata_rdata_txt_record_model = ResourceRecordUpdateInputRdataRdataTxtRecord.from_dict(resource_record_update_input_rdata_rdata_txt_record_model_json)
        assert resource_record_update_input_rdata_rdata_txt_record_model != False

        # Construct a model instance of ResourceRecordUpdateInputRdataRdataTxtRecord by calling from_dict on the json representation
        resource_record_update_input_rdata_rdata_txt_record_model_dict = ResourceRecordUpdateInputRdataRdataTxtRecord.from_dict(resource_record_update_input_rdata_rdata_txt_record_model_json).__dict__
        resource_record_update_input_rdata_rdata_txt_record_model2 = ResourceRecordUpdateInputRdataRdataTxtRecord(**resource_record_update_input_rdata_rdata_txt_record_model_dict)

        # Verify the model instances are equivalent
        assert resource_record_update_input_rdata_rdata_txt_record_model == resource_record_update_input_rdata_rdata_txt_record_model2

        # Convert model instance back to dict and verify no loss of data
        resource_record_update_input_rdata_rdata_txt_record_model_json2 = resource_record_update_input_rdata_rdata_txt_record_model.to_dict()
        assert resource_record_update_input_rdata_rdata_txt_record_model_json2 == resource_record_update_input_rdata_rdata_txt_record_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
