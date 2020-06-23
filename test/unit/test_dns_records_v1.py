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

    #--------------------------------------------------------
    # list_all_dns_records()
    #--------------------------------------------------------
    @responses.activate
    def test_list_all_dns_records_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/dns_records'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "host-1.test-example.com", "type": "A", "content": "169.154.10.10", "zone_id": "023e105f4ecef8ad9ca31a8372d0c353", "zone_name": "test-example.com", "proxiable": true, "proxied": false, "ttl": 120, "priority": 5, "data": "unknown property type: data"}], "result_info": {"page": 1, "per_page": 20, "count": 1, "total_count": 2000}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        type = 'testString'
        name = 'testString'
        content = 'testString'
        page = 38
        per_page = 38
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
            match=match
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
        url = base_url + '/v1/testString/zones/testString/dns_records'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "host-1.test-example.com", "type": "A", "content": "169.154.10.10", "zone_id": "023e105f4ecef8ad9ca31a8372d0c353", "zone_name": "test-example.com", "proxiable": true, "proxied": false, "ttl": 120, "priority": 5, "data": "unknown property type: data"}], "result_info": {"page": 1, "per_page": 20, "count": 1, "total_count": 2000}}'
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


#-----------------------------------------------------------------------------
# Test Class for create_dns_record
#-----------------------------------------------------------------------------
class TestCreateDnsRecord():

    #--------------------------------------------------------
    # create_dns_record()
    #--------------------------------------------------------
    @responses.activate
    def test_create_dns_record_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/dns_records'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "host-1.test-example.com", "type": "A", "content": "169.154.10.10", "zone_id": "023e105f4ecef8ad9ca31a8372d0c353", "zone_name": "test-example.com", "proxiable": true, "proxied": false, "ttl": 120, "priority": 5, "data": "unknown property type: data"}}'
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
        data = 'unknown type: object'

        # Invoke method
        response = service.create_dns_record(
            type=type,
            name=name,
            content=content,
            priority=priority,
            data=data,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['type'] == type
        assert req_body['name'] == name
        assert req_body['content'] == content
        assert req_body['priority'] == priority
        assert req_body['data'] == data


    #--------------------------------------------------------
    # test_create_dns_record_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_dns_record_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/dns_records'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "host-1.test-example.com", "type": "A", "content": "169.154.10.10", "zone_id": "023e105f4ecef8ad9ca31a8372d0c353", "zone_name": "test-example.com", "proxiable": true, "proxied": false, "ttl": 120, "priority": 5, "data": "unknown property type: data"}}'
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


#-----------------------------------------------------------------------------
# Test Class for delete_dns_record
#-----------------------------------------------------------------------------
class TestDeleteDnsRecord():

    #--------------------------------------------------------
    # delete_dns_record()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_dns_record_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/dns_records/testString'
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
            dnsrecord_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_delete_dns_record_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_dns_record_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/dns_records/testString'
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
            dnsrecord_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for get_dns_record
#-----------------------------------------------------------------------------
class TestGetDnsRecord():

    #--------------------------------------------------------
    # get_dns_record()
    #--------------------------------------------------------
    @responses.activate
    def test_get_dns_record_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/dns_records/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "host-1.test-example.com", "type": "A", "content": "169.154.10.10", "zone_id": "023e105f4ecef8ad9ca31a8372d0c353", "zone_name": "test-example.com", "proxiable": true, "proxied": false, "ttl": 120, "priority": 5, "data": "unknown property type: data"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        dnsrecord_identifier = 'testString'

        # Invoke method
        response = service.get_dns_record(
            dnsrecord_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_dns_record_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_dns_record_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/dns_records/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "host-1.test-example.com", "type": "A", "content": "169.154.10.10", "zone_id": "023e105f4ecef8ad9ca31a8372d0c353", "zone_name": "test-example.com", "proxiable": true, "proxied": false, "ttl": 120, "priority": 5, "data": "unknown property type: data"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        dnsrecord_identifier = 'testString'

        # Invoke method
        response = service.get_dns_record(
            dnsrecord_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for update_dns_record
#-----------------------------------------------------------------------------
class TestUpdateDnsRecord():

    #--------------------------------------------------------
    # update_dns_record()
    #--------------------------------------------------------
    @responses.activate
    def test_update_dns_record_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/dns_records/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "host-1.test-example.com", "type": "A", "content": "169.154.10.10", "zone_id": "023e105f4ecef8ad9ca31a8372d0c353", "zone_name": "test-example.com", "proxiable": true, "proxied": false, "ttl": 120, "priority": 5, "data": "unknown property type: data"}}'
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
        data = 'unknown type: object'

        # Invoke method
        response = service.update_dns_record(
            dnsrecord_identifier,
            type=type,
            name=name,
            content=content,
            priority=priority,
            proxied=proxied,
            data=data,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['type'] == type
        assert req_body['name'] == name
        assert req_body['content'] == content
        assert req_body['priority'] == priority
        assert req_body['proxied'] == proxied
        assert req_body['data'] == data


    #--------------------------------------------------------
    # test_update_dns_record_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_dns_record_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/dns_records/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "host-1.test-example.com", "type": "A", "content": "169.154.10.10", "zone_id": "023e105f4ecef8ad9ca31a8372d0c353", "zone_name": "test-example.com", "proxiable": true, "proxied": false, "ttl": 120, "priority": 5, "data": "unknown property type: data"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        dnsrecord_identifier = 'testString'

        # Invoke method
        response = service.update_dns_record(
            dnsrecord_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: DNSRecords
##############################################################################

