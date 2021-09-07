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
import responses
from ibm_cloud_networking_services.zones_settings_v1 import *

crn = 'testString'
zone_identifier = 'testString'

service = ZonesSettingsV1(
    authenticator=NoAuthAuthenticator(),
    crn=crn,
    zone_identifier=zone_identifier
    )

base_url = 'https://api.cis.cloud.ibm.com'
service.set_service_url(base_url)

##############################################################################
# Start of Service: ZonesSettings
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_zone_dnssec
#-----------------------------------------------------------------------------
class TestGetZoneDnssec():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_zone_dnssec()
    #--------------------------------------------------------
    @responses.activate
    def test_get_zone_dnssec_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/dnssec')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"status": "active", "flags": 257, "algorithm": "13", "key_type": "ECDSAP256SHA256", "digest_type": "2", "digest_algorithm": "SHA256", "digest": "48E939042E82C22542CB377B580DFDC52A361CEFDC72E7F9107E2B6BD9306A45", "ds": "example.com. 3600 IN DS 16953 13 2 248E939042E82C22542CB377B580DFDC52A361CEFDC72E7F9107E2B6BD9306A45", "key_tag": 42, "public_key": "oXiGYrSTO+LSCJ3mohc8EP+CzF9KxBj8/ydXJ22pKuZP3VAC3/Md/k7xZfz470CoRyZJ6gV6vml07IC3d8xqhA=="}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_zone_dnssec()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_zone_dnssec_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_zone_dnssec_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/dnssec')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"status": "active", "flags": 257, "algorithm": "13", "key_type": "ECDSAP256SHA256", "digest_type": "2", "digest_algorithm": "SHA256", "digest": "48E939042E82C22542CB377B580DFDC52A361CEFDC72E7F9107E2B6BD9306A45", "ds": "example.com. 3600 IN DS 16953 13 2 248E939042E82C22542CB377B580DFDC52A361CEFDC72E7F9107E2B6BD9306A45", "key_tag": 42, "public_key": "oXiGYrSTO+LSCJ3mohc8EP+CzF9KxBj8/ydXJ22pKuZP3VAC3/Md/k7xZfz470CoRyZJ6gV6vml07IC3d8xqhA=="}}'
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
                service.get_zone_dnssec(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_zone_dnssec
#-----------------------------------------------------------------------------
class TestUpdateZoneDnssec():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_zone_dnssec()
    #--------------------------------------------------------
    @responses.activate
    def test_update_zone_dnssec_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/dnssec')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"status": "active", "flags": 257, "algorithm": "13", "key_type": "ECDSAP256SHA256", "digest_type": "2", "digest_algorithm": "SHA256", "digest": "48E939042E82C22542CB377B580DFDC52A361CEFDC72E7F9107E2B6BD9306A45", "ds": "example.com. 3600 IN DS 16953 13 2 248E939042E82C22542CB377B580DFDC52A361CEFDC72E7F9107E2B6BD9306A45", "key_tag": 42, "public_key": "oXiGYrSTO+LSCJ3mohc8EP+CzF9KxBj8/ydXJ22pKuZP3VAC3/Md/k7xZfz470CoRyZJ6gV6vml07IC3d8xqhA=="}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        status = 'active'

        # Invoke method
        response = service.update_zone_dnssec(
            status=status,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['status'] == 'active'


    #--------------------------------------------------------
    # test_update_zone_dnssec_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_zone_dnssec_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/dnssec')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"status": "active", "flags": 257, "algorithm": "13", "key_type": "ECDSAP256SHA256", "digest_type": "2", "digest_algorithm": "SHA256", "digest": "48E939042E82C22542CB377B580DFDC52A361CEFDC72E7F9107E2B6BD9306A45", "ds": "example.com. 3600 IN DS 16953 13 2 248E939042E82C22542CB377B580DFDC52A361CEFDC72E7F9107E2B6BD9306A45", "key_tag": 42, "public_key": "oXiGYrSTO+LSCJ3mohc8EP+CzF9KxBj8/ydXJ22pKuZP3VAC3/Md/k7xZfz470CoRyZJ6gV6vml07IC3d8xqhA=="}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.update_zone_dnssec()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_zone_dnssec_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_zone_dnssec_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/dnssec')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"status": "active", "flags": 257, "algorithm": "13", "key_type": "ECDSAP256SHA256", "digest_type": "2", "digest_algorithm": "SHA256", "digest": "48E939042E82C22542CB377B580DFDC52A361CEFDC72E7F9107E2B6BD9306A45", "ds": "example.com. 3600 IN DS 16953 13 2 248E939042E82C22542CB377B580DFDC52A361CEFDC72E7F9107E2B6BD9306A45", "key_tag": 42, "public_key": "oXiGYrSTO+LSCJ3mohc8EP+CzF9KxBj8/ydXJ22pKuZP3VAC3/Md/k7xZfz470CoRyZJ6gV6vml07IC3d8xqhA=="}}'
        responses.add(responses.PATCH,
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
                service.update_zone_dnssec(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_zone_cname_flattening
#-----------------------------------------------------------------------------
class TestGetZoneCnameFlattening():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_zone_cname_flattening()
    #--------------------------------------------------------
    @responses.activate
    def test_get_zone_cname_flattening_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/cname_flattening')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "cname_flattening", "value": "flatten_all", "modified_on": "2019-01-01T12:00:00", "editable": true}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_zone_cname_flattening()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_zone_cname_flattening_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_zone_cname_flattening_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/cname_flattening')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "cname_flattening", "value": "flatten_all", "modified_on": "2019-01-01T12:00:00", "editable": true}}'
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
                service.get_zone_cname_flattening(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_zone_cname_flattening
#-----------------------------------------------------------------------------
class TestUpdateZoneCnameFlattening():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_zone_cname_flattening()
    #--------------------------------------------------------
    @responses.activate
    def test_update_zone_cname_flattening_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/cname_flattening')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "cname_flattening", "value": "flatten_all", "modified_on": "2019-01-01T12:00:00", "editable": true}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        value = 'flatten_all'

        # Invoke method
        response = service.update_zone_cname_flattening(
            value=value,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'flatten_all'


    #--------------------------------------------------------
    # test_update_zone_cname_flattening_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_zone_cname_flattening_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/cname_flattening')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "cname_flattening", "value": "flatten_all", "modified_on": "2019-01-01T12:00:00", "editable": true}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.update_zone_cname_flattening()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_zone_cname_flattening_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_zone_cname_flattening_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/cname_flattening')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "cname_flattening", "value": "flatten_all", "modified_on": "2019-01-01T12:00:00", "editable": true}}'
        responses.add(responses.PATCH,
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
                service.update_zone_cname_flattening(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_opportunistic_encryption
#-----------------------------------------------------------------------------
class TestGetOpportunisticEncryption():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_opportunistic_encryption()
    #--------------------------------------------------------
    @responses.activate
    def test_get_opportunistic_encryption_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/opportunistic_encryption')
        mock_response = '{"result": {"id": "opportunistic_encryption", "value": "off", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_opportunistic_encryption()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_opportunistic_encryption_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_opportunistic_encryption_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/opportunistic_encryption')
        mock_response = '{"result": {"id": "opportunistic_encryption", "value": "off", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                service.get_opportunistic_encryption(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_opportunistic_encryption
#-----------------------------------------------------------------------------
class TestUpdateOpportunisticEncryption():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_opportunistic_encryption()
    #--------------------------------------------------------
    @responses.activate
    def test_update_opportunistic_encryption_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/opportunistic_encryption')
        mock_response = '{"result": {"id": "opportunistic_encryption", "value": "off", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        value = 'false'

        # Invoke method
        response = service.update_opportunistic_encryption(
            value=value,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'false'


    #--------------------------------------------------------
    # test_update_opportunistic_encryption_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_opportunistic_encryption_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/opportunistic_encryption')
        mock_response = '{"result": {"id": "opportunistic_encryption", "value": "off", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.update_opportunistic_encryption()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_opportunistic_encryption_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_opportunistic_encryption_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/opportunistic_encryption')
        mock_response = '{"result": {"id": "opportunistic_encryption", "value": "off", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
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
                service.update_opportunistic_encryption(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_challenge_ttl
#-----------------------------------------------------------------------------
class TestGetChallengeTtl():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_challenge_ttl()
    #--------------------------------------------------------
    @responses.activate
    def test_get_challenge_ttl_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/challenge_ttl')
        mock_response = '{"result": {"id": "challenge_ttl", "value": 1800, "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_challenge_ttl()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_challenge_ttl_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_challenge_ttl_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/challenge_ttl')
        mock_response = '{"result": {"id": "challenge_ttl", "value": 1800, "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                service.get_challenge_ttl(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_challenge_ttl
#-----------------------------------------------------------------------------
class TestUpdateChallengeTtl():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_challenge_ttl()
    #--------------------------------------------------------
    @responses.activate
    def test_update_challenge_ttl_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/challenge_ttl')
        mock_response = '{"result": {"id": "challenge_ttl", "value": 1800, "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        value = 1800

        # Invoke method
        response = service.update_challenge_ttl(
            value=value,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 1800


    #--------------------------------------------------------
    # test_update_challenge_ttl_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_challenge_ttl_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/challenge_ttl')
        mock_response = '{"result": {"id": "challenge_ttl", "value": 1800, "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.update_challenge_ttl()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_challenge_ttl_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_challenge_ttl_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/challenge_ttl')
        mock_response = '{"result": {"id": "challenge_ttl", "value": 1800, "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
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
                service.update_challenge_ttl(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_automatic_https_rewrites
#-----------------------------------------------------------------------------
class TestGetAutomaticHttpsRewrites():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_automatic_https_rewrites()
    #--------------------------------------------------------
    @responses.activate
    def test_get_automatic_https_rewrites_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/automatic_https_rewrites')
        mock_response = '{"result": {"id": "automatic_https_rewrites", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_automatic_https_rewrites()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_automatic_https_rewrites_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_automatic_https_rewrites_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/automatic_https_rewrites')
        mock_response = '{"result": {"id": "automatic_https_rewrites", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                service.get_automatic_https_rewrites(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_automatic_https_rewrites
#-----------------------------------------------------------------------------
class TestUpdateAutomaticHttpsRewrites():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_automatic_https_rewrites()
    #--------------------------------------------------------
    @responses.activate
    def test_update_automatic_https_rewrites_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/automatic_https_rewrites')
        mock_response = '{"result": {"id": "automatic_https_rewrites", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        value = 'false'

        # Invoke method
        response = service.update_automatic_https_rewrites(
            value=value,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'false'


    #--------------------------------------------------------
    # test_update_automatic_https_rewrites_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_automatic_https_rewrites_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/automatic_https_rewrites')
        mock_response = '{"result": {"id": "automatic_https_rewrites", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.update_automatic_https_rewrites()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_automatic_https_rewrites_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_automatic_https_rewrites_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/automatic_https_rewrites')
        mock_response = '{"result": {"id": "automatic_https_rewrites", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
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
                service.update_automatic_https_rewrites(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_true_client_ip
#-----------------------------------------------------------------------------
class TestGetTrueClientIp():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_true_client_ip()
    #--------------------------------------------------------
    @responses.activate
    def test_get_true_client_ip_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/true_client_ip_header')
        mock_response = '{"result": {"id": "true_client_ip_header", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_true_client_ip()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_true_client_ip_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_true_client_ip_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/true_client_ip_header')
        mock_response = '{"result": {"id": "true_client_ip_header", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                service.get_true_client_ip(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_true_client_ip
#-----------------------------------------------------------------------------
class TestUpdateTrueClientIp():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_true_client_ip()
    #--------------------------------------------------------
    @responses.activate
    def test_update_true_client_ip_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/true_client_ip_header')
        mock_response = '{"result": {"id": "true_client_ip_header", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        value = 'true'

        # Invoke method
        response = service.update_true_client_ip(
            value=value,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'true'


    #--------------------------------------------------------
    # test_update_true_client_ip_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_true_client_ip_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/true_client_ip_header')
        mock_response = '{"result": {"id": "true_client_ip_header", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.update_true_client_ip()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_true_client_ip_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_true_client_ip_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/true_client_ip_header')
        mock_response = '{"result": {"id": "true_client_ip_header", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
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
                service.update_true_client_ip(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_always_use_https
#-----------------------------------------------------------------------------
class TestGetAlwaysUseHttps():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_always_use_https()
    #--------------------------------------------------------
    @responses.activate
    def test_get_always_use_https_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/always_use_https')
        mock_response = '{"result": {"id": "always_use_https", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_always_use_https()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_always_use_https_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_always_use_https_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/always_use_https')
        mock_response = '{"result": {"id": "always_use_https", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                service.get_always_use_https(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_always_use_https
#-----------------------------------------------------------------------------
class TestUpdateAlwaysUseHttps():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_always_use_https()
    #--------------------------------------------------------
    @responses.activate
    def test_update_always_use_https_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/always_use_https')
        mock_response = '{"result": {"id": "always_use_https", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        value = 'true'

        # Invoke method
        response = service.update_always_use_https(
            value=value,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'true'


    #--------------------------------------------------------
    # test_update_always_use_https_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_always_use_https_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/always_use_https')
        mock_response = '{"result": {"id": "always_use_https", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.update_always_use_https()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_always_use_https_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_always_use_https_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/always_use_https')
        mock_response = '{"result": {"id": "always_use_https", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
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
                service.update_always_use_https(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_image_size_optimization
#-----------------------------------------------------------------------------
class TestGetImageSizeOptimization():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_image_size_optimization()
    #--------------------------------------------------------
    @responses.activate
    def test_get_image_size_optimization_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/image_size_optimization')
        mock_response = '{"result": {"id": "image_size_optimization", "value": "lossless", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_image_size_optimization()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_image_size_optimization_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_image_size_optimization_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/image_size_optimization')
        mock_response = '{"result": {"id": "image_size_optimization", "value": "lossless", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                service.get_image_size_optimization(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_image_size_optimization
#-----------------------------------------------------------------------------
class TestUpdateImageSizeOptimization():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_image_size_optimization()
    #--------------------------------------------------------
    @responses.activate
    def test_update_image_size_optimization_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/image_size_optimization')
        mock_response = '{"result": {"id": "image_size_optimization", "value": "lossless", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        value = 'lossless'

        # Invoke method
        response = service.update_image_size_optimization(
            value=value,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'lossless'


    #--------------------------------------------------------
    # test_update_image_size_optimization_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_image_size_optimization_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/image_size_optimization')
        mock_response = '{"result": {"id": "image_size_optimization", "value": "lossless", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.update_image_size_optimization()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_image_size_optimization_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_image_size_optimization_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/image_size_optimization')
        mock_response = '{"result": {"id": "image_size_optimization", "value": "lossless", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
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
                service.update_image_size_optimization(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_script_load_optimization
#-----------------------------------------------------------------------------
class TestGetScriptLoadOptimization():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_script_load_optimization()
    #--------------------------------------------------------
    @responses.activate
    def test_get_script_load_optimization_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/script_load_optimization')
        mock_response = '{"result": {"id": "script_load_optimization", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_script_load_optimization()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_script_load_optimization_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_script_load_optimization_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/script_load_optimization')
        mock_response = '{"result": {"id": "script_load_optimization", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                service.get_script_load_optimization(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_script_load_optimization
#-----------------------------------------------------------------------------
class TestUpdateScriptLoadOptimization():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_script_load_optimization()
    #--------------------------------------------------------
    @responses.activate
    def test_update_script_load_optimization_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/script_load_optimization')
        mock_response = '{"result": {"id": "script_load_optimization", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        value = 'true'

        # Invoke method
        response = service.update_script_load_optimization(
            value=value,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'true'


    #--------------------------------------------------------
    # test_update_script_load_optimization_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_script_load_optimization_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/script_load_optimization')
        mock_response = '{"result": {"id": "script_load_optimization", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.update_script_load_optimization()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_script_load_optimization_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_script_load_optimization_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/script_load_optimization')
        mock_response = '{"result": {"id": "script_load_optimization", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
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
                service.update_script_load_optimization(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_image_load_optimization
#-----------------------------------------------------------------------------
class TestGetImageLoadOptimization():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_image_load_optimization()
    #--------------------------------------------------------
    @responses.activate
    def test_get_image_load_optimization_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/image_load_optimization')
        mock_response = '{"result": {"id": "image_load_optimization", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_image_load_optimization()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_image_load_optimization_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_image_load_optimization_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/image_load_optimization')
        mock_response = '{"result": {"id": "image_load_optimization", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                service.get_image_load_optimization(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_image_load_optimization
#-----------------------------------------------------------------------------
class TestUpdateImageLoadOptimization():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_image_load_optimization()
    #--------------------------------------------------------
    @responses.activate
    def test_update_image_load_optimization_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/image_load_optimization')
        mock_response = '{"result": {"id": "image_load_optimization", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        value = 'true'

        # Invoke method
        response = service.update_image_load_optimization(
            value=value,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'true'


    #--------------------------------------------------------
    # test_update_image_load_optimization_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_image_load_optimization_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/image_load_optimization')
        mock_response = '{"result": {"id": "image_load_optimization", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.update_image_load_optimization()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_image_load_optimization_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_image_load_optimization_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/image_load_optimization')
        mock_response = '{"result": {"id": "image_load_optimization", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
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
                service.update_image_load_optimization(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_minify
#-----------------------------------------------------------------------------
class TestGetMinify():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_minify()
    #--------------------------------------------------------
    @responses.activate
    def test_get_minify_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/minify')
        mock_response = '{"result": {"id": "minify", "value": {"css": "true", "html": "true", "js": "true"}, "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_minify()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_minify_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_minify_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/minify')
        mock_response = '{"result": {"id": "minify", "value": {"css": "true", "html": "true", "js": "true"}, "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                service.get_minify(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_minify
#-----------------------------------------------------------------------------
class TestUpdateMinify():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_minify()
    #--------------------------------------------------------
    @responses.activate
    def test_update_minify_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/minify')
        mock_response = '{"result": {"id": "minify", "value": {"css": "true", "html": "true", "js": "true"}, "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a MinifySettingValue model
        minify_setting_value_model = {}
        minify_setting_value_model['css'] = 'false'
        minify_setting_value_model['html'] = 'false'
        minify_setting_value_model['js'] = 'false'

        # Set up parameter values
        value = minify_setting_value_model

        # Invoke method
        response = service.update_minify(
            value=value,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == minify_setting_value_model


    #--------------------------------------------------------
    # test_update_minify_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_minify_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/minify')
        mock_response = '{"result": {"id": "minify", "value": {"css": "true", "html": "true", "js": "true"}, "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.update_minify()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_minify_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_minify_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/minify')
        mock_response = '{"result": {"id": "minify", "value": {"css": "true", "html": "true", "js": "true"}, "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
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
                service.update_minify(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_min_tls_version
#-----------------------------------------------------------------------------
class TestGetMinTlsVersion():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_min_tls_version()
    #--------------------------------------------------------
    @responses.activate
    def test_get_min_tls_version_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/min_tls_version')
        mock_response = '{"result": {"id": "min_tls_version", "value": "1.2", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_min_tls_version()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_min_tls_version_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_min_tls_version_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/min_tls_version')
        mock_response = '{"result": {"id": "min_tls_version", "value": "1.2", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                service.get_min_tls_version(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_min_tls_version
#-----------------------------------------------------------------------------
class TestUpdateMinTlsVersion():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_min_tls_version()
    #--------------------------------------------------------
    @responses.activate
    def test_update_min_tls_version_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/min_tls_version')
        mock_response = '{"result": {"id": "min_tls_version", "value": "1.2", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        value = '1.2'

        # Invoke method
        response = service.update_min_tls_version(
            value=value,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == '1.2'


    #--------------------------------------------------------
    # test_update_min_tls_version_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_min_tls_version_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/min_tls_version')
        mock_response = '{"result": {"id": "min_tls_version", "value": "1.2", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.update_min_tls_version()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_min_tls_version_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_min_tls_version_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/min_tls_version')
        mock_response = '{"result": {"id": "min_tls_version", "value": "1.2", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
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
                service.update_min_tls_version(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_ip_geolocation
#-----------------------------------------------------------------------------
class TestGetIpGeolocation():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_ip_geolocation()
    #--------------------------------------------------------
    @responses.activate
    def test_get_ip_geolocation_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/ip_geolocation')
        mock_response = '{"result": {"id": "ip_geolocation", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_ip_geolocation()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_ip_geolocation_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_ip_geolocation_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/ip_geolocation')
        mock_response = '{"result": {"id": "ip_geolocation", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                service.get_ip_geolocation(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_ip_geolocation
#-----------------------------------------------------------------------------
class TestUpdateIpGeolocation():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_ip_geolocation()
    #--------------------------------------------------------
    @responses.activate
    def test_update_ip_geolocation_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/ip_geolocation')
        mock_response = '{"result": {"id": "ip_geolocation", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        value = 'true'

        # Invoke method
        response = service.update_ip_geolocation(
            value=value,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'true'


    #--------------------------------------------------------
    # test_update_ip_geolocation_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_ip_geolocation_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/ip_geolocation')
        mock_response = '{"result": {"id": "ip_geolocation", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.update_ip_geolocation()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_ip_geolocation_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_ip_geolocation_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/ip_geolocation')
        mock_response = '{"result": {"id": "ip_geolocation", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
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
                service.update_ip_geolocation(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_server_side_exclude
#-----------------------------------------------------------------------------
class TestGetServerSideExclude():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_server_side_exclude()
    #--------------------------------------------------------
    @responses.activate
    def test_get_server_side_exclude_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/server_side_exclude')
        mock_response = '{"result": {"id": "server_side_exclude", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_server_side_exclude()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_server_side_exclude_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_server_side_exclude_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/server_side_exclude')
        mock_response = '{"result": {"id": "server_side_exclude", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                service.get_server_side_exclude(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_server_side_exclude
#-----------------------------------------------------------------------------
class TestUpdateServerSideExclude():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_server_side_exclude()
    #--------------------------------------------------------
    @responses.activate
    def test_update_server_side_exclude_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/server_side_exclude')
        mock_response = '{"result": {"id": "server_side_exclude", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        value = 'true'

        # Invoke method
        response = service.update_server_side_exclude(
            value=value,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'true'


    #--------------------------------------------------------
    # test_update_server_side_exclude_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_server_side_exclude_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/server_side_exclude')
        mock_response = '{"result": {"id": "server_side_exclude", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.update_server_side_exclude()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_server_side_exclude_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_server_side_exclude_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/server_side_exclude')
        mock_response = '{"result": {"id": "server_side_exclude", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
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
                service.update_server_side_exclude(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_security_header
#-----------------------------------------------------------------------------
class TestGetSecurityHeader():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_security_header()
    #--------------------------------------------------------
    @responses.activate
    def test_get_security_header_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/security_header')
        mock_response = '{"result": {"id": "security_header", "value": {"strict_transport_security": {"enabled": true, "max_age": 86400, "include_subdomains": true, "nosniff": true}}, "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_security_header()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_security_header_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_security_header_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/security_header')
        mock_response = '{"result": {"id": "security_header", "value": {"strict_transport_security": {"enabled": true, "max_age": 86400, "include_subdomains": true, "nosniff": true}}, "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                service.get_security_header(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_security_header
#-----------------------------------------------------------------------------
class TestUpdateSecurityHeader():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_security_header()
    #--------------------------------------------------------
    @responses.activate
    def test_update_security_header_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/security_header')
        mock_response = '{"result": {"id": "security_header", "value": {"strict_transport_security": {"enabled": true, "max_age": 86400, "include_subdomains": true, "nosniff": true}}, "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a SecurityHeaderSettingValueStrictTransportSecurity model
        security_header_setting_value_strict_transport_security_model = {}
        security_header_setting_value_strict_transport_security_model['enabled'] = True
        security_header_setting_value_strict_transport_security_model['max_age'] = 86400
        security_header_setting_value_strict_transport_security_model['include_subdomains'] = True
        security_header_setting_value_strict_transport_security_model['nosniff'] = True

        # Construct a dict representation of a SecurityHeaderSettingValue model
        security_header_setting_value_model = {}
        security_header_setting_value_model['strict_transport_security'] = security_header_setting_value_strict_transport_security_model

        # Set up parameter values
        value = security_header_setting_value_model

        # Invoke method
        response = service.update_security_header(
            value=value,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == security_header_setting_value_model


    #--------------------------------------------------------
    # test_update_security_header_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_security_header_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/security_header')
        mock_response = '{"result": {"id": "security_header", "value": {"strict_transport_security": {"enabled": true, "max_age": 86400, "include_subdomains": true, "nosniff": true}}, "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.update_security_header()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_security_header_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_security_header_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/security_header')
        mock_response = '{"result": {"id": "security_header", "value": {"strict_transport_security": {"enabled": true, "max_age": 86400, "include_subdomains": true, "nosniff": true}}, "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
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
                service.update_security_header(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_mobile_redirect
#-----------------------------------------------------------------------------
class TestGetMobileRedirect():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_mobile_redirect()
    #--------------------------------------------------------
    @responses.activate
    def test_get_mobile_redirect_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/mobile_redirect')
        mock_response = '{"result": {"id": "mobile_redirect", "value": {"status": "true", "mobile_subdomain": "m", "strip_uri": false}, "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_mobile_redirect()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_mobile_redirect_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_mobile_redirect_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/mobile_redirect')
        mock_response = '{"result": {"id": "mobile_redirect", "value": {"status": "true", "mobile_subdomain": "m", "strip_uri": false}, "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                service.get_mobile_redirect(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_mobile_redirect
#-----------------------------------------------------------------------------
class TestUpdateMobileRedirect():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_mobile_redirect()
    #--------------------------------------------------------
    @responses.activate
    def test_update_mobile_redirect_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/mobile_redirect')
        mock_response = '{"result": {"id": "mobile_redirect", "value": {"status": "true", "mobile_subdomain": "m", "strip_uri": false}, "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a MobileRedirecSettingValue model
        mobile_redirec_setting_value_model = {}
        mobile_redirec_setting_value_model['status'] = 'true'
        mobile_redirec_setting_value_model['mobile_subdomain'] = 'm'
        mobile_redirec_setting_value_model['strip_uri'] = False

        # Set up parameter values
        value = mobile_redirec_setting_value_model

        # Invoke method
        response = service.update_mobile_redirect(
            value=value,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == mobile_redirec_setting_value_model


    #--------------------------------------------------------
    # test_update_mobile_redirect_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_mobile_redirect_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/mobile_redirect')
        mock_response = '{"result": {"id": "mobile_redirect", "value": {"status": "true", "mobile_subdomain": "m", "strip_uri": false}, "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.update_mobile_redirect()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_mobile_redirect_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_mobile_redirect_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/mobile_redirect')
        mock_response = '{"result": {"id": "mobile_redirect", "value": {"status": "true", "mobile_subdomain": "m", "strip_uri": false}, "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
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
                service.update_mobile_redirect(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_prefetch_preload
#-----------------------------------------------------------------------------
class TestGetPrefetchPreload():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_prefetch_preload()
    #--------------------------------------------------------
    @responses.activate
    def test_get_prefetch_preload_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/prefetch_preload')
        mock_response = '{"result": {"id": "prefetch_preload", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_prefetch_preload()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_prefetch_preload_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_prefetch_preload_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/prefetch_preload')
        mock_response = '{"result": {"id": "prefetch_preload", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                service.get_prefetch_preload(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_prefetch_preload
#-----------------------------------------------------------------------------
class TestUpdatePrefetchPreload():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_prefetch_preload()
    #--------------------------------------------------------
    @responses.activate
    def test_update_prefetch_preload_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/prefetch_preload')
        mock_response = '{"result": {"id": "prefetch_preload", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        value = 'true'

        # Invoke method
        response = service.update_prefetch_preload(
            value=value,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'true'


    #--------------------------------------------------------
    # test_update_prefetch_preload_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_prefetch_preload_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/prefetch_preload')
        mock_response = '{"result": {"id": "prefetch_preload", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.update_prefetch_preload()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_prefetch_preload_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_prefetch_preload_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/prefetch_preload')
        mock_response = '{"result": {"id": "prefetch_preload", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
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
                service.update_prefetch_preload(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_http2
#-----------------------------------------------------------------------------
class TestGetHttp2():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_http2()
    #--------------------------------------------------------
    @responses.activate
    def test_get_http2_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/http2')
        mock_response = '{"result": {"id": "http2", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_http2()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_http2_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_http2_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/http2')
        mock_response = '{"result": {"id": "http2", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                service.get_http2(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_http2
#-----------------------------------------------------------------------------
class TestUpdateHttp2():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_http2()
    #--------------------------------------------------------
    @responses.activate
    def test_update_http2_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/http2')
        mock_response = '{"result": {"id": "http2", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        value = 'true'

        # Invoke method
        response = service.update_http2(
            value=value,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'true'


    #--------------------------------------------------------
    # test_update_http2_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_http2_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/http2')
        mock_response = '{"result": {"id": "http2", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.update_http2()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_http2_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_http2_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/http2')
        mock_response = '{"result": {"id": "http2", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
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
                service.update_http2(**req_copy)


#-----------------------------------------------------------------------------
# Test Class for get_http3
#-----------------------------------------------------------------------------
class TestGetHttp3():
    """
    Test Class for get_http3
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_http3_all_params(self):
        """
        get_http3()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/http3')
        mock_response = '{"result": {"id": "http3", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_http3()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_http3_value_error(self):
        """
        test_get_http3_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/http3')
        mock_response = '{"result": {"id": "http3", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                service.get_http3(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_http3
#-----------------------------------------------------------------------------
class TestUpdateHttp3():
    """
    Test Class for update_http3
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_update_http3_all_params(self):
        """
        update_http3()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/http3')
        mock_response = '{"result": {"id": "http3", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        value = 'on'

        # Invoke method
        response = service.update_http3(
            value=value,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'on'


    @responses.activate
    def test_update_http3_required_params(self):
        """
        test_update_http3_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/http3')
        mock_response = '{"result": {"id": "http3", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.update_http3()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_update_http3_value_error(self):
        """
        test_update_http3_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/http3')
        mock_response = '{"result": {"id": "http3", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
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
                service.update_http3(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_ipv6
#-----------------------------------------------------------------------------
class TestGetIpv6():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_ipv6()
    #--------------------------------------------------------
    @responses.activate
    def test_get_ipv6_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/ipv6')
        mock_response = '{"result": {"id": "ipv6", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_ipv6()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_ipv6_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_ipv6_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/ipv6')
        mock_response = '{"result": {"id": "ipv6", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                service.get_ipv6(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_ipv6
#-----------------------------------------------------------------------------
class TestUpdateIpv6():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_ipv6()
    #--------------------------------------------------------
    @responses.activate
    def test_update_ipv6_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/ipv6')
        mock_response = '{"result": {"id": "ipv6", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        value = 'true'

        # Invoke method
        response = service.update_ipv6(
            value=value,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'true'


    #--------------------------------------------------------
    # test_update_ipv6_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_ipv6_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/ipv6')
        mock_response = '{"result": {"id": "ipv6", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.update_ipv6()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_ipv6_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_ipv6_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/ipv6')
        mock_response = '{"result": {"id": "ipv6", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
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
                service.update_ipv6(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_web_sockets
#-----------------------------------------------------------------------------
class TestGetWebSockets():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_web_sockets()
    #--------------------------------------------------------
    @responses.activate
    def test_get_web_sockets_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/websockets')
        mock_response = '{"result": {"id": "websockets", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_web_sockets()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_web_sockets_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_web_sockets_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/websockets')
        mock_response = '{"result": {"id": "websockets", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                service.get_web_sockets(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_web_sockets
#-----------------------------------------------------------------------------
class TestUpdateWebSockets():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_web_sockets()
    #--------------------------------------------------------
    @responses.activate
    def test_update_web_sockets_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/websockets')
        mock_response = '{"result": {"id": "websockets", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        value = 'true'

        # Invoke method
        response = service.update_web_sockets(
            value=value,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'true'


    #--------------------------------------------------------
    # test_update_web_sockets_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_web_sockets_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/websockets')
        mock_response = '{"result": {"id": "websockets", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.update_web_sockets()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_web_sockets_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_web_sockets_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/websockets')
        mock_response = '{"result": {"id": "websockets", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
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
                service.update_web_sockets(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_pseudo_ipv4
#-----------------------------------------------------------------------------
class TestGetPseudoIpv4():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_pseudo_ipv4()
    #--------------------------------------------------------
    @responses.activate
    def test_get_pseudo_ipv4_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/pseudo_ipv4')
        mock_response = '{"result": {"id": "pseudo_ipv4", "value": "add_header", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_pseudo_ipv4()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_pseudo_ipv4_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_pseudo_ipv4_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/pseudo_ipv4')
        mock_response = '{"result": {"id": "pseudo_ipv4", "value": "add_header", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                service.get_pseudo_ipv4(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_pseudo_ipv4
#-----------------------------------------------------------------------------
class TestUpdatePseudoIpv4():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_pseudo_ipv4()
    #--------------------------------------------------------
    @responses.activate
    def test_update_pseudo_ipv4_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/pseudo_ipv4')
        mock_response = '{"result": {"id": "pseudo_ipv4", "value": "add_header", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        value = 'add_header'

        # Invoke method
        response = service.update_pseudo_ipv4(
            value=value,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'add_header'


    #--------------------------------------------------------
    # test_update_pseudo_ipv4_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_pseudo_ipv4_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/pseudo_ipv4')
        mock_response = '{"result": {"id": "pseudo_ipv4", "value": "add_header", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.update_pseudo_ipv4()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_pseudo_ipv4_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_pseudo_ipv4_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/pseudo_ipv4')
        mock_response = '{"result": {"id": "pseudo_ipv4", "value": "add_header", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
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
                service.update_pseudo_ipv4(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_response_buffering
#-----------------------------------------------------------------------------
class TestGetResponseBuffering():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_response_buffering()
    #--------------------------------------------------------
    @responses.activate
    def test_get_response_buffering_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/response_buffering')
        mock_response = '{"result": {"id": "response_buffering", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_response_buffering()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_response_buffering_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_response_buffering_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/response_buffering')
        mock_response = '{"result": {"id": "response_buffering", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                service.get_response_buffering(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_response_buffering
#-----------------------------------------------------------------------------
class TestUpdateResponseBuffering():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_response_buffering()
    #--------------------------------------------------------
    @responses.activate
    def test_update_response_buffering_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/response_buffering')
        mock_response = '{"result": {"id": "response_buffering", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        value = 'true'

        # Invoke method
        response = service.update_response_buffering(
            value=value,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'true'


    #--------------------------------------------------------
    # test_update_response_buffering_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_response_buffering_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/response_buffering')
        mock_response = '{"result": {"id": "response_buffering", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.update_response_buffering()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_response_buffering_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_response_buffering_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/response_buffering')
        mock_response = '{"result": {"id": "response_buffering", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
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
                service.update_response_buffering(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_hotlink_protection
#-----------------------------------------------------------------------------
class TestGetHotlinkProtection():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_hotlink_protection()
    #--------------------------------------------------------
    @responses.activate
    def test_get_hotlink_protection_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/hotlink_protection')
        mock_response = '{"result": {"id": "hotlink_protection", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_hotlink_protection()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_hotlink_protection_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_hotlink_protection_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/hotlink_protection')
        mock_response = '{"result": {"id": "hotlink_protection", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                service.get_hotlink_protection(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_hotlink_protection
#-----------------------------------------------------------------------------
class TestUpdateHotlinkProtection():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_hotlink_protection()
    #--------------------------------------------------------
    @responses.activate
    def test_update_hotlink_protection_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/hotlink_protection')
        mock_response = '{"result": {"id": "hotlink_protection", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        value = 'true'

        # Invoke method
        response = service.update_hotlink_protection(
            value=value,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'true'


    #--------------------------------------------------------
    # test_update_hotlink_protection_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_hotlink_protection_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/hotlink_protection')
        mock_response = '{"result": {"id": "hotlink_protection", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.update_hotlink_protection()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_hotlink_protection_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_hotlink_protection_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/hotlink_protection')
        mock_response = '{"result": {"id": "hotlink_protection", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
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
                service.update_hotlink_protection(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_max_upload
#-----------------------------------------------------------------------------
class TestGetMaxUpload():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_max_upload()
    #--------------------------------------------------------
    @responses.activate
    def test_get_max_upload_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/max_upload')
        mock_response = '{"result": {"id": "max_upload", "value": 300, "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_max_upload()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_max_upload_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_max_upload_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/max_upload')
        mock_response = '{"result": {"id": "max_upload", "value": 300, "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                service.get_max_upload(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_max_upload
#-----------------------------------------------------------------------------
class TestUpdateMaxUpload():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_max_upload()
    #--------------------------------------------------------
    @responses.activate
    def test_update_max_upload_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/max_upload')
        mock_response = '{"result": {"id": "max_upload", "value": 300, "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        value = 300

        # Invoke method
        response = service.update_max_upload(
            value=value,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 300


    #--------------------------------------------------------
    # test_update_max_upload_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_max_upload_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/max_upload')
        mock_response = '{"result": {"id": "max_upload", "value": 300, "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.update_max_upload()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_max_upload_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_max_upload_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/max_upload')
        mock_response = '{"result": {"id": "max_upload", "value": 300, "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
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
                service.update_max_upload(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_tls_client_auth
#-----------------------------------------------------------------------------
class TestGetTlsClientAuth():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_tls_client_auth()
    #--------------------------------------------------------
    @responses.activate
    def test_get_tls_client_auth_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/tls_client_auth')
        mock_response = '{"result": {"id": "tls_client_auth", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_tls_client_auth()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_tls_client_auth_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_tls_client_auth_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/tls_client_auth')
        mock_response = '{"result": {"id": "tls_client_auth", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                service.get_tls_client_auth(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_tls_client_auth
#-----------------------------------------------------------------------------
class TestUpdateTlsClientAuth():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_tls_client_auth()
    #--------------------------------------------------------
    @responses.activate
    def test_update_tls_client_auth_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/tls_client_auth')
        mock_response = '{"result": {"id": "tls_client_auth", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        value = 'true'

        # Invoke method
        response = service.update_tls_client_auth(
            value=value,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'true'


    #--------------------------------------------------------
    # test_update_tls_client_auth_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_tls_client_auth_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/tls_client_auth')
        mock_response = '{"result": {"id": "tls_client_auth", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.update_tls_client_auth()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_tls_client_auth_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_tls_client_auth_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/tls_client_auth')
        mock_response = '{"result": {"id": "tls_client_auth", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
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
                service.update_tls_client_auth(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_browser_check
#-----------------------------------------------------------------------------
class TestGetBrowserCheck():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_browser_check()
    #--------------------------------------------------------
    @responses.activate
    def test_get_browser_check_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/browser_check')
        mock_response = '{"result": {"id": "browser_check", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_browser_check()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_browser_check_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_browser_check_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/browser_check')
        mock_response = '{"result": {"id": "browser_check", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                service.get_browser_check(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_browser_check
#-----------------------------------------------------------------------------
class TestUpdateBrowserCheck():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_browser_check()
    #--------------------------------------------------------
    @responses.activate
    def test_update_browser_check_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/browser_check')
        mock_response = '{"result": {"id": "browser_check", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        value = 'true'

        # Invoke method
        response = service.update_browser_check(
            value=value,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'true'


    #--------------------------------------------------------
    # test_update_browser_check_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_browser_check_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/browser_check')
        mock_response = '{"result": {"id": "browser_check", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.update_browser_check()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_browser_check_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_browser_check_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/browser_check')
        mock_response = '{"result": {"id": "browser_check", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
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
                service.update_browser_check(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_enable_error_pages_on
#-----------------------------------------------------------------------------
class TestGetEnableErrorPagesOn():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_enable_error_pages_on()
    #--------------------------------------------------------
    @responses.activate
    def test_get_enable_error_pages_on_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/origin_error_page_pass_thru')
        mock_response = '{"result": {"id": "origin_error_page_pass_thru", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_enable_error_pages_on()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_enable_error_pages_on_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_enable_error_pages_on_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/origin_error_page_pass_thru')
        mock_response = '{"result": {"id": "origin_error_page_pass_thru", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                service.get_enable_error_pages_on(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_enable_error_pages_on
#-----------------------------------------------------------------------------
class TestUpdateEnableErrorPagesOn():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_enable_error_pages_on()
    #--------------------------------------------------------
    @responses.activate
    def test_update_enable_error_pages_on_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/origin_error_page_pass_thru')
        mock_response = '{"result": {"id": "origin_error_page_pass_thru", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        value = 'true'

        # Invoke method
        response = service.update_enable_error_pages_on(
            value=value,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'true'


    #--------------------------------------------------------
    # test_update_enable_error_pages_on_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_enable_error_pages_on_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/origin_error_page_pass_thru')
        mock_response = '{"result": {"id": "origin_error_page_pass_thru", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.update_enable_error_pages_on()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_enable_error_pages_on_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_enable_error_pages_on_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/origin_error_page_pass_thru')
        mock_response = '{"result": {"id": "origin_error_page_pass_thru", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
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
                service.update_enable_error_pages_on(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_web_application_firewall
#-----------------------------------------------------------------------------
class TestGetWebApplicationFirewall():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_web_application_firewall()
    #--------------------------------------------------------
    @responses.activate
    def test_get_web_application_firewall_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/waf')
        mock_response = '{"result": {"id": "waf", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_web_application_firewall()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_web_application_firewall_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_web_application_firewall_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/waf')
        mock_response = '{"result": {"id": "waf", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                service.get_web_application_firewall(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_web_application_firewall
#-----------------------------------------------------------------------------
class TestUpdateWebApplicationFirewall():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_web_application_firewall()
    #--------------------------------------------------------
    @responses.activate
    def test_update_web_application_firewall_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/waf')
        mock_response = '{"result": {"id": "waf", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        value = 'true'

        # Invoke method
        response = service.update_web_application_firewall(
            value=value,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'true'


    #--------------------------------------------------------
    # test_update_web_application_firewall_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_web_application_firewall_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/waf')
        mock_response = '{"result": {"id": "waf", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.update_web_application_firewall()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_web_application_firewall_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_web_application_firewall_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/waf')
        mock_response = '{"result": {"id": "waf", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
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
                service.update_web_application_firewall(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_ciphers
#-----------------------------------------------------------------------------
class TestGetCiphers():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_ciphers()
    #--------------------------------------------------------
    @responses.activate
    def test_get_ciphers_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/ciphers')
        mock_response = '{"result": {"id": "ciphers", "value": ["value"], "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_ciphers()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_ciphers_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_ciphers_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/ciphers')
        mock_response = '{"result": {"id": "ciphers", "value": ["value"], "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                service.get_ciphers(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_ciphers
#-----------------------------------------------------------------------------
class TestUpdateCiphers():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_ciphers()
    #--------------------------------------------------------
    @responses.activate
    def test_update_ciphers_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/ciphers')
        mock_response = '{"result": {"id": "ciphers", "value": ["value"], "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        value = ['ECDHE-ECDSA-AES128-GCM-SHA256']

        # Invoke method
        response = service.update_ciphers(
            value=value,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == ['ECDHE-ECDSA-AES128-GCM-SHA256']


    #--------------------------------------------------------
    # test_update_ciphers_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_ciphers_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/ciphers')
        mock_response = '{"result": {"id": "ciphers", "value": ["value"], "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.update_ciphers()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_ciphers_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_ciphers_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/ciphers')
        mock_response = '{"result": {"id": "ciphers", "value": ["value"], "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
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
                service.update_ciphers(**req_copy)



# endregion
##############################################################################
# End of Service: ZonesSettings
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
#-----------------------------------------------------------------------------
# Test Class for AlwaysUseHttpsRespResult
#-----------------------------------------------------------------------------
class TestAlwaysUseHttpsRespResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for AlwaysUseHttpsRespResult
    #--------------------------------------------------------
    def test_always_use_https_resp_result_serialization(self):

        # Construct a json representation of a AlwaysUseHttpsRespResult model
        always_use_https_resp_result_model_json = {}
        always_use_https_resp_result_model_json['id'] = 'always_use_https'
        always_use_https_resp_result_model_json['value'] = 'false'
        always_use_https_resp_result_model_json['editable'] = True
        always_use_https_resp_result_model_json['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of AlwaysUseHttpsRespResult by calling from_dict on the json representation
        always_use_https_resp_result_model = AlwaysUseHttpsRespResult.from_dict(always_use_https_resp_result_model_json)
        assert always_use_https_resp_result_model != False

        # Construct a model instance of AlwaysUseHttpsRespResult by calling from_dict on the json representation
        always_use_https_resp_result_model_dict = AlwaysUseHttpsRespResult.from_dict(always_use_https_resp_result_model_json).__dict__
        always_use_https_resp_result_model2 = AlwaysUseHttpsRespResult(**always_use_https_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert always_use_https_resp_result_model == always_use_https_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        always_use_https_resp_result_model_json2 = always_use_https_resp_result_model.to_dict()
        assert always_use_https_resp_result_model_json2 == always_use_https_resp_result_model_json

#-----------------------------------------------------------------------------
# Test Class for AutomaticHttpsRewritesRespResult
#-----------------------------------------------------------------------------
class TestAutomaticHttpsRewritesRespResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for AutomaticHttpsRewritesRespResult
    #--------------------------------------------------------
    def test_automatic_https_rewrites_resp_result_serialization(self):

        # Construct a json representation of a AutomaticHttpsRewritesRespResult model
        automatic_https_rewrites_resp_result_model_json = {}
        automatic_https_rewrites_resp_result_model_json['id'] = 'automatic_https_rewrites'
        automatic_https_rewrites_resp_result_model_json['value'] = 'false'
        automatic_https_rewrites_resp_result_model_json['editable'] = True
        automatic_https_rewrites_resp_result_model_json['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of AutomaticHttpsRewritesRespResult by calling from_dict on the json representation
        automatic_https_rewrites_resp_result_model = AutomaticHttpsRewritesRespResult.from_dict(automatic_https_rewrites_resp_result_model_json)
        assert automatic_https_rewrites_resp_result_model != False

        # Construct a model instance of AutomaticHttpsRewritesRespResult by calling from_dict on the json representation
        automatic_https_rewrites_resp_result_model_dict = AutomaticHttpsRewritesRespResult.from_dict(automatic_https_rewrites_resp_result_model_json).__dict__
        automatic_https_rewrites_resp_result_model2 = AutomaticHttpsRewritesRespResult(**automatic_https_rewrites_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert automatic_https_rewrites_resp_result_model == automatic_https_rewrites_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        automatic_https_rewrites_resp_result_model_json2 = automatic_https_rewrites_resp_result_model.to_dict()
        assert automatic_https_rewrites_resp_result_model_json2 == automatic_https_rewrites_resp_result_model_json

#-----------------------------------------------------------------------------
# Test Class for BrowserCheckRespResult
#-----------------------------------------------------------------------------
class TestBrowserCheckRespResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for BrowserCheckRespResult
    #--------------------------------------------------------
    def test_browser_check_resp_result_serialization(self):

        # Construct a json representation of a BrowserCheckRespResult model
        browser_check_resp_result_model_json = {}
        browser_check_resp_result_model_json['id'] = 'browser_check'
        browser_check_resp_result_model_json['value'] = 'false'
        browser_check_resp_result_model_json['editable'] = True
        browser_check_resp_result_model_json['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of BrowserCheckRespResult by calling from_dict on the json representation
        browser_check_resp_result_model = BrowserCheckRespResult.from_dict(browser_check_resp_result_model_json)
        assert browser_check_resp_result_model != False

        # Construct a model instance of BrowserCheckRespResult by calling from_dict on the json representation
        browser_check_resp_result_model_dict = BrowserCheckRespResult.from_dict(browser_check_resp_result_model_json).__dict__
        browser_check_resp_result_model2 = BrowserCheckRespResult(**browser_check_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert browser_check_resp_result_model == browser_check_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        browser_check_resp_result_model_json2 = browser_check_resp_result_model.to_dict()
        assert browser_check_resp_result_model_json2 == browser_check_resp_result_model_json

#-----------------------------------------------------------------------------
# Test Class for ChallengeTtlRespResult
#-----------------------------------------------------------------------------
class TestChallengeTtlRespResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for ChallengeTtlRespResult
    #--------------------------------------------------------
    def test_challenge_ttl_resp_result_serialization(self):

        # Construct a json representation of a ChallengeTtlRespResult model
        challenge_ttl_resp_result_model_json = {}
        challenge_ttl_resp_result_model_json['id'] = 'challenge_ttl'
        challenge_ttl_resp_result_model_json['value'] = 1800
        challenge_ttl_resp_result_model_json['editable'] = True
        challenge_ttl_resp_result_model_json['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of ChallengeTtlRespResult by calling from_dict on the json representation
        challenge_ttl_resp_result_model = ChallengeTtlRespResult.from_dict(challenge_ttl_resp_result_model_json)
        assert challenge_ttl_resp_result_model != False

        # Construct a model instance of ChallengeTtlRespResult by calling from_dict on the json representation
        challenge_ttl_resp_result_model_dict = ChallengeTtlRespResult.from_dict(challenge_ttl_resp_result_model_json).__dict__
        challenge_ttl_resp_result_model2 = ChallengeTtlRespResult(**challenge_ttl_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert challenge_ttl_resp_result_model == challenge_ttl_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        challenge_ttl_resp_result_model_json2 = challenge_ttl_resp_result_model.to_dict()
        assert challenge_ttl_resp_result_model_json2 == challenge_ttl_resp_result_model_json

#-----------------------------------------------------------------------------
# Test Class for CiphersRespResult
#-----------------------------------------------------------------------------
class TestCiphersRespResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for CiphersRespResult
    #--------------------------------------------------------
    def test_ciphers_resp_result_serialization(self):

        # Construct a json representation of a CiphersRespResult model
        ciphers_resp_result_model_json = {}
        ciphers_resp_result_model_json['id'] = 'ciphers'
        ciphers_resp_result_model_json['value'] = ['testString']
        ciphers_resp_result_model_json['editable'] = True
        ciphers_resp_result_model_json['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of CiphersRespResult by calling from_dict on the json representation
        ciphers_resp_result_model = CiphersRespResult.from_dict(ciphers_resp_result_model_json)
        assert ciphers_resp_result_model != False

        # Construct a model instance of CiphersRespResult by calling from_dict on the json representation
        ciphers_resp_result_model_dict = CiphersRespResult.from_dict(ciphers_resp_result_model_json).__dict__
        ciphers_resp_result_model2 = CiphersRespResult(**ciphers_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert ciphers_resp_result_model == ciphers_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        ciphers_resp_result_model_json2 = ciphers_resp_result_model.to_dict()
        assert ciphers_resp_result_model_json2 == ciphers_resp_result_model_json

#-----------------------------------------------------------------------------
# Test Class for HotlinkProtectionRespResult
#-----------------------------------------------------------------------------
class TestHotlinkProtectionRespResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for HotlinkProtectionRespResult
    #--------------------------------------------------------
    def test_hotlink_protection_resp_result_serialization(self):

        # Construct a json representation of a HotlinkProtectionRespResult model
        hotlink_protection_resp_result_model_json = {}
        hotlink_protection_resp_result_model_json['id'] = 'hotlink_protection'
        hotlink_protection_resp_result_model_json['value'] = 'false'
        hotlink_protection_resp_result_model_json['editable'] = True
        hotlink_protection_resp_result_model_json['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of HotlinkProtectionRespResult by calling from_dict on the json representation
        hotlink_protection_resp_result_model = HotlinkProtectionRespResult.from_dict(hotlink_protection_resp_result_model_json)
        assert hotlink_protection_resp_result_model != False

        # Construct a model instance of HotlinkProtectionRespResult by calling from_dict on the json representation
        hotlink_protection_resp_result_model_dict = HotlinkProtectionRespResult.from_dict(hotlink_protection_resp_result_model_json).__dict__
        hotlink_protection_resp_result_model2 = HotlinkProtectionRespResult(**hotlink_protection_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert hotlink_protection_resp_result_model == hotlink_protection_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        hotlink_protection_resp_result_model_json2 = hotlink_protection_resp_result_model.to_dict()
        assert hotlink_protection_resp_result_model_json2 == hotlink_protection_resp_result_model_json

#-----------------------------------------------------------------------------
# Test Class for Http2RespResult
#-----------------------------------------------------------------------------
class TestHttp2RespResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for Http2RespResult
    #--------------------------------------------------------
    def test_http2_resp_result_serialization(self):

        # Construct a json representation of a Http2RespResult model
        http2_resp_result_model_json = {}
        http2_resp_result_model_json['id'] = 'http2'
        http2_resp_result_model_json['value'] = 'false'
        http2_resp_result_model_json['editable'] = True
        http2_resp_result_model_json['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of Http2RespResult by calling from_dict on the json representation
        http2_resp_result_model = Http2RespResult.from_dict(http2_resp_result_model_json)
        assert http2_resp_result_model != False

        # Construct a model instance of Http2RespResult by calling from_dict on the json representation
        http2_resp_result_model_dict = Http2RespResult.from_dict(http2_resp_result_model_json).__dict__
        http2_resp_result_model2 = Http2RespResult(**http2_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert http2_resp_result_model == http2_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        http2_resp_result_model_json2 = http2_resp_result_model.to_dict()
        assert http2_resp_result_model_json2 == http2_resp_result_model_json


#-----------------------------------------------------------------------------
# Test Class for Http3RespResult
#-----------------------------------------------------------------------------
class TestHttp3RespResult():
    """
    Test Class for Http3RespResult
    """

    def test_http3_resp_result_serialization(self):
        """
        Test serialization/deserialization for Http3RespResult
        """

        # Construct a json representation of a Http3RespResult model
        http3_resp_result_model_json = {}
        http3_resp_result_model_json['id'] = 'http3'
        http3_resp_result_model_json['value'] = 'off'
        http3_resp_result_model_json['editable'] = True
        http3_resp_result_model_json['modified_on'] = '2015-03-14T09:26:53.123456Z'

        # Construct a model instance of Http3RespResult by calling from_dict on the json representation
        http3_resp_result_model = Http3RespResult.from_dict(http3_resp_result_model_json)
        assert http3_resp_result_model != False

        # Construct a model instance of Http3RespResult by calling from_dict on the json representation
        http3_resp_result_model_dict = Http3RespResult.from_dict(http3_resp_result_model_json).__dict__
        http3_resp_result_model2 = Http3RespResult(**http3_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert http3_resp_result_model == http3_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        http3_resp_result_model_json2 = http3_resp_result_model.to_dict()
        assert http3_resp_result_model_json2 == http3_resp_result_model_json


#-----------------------------------------------------------------------------
# Test Class for ImageLoadOptimizationRespResult
#-----------------------------------------------------------------------------
class TestImageLoadOptimizationRespResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for ImageLoadOptimizationRespResult
    #--------------------------------------------------------
    def test_image_load_optimization_resp_result_serialization(self):

        # Construct a json representation of a ImageLoadOptimizationRespResult model
        image_load_optimization_resp_result_model_json = {}
        image_load_optimization_resp_result_model_json['id'] = 'image_load_optimization'
        image_load_optimization_resp_result_model_json['value'] = 'false'
        image_load_optimization_resp_result_model_json['editable'] = True
        image_load_optimization_resp_result_model_json['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of ImageLoadOptimizationRespResult by calling from_dict on the json representation
        image_load_optimization_resp_result_model = ImageLoadOptimizationRespResult.from_dict(image_load_optimization_resp_result_model_json)
        assert image_load_optimization_resp_result_model != False

        # Construct a model instance of ImageLoadOptimizationRespResult by calling from_dict on the json representation
        image_load_optimization_resp_result_model_dict = ImageLoadOptimizationRespResult.from_dict(image_load_optimization_resp_result_model_json).__dict__
        image_load_optimization_resp_result_model2 = ImageLoadOptimizationRespResult(**image_load_optimization_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert image_load_optimization_resp_result_model == image_load_optimization_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        image_load_optimization_resp_result_model_json2 = image_load_optimization_resp_result_model.to_dict()
        assert image_load_optimization_resp_result_model_json2 == image_load_optimization_resp_result_model_json

#-----------------------------------------------------------------------------
# Test Class for ImageSizeOptimizationRespResult
#-----------------------------------------------------------------------------
class TestImageSizeOptimizationRespResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for ImageSizeOptimizationRespResult
    #--------------------------------------------------------
    def test_image_size_optimization_resp_result_serialization(self):

        # Construct a json representation of a ImageSizeOptimizationRespResult model
        image_size_optimization_resp_result_model_json = {}
        image_size_optimization_resp_result_model_json['id'] = 'image_size_optimization'
        image_size_optimization_resp_result_model_json['value'] = 'lossless'
        image_size_optimization_resp_result_model_json['editable'] = True
        image_size_optimization_resp_result_model_json['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of ImageSizeOptimizationRespResult by calling from_dict on the json representation
        image_size_optimization_resp_result_model = ImageSizeOptimizationRespResult.from_dict(image_size_optimization_resp_result_model_json)
        assert image_size_optimization_resp_result_model != False

        # Construct a model instance of ImageSizeOptimizationRespResult by calling from_dict on the json representation
        image_size_optimization_resp_result_model_dict = ImageSizeOptimizationRespResult.from_dict(image_size_optimization_resp_result_model_json).__dict__
        image_size_optimization_resp_result_model2 = ImageSizeOptimizationRespResult(**image_size_optimization_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert image_size_optimization_resp_result_model == image_size_optimization_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        image_size_optimization_resp_result_model_json2 = image_size_optimization_resp_result_model.to_dict()
        assert image_size_optimization_resp_result_model_json2 == image_size_optimization_resp_result_model_json

#-----------------------------------------------------------------------------
# Test Class for IpGeolocationRespResult
#-----------------------------------------------------------------------------
class TestIpGeolocationRespResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for IpGeolocationRespResult
    #--------------------------------------------------------
    def test_ip_geolocation_resp_result_serialization(self):

        # Construct a json representation of a IpGeolocationRespResult model
        ip_geolocation_resp_result_model_json = {}
        ip_geolocation_resp_result_model_json['id'] = 'ip_geolocation'
        ip_geolocation_resp_result_model_json['value'] = 'false'
        ip_geolocation_resp_result_model_json['editable'] = True
        ip_geolocation_resp_result_model_json['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of IpGeolocationRespResult by calling from_dict on the json representation
        ip_geolocation_resp_result_model = IpGeolocationRespResult.from_dict(ip_geolocation_resp_result_model_json)
        assert ip_geolocation_resp_result_model != False

        # Construct a model instance of IpGeolocationRespResult by calling from_dict on the json representation
        ip_geolocation_resp_result_model_dict = IpGeolocationRespResult.from_dict(ip_geolocation_resp_result_model_json).__dict__
        ip_geolocation_resp_result_model2 = IpGeolocationRespResult(**ip_geolocation_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert ip_geolocation_resp_result_model == ip_geolocation_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        ip_geolocation_resp_result_model_json2 = ip_geolocation_resp_result_model.to_dict()
        assert ip_geolocation_resp_result_model_json2 == ip_geolocation_resp_result_model_json

#-----------------------------------------------------------------------------
# Test Class for Ipv6RespResult
#-----------------------------------------------------------------------------
class TestIpv6RespResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for Ipv6RespResult
    #--------------------------------------------------------
    def test_ipv6_resp_result_serialization(self):

        # Construct a json representation of a Ipv6RespResult model
        ipv6_resp_result_model_json = {}
        ipv6_resp_result_model_json['id'] = 'ipv6'
        ipv6_resp_result_model_json['value'] = 'false'
        ipv6_resp_result_model_json['editable'] = True
        ipv6_resp_result_model_json['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of Ipv6RespResult by calling from_dict on the json representation
        ipv6_resp_result_model = Ipv6RespResult.from_dict(ipv6_resp_result_model_json)
        assert ipv6_resp_result_model != False

        # Construct a model instance of Ipv6RespResult by calling from_dict on the json representation
        ipv6_resp_result_model_dict = Ipv6RespResult.from_dict(ipv6_resp_result_model_json).__dict__
        ipv6_resp_result_model2 = Ipv6RespResult(**ipv6_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert ipv6_resp_result_model == ipv6_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        ipv6_resp_result_model_json2 = ipv6_resp_result_model.to_dict()
        assert ipv6_resp_result_model_json2 == ipv6_resp_result_model_json

#-----------------------------------------------------------------------------
# Test Class for MaxUploadRespResult
#-----------------------------------------------------------------------------
class TestMaxUploadRespResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for MaxUploadRespResult
    #--------------------------------------------------------
    def test_max_upload_resp_result_serialization(self):

        # Construct a json representation of a MaxUploadRespResult model
        max_upload_resp_result_model_json = {}
        max_upload_resp_result_model_json['id'] = 'max_upload'
        max_upload_resp_result_model_json['value'] = 300
        max_upload_resp_result_model_json['editable'] = True
        max_upload_resp_result_model_json['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of MaxUploadRespResult by calling from_dict on the json representation
        max_upload_resp_result_model = MaxUploadRespResult.from_dict(max_upload_resp_result_model_json)
        assert max_upload_resp_result_model != False

        # Construct a model instance of MaxUploadRespResult by calling from_dict on the json representation
        max_upload_resp_result_model_dict = MaxUploadRespResult.from_dict(max_upload_resp_result_model_json).__dict__
        max_upload_resp_result_model2 = MaxUploadRespResult(**max_upload_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert max_upload_resp_result_model == max_upload_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        max_upload_resp_result_model_json2 = max_upload_resp_result_model.to_dict()
        assert max_upload_resp_result_model_json2 == max_upload_resp_result_model_json

#-----------------------------------------------------------------------------
# Test Class for MinTlsVersionRespResult
#-----------------------------------------------------------------------------
class TestMinTlsVersionRespResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for MinTlsVersionRespResult
    #--------------------------------------------------------
    def test_min_tls_version_resp_result_serialization(self):

        # Construct a json representation of a MinTlsVersionRespResult model
        min_tls_version_resp_result_model_json = {}
        min_tls_version_resp_result_model_json['id'] = 'min_tls_version'
        min_tls_version_resp_result_model_json['value'] = '1.2'
        min_tls_version_resp_result_model_json['editable'] = True
        min_tls_version_resp_result_model_json['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of MinTlsVersionRespResult by calling from_dict on the json representation
        min_tls_version_resp_result_model = MinTlsVersionRespResult.from_dict(min_tls_version_resp_result_model_json)
        assert min_tls_version_resp_result_model != False

        # Construct a model instance of MinTlsVersionRespResult by calling from_dict on the json representation
        min_tls_version_resp_result_model_dict = MinTlsVersionRespResult.from_dict(min_tls_version_resp_result_model_json).__dict__
        min_tls_version_resp_result_model2 = MinTlsVersionRespResult(**min_tls_version_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert min_tls_version_resp_result_model == min_tls_version_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        min_tls_version_resp_result_model_json2 = min_tls_version_resp_result_model.to_dict()
        assert min_tls_version_resp_result_model_json2 == min_tls_version_resp_result_model_json

#-----------------------------------------------------------------------------
# Test Class for MinifyRespResult
#-----------------------------------------------------------------------------
class TestMinifyRespResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for MinifyRespResult
    #--------------------------------------------------------
    def test_minify_resp_result_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        minify_resp_result_value_model = {} # MinifyRespResultValue
        minify_resp_result_value_model['css'] = 'true'
        minify_resp_result_value_model['html'] = 'true'
        minify_resp_result_value_model['js'] = 'true'

        # Construct a json representation of a MinifyRespResult model
        minify_resp_result_model_json = {}
        minify_resp_result_model_json['id'] = 'minify'
        minify_resp_result_model_json['value'] = minify_resp_result_value_model
        minify_resp_result_model_json['editable'] = True
        minify_resp_result_model_json['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of MinifyRespResult by calling from_dict on the json representation
        minify_resp_result_model = MinifyRespResult.from_dict(minify_resp_result_model_json)
        assert minify_resp_result_model != False

        # Construct a model instance of MinifyRespResult by calling from_dict on the json representation
        minify_resp_result_model_dict = MinifyRespResult.from_dict(minify_resp_result_model_json).__dict__
        minify_resp_result_model2 = MinifyRespResult(**minify_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert minify_resp_result_model == minify_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        minify_resp_result_model_json2 = minify_resp_result_model.to_dict()
        assert minify_resp_result_model_json2 == minify_resp_result_model_json

#-----------------------------------------------------------------------------
# Test Class for MinifyRespResultValue
#-----------------------------------------------------------------------------
class TestMinifyRespResultValue():

    #--------------------------------------------------------
    # Test serialization/deserialization for MinifyRespResultValue
    #--------------------------------------------------------
    def test_minify_resp_result_value_serialization(self):

        # Construct a json representation of a MinifyRespResultValue model
        minify_resp_result_value_model_json = {}
        minify_resp_result_value_model_json['css'] = 'true'
        minify_resp_result_value_model_json['html'] = 'true'
        minify_resp_result_value_model_json['js'] = 'true'

        # Construct a model instance of MinifyRespResultValue by calling from_dict on the json representation
        minify_resp_result_value_model = MinifyRespResultValue.from_dict(minify_resp_result_value_model_json)
        assert minify_resp_result_value_model != False

        # Construct a model instance of MinifyRespResultValue by calling from_dict on the json representation
        minify_resp_result_value_model_dict = MinifyRespResultValue.from_dict(minify_resp_result_value_model_json).__dict__
        minify_resp_result_value_model2 = MinifyRespResultValue(**minify_resp_result_value_model_dict)

        # Verify the model instances are equivalent
        assert minify_resp_result_value_model == minify_resp_result_value_model2

        # Convert model instance back to dict and verify no loss of data
        minify_resp_result_value_model_json2 = minify_resp_result_value_model.to_dict()
        assert minify_resp_result_value_model_json2 == minify_resp_result_value_model_json

#-----------------------------------------------------------------------------
# Test Class for MinifySettingValue
#-----------------------------------------------------------------------------
class TestMinifySettingValue():

    #--------------------------------------------------------
    # Test serialization/deserialization for MinifySettingValue
    #--------------------------------------------------------
    def test_minify_setting_value_serialization(self):

        # Construct a json representation of a MinifySettingValue model
        minify_setting_value_model_json = {}
        minify_setting_value_model_json['css'] = 'false'
        minify_setting_value_model_json['html'] = 'false'
        minify_setting_value_model_json['js'] = 'false'

        # Construct a model instance of MinifySettingValue by calling from_dict on the json representation
        minify_setting_value_model = MinifySettingValue.from_dict(minify_setting_value_model_json)
        assert minify_setting_value_model != False

        # Construct a model instance of MinifySettingValue by calling from_dict on the json representation
        minify_setting_value_model_dict = MinifySettingValue.from_dict(minify_setting_value_model_json).__dict__
        minify_setting_value_model2 = MinifySettingValue(**minify_setting_value_model_dict)

        # Verify the model instances are equivalent
        assert minify_setting_value_model == minify_setting_value_model2

        # Convert model instance back to dict and verify no loss of data
        minify_setting_value_model_json2 = minify_setting_value_model.to_dict()
        assert minify_setting_value_model_json2 == minify_setting_value_model_json

#-----------------------------------------------------------------------------
# Test Class for MobileRedirecSettingValue
#-----------------------------------------------------------------------------
class TestMobileRedirecSettingValue():

    #--------------------------------------------------------
    # Test serialization/deserialization for MobileRedirecSettingValue
    #--------------------------------------------------------
    def test_mobile_redirec_setting_value_serialization(self):

        # Construct a json representation of a MobileRedirecSettingValue model
        mobile_redirec_setting_value_model_json = {}
        mobile_redirec_setting_value_model_json['status'] = 'true'
        mobile_redirec_setting_value_model_json['mobile_subdomain'] = 'm'
        mobile_redirec_setting_value_model_json['strip_uri'] = False

        # Construct a model instance of MobileRedirecSettingValue by calling from_dict on the json representation
        mobile_redirec_setting_value_model = MobileRedirecSettingValue.from_dict(mobile_redirec_setting_value_model_json)
        assert mobile_redirec_setting_value_model != False

        # Construct a model instance of MobileRedirecSettingValue by calling from_dict on the json representation
        mobile_redirec_setting_value_model_dict = MobileRedirecSettingValue.from_dict(mobile_redirec_setting_value_model_json).__dict__
        mobile_redirec_setting_value_model2 = MobileRedirecSettingValue(**mobile_redirec_setting_value_model_dict)

        # Verify the model instances are equivalent
        assert mobile_redirec_setting_value_model == mobile_redirec_setting_value_model2

        # Convert model instance back to dict and verify no loss of data
        mobile_redirec_setting_value_model_json2 = mobile_redirec_setting_value_model.to_dict()
        assert mobile_redirec_setting_value_model_json2 == mobile_redirec_setting_value_model_json

#-----------------------------------------------------------------------------
# Test Class for MobileRedirectRespResult
#-----------------------------------------------------------------------------
class TestMobileRedirectRespResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for MobileRedirectRespResult
    #--------------------------------------------------------
    def test_mobile_redirect_resp_result_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        mobile_redirect_resp_result_value_model = {} # MobileRedirectRespResultValue
        mobile_redirect_resp_result_value_model['status'] = 'true'
        mobile_redirect_resp_result_value_model['mobile_subdomain'] = 'm'
        mobile_redirect_resp_result_value_model['strip_uri'] = False

        # Construct a json representation of a MobileRedirectRespResult model
        mobile_redirect_resp_result_model_json = {}
        mobile_redirect_resp_result_model_json['id'] = 'mobile_redirect'
        mobile_redirect_resp_result_model_json['value'] = mobile_redirect_resp_result_value_model
        mobile_redirect_resp_result_model_json['editable'] = True
        mobile_redirect_resp_result_model_json['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of MobileRedirectRespResult by calling from_dict on the json representation
        mobile_redirect_resp_result_model = MobileRedirectRespResult.from_dict(mobile_redirect_resp_result_model_json)
        assert mobile_redirect_resp_result_model != False

        # Construct a model instance of MobileRedirectRespResult by calling from_dict on the json representation
        mobile_redirect_resp_result_model_dict = MobileRedirectRespResult.from_dict(mobile_redirect_resp_result_model_json).__dict__
        mobile_redirect_resp_result_model2 = MobileRedirectRespResult(**mobile_redirect_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert mobile_redirect_resp_result_model == mobile_redirect_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        mobile_redirect_resp_result_model_json2 = mobile_redirect_resp_result_model.to_dict()
        assert mobile_redirect_resp_result_model_json2 == mobile_redirect_resp_result_model_json

#-----------------------------------------------------------------------------
# Test Class for MobileRedirectRespResultValue
#-----------------------------------------------------------------------------
class TestMobileRedirectRespResultValue():

    #--------------------------------------------------------
    # Test serialization/deserialization for MobileRedirectRespResultValue
    #--------------------------------------------------------
    def test_mobile_redirect_resp_result_value_serialization(self):

        # Construct a json representation of a MobileRedirectRespResultValue model
        mobile_redirect_resp_result_value_model_json = {}
        mobile_redirect_resp_result_value_model_json['status'] = 'true'
        mobile_redirect_resp_result_value_model_json['mobile_subdomain'] = 'm'
        mobile_redirect_resp_result_value_model_json['strip_uri'] = False

        # Construct a model instance of MobileRedirectRespResultValue by calling from_dict on the json representation
        mobile_redirect_resp_result_value_model = MobileRedirectRespResultValue.from_dict(mobile_redirect_resp_result_value_model_json)
        assert mobile_redirect_resp_result_value_model != False

        # Construct a model instance of MobileRedirectRespResultValue by calling from_dict on the json representation
        mobile_redirect_resp_result_value_model_dict = MobileRedirectRespResultValue.from_dict(mobile_redirect_resp_result_value_model_json).__dict__
        mobile_redirect_resp_result_value_model2 = MobileRedirectRespResultValue(**mobile_redirect_resp_result_value_model_dict)

        # Verify the model instances are equivalent
        assert mobile_redirect_resp_result_value_model == mobile_redirect_resp_result_value_model2

        # Convert model instance back to dict and verify no loss of data
        mobile_redirect_resp_result_value_model_json2 = mobile_redirect_resp_result_value_model.to_dict()
        assert mobile_redirect_resp_result_value_model_json2 == mobile_redirect_resp_result_value_model_json

#-----------------------------------------------------------------------------
# Test Class for OpportunisticEncryptionRespResult
#-----------------------------------------------------------------------------
class TestOpportunisticEncryptionRespResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for OpportunisticEncryptionRespResult
    #--------------------------------------------------------
    def test_opportunistic_encryption_resp_result_serialization(self):

        # Construct a json representation of a OpportunisticEncryptionRespResult model
        opportunistic_encryption_resp_result_model_json = {}
        opportunistic_encryption_resp_result_model_json['id'] = 'opportunistic_encryption'
        opportunistic_encryption_resp_result_model_json['value'] = 'off'
        opportunistic_encryption_resp_result_model_json['editable'] = True
        opportunistic_encryption_resp_result_model_json['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of OpportunisticEncryptionRespResult by calling from_dict on the json representation
        opportunistic_encryption_resp_result_model = OpportunisticEncryptionRespResult.from_dict(opportunistic_encryption_resp_result_model_json)
        assert opportunistic_encryption_resp_result_model != False

        # Construct a model instance of OpportunisticEncryptionRespResult by calling from_dict on the json representation
        opportunistic_encryption_resp_result_model_dict = OpportunisticEncryptionRespResult.from_dict(opportunistic_encryption_resp_result_model_json).__dict__
        opportunistic_encryption_resp_result_model2 = OpportunisticEncryptionRespResult(**opportunistic_encryption_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert opportunistic_encryption_resp_result_model == opportunistic_encryption_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        opportunistic_encryption_resp_result_model_json2 = opportunistic_encryption_resp_result_model.to_dict()
        assert opportunistic_encryption_resp_result_model_json2 == opportunistic_encryption_resp_result_model_json

#-----------------------------------------------------------------------------
# Test Class for OriginErrorPagePassThruRespResult
#-----------------------------------------------------------------------------
class TestOriginErrorPagePassThruRespResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for OriginErrorPagePassThruRespResult
    #--------------------------------------------------------
    def test_origin_error_page_pass_thru_resp_result_serialization(self):

        # Construct a json representation of a OriginErrorPagePassThruRespResult model
        origin_error_page_pass_thru_resp_result_model_json = {}
        origin_error_page_pass_thru_resp_result_model_json['id'] = 'origin_error_page_pass_thru'
        origin_error_page_pass_thru_resp_result_model_json['value'] = 'false'
        origin_error_page_pass_thru_resp_result_model_json['editable'] = True
        origin_error_page_pass_thru_resp_result_model_json['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of OriginErrorPagePassThruRespResult by calling from_dict on the json representation
        origin_error_page_pass_thru_resp_result_model = OriginErrorPagePassThruRespResult.from_dict(origin_error_page_pass_thru_resp_result_model_json)
        assert origin_error_page_pass_thru_resp_result_model != False

        # Construct a model instance of OriginErrorPagePassThruRespResult by calling from_dict on the json representation
        origin_error_page_pass_thru_resp_result_model_dict = OriginErrorPagePassThruRespResult.from_dict(origin_error_page_pass_thru_resp_result_model_json).__dict__
        origin_error_page_pass_thru_resp_result_model2 = OriginErrorPagePassThruRespResult(**origin_error_page_pass_thru_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert origin_error_page_pass_thru_resp_result_model == origin_error_page_pass_thru_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        origin_error_page_pass_thru_resp_result_model_json2 = origin_error_page_pass_thru_resp_result_model.to_dict()
        assert origin_error_page_pass_thru_resp_result_model_json2 == origin_error_page_pass_thru_resp_result_model_json

#-----------------------------------------------------------------------------
# Test Class for PrefetchPreloadRespResult
#-----------------------------------------------------------------------------
class TestPrefetchPreloadRespResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for PrefetchPreloadRespResult
    #--------------------------------------------------------
    def test_prefetch_preload_resp_result_serialization(self):

        # Construct a json representation of a PrefetchPreloadRespResult model
        prefetch_preload_resp_result_model_json = {}
        prefetch_preload_resp_result_model_json['id'] = 'prefetch_preload'
        prefetch_preload_resp_result_model_json['value'] = 'false'
        prefetch_preload_resp_result_model_json['editable'] = True
        prefetch_preload_resp_result_model_json['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of PrefetchPreloadRespResult by calling from_dict on the json representation
        prefetch_preload_resp_result_model = PrefetchPreloadRespResult.from_dict(prefetch_preload_resp_result_model_json)
        assert prefetch_preload_resp_result_model != False

        # Construct a model instance of PrefetchPreloadRespResult by calling from_dict on the json representation
        prefetch_preload_resp_result_model_dict = PrefetchPreloadRespResult.from_dict(prefetch_preload_resp_result_model_json).__dict__
        prefetch_preload_resp_result_model2 = PrefetchPreloadRespResult(**prefetch_preload_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert prefetch_preload_resp_result_model == prefetch_preload_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        prefetch_preload_resp_result_model_json2 = prefetch_preload_resp_result_model.to_dict()
        assert prefetch_preload_resp_result_model_json2 == prefetch_preload_resp_result_model_json

#-----------------------------------------------------------------------------
# Test Class for PseudoIpv4RespResult
#-----------------------------------------------------------------------------
class TestPseudoIpv4RespResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for PseudoIpv4RespResult
    #--------------------------------------------------------
    def test_pseudo_ipv4_resp_result_serialization(self):

        # Construct a json representation of a PseudoIpv4RespResult model
        pseudo_ipv4_resp_result_model_json = {}
        pseudo_ipv4_resp_result_model_json['id'] = 'pseudo_ipv4'
        pseudo_ipv4_resp_result_model_json['value'] = 'add_header'
        pseudo_ipv4_resp_result_model_json['editable'] = True
        pseudo_ipv4_resp_result_model_json['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of PseudoIpv4RespResult by calling from_dict on the json representation
        pseudo_ipv4_resp_result_model = PseudoIpv4RespResult.from_dict(pseudo_ipv4_resp_result_model_json)
        assert pseudo_ipv4_resp_result_model != False

        # Construct a model instance of PseudoIpv4RespResult by calling from_dict on the json representation
        pseudo_ipv4_resp_result_model_dict = PseudoIpv4RespResult.from_dict(pseudo_ipv4_resp_result_model_json).__dict__
        pseudo_ipv4_resp_result_model2 = PseudoIpv4RespResult(**pseudo_ipv4_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert pseudo_ipv4_resp_result_model == pseudo_ipv4_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        pseudo_ipv4_resp_result_model_json2 = pseudo_ipv4_resp_result_model.to_dict()
        assert pseudo_ipv4_resp_result_model_json2 == pseudo_ipv4_resp_result_model_json

#-----------------------------------------------------------------------------
# Test Class for ResponseBufferingRespResult
#-----------------------------------------------------------------------------
class TestResponseBufferingRespResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for ResponseBufferingRespResult
    #--------------------------------------------------------
    def test_response_buffering_resp_result_serialization(self):

        # Construct a json representation of a ResponseBufferingRespResult model
        response_buffering_resp_result_model_json = {}
        response_buffering_resp_result_model_json['id'] = 'response_buffering'
        response_buffering_resp_result_model_json['value'] = 'false'
        response_buffering_resp_result_model_json['editable'] = True
        response_buffering_resp_result_model_json['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of ResponseBufferingRespResult by calling from_dict on the json representation
        response_buffering_resp_result_model = ResponseBufferingRespResult.from_dict(response_buffering_resp_result_model_json)
        assert response_buffering_resp_result_model != False

        # Construct a model instance of ResponseBufferingRespResult by calling from_dict on the json representation
        response_buffering_resp_result_model_dict = ResponseBufferingRespResult.from_dict(response_buffering_resp_result_model_json).__dict__
        response_buffering_resp_result_model2 = ResponseBufferingRespResult(**response_buffering_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert response_buffering_resp_result_model == response_buffering_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        response_buffering_resp_result_model_json2 = response_buffering_resp_result_model.to_dict()
        assert response_buffering_resp_result_model_json2 == response_buffering_resp_result_model_json

#-----------------------------------------------------------------------------
# Test Class for ScriptLoadOptimizationRespResult
#-----------------------------------------------------------------------------
class TestScriptLoadOptimizationRespResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for ScriptLoadOptimizationRespResult
    #--------------------------------------------------------
    def test_script_load_optimization_resp_result_serialization(self):

        # Construct a json representation of a ScriptLoadOptimizationRespResult model
        script_load_optimization_resp_result_model_json = {}
        script_load_optimization_resp_result_model_json['id'] = 'script_load_optimization'
        script_load_optimization_resp_result_model_json['value'] = 'false'
        script_load_optimization_resp_result_model_json['editable'] = True
        script_load_optimization_resp_result_model_json['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of ScriptLoadOptimizationRespResult by calling from_dict on the json representation
        script_load_optimization_resp_result_model = ScriptLoadOptimizationRespResult.from_dict(script_load_optimization_resp_result_model_json)
        assert script_load_optimization_resp_result_model != False

        # Construct a model instance of ScriptLoadOptimizationRespResult by calling from_dict on the json representation
        script_load_optimization_resp_result_model_dict = ScriptLoadOptimizationRespResult.from_dict(script_load_optimization_resp_result_model_json).__dict__
        script_load_optimization_resp_result_model2 = ScriptLoadOptimizationRespResult(**script_load_optimization_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert script_load_optimization_resp_result_model == script_load_optimization_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        script_load_optimization_resp_result_model_json2 = script_load_optimization_resp_result_model.to_dict()
        assert script_load_optimization_resp_result_model_json2 == script_load_optimization_resp_result_model_json

#-----------------------------------------------------------------------------
# Test Class for SecurityHeaderRespResult
#-----------------------------------------------------------------------------
class TestSecurityHeaderRespResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for SecurityHeaderRespResult
    #--------------------------------------------------------
    def test_security_header_resp_result_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        security_header_resp_result_value_strict_transport_security_model = {} # SecurityHeaderRespResultValueStrictTransportSecurity
        security_header_resp_result_value_strict_transport_security_model['enabled'] = True
        security_header_resp_result_value_strict_transport_security_model['max_age'] = 86400
        security_header_resp_result_value_strict_transport_security_model['include_subdomains'] = True
        security_header_resp_result_value_strict_transport_security_model['nosniff'] = True

        security_header_resp_result_value_model = {} # SecurityHeaderRespResultValue
        security_header_resp_result_value_model['strict_transport_security'] = security_header_resp_result_value_strict_transport_security_model

        # Construct a json representation of a SecurityHeaderRespResult model
        security_header_resp_result_model_json = {}
        security_header_resp_result_model_json['id'] = 'security_header'
        security_header_resp_result_model_json['value'] = security_header_resp_result_value_model
        security_header_resp_result_model_json['editable'] = True
        security_header_resp_result_model_json['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of SecurityHeaderRespResult by calling from_dict on the json representation
        security_header_resp_result_model = SecurityHeaderRespResult.from_dict(security_header_resp_result_model_json)
        assert security_header_resp_result_model != False

        # Construct a model instance of SecurityHeaderRespResult by calling from_dict on the json representation
        security_header_resp_result_model_dict = SecurityHeaderRespResult.from_dict(security_header_resp_result_model_json).__dict__
        security_header_resp_result_model2 = SecurityHeaderRespResult(**security_header_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert security_header_resp_result_model == security_header_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        security_header_resp_result_model_json2 = security_header_resp_result_model.to_dict()
        assert security_header_resp_result_model_json2 == security_header_resp_result_model_json

#-----------------------------------------------------------------------------
# Test Class for SecurityHeaderRespResultValue
#-----------------------------------------------------------------------------
class TestSecurityHeaderRespResultValue():

    #--------------------------------------------------------
    # Test serialization/deserialization for SecurityHeaderRespResultValue
    #--------------------------------------------------------
    def test_security_header_resp_result_value_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        security_header_resp_result_value_strict_transport_security_model = {} # SecurityHeaderRespResultValueStrictTransportSecurity
        security_header_resp_result_value_strict_transport_security_model['enabled'] = True
        security_header_resp_result_value_strict_transport_security_model['max_age'] = 86400
        security_header_resp_result_value_strict_transport_security_model['include_subdomains'] = True
        security_header_resp_result_value_strict_transport_security_model['nosniff'] = True

        # Construct a json representation of a SecurityHeaderRespResultValue model
        security_header_resp_result_value_model_json = {}
        security_header_resp_result_value_model_json['strict_transport_security'] = security_header_resp_result_value_strict_transport_security_model

        # Construct a model instance of SecurityHeaderRespResultValue by calling from_dict on the json representation
        security_header_resp_result_value_model = SecurityHeaderRespResultValue.from_dict(security_header_resp_result_value_model_json)
        assert security_header_resp_result_value_model != False

        # Construct a model instance of SecurityHeaderRespResultValue by calling from_dict on the json representation
        security_header_resp_result_value_model_dict = SecurityHeaderRespResultValue.from_dict(security_header_resp_result_value_model_json).__dict__
        security_header_resp_result_value_model2 = SecurityHeaderRespResultValue(**security_header_resp_result_value_model_dict)

        # Verify the model instances are equivalent
        assert security_header_resp_result_value_model == security_header_resp_result_value_model2

        # Convert model instance back to dict and verify no loss of data
        security_header_resp_result_value_model_json2 = security_header_resp_result_value_model.to_dict()
        assert security_header_resp_result_value_model_json2 == security_header_resp_result_value_model_json

#-----------------------------------------------------------------------------
# Test Class for SecurityHeaderRespResultValueStrictTransportSecurity
#-----------------------------------------------------------------------------
class TestSecurityHeaderRespResultValueStrictTransportSecurity():

    #--------------------------------------------------------
    # Test serialization/deserialization for SecurityHeaderRespResultValueStrictTransportSecurity
    #--------------------------------------------------------
    def test_security_header_resp_result_value_strict_transport_security_serialization(self):

        # Construct a json representation of a SecurityHeaderRespResultValueStrictTransportSecurity model
        security_header_resp_result_value_strict_transport_security_model_json = {}
        security_header_resp_result_value_strict_transport_security_model_json['enabled'] = True
        security_header_resp_result_value_strict_transport_security_model_json['max_age'] = 86400
        security_header_resp_result_value_strict_transport_security_model_json['include_subdomains'] = True
        security_header_resp_result_value_strict_transport_security_model_json['nosniff'] = True

        # Construct a model instance of SecurityHeaderRespResultValueStrictTransportSecurity by calling from_dict on the json representation
        security_header_resp_result_value_strict_transport_security_model = SecurityHeaderRespResultValueStrictTransportSecurity.from_dict(security_header_resp_result_value_strict_transport_security_model_json)
        assert security_header_resp_result_value_strict_transport_security_model != False

        # Construct a model instance of SecurityHeaderRespResultValueStrictTransportSecurity by calling from_dict on the json representation
        security_header_resp_result_value_strict_transport_security_model_dict = SecurityHeaderRespResultValueStrictTransportSecurity.from_dict(security_header_resp_result_value_strict_transport_security_model_json).__dict__
        security_header_resp_result_value_strict_transport_security_model2 = SecurityHeaderRespResultValueStrictTransportSecurity(**security_header_resp_result_value_strict_transport_security_model_dict)

        # Verify the model instances are equivalent
        assert security_header_resp_result_value_strict_transport_security_model == security_header_resp_result_value_strict_transport_security_model2

        # Convert model instance back to dict and verify no loss of data
        security_header_resp_result_value_strict_transport_security_model_json2 = security_header_resp_result_value_strict_transport_security_model.to_dict()
        assert security_header_resp_result_value_strict_transport_security_model_json2 == security_header_resp_result_value_strict_transport_security_model_json

#-----------------------------------------------------------------------------
# Test Class for SecurityHeaderSettingValue
#-----------------------------------------------------------------------------
class TestSecurityHeaderSettingValue():

    #--------------------------------------------------------
    # Test serialization/deserialization for SecurityHeaderSettingValue
    #--------------------------------------------------------
    def test_security_header_setting_value_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        security_header_setting_value_strict_transport_security_model = {} # SecurityHeaderSettingValueStrictTransportSecurity
        security_header_setting_value_strict_transport_security_model['enabled'] = True
        security_header_setting_value_strict_transport_security_model['max_age'] = 86400
        security_header_setting_value_strict_transport_security_model['include_subdomains'] = True
        security_header_setting_value_strict_transport_security_model['nosniff'] = True

        # Construct a json representation of a SecurityHeaderSettingValue model
        security_header_setting_value_model_json = {}
        security_header_setting_value_model_json['strict_transport_security'] = security_header_setting_value_strict_transport_security_model

        # Construct a model instance of SecurityHeaderSettingValue by calling from_dict on the json representation
        security_header_setting_value_model = SecurityHeaderSettingValue.from_dict(security_header_setting_value_model_json)
        assert security_header_setting_value_model != False

        # Construct a model instance of SecurityHeaderSettingValue by calling from_dict on the json representation
        security_header_setting_value_model_dict = SecurityHeaderSettingValue.from_dict(security_header_setting_value_model_json).__dict__
        security_header_setting_value_model2 = SecurityHeaderSettingValue(**security_header_setting_value_model_dict)

        # Verify the model instances are equivalent
        assert security_header_setting_value_model == security_header_setting_value_model2

        # Convert model instance back to dict and verify no loss of data
        security_header_setting_value_model_json2 = security_header_setting_value_model.to_dict()
        assert security_header_setting_value_model_json2 == security_header_setting_value_model_json

#-----------------------------------------------------------------------------
# Test Class for SecurityHeaderSettingValueStrictTransportSecurity
#-----------------------------------------------------------------------------
class TestSecurityHeaderSettingValueStrictTransportSecurity():

    #--------------------------------------------------------
    # Test serialization/deserialization for SecurityHeaderSettingValueStrictTransportSecurity
    #--------------------------------------------------------
    def test_security_header_setting_value_strict_transport_security_serialization(self):

        # Construct a json representation of a SecurityHeaderSettingValueStrictTransportSecurity model
        security_header_setting_value_strict_transport_security_model_json = {}
        security_header_setting_value_strict_transport_security_model_json['enabled'] = True
        security_header_setting_value_strict_transport_security_model_json['max_age'] = 86400
        security_header_setting_value_strict_transport_security_model_json['include_subdomains'] = True
        security_header_setting_value_strict_transport_security_model_json['nosniff'] = True

        # Construct a model instance of SecurityHeaderSettingValueStrictTransportSecurity by calling from_dict on the json representation
        security_header_setting_value_strict_transport_security_model = SecurityHeaderSettingValueStrictTransportSecurity.from_dict(security_header_setting_value_strict_transport_security_model_json)
        assert security_header_setting_value_strict_transport_security_model != False

        # Construct a model instance of SecurityHeaderSettingValueStrictTransportSecurity by calling from_dict on the json representation
        security_header_setting_value_strict_transport_security_model_dict = SecurityHeaderSettingValueStrictTransportSecurity.from_dict(security_header_setting_value_strict_transport_security_model_json).__dict__
        security_header_setting_value_strict_transport_security_model2 = SecurityHeaderSettingValueStrictTransportSecurity(**security_header_setting_value_strict_transport_security_model_dict)

        # Verify the model instances are equivalent
        assert security_header_setting_value_strict_transport_security_model == security_header_setting_value_strict_transport_security_model2

        # Convert model instance back to dict and verify no loss of data
        security_header_setting_value_strict_transport_security_model_json2 = security_header_setting_value_strict_transport_security_model.to_dict()
        assert security_header_setting_value_strict_transport_security_model_json2 == security_header_setting_value_strict_transport_security_model_json

#-----------------------------------------------------------------------------
# Test Class for ServerSideExcludeRespResult
#-----------------------------------------------------------------------------
class TestServerSideExcludeRespResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for ServerSideExcludeRespResult
    #--------------------------------------------------------
    def test_server_side_exclude_resp_result_serialization(self):

        # Construct a json representation of a ServerSideExcludeRespResult model
        server_side_exclude_resp_result_model_json = {}
        server_side_exclude_resp_result_model_json['id'] = 'server_side_exclude'
        server_side_exclude_resp_result_model_json['value'] = 'false'
        server_side_exclude_resp_result_model_json['editable'] = True
        server_side_exclude_resp_result_model_json['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of ServerSideExcludeRespResult by calling from_dict on the json representation
        server_side_exclude_resp_result_model = ServerSideExcludeRespResult.from_dict(server_side_exclude_resp_result_model_json)
        assert server_side_exclude_resp_result_model != False

        # Construct a model instance of ServerSideExcludeRespResult by calling from_dict on the json representation
        server_side_exclude_resp_result_model_dict = ServerSideExcludeRespResult.from_dict(server_side_exclude_resp_result_model_json).__dict__
        server_side_exclude_resp_result_model2 = ServerSideExcludeRespResult(**server_side_exclude_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert server_side_exclude_resp_result_model == server_side_exclude_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        server_side_exclude_resp_result_model_json2 = server_side_exclude_resp_result_model.to_dict()
        assert server_side_exclude_resp_result_model_json2 == server_side_exclude_resp_result_model_json

#-----------------------------------------------------------------------------
# Test Class for TlsClientAuthRespResult
#-----------------------------------------------------------------------------
class TestTlsClientAuthRespResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for TlsClientAuthRespResult
    #--------------------------------------------------------
    def test_tls_client_auth_resp_result_serialization(self):

        # Construct a json representation of a TlsClientAuthRespResult model
        tls_client_auth_resp_result_model_json = {}
        tls_client_auth_resp_result_model_json['id'] = 'tls_client_auth'
        tls_client_auth_resp_result_model_json['value'] = 'false'
        tls_client_auth_resp_result_model_json['editable'] = True
        tls_client_auth_resp_result_model_json['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of TlsClientAuthRespResult by calling from_dict on the json representation
        tls_client_auth_resp_result_model = TlsClientAuthRespResult.from_dict(tls_client_auth_resp_result_model_json)
        assert tls_client_auth_resp_result_model != False

        # Construct a model instance of TlsClientAuthRespResult by calling from_dict on the json representation
        tls_client_auth_resp_result_model_dict = TlsClientAuthRespResult.from_dict(tls_client_auth_resp_result_model_json).__dict__
        tls_client_auth_resp_result_model2 = TlsClientAuthRespResult(**tls_client_auth_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert tls_client_auth_resp_result_model == tls_client_auth_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        tls_client_auth_resp_result_model_json2 = tls_client_auth_resp_result_model.to_dict()
        assert tls_client_auth_resp_result_model_json2 == tls_client_auth_resp_result_model_json

#-----------------------------------------------------------------------------
# Test Class for TrueClientIpRespResult
#-----------------------------------------------------------------------------
class TestTrueClientIpRespResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for TrueClientIpRespResult
    #--------------------------------------------------------
    def test_true_client_ip_resp_result_serialization(self):

        # Construct a json representation of a TrueClientIpRespResult model
        true_client_ip_resp_result_model_json = {}
        true_client_ip_resp_result_model_json['id'] = 'true_client_ip_header'
        true_client_ip_resp_result_model_json['value'] = 'false'
        true_client_ip_resp_result_model_json['editable'] = True
        true_client_ip_resp_result_model_json['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of TrueClientIpRespResult by calling from_dict on the json representation
        true_client_ip_resp_result_model = TrueClientIpRespResult.from_dict(true_client_ip_resp_result_model_json)
        assert true_client_ip_resp_result_model != False

        # Construct a model instance of TrueClientIpRespResult by calling from_dict on the json representation
        true_client_ip_resp_result_model_dict = TrueClientIpRespResult.from_dict(true_client_ip_resp_result_model_json).__dict__
        true_client_ip_resp_result_model2 = TrueClientIpRespResult(**true_client_ip_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert true_client_ip_resp_result_model == true_client_ip_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        true_client_ip_resp_result_model_json2 = true_client_ip_resp_result_model.to_dict()
        assert true_client_ip_resp_result_model_json2 == true_client_ip_resp_result_model_json

#-----------------------------------------------------------------------------
# Test Class for WafRespResult
#-----------------------------------------------------------------------------
class TestWafRespResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for WafRespResult
    #--------------------------------------------------------
    def test_waf_resp_result_serialization(self):

        # Construct a json representation of a WafRespResult model
        waf_resp_result_model_json = {}
        waf_resp_result_model_json['id'] = 'waf'
        waf_resp_result_model_json['value'] = 'false'
        waf_resp_result_model_json['editable'] = True
        waf_resp_result_model_json['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of WafRespResult by calling from_dict on the json representation
        waf_resp_result_model = WafRespResult.from_dict(waf_resp_result_model_json)
        assert waf_resp_result_model != False

        # Construct a model instance of WafRespResult by calling from_dict on the json representation
        waf_resp_result_model_dict = WafRespResult.from_dict(waf_resp_result_model_json).__dict__
        waf_resp_result_model2 = WafRespResult(**waf_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert waf_resp_result_model == waf_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        waf_resp_result_model_json2 = waf_resp_result_model.to_dict()
        assert waf_resp_result_model_json2 == waf_resp_result_model_json

#-----------------------------------------------------------------------------
# Test Class for WebsocketsRespResult
#-----------------------------------------------------------------------------
class TestWebsocketsRespResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for WebsocketsRespResult
    #--------------------------------------------------------
    def test_websockets_resp_result_serialization(self):

        # Construct a json representation of a WebsocketsRespResult model
        websockets_resp_result_model_json = {}
        websockets_resp_result_model_json['id'] = 'websockets'
        websockets_resp_result_model_json['value'] = 'false'
        websockets_resp_result_model_json['editable'] = True
        websockets_resp_result_model_json['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of WebsocketsRespResult by calling from_dict on the json representation
        websockets_resp_result_model = WebsocketsRespResult.from_dict(websockets_resp_result_model_json)
        assert websockets_resp_result_model != False

        # Construct a model instance of WebsocketsRespResult by calling from_dict on the json representation
        websockets_resp_result_model_dict = WebsocketsRespResult.from_dict(websockets_resp_result_model_json).__dict__
        websockets_resp_result_model2 = WebsocketsRespResult(**websockets_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert websockets_resp_result_model == websockets_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        websockets_resp_result_model_json2 = websockets_resp_result_model.to_dict()
        assert websockets_resp_result_model_json2 == websockets_resp_result_model_json

#-----------------------------------------------------------------------------
# Test Class for ZonesDnssecRespResult
#-----------------------------------------------------------------------------
class TestZonesDnssecRespResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for ZonesDnssecRespResult
    #--------------------------------------------------------
    def test_zones_dnssec_resp_result_serialization(self):

        # Construct a json representation of a ZonesDnssecRespResult model
        zones_dnssec_resp_result_model_json = {}
        zones_dnssec_resp_result_model_json['status'] = 'active'
        zones_dnssec_resp_result_model_json['flags'] = 257
        zones_dnssec_resp_result_model_json['algorithm'] = '13'
        zones_dnssec_resp_result_model_json['key_type'] = 'ECDSAP256SHA256'
        zones_dnssec_resp_result_model_json['digest_type'] = '2'
        zones_dnssec_resp_result_model_json['digest_algorithm'] = 'SHA256'
        zones_dnssec_resp_result_model_json['digest'] = '48E939042E82C22542CB377B580DFDC52A361CEFDC72E7F9107E2B6BD9306A45'
        zones_dnssec_resp_result_model_json['ds'] = 'example.com. 3600 IN DS 16953 13 2 248E939042E82C22542CB377B580DFDC52A361CEFDC72E7F9107E2B6BD9306A45'
        zones_dnssec_resp_result_model_json['key_tag'] = 42
        zones_dnssec_resp_result_model_json['public_key'] = 'oXiGYrSTO+LSCJ3mohc8EP+CzF9KxBj8/ydXJ22pKuZP3VAC3/Md/k7xZfz470CoRyZJ6gV6vml07IC3d8xqhA=='

        # Construct a model instance of ZonesDnssecRespResult by calling from_dict on the json representation
        zones_dnssec_resp_result_model = ZonesDnssecRespResult.from_dict(zones_dnssec_resp_result_model_json)
        assert zones_dnssec_resp_result_model != False

        # Construct a model instance of ZonesDnssecRespResult by calling from_dict on the json representation
        zones_dnssec_resp_result_model_dict = ZonesDnssecRespResult.from_dict(zones_dnssec_resp_result_model_json).__dict__
        zones_dnssec_resp_result_model2 = ZonesDnssecRespResult(**zones_dnssec_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert zones_dnssec_resp_result_model == zones_dnssec_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        zones_dnssec_resp_result_model_json2 = zones_dnssec_resp_result_model.to_dict()
        assert zones_dnssec_resp_result_model_json2 == zones_dnssec_resp_result_model_json

#-----------------------------------------------------------------------------
# Test Class for AlwaysUseHttpsResp
#-----------------------------------------------------------------------------
class TestAlwaysUseHttpsResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for AlwaysUseHttpsResp
    #--------------------------------------------------------
    def test_always_use_https_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        always_use_https_resp_result_model = {} # AlwaysUseHttpsRespResult
        always_use_https_resp_result_model['id'] = 'always_use_https'
        always_use_https_resp_result_model['value'] = 'false'
        always_use_https_resp_result_model['editable'] = True
        always_use_https_resp_result_model['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a json representation of a AlwaysUseHttpsResp model
        always_use_https_resp_model_json = {}
        always_use_https_resp_model_json['result'] = always_use_https_resp_result_model
        always_use_https_resp_model_json['success'] = True
        always_use_https_resp_model_json['errors'] = [['testString']]
        always_use_https_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of AlwaysUseHttpsResp by calling from_dict on the json representation
        always_use_https_resp_model = AlwaysUseHttpsResp.from_dict(always_use_https_resp_model_json)
        assert always_use_https_resp_model != False

        # Construct a model instance of AlwaysUseHttpsResp by calling from_dict on the json representation
        always_use_https_resp_model_dict = AlwaysUseHttpsResp.from_dict(always_use_https_resp_model_json).__dict__
        always_use_https_resp_model2 = AlwaysUseHttpsResp(**always_use_https_resp_model_dict)

        # Verify the model instances are equivalent
        assert always_use_https_resp_model == always_use_https_resp_model2

        # Convert model instance back to dict and verify no loss of data
        always_use_https_resp_model_json2 = always_use_https_resp_model.to_dict()
        assert always_use_https_resp_model_json2 == always_use_https_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for AutomaticHttpsRewritesResp
#-----------------------------------------------------------------------------
class TestAutomaticHttpsRewritesResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for AutomaticHttpsRewritesResp
    #--------------------------------------------------------
    def test_automatic_https_rewrites_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        automatic_https_rewrites_resp_result_model = {} # AutomaticHttpsRewritesRespResult
        automatic_https_rewrites_resp_result_model['id'] = 'automatic_https_rewrites'
        automatic_https_rewrites_resp_result_model['value'] = 'false'
        automatic_https_rewrites_resp_result_model['editable'] = True
        automatic_https_rewrites_resp_result_model['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a json representation of a AutomaticHttpsRewritesResp model
        automatic_https_rewrites_resp_model_json = {}
        automatic_https_rewrites_resp_model_json['result'] = automatic_https_rewrites_resp_result_model
        automatic_https_rewrites_resp_model_json['success'] = True
        automatic_https_rewrites_resp_model_json['errors'] = [['testString']]
        automatic_https_rewrites_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of AutomaticHttpsRewritesResp by calling from_dict on the json representation
        automatic_https_rewrites_resp_model = AutomaticHttpsRewritesResp.from_dict(automatic_https_rewrites_resp_model_json)
        assert automatic_https_rewrites_resp_model != False

        # Construct a model instance of AutomaticHttpsRewritesResp by calling from_dict on the json representation
        automatic_https_rewrites_resp_model_dict = AutomaticHttpsRewritesResp.from_dict(automatic_https_rewrites_resp_model_json).__dict__
        automatic_https_rewrites_resp_model2 = AutomaticHttpsRewritesResp(**automatic_https_rewrites_resp_model_dict)

        # Verify the model instances are equivalent
        assert automatic_https_rewrites_resp_model == automatic_https_rewrites_resp_model2

        # Convert model instance back to dict and verify no loss of data
        automatic_https_rewrites_resp_model_json2 = automatic_https_rewrites_resp_model.to_dict()
        assert automatic_https_rewrites_resp_model_json2 == automatic_https_rewrites_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for BrowserCheckResp
#-----------------------------------------------------------------------------
class TestBrowserCheckResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for BrowserCheckResp
    #--------------------------------------------------------
    def test_browser_check_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        browser_check_resp_result_model = {} # BrowserCheckRespResult
        browser_check_resp_result_model['id'] = 'browser_check'
        browser_check_resp_result_model['value'] = 'false'
        browser_check_resp_result_model['editable'] = True
        browser_check_resp_result_model['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a json representation of a BrowserCheckResp model
        browser_check_resp_model_json = {}
        browser_check_resp_model_json['result'] = browser_check_resp_result_model
        browser_check_resp_model_json['success'] = True
        browser_check_resp_model_json['errors'] = [['testString']]
        browser_check_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of BrowserCheckResp by calling from_dict on the json representation
        browser_check_resp_model = BrowserCheckResp.from_dict(browser_check_resp_model_json)
        assert browser_check_resp_model != False

        # Construct a model instance of BrowserCheckResp by calling from_dict on the json representation
        browser_check_resp_model_dict = BrowserCheckResp.from_dict(browser_check_resp_model_json).__dict__
        browser_check_resp_model2 = BrowserCheckResp(**browser_check_resp_model_dict)

        # Verify the model instances are equivalent
        assert browser_check_resp_model == browser_check_resp_model2

        # Convert model instance back to dict and verify no loss of data
        browser_check_resp_model_json2 = browser_check_resp_model.to_dict()
        assert browser_check_resp_model_json2 == browser_check_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for ChallengeTtlResp
#-----------------------------------------------------------------------------
class TestChallengeTtlResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for ChallengeTtlResp
    #--------------------------------------------------------
    def test_challenge_ttl_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        challenge_ttl_resp_result_model = {} # ChallengeTtlRespResult
        challenge_ttl_resp_result_model['id'] = 'challenge_ttl'
        challenge_ttl_resp_result_model['value'] = 1800
        challenge_ttl_resp_result_model['editable'] = True
        challenge_ttl_resp_result_model['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a json representation of a ChallengeTtlResp model
        challenge_ttl_resp_model_json = {}
        challenge_ttl_resp_model_json['result'] = challenge_ttl_resp_result_model
        challenge_ttl_resp_model_json['success'] = True
        challenge_ttl_resp_model_json['errors'] = [['testString']]
        challenge_ttl_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of ChallengeTtlResp by calling from_dict on the json representation
        challenge_ttl_resp_model = ChallengeTtlResp.from_dict(challenge_ttl_resp_model_json)
        assert challenge_ttl_resp_model != False

        # Construct a model instance of ChallengeTtlResp by calling from_dict on the json representation
        challenge_ttl_resp_model_dict = ChallengeTtlResp.from_dict(challenge_ttl_resp_model_json).__dict__
        challenge_ttl_resp_model2 = ChallengeTtlResp(**challenge_ttl_resp_model_dict)

        # Verify the model instances are equivalent
        assert challenge_ttl_resp_model == challenge_ttl_resp_model2

        # Convert model instance back to dict and verify no loss of data
        challenge_ttl_resp_model_json2 = challenge_ttl_resp_model.to_dict()
        assert challenge_ttl_resp_model_json2 == challenge_ttl_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for CiphersResp
#-----------------------------------------------------------------------------
class TestCiphersResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for CiphersResp
    #--------------------------------------------------------
    def test_ciphers_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        ciphers_resp_result_model = {} # CiphersRespResult
        ciphers_resp_result_model['id'] = 'ciphers'
        ciphers_resp_result_model['value'] = ['testString']
        ciphers_resp_result_model['editable'] = True
        ciphers_resp_result_model['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a json representation of a CiphersResp model
        ciphers_resp_model_json = {}
        ciphers_resp_model_json['result'] = ciphers_resp_result_model
        ciphers_resp_model_json['success'] = True
        ciphers_resp_model_json['errors'] = [['testString']]
        ciphers_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of CiphersResp by calling from_dict on the json representation
        ciphers_resp_model = CiphersResp.from_dict(ciphers_resp_model_json)
        assert ciphers_resp_model != False

        # Construct a model instance of CiphersResp by calling from_dict on the json representation
        ciphers_resp_model_dict = CiphersResp.from_dict(ciphers_resp_model_json).__dict__
        ciphers_resp_model2 = CiphersResp(**ciphers_resp_model_dict)

        # Verify the model instances are equivalent
        assert ciphers_resp_model == ciphers_resp_model2

        # Convert model instance back to dict and verify no loss of data
        ciphers_resp_model_json2 = ciphers_resp_model.to_dict()
        assert ciphers_resp_model_json2 == ciphers_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for CnameFlatteningResponse
#-----------------------------------------------------------------------------
class TestCnameFlatteningResponse():

    #--------------------------------------------------------
    # Test serialization/deserialization for CnameFlatteningResponse
    #--------------------------------------------------------
    def test_cname_flattening_response_serialization(self):

        # Construct a json representation of a CnameFlatteningResponse model
        cname_flattening_response_model_json = {}
        cname_flattening_response_model_json['id'] = 'cname_flattening'
        cname_flattening_response_model_json['value'] = 'flatten_all'
        cname_flattening_response_model_json['modified_on'] = '2020-01-28T18:40:40.123456Z'
        cname_flattening_response_model_json['editable'] = True

        # Construct a model instance of CnameFlatteningResponse by calling from_dict on the json representation
        cname_flattening_response_model = CnameFlatteningResponse.from_dict(cname_flattening_response_model_json)
        assert cname_flattening_response_model != False

        # Construct a model instance of CnameFlatteningResponse by calling from_dict on the json representation
        cname_flattening_response_model_dict = CnameFlatteningResponse.from_dict(cname_flattening_response_model_json).__dict__
        cname_flattening_response_model2 = CnameFlatteningResponse(**cname_flattening_response_model_dict)

        # Verify the model instances are equivalent
        assert cname_flattening_response_model == cname_flattening_response_model2

        # Convert model instance back to dict and verify no loss of data
        cname_flattening_response_model_json2 = cname_flattening_response_model.to_dict()
        assert cname_flattening_response_model_json2 == cname_flattening_response_model_json

#-----------------------------------------------------------------------------
# Test Class for HotlinkProtectionResp
#-----------------------------------------------------------------------------
class TestHotlinkProtectionResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for HotlinkProtectionResp
    #--------------------------------------------------------
    def test_hotlink_protection_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        hotlink_protection_resp_result_model = {} # HotlinkProtectionRespResult
        hotlink_protection_resp_result_model['id'] = 'hotlink_protection'
        hotlink_protection_resp_result_model['value'] = 'false'
        hotlink_protection_resp_result_model['editable'] = True
        hotlink_protection_resp_result_model['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a json representation of a HotlinkProtectionResp model
        hotlink_protection_resp_model_json = {}
        hotlink_protection_resp_model_json['result'] = hotlink_protection_resp_result_model
        hotlink_protection_resp_model_json['success'] = True
        hotlink_protection_resp_model_json['errors'] = [['testString']]
        hotlink_protection_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of HotlinkProtectionResp by calling from_dict on the json representation
        hotlink_protection_resp_model = HotlinkProtectionResp.from_dict(hotlink_protection_resp_model_json)
        assert hotlink_protection_resp_model != False

        # Construct a model instance of HotlinkProtectionResp by calling from_dict on the json representation
        hotlink_protection_resp_model_dict = HotlinkProtectionResp.from_dict(hotlink_protection_resp_model_json).__dict__
        hotlink_protection_resp_model2 = HotlinkProtectionResp(**hotlink_protection_resp_model_dict)

        # Verify the model instances are equivalent
        assert hotlink_protection_resp_model == hotlink_protection_resp_model2

        # Convert model instance back to dict and verify no loss of data
        hotlink_protection_resp_model_json2 = hotlink_protection_resp_model.to_dict()
        assert hotlink_protection_resp_model_json2 == hotlink_protection_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for Http2Resp
#-----------------------------------------------------------------------------
class TestHttp2Resp():

    #--------------------------------------------------------
    # Test serialization/deserialization for Http2Resp
    #--------------------------------------------------------
    def test_http2_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        http2_resp_result_model = {} # Http2RespResult
        http2_resp_result_model['id'] = 'http2'
        http2_resp_result_model['value'] = 'false'
        http2_resp_result_model['editable'] = True
        http2_resp_result_model['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a json representation of a Http2Resp model
        http2_resp_model_json = {}
        http2_resp_model_json['result'] = http2_resp_result_model
        http2_resp_model_json['success'] = True
        http2_resp_model_json['errors'] = [['testString']]
        http2_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of Http2Resp by calling from_dict on the json representation
        http2_resp_model = Http2Resp.from_dict(http2_resp_model_json)
        assert http2_resp_model != False

        # Construct a model instance of Http2Resp by calling from_dict on the json representation
        http2_resp_model_dict = Http2Resp.from_dict(http2_resp_model_json).__dict__
        http2_resp_model2 = Http2Resp(**http2_resp_model_dict)

        # Verify the model instances are equivalent
        assert http2_resp_model == http2_resp_model2

        # Convert model instance back to dict and verify no loss of data
        http2_resp_model_json2 = http2_resp_model.to_dict()
        assert http2_resp_model_json2 == http2_resp_model_json


#-----------------------------------------------------------------------------
# Test Class for Http2Resp
#-----------------------------------------------------------------------------
class TestHttp3Resp():
    """
    Test Class for Http3Resp
    """

    def test_http3_resp_serialization(self):
        """
        Test serialization/deserialization for Http3Resp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        http3_resp_result_model = {} # Http3RespResult
        http3_resp_result_model['id'] = 'http3'
        http3_resp_result_model['value'] = 'off'
        http3_resp_result_model['editable'] = True
        http3_resp_result_model['modified_on'] = '2015-03-14T09:26:53.123456Z'

        # Construct a json representation of a Http3Resp model
        http3_resp_model_json = {}
        http3_resp_model_json['result'] = http3_resp_result_model
        http3_resp_model_json['success'] = True
        http3_resp_model_json['errors'] = [['testString']]
        http3_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of Http3Resp by calling from_dict on the json representation
        http3_resp_model = Http3Resp.from_dict(http3_resp_model_json)
        assert http3_resp_model != False

        # Construct a model instance of Http3Resp by calling from_dict on the json representation
        http3_resp_model_dict = Http3Resp.from_dict(http3_resp_model_json).__dict__
        http3_resp_model2 = Http3Resp(**http3_resp_model_dict)

        # Verify the model instances are equivalent
        assert http3_resp_model == http3_resp_model2

        # Convert model instance back to dict and verify no loss of data
        http3_resp_model_json2 = http3_resp_model.to_dict()
        assert http3_resp_model_json2 == http3_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for ImageLoadOptimizationResp
#-----------------------------------------------------------------------------
class TestImageLoadOptimizationResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for ImageLoadOptimizationResp
    #--------------------------------------------------------
    def test_image_load_optimization_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        image_load_optimization_resp_result_model = {} # ImageLoadOptimizationRespResult
        image_load_optimization_resp_result_model['id'] = 'image_load_optimization'
        image_load_optimization_resp_result_model['value'] = 'false'
        image_load_optimization_resp_result_model['editable'] = True
        image_load_optimization_resp_result_model['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a json representation of a ImageLoadOptimizationResp model
        image_load_optimization_resp_model_json = {}
        image_load_optimization_resp_model_json['result'] = image_load_optimization_resp_result_model
        image_load_optimization_resp_model_json['success'] = True
        image_load_optimization_resp_model_json['errors'] = [['testString']]
        image_load_optimization_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of ImageLoadOptimizationResp by calling from_dict on the json representation
        image_load_optimization_resp_model = ImageLoadOptimizationResp.from_dict(image_load_optimization_resp_model_json)
        assert image_load_optimization_resp_model != False

        # Construct a model instance of ImageLoadOptimizationResp by calling from_dict on the json representation
        image_load_optimization_resp_model_dict = ImageLoadOptimizationResp.from_dict(image_load_optimization_resp_model_json).__dict__
        image_load_optimization_resp_model2 = ImageLoadOptimizationResp(**image_load_optimization_resp_model_dict)

        # Verify the model instances are equivalent
        assert image_load_optimization_resp_model == image_load_optimization_resp_model2

        # Convert model instance back to dict and verify no loss of data
        image_load_optimization_resp_model_json2 = image_load_optimization_resp_model.to_dict()
        assert image_load_optimization_resp_model_json2 == image_load_optimization_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for ImageSizeOptimizationResp
#-----------------------------------------------------------------------------
class TestImageSizeOptimizationResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for ImageSizeOptimizationResp
    #--------------------------------------------------------
    def test_image_size_optimization_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        image_size_optimization_resp_result_model = {} # ImageSizeOptimizationRespResult
        image_size_optimization_resp_result_model['id'] = 'image_size_optimization'
        image_size_optimization_resp_result_model['value'] = 'lossless'
        image_size_optimization_resp_result_model['editable'] = True
        image_size_optimization_resp_result_model['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a json representation of a ImageSizeOptimizationResp model
        image_size_optimization_resp_model_json = {}
        image_size_optimization_resp_model_json['result'] = image_size_optimization_resp_result_model
        image_size_optimization_resp_model_json['success'] = True
        image_size_optimization_resp_model_json['errors'] = [['testString']]
        image_size_optimization_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of ImageSizeOptimizationResp by calling from_dict on the json representation
        image_size_optimization_resp_model = ImageSizeOptimizationResp.from_dict(image_size_optimization_resp_model_json)
        assert image_size_optimization_resp_model != False

        # Construct a model instance of ImageSizeOptimizationResp by calling from_dict on the json representation
        image_size_optimization_resp_model_dict = ImageSizeOptimizationResp.from_dict(image_size_optimization_resp_model_json).__dict__
        image_size_optimization_resp_model2 = ImageSizeOptimizationResp(**image_size_optimization_resp_model_dict)

        # Verify the model instances are equivalent
        assert image_size_optimization_resp_model == image_size_optimization_resp_model2

        # Convert model instance back to dict and verify no loss of data
        image_size_optimization_resp_model_json2 = image_size_optimization_resp_model.to_dict()
        assert image_size_optimization_resp_model_json2 == image_size_optimization_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for IpGeolocationResp
#-----------------------------------------------------------------------------
class TestIpGeolocationResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for IpGeolocationResp
    #--------------------------------------------------------
    def test_ip_geolocation_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        ip_geolocation_resp_result_model = {} # IpGeolocationRespResult
        ip_geolocation_resp_result_model['id'] = 'ip_geolocation'
        ip_geolocation_resp_result_model['value'] = 'false'
        ip_geolocation_resp_result_model['editable'] = True
        ip_geolocation_resp_result_model['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a json representation of a IpGeolocationResp model
        ip_geolocation_resp_model_json = {}
        ip_geolocation_resp_model_json['result'] = ip_geolocation_resp_result_model
        ip_geolocation_resp_model_json['success'] = True
        ip_geolocation_resp_model_json['errors'] = [['testString']]
        ip_geolocation_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of IpGeolocationResp by calling from_dict on the json representation
        ip_geolocation_resp_model = IpGeolocationResp.from_dict(ip_geolocation_resp_model_json)
        assert ip_geolocation_resp_model != False

        # Construct a model instance of IpGeolocationResp by calling from_dict on the json representation
        ip_geolocation_resp_model_dict = IpGeolocationResp.from_dict(ip_geolocation_resp_model_json).__dict__
        ip_geolocation_resp_model2 = IpGeolocationResp(**ip_geolocation_resp_model_dict)

        # Verify the model instances are equivalent
        assert ip_geolocation_resp_model == ip_geolocation_resp_model2

        # Convert model instance back to dict and verify no loss of data
        ip_geolocation_resp_model_json2 = ip_geolocation_resp_model.to_dict()
        assert ip_geolocation_resp_model_json2 == ip_geolocation_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for Ipv6Resp
#-----------------------------------------------------------------------------
class TestIpv6Resp():

    #--------------------------------------------------------
    # Test serialization/deserialization for Ipv6Resp
    #--------------------------------------------------------
    def test_ipv6_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        ipv6_resp_result_model = {} # Ipv6RespResult
        ipv6_resp_result_model['id'] = 'ipv6'
        ipv6_resp_result_model['value'] = 'false'
        ipv6_resp_result_model['editable'] = True
        ipv6_resp_result_model['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a json representation of a Ipv6Resp model
        ipv6_resp_model_json = {}
        ipv6_resp_model_json['result'] = ipv6_resp_result_model
        ipv6_resp_model_json['success'] = True
        ipv6_resp_model_json['errors'] = [['testString']]
        ipv6_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of Ipv6Resp by calling from_dict on the json representation
        ipv6_resp_model = Ipv6Resp.from_dict(ipv6_resp_model_json)
        assert ipv6_resp_model != False

        # Construct a model instance of Ipv6Resp by calling from_dict on the json representation
        ipv6_resp_model_dict = Ipv6Resp.from_dict(ipv6_resp_model_json).__dict__
        ipv6_resp_model2 = Ipv6Resp(**ipv6_resp_model_dict)

        # Verify the model instances are equivalent
        assert ipv6_resp_model == ipv6_resp_model2

        # Convert model instance back to dict and verify no loss of data
        ipv6_resp_model_json2 = ipv6_resp_model.to_dict()
        assert ipv6_resp_model_json2 == ipv6_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for MaxUploadResp
#-----------------------------------------------------------------------------
class TestMaxUploadResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for MaxUploadResp
    #--------------------------------------------------------
    def test_max_upload_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        max_upload_resp_result_model = {} # MaxUploadRespResult
        max_upload_resp_result_model['id'] = 'max_upload'
        max_upload_resp_result_model['value'] = 300
        max_upload_resp_result_model['editable'] = True
        max_upload_resp_result_model['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a json representation of a MaxUploadResp model
        max_upload_resp_model_json = {}
        max_upload_resp_model_json['result'] = max_upload_resp_result_model
        max_upload_resp_model_json['success'] = True
        max_upload_resp_model_json['errors'] = [['testString']]
        max_upload_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of MaxUploadResp by calling from_dict on the json representation
        max_upload_resp_model = MaxUploadResp.from_dict(max_upload_resp_model_json)
        assert max_upload_resp_model != False

        # Construct a model instance of MaxUploadResp by calling from_dict on the json representation
        max_upload_resp_model_dict = MaxUploadResp.from_dict(max_upload_resp_model_json).__dict__
        max_upload_resp_model2 = MaxUploadResp(**max_upload_resp_model_dict)

        # Verify the model instances are equivalent
        assert max_upload_resp_model == max_upload_resp_model2

        # Convert model instance back to dict and verify no loss of data
        max_upload_resp_model_json2 = max_upload_resp_model.to_dict()
        assert max_upload_resp_model_json2 == max_upload_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for MinTlsVersionResp
#-----------------------------------------------------------------------------
class TestMinTlsVersionResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for MinTlsVersionResp
    #--------------------------------------------------------
    def test_min_tls_version_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        min_tls_version_resp_result_model = {} # MinTlsVersionRespResult
        min_tls_version_resp_result_model['id'] = 'min_tls_version'
        min_tls_version_resp_result_model['value'] = '1.2'
        min_tls_version_resp_result_model['editable'] = True
        min_tls_version_resp_result_model['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a json representation of a MinTlsVersionResp model
        min_tls_version_resp_model_json = {}
        min_tls_version_resp_model_json['result'] = min_tls_version_resp_result_model
        min_tls_version_resp_model_json['success'] = True
        min_tls_version_resp_model_json['errors'] = [['testString']]
        min_tls_version_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of MinTlsVersionResp by calling from_dict on the json representation
        min_tls_version_resp_model = MinTlsVersionResp.from_dict(min_tls_version_resp_model_json)
        assert min_tls_version_resp_model != False

        # Construct a model instance of MinTlsVersionResp by calling from_dict on the json representation
        min_tls_version_resp_model_dict = MinTlsVersionResp.from_dict(min_tls_version_resp_model_json).__dict__
        min_tls_version_resp_model2 = MinTlsVersionResp(**min_tls_version_resp_model_dict)

        # Verify the model instances are equivalent
        assert min_tls_version_resp_model == min_tls_version_resp_model2

        # Convert model instance back to dict and verify no loss of data
        min_tls_version_resp_model_json2 = min_tls_version_resp_model.to_dict()
        assert min_tls_version_resp_model_json2 == min_tls_version_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for MinifyResp
#-----------------------------------------------------------------------------
class TestMinifyResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for MinifyResp
    #--------------------------------------------------------
    def test_minify_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        minify_resp_result_value_model = {} # MinifyRespResultValue
        minify_resp_result_value_model['css'] = 'true'
        minify_resp_result_value_model['html'] = 'true'
        minify_resp_result_value_model['js'] = 'true'

        minify_resp_result_model = {} # MinifyRespResult
        minify_resp_result_model['id'] = 'minify'
        minify_resp_result_model['value'] = minify_resp_result_value_model
        minify_resp_result_model['editable'] = True
        minify_resp_result_model['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a json representation of a MinifyResp model
        minify_resp_model_json = {}
        minify_resp_model_json['result'] = minify_resp_result_model
        minify_resp_model_json['success'] = True
        minify_resp_model_json['errors'] = [['testString']]
        minify_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of MinifyResp by calling from_dict on the json representation
        minify_resp_model = MinifyResp.from_dict(minify_resp_model_json)
        assert minify_resp_model != False

        # Construct a model instance of MinifyResp by calling from_dict on the json representation
        minify_resp_model_dict = MinifyResp.from_dict(minify_resp_model_json).__dict__
        minify_resp_model2 = MinifyResp(**minify_resp_model_dict)

        # Verify the model instances are equivalent
        assert minify_resp_model == minify_resp_model2

        # Convert model instance back to dict and verify no loss of data
        minify_resp_model_json2 = minify_resp_model.to_dict()
        assert minify_resp_model_json2 == minify_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for MobileRedirectResp
#-----------------------------------------------------------------------------
class TestMobileRedirectResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for MobileRedirectResp
    #--------------------------------------------------------
    def test_mobile_redirect_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        mobile_redirect_resp_result_value_model = {} # MobileRedirectRespResultValue
        mobile_redirect_resp_result_value_model['status'] = 'true'
        mobile_redirect_resp_result_value_model['mobile_subdomain'] = 'mobile'
        mobile_redirect_resp_result_value_model['strip_uri'] = False

        mobile_redirect_resp_result_model = {} # MobileRedirectRespResult
        mobile_redirect_resp_result_model['id'] = 'mobile_redirect'
        mobile_redirect_resp_result_model['value'] = mobile_redirect_resp_result_value_model
        mobile_redirect_resp_result_model['editable'] = True
        mobile_redirect_resp_result_model['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a json representation of a MobileRedirectResp model
        mobile_redirect_resp_model_json = {}
        mobile_redirect_resp_model_json['result'] = mobile_redirect_resp_result_model
        mobile_redirect_resp_model_json['success'] = True
        mobile_redirect_resp_model_json['errors'] = [['testString']]
        mobile_redirect_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of MobileRedirectResp by calling from_dict on the json representation
        mobile_redirect_resp_model = MobileRedirectResp.from_dict(mobile_redirect_resp_model_json)
        assert mobile_redirect_resp_model != False

        # Construct a model instance of MobileRedirectResp by calling from_dict on the json representation
        mobile_redirect_resp_model_dict = MobileRedirectResp.from_dict(mobile_redirect_resp_model_json).__dict__
        mobile_redirect_resp_model2 = MobileRedirectResp(**mobile_redirect_resp_model_dict)

        # Verify the model instances are equivalent
        assert mobile_redirect_resp_model == mobile_redirect_resp_model2

        # Convert model instance back to dict and verify no loss of data
        mobile_redirect_resp_model_json2 = mobile_redirect_resp_model.to_dict()
        assert mobile_redirect_resp_model_json2 == mobile_redirect_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for OpportunisticEncryptionResp
#-----------------------------------------------------------------------------
class TestOpportunisticEncryptionResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for OpportunisticEncryptionResp
    #--------------------------------------------------------
    def test_opportunistic_encryption_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        opportunistic_encryption_resp_result_model = {} # OpportunisticEncryptionRespResult
        opportunistic_encryption_resp_result_model['id'] = 'opportunistic_encryption'
        opportunistic_encryption_resp_result_model['value'] = 'off'
        opportunistic_encryption_resp_result_model['editable'] = True
        opportunistic_encryption_resp_result_model['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a json representation of a OpportunisticEncryptionResp model
        opportunistic_encryption_resp_model_json = {}
        opportunistic_encryption_resp_model_json['result'] = opportunistic_encryption_resp_result_model
        opportunistic_encryption_resp_model_json['success'] = True
        opportunistic_encryption_resp_model_json['errors'] = [['testString']]
        opportunistic_encryption_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of OpportunisticEncryptionResp by calling from_dict on the json representation
        opportunistic_encryption_resp_model = OpportunisticEncryptionResp.from_dict(opportunistic_encryption_resp_model_json)
        assert opportunistic_encryption_resp_model != False

        # Construct a model instance of OpportunisticEncryptionResp by calling from_dict on the json representation
        opportunistic_encryption_resp_model_dict = OpportunisticEncryptionResp.from_dict(opportunistic_encryption_resp_model_json).__dict__
        opportunistic_encryption_resp_model2 = OpportunisticEncryptionResp(**opportunistic_encryption_resp_model_dict)

        # Verify the model instances are equivalent
        assert opportunistic_encryption_resp_model == opportunistic_encryption_resp_model2

        # Convert model instance back to dict and verify no loss of data
        opportunistic_encryption_resp_model_json2 = opportunistic_encryption_resp_model.to_dict()
        assert opportunistic_encryption_resp_model_json2 == opportunistic_encryption_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for OriginErrorPagePassThruResp
#-----------------------------------------------------------------------------
class TestOriginErrorPagePassThruResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for OriginErrorPagePassThruResp
    #--------------------------------------------------------
    def test_origin_error_page_pass_thru_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        origin_error_page_pass_thru_resp_result_model = {} # OriginErrorPagePassThruRespResult
        origin_error_page_pass_thru_resp_result_model['id'] = 'origin_error_page_pass_thru'
        origin_error_page_pass_thru_resp_result_model['value'] = 'false'
        origin_error_page_pass_thru_resp_result_model['editable'] = True
        origin_error_page_pass_thru_resp_result_model['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a json representation of a OriginErrorPagePassThruResp model
        origin_error_page_pass_thru_resp_model_json = {}
        origin_error_page_pass_thru_resp_model_json['result'] = origin_error_page_pass_thru_resp_result_model
        origin_error_page_pass_thru_resp_model_json['success'] = True
        origin_error_page_pass_thru_resp_model_json['errors'] = [['testString']]
        origin_error_page_pass_thru_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of OriginErrorPagePassThruResp by calling from_dict on the json representation
        origin_error_page_pass_thru_resp_model = OriginErrorPagePassThruResp.from_dict(origin_error_page_pass_thru_resp_model_json)
        assert origin_error_page_pass_thru_resp_model != False

        # Construct a model instance of OriginErrorPagePassThruResp by calling from_dict on the json representation
        origin_error_page_pass_thru_resp_model_dict = OriginErrorPagePassThruResp.from_dict(origin_error_page_pass_thru_resp_model_json).__dict__
        origin_error_page_pass_thru_resp_model2 = OriginErrorPagePassThruResp(**origin_error_page_pass_thru_resp_model_dict)

        # Verify the model instances are equivalent
        assert origin_error_page_pass_thru_resp_model == origin_error_page_pass_thru_resp_model2

        # Convert model instance back to dict and verify no loss of data
        origin_error_page_pass_thru_resp_model_json2 = origin_error_page_pass_thru_resp_model.to_dict()
        assert origin_error_page_pass_thru_resp_model_json2 == origin_error_page_pass_thru_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for PrefetchPreloadResp
#-----------------------------------------------------------------------------
class TestPrefetchPreloadResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for PrefetchPreloadResp
    #--------------------------------------------------------
    def test_prefetch_preload_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        prefetch_preload_resp_result_model = {} # PrefetchPreloadRespResult
        prefetch_preload_resp_result_model['id'] = 'prefetch_preload'
        prefetch_preload_resp_result_model['value'] = 'false'
        prefetch_preload_resp_result_model['editable'] = True
        prefetch_preload_resp_result_model['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a json representation of a PrefetchPreloadResp model
        prefetch_preload_resp_model_json = {}
        prefetch_preload_resp_model_json['result'] = prefetch_preload_resp_result_model
        prefetch_preload_resp_model_json['success'] = True
        prefetch_preload_resp_model_json['errors'] = [['testString']]
        prefetch_preload_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of PrefetchPreloadResp by calling from_dict on the json representation
        prefetch_preload_resp_model = PrefetchPreloadResp.from_dict(prefetch_preload_resp_model_json)
        assert prefetch_preload_resp_model != False

        # Construct a model instance of PrefetchPreloadResp by calling from_dict on the json representation
        prefetch_preload_resp_model_dict = PrefetchPreloadResp.from_dict(prefetch_preload_resp_model_json).__dict__
        prefetch_preload_resp_model2 = PrefetchPreloadResp(**prefetch_preload_resp_model_dict)

        # Verify the model instances are equivalent
        assert prefetch_preload_resp_model == prefetch_preload_resp_model2

        # Convert model instance back to dict and verify no loss of data
        prefetch_preload_resp_model_json2 = prefetch_preload_resp_model.to_dict()
        assert prefetch_preload_resp_model_json2 == prefetch_preload_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for PseudoIpv4Resp
#-----------------------------------------------------------------------------
class TestPseudoIpv4Resp():

    #--------------------------------------------------------
    # Test serialization/deserialization for PseudoIpv4Resp
    #--------------------------------------------------------
    def test_pseudo_ipv4_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        pseudo_ipv4_resp_result_model = {} # PseudoIpv4RespResult
        pseudo_ipv4_resp_result_model['id'] = 'pseudo_ipv4'
        pseudo_ipv4_resp_result_model['value'] = 'add_header'
        pseudo_ipv4_resp_result_model['editable'] = True
        pseudo_ipv4_resp_result_model['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a json representation of a PseudoIpv4Resp model
        pseudo_ipv4_resp_model_json = {}
        pseudo_ipv4_resp_model_json['result'] = pseudo_ipv4_resp_result_model
        pseudo_ipv4_resp_model_json['success'] = True
        pseudo_ipv4_resp_model_json['errors'] = [['testString']]
        pseudo_ipv4_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of PseudoIpv4Resp by calling from_dict on the json representation
        pseudo_ipv4_resp_model = PseudoIpv4Resp.from_dict(pseudo_ipv4_resp_model_json)
        assert pseudo_ipv4_resp_model != False

        # Construct a model instance of PseudoIpv4Resp by calling from_dict on the json representation
        pseudo_ipv4_resp_model_dict = PseudoIpv4Resp.from_dict(pseudo_ipv4_resp_model_json).__dict__
        pseudo_ipv4_resp_model2 = PseudoIpv4Resp(**pseudo_ipv4_resp_model_dict)

        # Verify the model instances are equivalent
        assert pseudo_ipv4_resp_model == pseudo_ipv4_resp_model2

        # Convert model instance back to dict and verify no loss of data
        pseudo_ipv4_resp_model_json2 = pseudo_ipv4_resp_model.to_dict()
        assert pseudo_ipv4_resp_model_json2 == pseudo_ipv4_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for ResponseBufferingResp
#-----------------------------------------------------------------------------
class TestResponseBufferingResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for ResponseBufferingResp
    #--------------------------------------------------------
    def test_response_buffering_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        response_buffering_resp_result_model = {} # ResponseBufferingRespResult
        response_buffering_resp_result_model['id'] = 'response_buffering'
        response_buffering_resp_result_model['value'] = 'false'
        response_buffering_resp_result_model['editable'] = True
        response_buffering_resp_result_model['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a json representation of a ResponseBufferingResp model
        response_buffering_resp_model_json = {}
        response_buffering_resp_model_json['result'] = response_buffering_resp_result_model
        response_buffering_resp_model_json['success'] = True
        response_buffering_resp_model_json['errors'] = [['testString']]
        response_buffering_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of ResponseBufferingResp by calling from_dict on the json representation
        response_buffering_resp_model = ResponseBufferingResp.from_dict(response_buffering_resp_model_json)
        assert response_buffering_resp_model != False

        # Construct a model instance of ResponseBufferingResp by calling from_dict on the json representation
        response_buffering_resp_model_dict = ResponseBufferingResp.from_dict(response_buffering_resp_model_json).__dict__
        response_buffering_resp_model2 = ResponseBufferingResp(**response_buffering_resp_model_dict)

        # Verify the model instances are equivalent
        assert response_buffering_resp_model == response_buffering_resp_model2

        # Convert model instance back to dict and verify no loss of data
        response_buffering_resp_model_json2 = response_buffering_resp_model.to_dict()
        assert response_buffering_resp_model_json2 == response_buffering_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for ScriptLoadOptimizationResp
#-----------------------------------------------------------------------------
class TestScriptLoadOptimizationResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for ScriptLoadOptimizationResp
    #--------------------------------------------------------
    def test_script_load_optimization_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        script_load_optimization_resp_result_model = {} # ScriptLoadOptimizationRespResult
        script_load_optimization_resp_result_model['id'] = 'script_load_optimization'
        script_load_optimization_resp_result_model['value'] = 'false'
        script_load_optimization_resp_result_model['editable'] = True
        script_load_optimization_resp_result_model['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a json representation of a ScriptLoadOptimizationResp model
        script_load_optimization_resp_model_json = {}
        script_load_optimization_resp_model_json['result'] = script_load_optimization_resp_result_model
        script_load_optimization_resp_model_json['success'] = True
        script_load_optimization_resp_model_json['errors'] = [['testString']]
        script_load_optimization_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of ScriptLoadOptimizationResp by calling from_dict on the json representation
        script_load_optimization_resp_model = ScriptLoadOptimizationResp.from_dict(script_load_optimization_resp_model_json)
        assert script_load_optimization_resp_model != False

        # Construct a model instance of ScriptLoadOptimizationResp by calling from_dict on the json representation
        script_load_optimization_resp_model_dict = ScriptLoadOptimizationResp.from_dict(script_load_optimization_resp_model_json).__dict__
        script_load_optimization_resp_model2 = ScriptLoadOptimizationResp(**script_load_optimization_resp_model_dict)

        # Verify the model instances are equivalent
        assert script_load_optimization_resp_model == script_load_optimization_resp_model2

        # Convert model instance back to dict and verify no loss of data
        script_load_optimization_resp_model_json2 = script_load_optimization_resp_model.to_dict()
        assert script_load_optimization_resp_model_json2 == script_load_optimization_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for SecurityHeaderResp
#-----------------------------------------------------------------------------
class TestSecurityHeaderResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for SecurityHeaderResp
    #--------------------------------------------------------
    def test_security_header_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        security_header_resp_result_value_strict_transport_security_model = {} # SecurityHeaderRespResultValueStrictTransportSecurity
        security_header_resp_result_value_strict_transport_security_model['enabled'] = True
        security_header_resp_result_value_strict_transport_security_model['max_age'] = 86400
        security_header_resp_result_value_strict_transport_security_model['include_subdomains'] = True
        security_header_resp_result_value_strict_transport_security_model['nosniff'] = True

        security_header_resp_result_value_model = {} # SecurityHeaderRespResultValue
        security_header_resp_result_value_model['strict_transport_security'] = security_header_resp_result_value_strict_transport_security_model

        security_header_resp_result_model = {} # SecurityHeaderRespResult
        security_header_resp_result_model['id'] = 'security_header'
        security_header_resp_result_model['value'] = security_header_resp_result_value_model
        security_header_resp_result_model['editable'] = True
        security_header_resp_result_model['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a json representation of a SecurityHeaderResp model
        security_header_resp_model_json = {}
        security_header_resp_model_json['result'] = security_header_resp_result_model
        security_header_resp_model_json['success'] = True
        security_header_resp_model_json['errors'] = [['testString']]
        security_header_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of SecurityHeaderResp by calling from_dict on the json representation
        security_header_resp_model = SecurityHeaderResp.from_dict(security_header_resp_model_json)
        assert security_header_resp_model != False

        # Construct a model instance of SecurityHeaderResp by calling from_dict on the json representation
        security_header_resp_model_dict = SecurityHeaderResp.from_dict(security_header_resp_model_json).__dict__
        security_header_resp_model2 = SecurityHeaderResp(**security_header_resp_model_dict)

        # Verify the model instances are equivalent
        assert security_header_resp_model == security_header_resp_model2

        # Convert model instance back to dict and verify no loss of data
        security_header_resp_model_json2 = security_header_resp_model.to_dict()
        assert security_header_resp_model_json2 == security_header_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for ServerSideExcludeResp
#-----------------------------------------------------------------------------
class TestServerSideExcludeResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for ServerSideExcludeResp
    #--------------------------------------------------------
    def test_server_side_exclude_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        server_side_exclude_resp_result_model = {} # ServerSideExcludeRespResult
        server_side_exclude_resp_result_model['id'] = 'server_side_exclude'
        server_side_exclude_resp_result_model['value'] = 'false'
        server_side_exclude_resp_result_model['editable'] = True
        server_side_exclude_resp_result_model['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a json representation of a ServerSideExcludeResp model
        server_side_exclude_resp_model_json = {}
        server_side_exclude_resp_model_json['result'] = server_side_exclude_resp_result_model
        server_side_exclude_resp_model_json['success'] = True
        server_side_exclude_resp_model_json['errors'] = [['testString']]
        server_side_exclude_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of ServerSideExcludeResp by calling from_dict on the json representation
        server_side_exclude_resp_model = ServerSideExcludeResp.from_dict(server_side_exclude_resp_model_json)
        assert server_side_exclude_resp_model != False

        # Construct a model instance of ServerSideExcludeResp by calling from_dict on the json representation
        server_side_exclude_resp_model_dict = ServerSideExcludeResp.from_dict(server_side_exclude_resp_model_json).__dict__
        server_side_exclude_resp_model2 = ServerSideExcludeResp(**server_side_exclude_resp_model_dict)

        # Verify the model instances are equivalent
        assert server_side_exclude_resp_model == server_side_exclude_resp_model2

        # Convert model instance back to dict and verify no loss of data
        server_side_exclude_resp_model_json2 = server_side_exclude_resp_model.to_dict()
        assert server_side_exclude_resp_model_json2 == server_side_exclude_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for TlsClientAuthResp
#-----------------------------------------------------------------------------
class TestTlsClientAuthResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for TlsClientAuthResp
    #--------------------------------------------------------
    def test_tls_client_auth_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        tls_client_auth_resp_result_model = {} # TlsClientAuthRespResult
        tls_client_auth_resp_result_model['id'] = 'tls_client_auth'
        tls_client_auth_resp_result_model['value'] = 'false'
        tls_client_auth_resp_result_model['editable'] = True
        tls_client_auth_resp_result_model['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a json representation of a TlsClientAuthResp model
        tls_client_auth_resp_model_json = {}
        tls_client_auth_resp_model_json['result'] = tls_client_auth_resp_result_model
        tls_client_auth_resp_model_json['success'] = True
        tls_client_auth_resp_model_json['errors'] = [['testString']]
        tls_client_auth_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of TlsClientAuthResp by calling from_dict on the json representation
        tls_client_auth_resp_model = TlsClientAuthResp.from_dict(tls_client_auth_resp_model_json)
        assert tls_client_auth_resp_model != False

        # Construct a model instance of TlsClientAuthResp by calling from_dict on the json representation
        tls_client_auth_resp_model_dict = TlsClientAuthResp.from_dict(tls_client_auth_resp_model_json).__dict__
        tls_client_auth_resp_model2 = TlsClientAuthResp(**tls_client_auth_resp_model_dict)

        # Verify the model instances are equivalent
        assert tls_client_auth_resp_model == tls_client_auth_resp_model2

        # Convert model instance back to dict and verify no loss of data
        tls_client_auth_resp_model_json2 = tls_client_auth_resp_model.to_dict()
        assert tls_client_auth_resp_model_json2 == tls_client_auth_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for TrueClientIpResp
#-----------------------------------------------------------------------------
class TestTrueClientIpResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for TrueClientIpResp
    #--------------------------------------------------------
    def test_true_client_ip_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        true_client_ip_resp_result_model = {} # TrueClientIpRespResult
        true_client_ip_resp_result_model['id'] = 'true_client_ip_header'
        true_client_ip_resp_result_model['value'] = 'false'
        true_client_ip_resp_result_model['editable'] = True
        true_client_ip_resp_result_model['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a json representation of a TrueClientIpResp model
        true_client_ip_resp_model_json = {}
        true_client_ip_resp_model_json['result'] = true_client_ip_resp_result_model
        true_client_ip_resp_model_json['success'] = True
        true_client_ip_resp_model_json['errors'] = [['testString']]
        true_client_ip_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of TrueClientIpResp by calling from_dict on the json representation
        true_client_ip_resp_model = TrueClientIpResp.from_dict(true_client_ip_resp_model_json)
        assert true_client_ip_resp_model != False

        # Construct a model instance of TrueClientIpResp by calling from_dict on the json representation
        true_client_ip_resp_model_dict = TrueClientIpResp.from_dict(true_client_ip_resp_model_json).__dict__
        true_client_ip_resp_model2 = TrueClientIpResp(**true_client_ip_resp_model_dict)

        # Verify the model instances are equivalent
        assert true_client_ip_resp_model == true_client_ip_resp_model2

        # Convert model instance back to dict and verify no loss of data
        true_client_ip_resp_model_json2 = true_client_ip_resp_model.to_dict()
        assert true_client_ip_resp_model_json2 == true_client_ip_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for WafResp
#-----------------------------------------------------------------------------
class TestWafResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for WafResp
    #--------------------------------------------------------
    def test_waf_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        waf_resp_result_model = {} # WafRespResult
        waf_resp_result_model['id'] = 'waf'
        waf_resp_result_model['value'] = 'false'
        waf_resp_result_model['editable'] = True
        waf_resp_result_model['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a json representation of a WafResp model
        waf_resp_model_json = {}
        waf_resp_model_json['result'] = waf_resp_result_model
        waf_resp_model_json['success'] = True
        waf_resp_model_json['errors'] = [['testString']]
        waf_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of WafResp by calling from_dict on the json representation
        waf_resp_model = WafResp.from_dict(waf_resp_model_json)
        assert waf_resp_model != False

        # Construct a model instance of WafResp by calling from_dict on the json representation
        waf_resp_model_dict = WafResp.from_dict(waf_resp_model_json).__dict__
        waf_resp_model2 = WafResp(**waf_resp_model_dict)

        # Verify the model instances are equivalent
        assert waf_resp_model == waf_resp_model2

        # Convert model instance back to dict and verify no loss of data
        waf_resp_model_json2 = waf_resp_model.to_dict()
        assert waf_resp_model_json2 == waf_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for WebsocketsResp
#-----------------------------------------------------------------------------
class TestWebsocketsResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for WebsocketsResp
    #--------------------------------------------------------
    def test_websockets_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        websockets_resp_result_model = {} # WebsocketsRespResult
        websockets_resp_result_model['id'] = 'websockets'
        websockets_resp_result_model['value'] = 'false'
        websockets_resp_result_model['editable'] = True
        websockets_resp_result_model['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a json representation of a WebsocketsResp model
        websockets_resp_model_json = {}
        websockets_resp_model_json['result'] = websockets_resp_result_model
        websockets_resp_model_json['success'] = True
        websockets_resp_model_json['errors'] = [['testString']]
        websockets_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of WebsocketsResp by calling from_dict on the json representation
        websockets_resp_model = WebsocketsResp.from_dict(websockets_resp_model_json)
        assert websockets_resp_model != False

        # Construct a model instance of WebsocketsResp by calling from_dict on the json representation
        websockets_resp_model_dict = WebsocketsResp.from_dict(websockets_resp_model_json).__dict__
        websockets_resp_model2 = WebsocketsResp(**websockets_resp_model_dict)

        # Verify the model instances are equivalent
        assert websockets_resp_model == websockets_resp_model2

        # Convert model instance back to dict and verify no loss of data
        websockets_resp_model_json2 = websockets_resp_model.to_dict()
        assert websockets_resp_model_json2 == websockets_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for ZonesCnameFlatteningResp
#-----------------------------------------------------------------------------
class TestZonesCnameFlatteningResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for ZonesCnameFlatteningResp
    #--------------------------------------------------------
    def test_zones_cname_flattening_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        cname_flattening_response_model = {} # CnameFlatteningResponse
        cname_flattening_response_model['id'] = 'cname_flattening'
        cname_flattening_response_model['value'] = 'flatten_all'
        cname_flattening_response_model['modified_on'] = '2020-01-28T18:40:40.123456Z'
        cname_flattening_response_model['editable'] = True

        # Construct a json representation of a ZonesCnameFlatteningResp model
        zones_cname_flattening_resp_model_json = {}
        zones_cname_flattening_resp_model_json['success'] = True
        zones_cname_flattening_resp_model_json['errors'] = [['testString']]
        zones_cname_flattening_resp_model_json['messages'] = [['testString']]
        zones_cname_flattening_resp_model_json['result'] = cname_flattening_response_model

        # Construct a model instance of ZonesCnameFlatteningResp by calling from_dict on the json representation
        zones_cname_flattening_resp_model = ZonesCnameFlatteningResp.from_dict(zones_cname_flattening_resp_model_json)
        assert zones_cname_flattening_resp_model != False

        # Construct a model instance of ZonesCnameFlatteningResp by calling from_dict on the json representation
        zones_cname_flattening_resp_model_dict = ZonesCnameFlatteningResp.from_dict(zones_cname_flattening_resp_model_json).__dict__
        zones_cname_flattening_resp_model2 = ZonesCnameFlatteningResp(**zones_cname_flattening_resp_model_dict)

        # Verify the model instances are equivalent
        assert zones_cname_flattening_resp_model == zones_cname_flattening_resp_model2

        # Convert model instance back to dict and verify no loss of data
        zones_cname_flattening_resp_model_json2 = zones_cname_flattening_resp_model.to_dict()
        assert zones_cname_flattening_resp_model_json2 == zones_cname_flattening_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for ZonesDnssecResp
#-----------------------------------------------------------------------------
class TestZonesDnssecResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for ZonesDnssecResp
    #--------------------------------------------------------
    def test_zones_dnssec_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        zones_dnssec_resp_result_model = {} # ZonesDnssecRespResult
        zones_dnssec_resp_result_model['status'] = 'active'
        zones_dnssec_resp_result_model['flags'] = 257
        zones_dnssec_resp_result_model['algorithm'] = '13'
        zones_dnssec_resp_result_model['key_type'] = 'ECDSAP256SHA256'
        zones_dnssec_resp_result_model['digest_type'] = '2'
        zones_dnssec_resp_result_model['digest_algorithm'] = 'SHA256'
        zones_dnssec_resp_result_model['digest'] = '48E939042E82C22542CB377B580DFDC52A361CEFDC72E7F9107E2B6BD9306A45'
        zones_dnssec_resp_result_model['ds'] = 'example.com. 3600 IN DS 16953 13 2 248E939042E82C22542CB377B580DFDC52A361CEFDC72E7F9107E2B6BD9306A45'
        zones_dnssec_resp_result_model['key_tag'] = 42
        zones_dnssec_resp_result_model['public_key'] = 'oXiGYrSTO+LSCJ3mohc8EP+CzF9KxBj8/ydXJ22pKuZP3VAC3/Md/k7xZfz470CoRyZJ6gV6vml07IC3d8xqhA=='

        # Construct a json representation of a ZonesDnssecResp model
        zones_dnssec_resp_model_json = {}
        zones_dnssec_resp_model_json['success'] = True
        zones_dnssec_resp_model_json['errors'] = [['testString']]
        zones_dnssec_resp_model_json['messages'] = [['testString']]
        zones_dnssec_resp_model_json['result'] = zones_dnssec_resp_result_model

        # Construct a model instance of ZonesDnssecResp by calling from_dict on the json representation
        zones_dnssec_resp_model = ZonesDnssecResp.from_dict(zones_dnssec_resp_model_json)
        assert zones_dnssec_resp_model != False

        # Construct a model instance of ZonesDnssecResp by calling from_dict on the json representation
        zones_dnssec_resp_model_dict = ZonesDnssecResp.from_dict(zones_dnssec_resp_model_json).__dict__
        zones_dnssec_resp_model2 = ZonesDnssecResp(**zones_dnssec_resp_model_dict)

        # Verify the model instances are equivalent
        assert zones_dnssec_resp_model == zones_dnssec_resp_model2

        # Convert model instance back to dict and verify no loss of data
        zones_dnssec_resp_model_json2 = zones_dnssec_resp_model.to_dict()
        assert zones_dnssec_resp_model_json2 == zones_dnssec_resp_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
