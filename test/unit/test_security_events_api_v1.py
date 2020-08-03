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
import re
import requests
import responses
from ibm_cloud_networking_services.security_events_api_v1 import *

crn = 'testString'
zone_id = 'testString'

service = SecurityEventsApiV1(
    authenticator=NoAuthAuthenticator(),
    crn=crn,
    zone_id=zone_id
    )

base_url = 'https://api.cis.cloud.ibm.com'
service.set_service_url(base_url)

##############################################################################
# Start of Service: SecurityEvents
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for security_events
#-----------------------------------------------------------------------------
class TestSecurityEvents():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # security_events()
    #--------------------------------------------------------
    @responses.activate
    def test_security_events_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/security/events')
        mock_response = '{"result": [{"ray_id": "4c6392789858b224", "kind": "firewall", "source": "rateLimit", "action": "drop", "rule_id": "fe38bd35ca284de69b5ecbaa6db87dc3", "ip": "192.168.1.1", "ip_class": "noRecord", "country": "CN", "colo": "HKG", "host": "www.example.com", "method": "GET", "proto": "HTTP/2", "scheme": "https", "ua": "curl/7.61.1", "uri": "/", "occurred_at": "2019-01-01T12:00:00", "matches": [{"rule_id": "fe38bd35ca284de69b5ecbaa6db87dc3", "source": "rateLimit", "action": "drop", "metadata": {"anyKey": "anyValue"}}]}], "result_info": {"cursors": {"after": "bnRIiaU-14b2YBxIefX28h7Zqw50XXPA4Vu4Sa-DPa4qaGH-z47uwtOR0Hm2Y3cSh56raQb1POqaBwGXD44", "before": "dmmGxcD665xj3RiQ8eRqclts94GF3M4KpHEJ7AVekLtOUsHLHssfGaV_d8nZgLszk_iElB9LckPhFgmkTXHX"}, "scanned_range": {"since": "2019-04-12 07:44:18", "until": "2019-04-12 07:44:18"}}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        ip_class = 'unknown'
        method = 'GET'
        scheme = 'unknown'
        ip = 'testString'
        host = 'testString'
        proto = 'UNK'
        uri = 'testString'
        ua = 'testString'
        colo = 'testString'
        ray_id = 'testString'
        kind = 'firewall'
        action = 'unknown'
        cursor = 'testString'
        country = 'testString'
        since = datetime.fromtimestamp(1580236840.123456, timezone.utc)
        source = 'unknown'
        limit = 10
        rule_id = 'testString'
        until = datetime.fromtimestamp(1580236840.123456, timezone.utc)

        # Invoke method
        response = service.security_events(
            ip_class=ip_class,
            method=method,
            scheme=scheme,
            ip=ip,
            host=host,
            proto=proto,
            uri=uri,
            ua=ua,
            colo=colo,
            ray_id=ray_id,
            kind=kind,
            action=action,
            cursor=cursor,
            country=country,
            since=since,
            source=source,
            limit=limit,
            rule_id=rule_id,
            until=until,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'ip_class={}'.format(ip_class) in query_string
        assert 'method={}'.format(method) in query_string
        assert 'scheme={}'.format(scheme) in query_string
        assert 'ip={}'.format(ip) in query_string
        assert 'host={}'.format(host) in query_string
        assert 'proto={}'.format(proto) in query_string
        assert 'uri={}'.format(uri) in query_string
        assert 'ua={}'.format(ua) in query_string
        assert 'colo={}'.format(colo) in query_string
        assert 'ray_id={}'.format(ray_id) in query_string
        assert 'kind={}'.format(kind) in query_string
        assert 'action={}'.format(action) in query_string
        assert 'cursor={}'.format(cursor) in query_string
        assert 'country={}'.format(country) in query_string
        assert 'source={}'.format(source) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'rule_id={}'.format(rule_id) in query_string


    #--------------------------------------------------------
    # test_security_events_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_security_events_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/security/events')
        mock_response = '{"result": [{"ray_id": "4c6392789858b224", "kind": "firewall", "source": "rateLimit", "action": "drop", "rule_id": "fe38bd35ca284de69b5ecbaa6db87dc3", "ip": "192.168.1.1", "ip_class": "noRecord", "country": "CN", "colo": "HKG", "host": "www.example.com", "method": "GET", "proto": "HTTP/2", "scheme": "https", "ua": "curl/7.61.1", "uri": "/", "occurred_at": "2019-01-01T12:00:00", "matches": [{"rule_id": "fe38bd35ca284de69b5ecbaa6db87dc3", "source": "rateLimit", "action": "drop", "metadata": {"anyKey": "anyValue"}}]}], "result_info": {"cursors": {"after": "bnRIiaU-14b2YBxIefX28h7Zqw50XXPA4Vu4Sa-DPa4qaGH-z47uwtOR0Hm2Y3cSh56raQb1POqaBwGXD44", "before": "dmmGxcD665xj3RiQ8eRqclts94GF3M4KpHEJ7AVekLtOUsHLHssfGaV_d8nZgLszk_iElB9LckPhFgmkTXHX"}, "scanned_range": {"since": "2019-04-12 07:44:18", "until": "2019-04-12 07:44:18"}}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.security_events()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_security_events_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_security_events_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/security/events')
        mock_response = '{"result": [{"ray_id": "4c6392789858b224", "kind": "firewall", "source": "rateLimit", "action": "drop", "rule_id": "fe38bd35ca284de69b5ecbaa6db87dc3", "ip": "192.168.1.1", "ip_class": "noRecord", "country": "CN", "colo": "HKG", "host": "www.example.com", "method": "GET", "proto": "HTTP/2", "scheme": "https", "ua": "curl/7.61.1", "uri": "/", "occurred_at": "2019-01-01T12:00:00", "matches": [{"rule_id": "fe38bd35ca284de69b5ecbaa6db87dc3", "source": "rateLimit", "action": "drop", "metadata": {"anyKey": "anyValue"}}]}], "result_info": {"cursors": {"after": "bnRIiaU-14b2YBxIefX28h7Zqw50XXPA4Vu4Sa-DPa4qaGH-z47uwtOR0Hm2Y3cSh56raQb1POqaBwGXD44", "before": "dmmGxcD665xj3RiQ8eRqclts94GF3M4KpHEJ7AVekLtOUsHLHssfGaV_d8nZgLszk_iElB9LckPhFgmkTXHX"}, "scanned_range": {"since": "2019-04-12 07:44:18", "until": "2019-04-12 07:44:18"}}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                service.security_events(**req_copy)



# endregion
##############################################################################
# End of Service: SecurityEvents
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
#-----------------------------------------------------------------------------
# Test Class for ResultInfoCursors
#-----------------------------------------------------------------------------
class TestResultInfoCursors():

    #--------------------------------------------------------
    # Test serialization/deserialization for ResultInfoCursors
    #--------------------------------------------------------
    def test_result_info_cursors_serialization(self):

        # Construct a json representation of a ResultInfoCursors model
        result_info_cursors_model_json = {}
        result_info_cursors_model_json['after'] = 'bnRIiaU-14b2YBxIefX28h7Zqw50XXPA4Vu4Sa-DPa4qaGH-z47uwtOR0Hm2Y3cSh56raQb1POqaBwGXD44'
        result_info_cursors_model_json['before'] = 'dmmGxcD665xj3RiQ8eRqclts94GF3M4KpHEJ7AVekLtOUsHLHssfGaV_d8nZgLszk_iElB9LckPhFgmkTXHX'

        # Construct a model instance of ResultInfoCursors by calling from_dict on the json representation
        result_info_cursors_model = ResultInfoCursors.from_dict(result_info_cursors_model_json)
        assert result_info_cursors_model != False

        # Construct a model instance of ResultInfoCursors by calling from_dict on the json representation
        result_info_cursors_model_dict = ResultInfoCursors.from_dict(result_info_cursors_model_json).__dict__
        result_info_cursors_model2 = ResultInfoCursors(**result_info_cursors_model_dict)

        # Verify the model instances are equivalent
        assert result_info_cursors_model == result_info_cursors_model2

        # Convert model instance back to dict and verify no loss of data
        result_info_cursors_model_json2 = result_info_cursors_model.to_dict()
        assert result_info_cursors_model_json2 == result_info_cursors_model_json

#-----------------------------------------------------------------------------
# Test Class for ResultInfoScannedRange
#-----------------------------------------------------------------------------
class TestResultInfoScannedRange():

    #--------------------------------------------------------
    # Test serialization/deserialization for ResultInfoScannedRange
    #--------------------------------------------------------
    def test_result_info_scanned_range_serialization(self):

        # Construct a json representation of a ResultInfoScannedRange model
        result_info_scanned_range_model_json = {}
        result_info_scanned_range_model_json['since'] = '2019-04-12 07:44:18'
        result_info_scanned_range_model_json['until'] = '2019-04-12 07:44:18'

        # Construct a model instance of ResultInfoScannedRange by calling from_dict on the json representation
        result_info_scanned_range_model = ResultInfoScannedRange.from_dict(result_info_scanned_range_model_json)
        assert result_info_scanned_range_model != False

        # Construct a model instance of ResultInfoScannedRange by calling from_dict on the json representation
        result_info_scanned_range_model_dict = ResultInfoScannedRange.from_dict(result_info_scanned_range_model_json).__dict__
        result_info_scanned_range_model2 = ResultInfoScannedRange(**result_info_scanned_range_model_dict)

        # Verify the model instances are equivalent
        assert result_info_scanned_range_model == result_info_scanned_range_model2

        # Convert model instance back to dict and verify no loss of data
        result_info_scanned_range_model_json2 = result_info_scanned_range_model.to_dict()
        assert result_info_scanned_range_model_json2 == result_info_scanned_range_model_json

#-----------------------------------------------------------------------------
# Test Class for SecurityEventObjectMatchesItem
#-----------------------------------------------------------------------------
class TestSecurityEventObjectMatchesItem():

    #--------------------------------------------------------
    # Test serialization/deserialization for SecurityEventObjectMatchesItem
    #--------------------------------------------------------
    def test_security_event_object_matches_item_serialization(self):

        # Construct a json representation of a SecurityEventObjectMatchesItem model
        security_event_object_matches_item_model_json = {}
        security_event_object_matches_item_model_json['rule_id'] = 'fe38bd35ca284de69b5ecbaa6db87dc3'
        security_event_object_matches_item_model_json['source'] = 'rateLimit'
        security_event_object_matches_item_model_json['action'] = 'drop'
        security_event_object_matches_item_model_json['metadata'] = { 'foo': 'bar' }

        # Construct a model instance of SecurityEventObjectMatchesItem by calling from_dict on the json representation
        security_event_object_matches_item_model = SecurityEventObjectMatchesItem.from_dict(security_event_object_matches_item_model_json)
        assert security_event_object_matches_item_model != False

        # Construct a model instance of SecurityEventObjectMatchesItem by calling from_dict on the json representation
        security_event_object_matches_item_model_dict = SecurityEventObjectMatchesItem.from_dict(security_event_object_matches_item_model_json).__dict__
        security_event_object_matches_item_model2 = SecurityEventObjectMatchesItem(**security_event_object_matches_item_model_dict)

        # Verify the model instances are equivalent
        assert security_event_object_matches_item_model == security_event_object_matches_item_model2

        # Convert model instance back to dict and verify no loss of data
        security_event_object_matches_item_model_json2 = security_event_object_matches_item_model.to_dict()
        assert security_event_object_matches_item_model_json2 == security_event_object_matches_item_model_json

#-----------------------------------------------------------------------------
# Test Class for ResultInfo
#-----------------------------------------------------------------------------
class TestResultInfo():

    #--------------------------------------------------------
    # Test serialization/deserialization for ResultInfo
    #--------------------------------------------------------
    def test_result_info_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        result_info_cursors_model = {} # ResultInfoCursors
        result_info_cursors_model['after'] = 'bnRIiaU-14b2YBxIefX28h7Zqw50XXPA4Vu4Sa-DPa4qaGH-z47uwtOR0Hm2Y3cSh56raQb1POqaBwGXD44'
        result_info_cursors_model['before'] = 'dmmGxcD665xj3RiQ8eRqclts94GF3M4KpHEJ7AVekLtOUsHLHssfGaV_d8nZgLszk_iElB9LckPhFgmkTXHX'

        result_info_scanned_range_model = {} # ResultInfoScannedRange
        result_info_scanned_range_model['since'] = '2019-04-12 07:44:18'
        result_info_scanned_range_model['until'] = '2019-04-12 07:44:18'

        # Construct a json representation of a ResultInfo model
        result_info_model_json = {}
        result_info_model_json['cursors'] = result_info_cursors_model
        result_info_model_json['scanned_range'] = result_info_scanned_range_model

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
# Test Class for SecurityEventObject
#-----------------------------------------------------------------------------
class TestSecurityEventObject():

    #--------------------------------------------------------
    # Test serialization/deserialization for SecurityEventObject
    #--------------------------------------------------------
    def test_security_event_object_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        security_event_object_matches_item_model = {} # SecurityEventObjectMatchesItem
        security_event_object_matches_item_model['rule_id'] = 'fe38bd35ca284de69b5ecbaa6db87dc3'
        security_event_object_matches_item_model['source'] = 'rateLimit'
        security_event_object_matches_item_model['action'] = 'drop'
        security_event_object_matches_item_model['metadata'] = { 'foo': 'bar' }

        # Construct a json representation of a SecurityEventObject model
        security_event_object_model_json = {}
        security_event_object_model_json['ray_id'] = '4c6392789858b224'
        security_event_object_model_json['kind'] = 'firewall'
        security_event_object_model_json['source'] = 'rateLimit'
        security_event_object_model_json['action'] = 'drop'
        security_event_object_model_json['rule_id'] = 'fe38bd35ca284de69b5ecbaa6db87dc3'
        security_event_object_model_json['ip'] = '192.168.1.1'
        security_event_object_model_json['ip_class'] = 'noRecord'
        security_event_object_model_json['country'] = 'CN'
        security_event_object_model_json['colo'] = 'HKG'
        security_event_object_model_json['host'] = 'www.example.com'
        security_event_object_model_json['method'] = 'GET'
        security_event_object_model_json['proto'] = 'HTTP/2'
        security_event_object_model_json['scheme'] = 'https'
        security_event_object_model_json['ua'] = 'curl/7.61.1'
        security_event_object_model_json['uri'] = '/'
        security_event_object_model_json['occurred_at'] = '2020-01-28T18:40:40.123456Z'
        security_event_object_model_json['matches'] = [security_event_object_matches_item_model]

        # Construct a model instance of SecurityEventObject by calling from_dict on the json representation
        security_event_object_model = SecurityEventObject.from_dict(security_event_object_model_json)
        assert security_event_object_model != False

        # Construct a model instance of SecurityEventObject by calling from_dict on the json representation
        security_event_object_model_dict = SecurityEventObject.from_dict(security_event_object_model_json).__dict__
        security_event_object_model2 = SecurityEventObject(**security_event_object_model_dict)

        # Verify the model instances are equivalent
        assert security_event_object_model == security_event_object_model2

        # Convert model instance back to dict and verify no loss of data
        security_event_object_model_json2 = security_event_object_model.to_dict()
        assert security_event_object_model_json2 == security_event_object_model_json

#-----------------------------------------------------------------------------
# Test Class for SecurityEvents
#-----------------------------------------------------------------------------
class TestSecurityEvents():

    #--------------------------------------------------------
    # Test serialization/deserialization for SecurityEvents
    #--------------------------------------------------------
    def test_security_events_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        result_info_cursors_model = {} # ResultInfoCursors
        result_info_cursors_model['after'] = 'bnRIiaU-14b2YBxIefX28h7Zqw50XXPA4Vu4Sa-DPa4qaGH-z47uwtOR0Hm2Y3cSh56raQb1POqaBwGXD44'
        result_info_cursors_model['before'] = 'dmmGxcD665xj3RiQ8eRqclts94GF3M4KpHEJ7AVekLtOUsHLHssfGaV_d8nZgLszk_iElB9LckPhFgmkTXHX'

        result_info_scanned_range_model = {} # ResultInfoScannedRange
        result_info_scanned_range_model['since'] = '2019-04-12 07:44:18'
        result_info_scanned_range_model['until'] = '2019-04-12 07:44:18'

        security_event_object_matches_item_model = {} # SecurityEventObjectMatchesItem
        security_event_object_matches_item_model['rule_id'] = 'fe38bd35ca284de69b5ecbaa6db87dc3'
        security_event_object_matches_item_model['source'] = 'rateLimit'
        security_event_object_matches_item_model['action'] = 'drop'
        security_event_object_matches_item_model['metadata'] = { 'foo': 'bar' }

        result_info_model = {} # ResultInfo
        result_info_model['cursors'] = result_info_cursors_model
        result_info_model['scanned_range'] = result_info_scanned_range_model

        security_event_object_model = {} # SecurityEventObject
        security_event_object_model['ray_id'] = '4c6392789858b224'
        security_event_object_model['kind'] = 'firewall'
        security_event_object_model['source'] = 'rateLimit'
        security_event_object_model['action'] = 'drop'
        security_event_object_model['rule_id'] = 'fe38bd35ca284de69b5ecbaa6db87dc3'
        security_event_object_model['ip'] = '192.168.1.1'
        security_event_object_model['ip_class'] = 'noRecord'
        security_event_object_model['country'] = 'CN'
        security_event_object_model['colo'] = 'HKG'
        security_event_object_model['host'] = 'www.example.com'
        security_event_object_model['method'] = 'GET'
        security_event_object_model['proto'] = 'HTTP/2'
        security_event_object_model['scheme'] = 'https'
        security_event_object_model['ua'] = 'curl/7.61.1'
        security_event_object_model['uri'] = '/'
        security_event_object_model['occurred_at'] = '2020-01-28T18:40:40.123456Z'
        security_event_object_model['matches'] = [security_event_object_matches_item_model]

        # Construct a json representation of a SecurityEvents model
        security_events_model_json = {}
        security_events_model_json['result'] = [security_event_object_model]
        security_events_model_json['result_info'] = result_info_model
        security_events_model_json['success'] = True
        security_events_model_json['errors'] = [['testString']]
        security_events_model_json['messages'] = [['testString']]

        # Construct a model instance of SecurityEvents by calling from_dict on the json representation
        security_events_model = SecurityEvents.from_dict(security_events_model_json)
        assert security_events_model != False

        # Construct a model instance of SecurityEvents by calling from_dict on the json representation
        security_events_model_dict = SecurityEvents.from_dict(security_events_model_json).__dict__
        security_events_model2 = SecurityEvents(**security_events_model_dict)

        # Verify the model instances are equivalent
        assert security_events_model == security_events_model2

        # Convert model instance back to dict and verify no loss of data
        security_events_model_json2 = security_events_model.to_dict()
        assert security_events_model_json2 == security_events_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
