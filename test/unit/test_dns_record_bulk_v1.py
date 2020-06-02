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
import responses
import tempfile
from ibm_cloud_networking_services import DnsRecordBulkV1

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
# Start of Service: ImportZoneFiles
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for post_dns_records_bulk
#-----------------------------------------------------------------------------
class TestPostDnsRecordsBulk():

    #--------------------------------------------------------
    # post_dns_records_bulk()
    #--------------------------------------------------------
    @responses.activate
    def test_post_dns_records_bulk_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/dns_records_bulk'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"recs_added": 5, "total_records_parsed": 5}, "timing": {"start_time": "2014-03-01T12:20:00Z", "end_time": "2014-03-01T12:20:01Z", "process_time": 1}}'
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
            file_content_type=file_content_type
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
        url = base_url + '/v1/testString/zones/testString/dns_records_bulk'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"recs_added": 5, "total_records_parsed": 5}, "timing": {"start_time": "2014-03-01T12:20:00Z", "end_time": "2014-03-01T12:20:01Z", "process_time": 1}}'
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


# endregion
##############################################################################
# End of Service: ImportZoneFiles
##############################################################################

##############################################################################
# Start of Service: ExportZoneFiles
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_dns_records_bulk
#-----------------------------------------------------------------------------
class TestGetDnsRecordsBulk():

    #--------------------------------------------------------
    # get_dns_records_bulk()
    #--------------------------------------------------------
    @responses.activate
    def test_get_dns_records_bulk_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/dns_records_bulk'
        mock_response = 'Contents of response byte-stream...'
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
    # test_get_dns_records_bulk_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_dns_records_bulk_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/dns_records_bulk'
        mock_response = 'Contents of response byte-stream...'
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


# endregion
##############################################################################
# End of Service: ExportZoneFiles
##############################################################################

