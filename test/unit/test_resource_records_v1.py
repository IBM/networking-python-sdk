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

    #--------------------------------------------------------
    # list_resource_records()
    #--------------------------------------------------------
    @responses.activate
    def test_list_resource_records_all_params(self):
        # Set up mock
        url = base_url + '/instances/testString/dnszones/testString/resource_records'
        mock_response = '{"resource_records": [{"id": "SRV:5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "name": "_sip._udp.test.example.com", "type": "SRV", "ttl": 120, "rdata": "unknown property type: rdata", "service": "_sip", "protocol": "udp"}], "offset": 0, "limit": 20, "total_count": 200, "first": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/resource_records?limit=20"}, "next": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/resource_records?offset=20&limit=20"}}'
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
    # test_list_resource_records_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_resource_records_required_params(self):
        # Set up mock
        url = base_url + '/instances/testString/dnszones/testString/resource_records'
        mock_response = '{"resource_records": [{"id": "SRV:5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "name": "_sip._udp.test.example.com", "type": "SRV", "ttl": 120, "rdata": "unknown property type: rdata", "service": "_sip", "protocol": "udp"}], "offset": 0, "limit": 20, "total_count": 200, "first": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/resource_records?limit=20"}, "next": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/resource_records?offset=20&limit=20"}}'
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
            dnszone_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for create_resource_record
#-----------------------------------------------------------------------------
class TestCreateResourceRecord():

    #--------------------------------------------------------
    # create_resource_record()
    #--------------------------------------------------------
    @responses.activate
    def test_create_resource_record_all_params(self):
        # Set up mock
        url = base_url + '/instances/testString/dnszones/testString/resource_records'
        mock_response = '{"id": "SRV:5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "name": "_sip._udp.test.example.com", "type": "SRV", "ttl": 120, "rdata": "unknown property type: rdata", "service": "_sip", "protocol": "udp"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a ResourceRecordInputRdataRdataARecord model
        resource_record_input_rdata_model =  {
            'ip': '10.110.201.214'
        }

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
            x_correlation_id=x_correlation_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['type'] == type
        assert req_body['name'] == name
        assert req_body['rdata'] == rdata
        assert req_body['ttl'] == ttl
        assert req_body['service'] == service
        assert req_body['protocol'] == protocol


    #--------------------------------------------------------
    # test_create_resource_record_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_resource_record_required_params(self):
        # Set up mock
        url = base_url + '/instances/testString/dnszones/testString/resource_records'
        mock_response = '{"id": "SRV:5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "name": "_sip._udp.test.example.com", "type": "SRV", "ttl": 120, "rdata": "unknown property type: rdata", "service": "_sip", "protocol": "udp"}'
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
            dnszone_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for delete_resource_record
#-----------------------------------------------------------------------------
class TestDeleteResourceRecord():

    #--------------------------------------------------------
    # delete_resource_record()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_resource_record_all_params(self):
        # Set up mock
        url = base_url + '/instances/testString/dnszones/testString/resource_records/testString'
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
            x_correlation_id=x_correlation_id
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
        url = base_url + '/instances/testString/dnszones/testString/resource_records/testString'
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
            record_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


#-----------------------------------------------------------------------------
# Test Class for get_resource_record
#-----------------------------------------------------------------------------
class TestGetResourceRecord():

    #--------------------------------------------------------
    # get_resource_record()
    #--------------------------------------------------------
    @responses.activate
    def test_get_resource_record_all_params(self):
        # Set up mock
        url = base_url + '/instances/testString/dnszones/testString/resource_records/testString'
        mock_response = '{"id": "SRV:5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "name": "_sip._udp.test.example.com", "type": "SRV", "ttl": 120, "rdata": "unknown property type: rdata", "service": "_sip", "protocol": "udp"}'
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
            x_correlation_id=x_correlation_id
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
        url = base_url + '/instances/testString/dnszones/testString/resource_records/testString'
        mock_response = '{"id": "SRV:5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "name": "_sip._udp.test.example.com", "type": "SRV", "ttl": 120, "rdata": "unknown property type: rdata", "service": "_sip", "protocol": "udp"}'
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
            record_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for update_resource_record
#-----------------------------------------------------------------------------
class TestUpdateResourceRecord():

    #--------------------------------------------------------
    # update_resource_record()
    #--------------------------------------------------------
    @responses.activate
    def test_update_resource_record_all_params(self):
        # Set up mock
        url = base_url + '/instances/testString/dnszones/testString/resource_records/testString'
        mock_response = '{"id": "SRV:5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "name": "_sip._udp.test.example.com", "type": "SRV", "ttl": 120, "rdata": "unknown property type: rdata", "service": "_sip", "protocol": "udp"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a ResourceRecordUpdateInputRdataRdataARecord model
        resource_record_update_input_rdata_model =  {
            'ip': '10.110.201.214'
        }

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
            x_correlation_id=x_correlation_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == name
        assert req_body['rdata'] == rdata
        assert req_body['ttl'] == ttl
        assert req_body['service'] == service
        assert req_body['protocol'] == protocol


    #--------------------------------------------------------
    # test_update_resource_record_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_resource_record_required_params(self):
        # Set up mock
        url = base_url + '/instances/testString/dnszones/testString/resource_records/testString'
        mock_response = '{"id": "SRV:5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "name": "_sip._udp.test.example.com", "type": "SRV", "ttl": 120, "rdata": "unknown property type: rdata", "service": "_sip", "protocol": "udp"}'
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
            record_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: ResourceRecords
##############################################################################

