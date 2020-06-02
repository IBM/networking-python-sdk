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
from ibm_cloud_networking_services.security_events_api_v1 import SecurityEventsApiV1

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

    #--------------------------------------------------------
    # security_events()
    #--------------------------------------------------------
    @responses.activate
    def test_security_events_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/security/events'
        mock_response = '{"result": [{"ray_id": "4c6392789858b224", "kind": "firewall", "source": "rateLimit", "action": "drop", "rule_id": "fe38bd35ca284de69b5ecbaa6db87dc3", "ip": "192.168.1.1", "ip_class": "noRecord", "country": "CN", "colo": "HKG", "host": "www.example.com", "method": "GET", "proto": "HTTP/2", "scheme": "https", "ua": "curl/7.61.1", "uri": "/", "occurred_at": "2019-01-01T12:00:00", "matches": [{"rule_id": "fe38bd35ca284de69b5ecbaa6db87dc3", "source": "rateLimit", "action": "drop", "metadata": "unknown property type: metadata"}]}], "result_info": {"cursors": {"after": "bnRIiaU-14b2YBxIefX28h7Zqw50XXPA4Vu4Sa-DPa4qaGH-z47uwtOR0Hm2Y3cSh56raQb1POqaBwGXD44", "before": "dmmGxcD665xj3RiQ8eRqclts94GF3M4KpHEJ7AVekLtOUsHLHssfGaV_d8nZgLszk_iElB9LckPhFgmkTXHX"}, "scanned_range": {"since": "2019-01-01T12:00:00", "until": "2019-01-01T12:00:00"}}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
        limit = 38
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
            until=until
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
        url = base_url + '/v1/testString/zones/testString/security/events'
        mock_response = '{"result": [{"ray_id": "4c6392789858b224", "kind": "firewall", "source": "rateLimit", "action": "drop", "rule_id": "fe38bd35ca284de69b5ecbaa6db87dc3", "ip": "192.168.1.1", "ip_class": "noRecord", "country": "CN", "colo": "HKG", "host": "www.example.com", "method": "GET", "proto": "HTTP/2", "scheme": "https", "ua": "curl/7.61.1", "uri": "/", "occurred_at": "2019-01-01T12:00:00", "matches": [{"rule_id": "fe38bd35ca284de69b5ecbaa6db87dc3", "source": "rateLimit", "action": "drop", "metadata": "unknown property type: metadata"}]}], "result_info": {"cursors": {"after": "bnRIiaU-14b2YBxIefX28h7Zqw50XXPA4Vu4Sa-DPa4qaGH-z47uwtOR0Hm2Y3cSh56raQb1POqaBwGXD44", "before": "dmmGxcD665xj3RiQ8eRqclts94GF3M4KpHEJ7AVekLtOUsHLHssfGaV_d8nZgLszk_iElB9LckPhFgmkTXHX"}, "scanned_range": {"since": "2019-01-01T12:00:00", "until": "2019-01-01T12:00:00"}}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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


# endregion
##############################################################################
# End of Service: SecurityEvents
##############################################################################

