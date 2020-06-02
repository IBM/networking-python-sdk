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
import responses
from ibm_cloud_networking_services.zones_settings_v1 import ZonesSettingsV1

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
# Start of Service: GetZoneDNSSEC
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_zone_dnssec
#-----------------------------------------------------------------------------
class TestGetZoneDnssec():

    #--------------------------------------------------------
    # get_zone_dnssec()
    #--------------------------------------------------------
    @responses.activate
    def test_get_zone_dnssec_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/dnssec'
        responses.add(responses.GET,
                      url,
                      status=200)

        # Invoke method
        response = service.get_zone_dnssec()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_zone_dnssec_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_zone_dnssec_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/dnssec'
        responses.add(responses.GET,
                      url,
                      status=200)

        # Invoke method
        response = service.get_zone_dnssec()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: GetZoneDNSSEC
##############################################################################

##############################################################################
# Start of Service: UpdateZoneDNSSEC
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for update_zone_dnssec
#-----------------------------------------------------------------------------
class TestUpdateZoneDnssec():

    #--------------------------------------------------------
    # update_zone_dnssec()
    #--------------------------------------------------------
    @responses.activate
    def test_update_zone_dnssec_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/dnssec'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"status": "active", "flags": 257, "algorithm": "13", "key_type": "ECDSAP256SHA256", "digest_type": "2", "digest_algorithm": "SHA256", "digest": "48E939042E82C22542CB377B580DFDC52A361CEFDC72E7F9107E2B6BD9306A45", "ds": "example.com. 3600 IN DS 16953 13 2 248E939042E82C22542CB377B580DFDC52A361CEFDC72E7F9107E2B6BD9306A45", "key_tag": 42, "public_key": "oXiGYrSTO+LSCJ3mohc8EP+CzF9KxBj8/ydXJ22pKuZP3VAC3/Md/k7xZfz470CoRyZJ6gV6vml07IC3d8xqhA=="}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'
        status = 'active'

        # Invoke method
        response = service.update_zone_dnssec(
            accept=accept,
            status=status,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['status'] == status


    #--------------------------------------------------------
    # test_update_zone_dnssec_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_zone_dnssec_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/dnssec'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"status": "active", "flags": 257, "algorithm": "13", "key_type": "ECDSAP256SHA256", "digest_type": "2", "digest_algorithm": "SHA256", "digest": "48E939042E82C22542CB377B580DFDC52A361CEFDC72E7F9107E2B6BD9306A45", "ds": "example.com. 3600 IN DS 16953 13 2 248E939042E82C22542CB377B580DFDC52A361CEFDC72E7F9107E2B6BD9306A45", "key_tag": 42, "public_key": "oXiGYrSTO+LSCJ3mohc8EP+CzF9KxBj8/ydXJ22pKuZP3VAC3/Md/k7xZfz470CoRyZJ6gV6vml07IC3d8xqhA=="}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.update_zone_dnssec()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: UpdateZoneDNSSEC
##############################################################################

##############################################################################
# Start of Service: GetZoneCNAMEFlattening
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_zone_cname_flattening
#-----------------------------------------------------------------------------
class TestGetZoneCnameFlattening():

    #--------------------------------------------------------
    # get_zone_cname_flattening()
    #--------------------------------------------------------
    @responses.activate
    def test_get_zone_cname_flattening_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/cname_flattening'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "cname_flattening", "value": "flatten_all", "modified_on": "2019-01-01T12:00:00", "editable": true}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'

        # Invoke method
        response = service.get_zone_cname_flattening(
            accept=accept
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_zone_cname_flattening_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_zone_cname_flattening_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/cname_flattening'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "cname_flattening", "value": "flatten_all", "modified_on": "2019-01-01T12:00:00", "editable": true}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.get_zone_cname_flattening()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: GetZoneCNAMEFlattening
##############################################################################

##############################################################################
# Start of Service: UpdateZoneCNAMEFlattening
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for update_zone_cname_flattening
#-----------------------------------------------------------------------------
class TestUpdateZoneCnameFlattening():

    #--------------------------------------------------------
    # update_zone_cname_flattening()
    #--------------------------------------------------------
    @responses.activate
    def test_update_zone_cname_flattening_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/cname_flattening'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "cname_flattening", "value": "flatten_all", "modified_on": "2019-01-01T12:00:00", "editable": true}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'
        value = 'flatten_all'

        # Invoke method
        response = service.update_zone_cname_flattening(
            accept=accept,
            value=value,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == value


    #--------------------------------------------------------
    # test_update_zone_cname_flattening_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_zone_cname_flattening_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/cname_flattening'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "cname_flattening", "value": "flatten_all", "modified_on": "2019-01-01T12:00:00", "editable": true}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.update_zone_cname_flattening()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: UpdateZoneCNAMEFlattening
##############################################################################

##############################################################################
# Start of Service: GetOpportunisticEncryptionSetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_opportunistic_encryption
#-----------------------------------------------------------------------------
class TestGetOpportunisticEncryption():

    #--------------------------------------------------------
    # get_opportunistic_encryption()
    #--------------------------------------------------------
    @responses.activate
    def test_get_opportunistic_encryption_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/opportunistic_encryption'
        mock_response = '{"result": {"id": "opportunistic_encryption", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'

        # Invoke method
        response = service.get_opportunistic_encryption(
            accept=accept
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_opportunistic_encryption_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_opportunistic_encryption_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/opportunistic_encryption'
        mock_response = '{"result": {"id": "opportunistic_encryption", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.get_opportunistic_encryption()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: GetOpportunisticEncryptionSetting
##############################################################################

##############################################################################
# Start of Service: UpdateOpportunisticEncryptionSetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for update_opportunistic_encryption
#-----------------------------------------------------------------------------
class TestUpdateOpportunisticEncryption():

    #--------------------------------------------------------
    # update_opportunistic_encryption()
    #--------------------------------------------------------
    @responses.activate
    def test_update_opportunistic_encryption_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/opportunistic_encryption'
        mock_response = '{"result": {"id": "opportunistic_encryption", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'
        value = 'false'

        # Invoke method
        response = service.update_opportunistic_encryption(
            accept=accept,
            value=value,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == value


    #--------------------------------------------------------
    # test_update_opportunistic_encryption_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_opportunistic_encryption_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/opportunistic_encryption'
        mock_response = '{"result": {"id": "opportunistic_encryption", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.update_opportunistic_encryption()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: UpdateOpportunisticEncryptionSetting
##############################################################################

##############################################################################
# Start of Service: GetChallengeTTLSetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_challenge_ttl
#-----------------------------------------------------------------------------
class TestGetChallengeTtl():

    #--------------------------------------------------------
    # get_challenge_ttl()
    #--------------------------------------------------------
    @responses.activate
    def test_get_challenge_ttl_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/challenge_ttl'
        mock_response = '{"result": {"id": "challenge_ttl", "value": 1800, "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'

        # Invoke method
        response = service.get_challenge_ttl(
            accept=accept
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_challenge_ttl_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_challenge_ttl_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/challenge_ttl'
        mock_response = '{"result": {"id": "challenge_ttl", "value": 1800, "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.get_challenge_ttl()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: GetChallengeTTLSetting
##############################################################################

##############################################################################
# Start of Service: UpdateChallengeTTLSetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for update_challenge_ttl
#-----------------------------------------------------------------------------
class TestUpdateChallengeTtl():

    #--------------------------------------------------------
    # update_challenge_ttl()
    #--------------------------------------------------------
    @responses.activate
    def test_update_challenge_ttl_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/challenge_ttl'
        mock_response = '{"result": {"id": "challenge_ttl", "value": 1800, "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'
        value = 1800

        # Invoke method
        response = service.update_challenge_ttl(
            accept=accept,
            value=value,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == value


    #--------------------------------------------------------
    # test_update_challenge_ttl_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_challenge_ttl_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/challenge_ttl'
        mock_response = '{"result": {"id": "challenge_ttl", "value": 1800, "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.update_challenge_ttl()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: UpdateChallengeTTLSetting
##############################################################################

##############################################################################
# Start of Service: GetAutomaticHttpsRewritesSetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_automatic_https_rewrites
#-----------------------------------------------------------------------------
class TestGetAutomaticHttpsRewrites():

    #--------------------------------------------------------
    # get_automatic_https_rewrites()
    #--------------------------------------------------------
    @responses.activate
    def test_get_automatic_https_rewrites_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/automatic_https_rewrites'
        mock_response = '{"result": {"id": "automatic_https_rewrites", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'

        # Invoke method
        response = service.get_automatic_https_rewrites(
            accept=accept
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_automatic_https_rewrites_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_automatic_https_rewrites_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/automatic_https_rewrites'
        mock_response = '{"result": {"id": "automatic_https_rewrites", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.get_automatic_https_rewrites()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: GetAutomaticHttpsRewritesSetting
##############################################################################

##############################################################################
# Start of Service: UpdateAutomaticHttpsRewritesSetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for update_automatic_https_rewrites
#-----------------------------------------------------------------------------
class TestUpdateAutomaticHttpsRewrites():

    #--------------------------------------------------------
    # update_automatic_https_rewrites()
    #--------------------------------------------------------
    @responses.activate
    def test_update_automatic_https_rewrites_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/automatic_https_rewrites'
        mock_response = '{"result": {"id": "automatic_https_rewrites", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'
        value = 'false'

        # Invoke method
        response = service.update_automatic_https_rewrites(
            accept=accept,
            value=value,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == value


    #--------------------------------------------------------
    # test_update_automatic_https_rewrites_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_automatic_https_rewrites_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/automatic_https_rewrites'
        mock_response = '{"result": {"id": "automatic_https_rewrites", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.update_automatic_https_rewrites()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: UpdateAutomaticHttpsRewritesSetting
##############################################################################

##############################################################################
# Start of Service: GetTrueClientIPSetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_ture_client_ip
#-----------------------------------------------------------------------------
class TestGetTureClientIp():

    #--------------------------------------------------------
    # get_ture_client_ip()
    #--------------------------------------------------------
    @responses.activate
    def test_get_ture_client_ip_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/true_client_ip_header'
        mock_response = '{"result": {"id": "true_client_ip_header", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'

        # Invoke method
        response = service.get_ture_client_ip(
            accept=accept
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_ture_client_ip_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_ture_client_ip_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/true_client_ip_header'
        mock_response = '{"result": {"id": "true_client_ip_header", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.get_ture_client_ip()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: GetTrueClientIPSetting
##############################################################################

##############################################################################
# Start of Service: UpdateTrueClientIPSetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for update_true_client_ip
#-----------------------------------------------------------------------------
class TestUpdateTrueClientIp():

    #--------------------------------------------------------
    # update_true_client_ip()
    #--------------------------------------------------------
    @responses.activate
    def test_update_true_client_ip_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/true_client_ip_header'
        mock_response = '{"result": {"id": "true_client_ip_header", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'
        value = 'true'

        # Invoke method
        response = service.update_true_client_ip(
            accept=accept,
            value=value,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == value


    #--------------------------------------------------------
    # test_update_true_client_ip_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_true_client_ip_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/true_client_ip_header'
        mock_response = '{"result": {"id": "true_client_ip_header", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.update_true_client_ip()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: UpdateTrueClientIPSetting
##############################################################################

##############################################################################
# Start of Service: GetAlwaysUseHttpsSetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_always_use_https
#-----------------------------------------------------------------------------
class TestGetAlwaysUseHttps():

    #--------------------------------------------------------
    # get_always_use_https()
    #--------------------------------------------------------
    @responses.activate
    def test_get_always_use_https_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/always_use_https'
        mock_response = '{"result": {"id": "always_use_https", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'

        # Invoke method
        response = service.get_always_use_https(
            accept=accept
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_always_use_https_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_always_use_https_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/always_use_https'
        mock_response = '{"result": {"id": "always_use_https", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.get_always_use_https()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: GetAlwaysUseHttpsSetting
##############################################################################

##############################################################################
# Start of Service: UpdateAlwaysUseHttpsSetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for update_always_use_https
#-----------------------------------------------------------------------------
class TestUpdateAlwaysUseHttps():

    #--------------------------------------------------------
    # update_always_use_https()
    #--------------------------------------------------------
    @responses.activate
    def test_update_always_use_https_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/always_use_https'
        mock_response = '{"result": {"id": "always_use_https", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'
        value = 'true'

        # Invoke method
        response = service.update_always_use_https(
            accept=accept,
            value=value,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == value


    #--------------------------------------------------------
    # test_update_always_use_https_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_always_use_https_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/always_use_https'
        mock_response = '{"result": {"id": "always_use_https", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.update_always_use_https()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: UpdateAlwaysUseHttpsSetting
##############################################################################

##############################################################################
# Start of Service: GetImageSizeOptimizationSetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_image_size_optimization
#-----------------------------------------------------------------------------
class TestGetImageSizeOptimization():

    #--------------------------------------------------------
    # get_image_size_optimization()
    #--------------------------------------------------------
    @responses.activate
    def test_get_image_size_optimization_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/image_size_optimization'
        mock_response = '{"result": {"id": "image_size_optimization", "value": "lossless", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'

        # Invoke method
        response = service.get_image_size_optimization(
            accept=accept
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_image_size_optimization_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_image_size_optimization_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/image_size_optimization'
        mock_response = '{"result": {"id": "image_size_optimization", "value": "lossless", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.get_image_size_optimization()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: GetImageSizeOptimizationSetting
##############################################################################

##############################################################################
# Start of Service: UpdateImageSizeOptimizationSetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for update_image_size_optimization
#-----------------------------------------------------------------------------
class TestUpdateImageSizeOptimization():

    #--------------------------------------------------------
    # update_image_size_optimization()
    #--------------------------------------------------------
    @responses.activate
    def test_update_image_size_optimization_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/image_size_optimization'
        mock_response = '{"result": {"id": "image_size_optimization", "value": "lossless", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'
        value = 'lossless'

        # Invoke method
        response = service.update_image_size_optimization(
            accept=accept,
            value=value,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == value


    #--------------------------------------------------------
    # test_update_image_size_optimization_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_image_size_optimization_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/image_size_optimization'
        mock_response = '{"result": {"id": "image_size_optimization", "value": "lossless", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.update_image_size_optimization()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: UpdateImageSizeOptimizationSetting
##############################################################################

##############################################################################
# Start of Service: GetScriptLoadOptimizationSetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_script_load_optimization
#-----------------------------------------------------------------------------
class TestGetScriptLoadOptimization():

    #--------------------------------------------------------
    # get_script_load_optimization()
    #--------------------------------------------------------
    @responses.activate
    def test_get_script_load_optimization_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/script_load_optimization'
        mock_response = '{"result": {"id": "script_load_optimization", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'

        # Invoke method
        response = service.get_script_load_optimization(
            accept=accept
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_script_load_optimization_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_script_load_optimization_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/script_load_optimization'
        mock_response = '{"result": {"id": "script_load_optimization", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.get_script_load_optimization()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: GetScriptLoadOptimizationSetting
##############################################################################

##############################################################################
# Start of Service: UpdateScriptLoadOptimizationSetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for update_script_load_optimization
#-----------------------------------------------------------------------------
class TestUpdateScriptLoadOptimization():

    #--------------------------------------------------------
    # update_script_load_optimization()
    #--------------------------------------------------------
    @responses.activate
    def test_update_script_load_optimization_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/script_load_optimization'
        mock_response = '{"result": {"id": "script_load_optimization", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'
        value = 'true'

        # Invoke method
        response = service.update_script_load_optimization(
            accept=accept,
            value=value,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == value


    #--------------------------------------------------------
    # test_update_script_load_optimization_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_script_load_optimization_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/script_load_optimization'
        mock_response = '{"result": {"id": "script_load_optimization", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.update_script_load_optimization()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: UpdateScriptLoadOptimizationSetting
##############################################################################

##############################################################################
# Start of Service: GetImageLoadOptimizationnSetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_image_load_optimization
#-----------------------------------------------------------------------------
class TestGetImageLoadOptimization():

    #--------------------------------------------------------
    # get_image_load_optimization()
    #--------------------------------------------------------
    @responses.activate
    def test_get_image_load_optimization_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/image_load_optimization'
        mock_response = '{"result": {"id": "image_load_optimization", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'

        # Invoke method
        response = service.get_image_load_optimization(
            accept=accept
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_image_load_optimization_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_image_load_optimization_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/image_load_optimization'
        mock_response = '{"result": {"id": "image_load_optimization", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.get_image_load_optimization()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: GetImageLoadOptimizationnSetting
##############################################################################

##############################################################################
# Start of Service: UpdateImageLoadOptimizationnSetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for update_image_load_optimization
#-----------------------------------------------------------------------------
class TestUpdateImageLoadOptimization():

    #--------------------------------------------------------
    # update_image_load_optimization()
    #--------------------------------------------------------
    @responses.activate
    def test_update_image_load_optimization_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/image_load_optimization'
        mock_response = '{"result": {"id": "image_load_optimization", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'
        value = 'true'

        # Invoke method
        response = service.update_image_load_optimization(
            accept=accept,
            value=value,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == value


    #--------------------------------------------------------
    # test_update_image_load_optimization_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_image_load_optimization_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/image_load_optimization'
        mock_response = '{"result": {"id": "image_load_optimization", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.update_image_load_optimization()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: UpdateImageLoadOptimizationnSetting
##############################################################################

##############################################################################
# Start of Service: GetMinifySetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_minify
#-----------------------------------------------------------------------------
class TestGetMinify():

    #--------------------------------------------------------
    # get_minify()
    #--------------------------------------------------------
    @responses.activate
    def test_get_minify_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/minify'
        mock_response = '{"result": {"id": "minify", "value": {"css": "true", "html": "true", "js": "true"}, "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'

        # Invoke method
        response = service.get_minify(
            accept=accept
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_minify_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_minify_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/minify'
        mock_response = '{"result": {"id": "minify", "value": {"css": "true", "html": "true", "js": "true"}, "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.get_minify()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: GetMinifySetting
##############################################################################

##############################################################################
# Start of Service: UpdateMinifySetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for update_minify
#-----------------------------------------------------------------------------
class TestUpdateMinify():

    #--------------------------------------------------------
    # update_minify()
    #--------------------------------------------------------
    @responses.activate
    def test_update_minify_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/minify'
        mock_response = '{"result": {"id": "minify", "value": {"css": "true", "html": "true", "js": "true"}, "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'
        css = 'false'
        html = 'false'
        js = 'false'

        # Invoke method
        response = service.update_minify(
            accept=accept,
            css=css,
            html=html,
            js=js,
        )
        print(response)
        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body.get("value")['css'] == css
        assert req_body.get("value")['html'] == html
        assert req_body.get("value")['js'] == js


    #--------------------------------------------------------
    # test_update_minify_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_minify_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/minify'
        mock_response = '{"result": {"id": "minify", "value": {"css": "true", "html": "true", "js": "true"}, "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.update_minify()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: UpdateMinifySetting
##############################################################################

##############################################################################
# Start of Service: GetMinimumTLSVersionSetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_min_tls_version
#-----------------------------------------------------------------------------
class TestGetMinTlsVersion():

    #--------------------------------------------------------
    # get_min_tls_version()
    #--------------------------------------------------------
    @responses.activate
    def test_get_min_tls_version_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/min_tls_version'
        mock_response = '{"result": {"id": "min_tls_version", "value": "1.2", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'

        # Invoke method
        response = service.get_min_tls_version(
            accept=accept
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_min_tls_version_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_min_tls_version_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/min_tls_version'
        mock_response = '{"result": {"id": "min_tls_version", "value": "1.2", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.get_min_tls_version()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: GetMinimumTLSVersionSetting
##############################################################################

##############################################################################
# Start of Service: UpdateMinimumTLSVersionSetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for update_min_tls_version
#-----------------------------------------------------------------------------
class TestUpdateMinTlsVersion():

    #--------------------------------------------------------
    # update_min_tls_version()
    #--------------------------------------------------------
    @responses.activate
    def test_update_min_tls_version_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/min_tls_version'
        mock_response = '{"result": {"id": "min_tls_version", "value": "1.2", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'
        value = '1.2'

        # Invoke method
        response = service.update_min_tls_version(
            accept=accept,
            value=value,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == value


    #--------------------------------------------------------
    # test_update_min_tls_version_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_min_tls_version_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/min_tls_version'
        mock_response = '{"result": {"id": "min_tls_version", "value": "1.2", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.update_min_tls_version()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: UpdateMinimumTLSVersionSetting
##############################################################################

##############################################################################
# Start of Service: GetIPGeolocationSetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_ip_geolocation
#-----------------------------------------------------------------------------
class TestGetIpGeolocation():

    #--------------------------------------------------------
    # get_ip_geolocation()
    #--------------------------------------------------------
    @responses.activate
    def test_get_ip_geolocation_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/ip_geolocation'
        mock_response = '{"result": {"id": "ip_geolocation", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'

        # Invoke method
        response = service.get_ip_geolocation(
            accept=accept
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_ip_geolocation_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_ip_geolocation_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/ip_geolocation'
        mock_response = '{"result": {"id": "ip_geolocation", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.get_ip_geolocation()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: GetIPGeolocationSetting
##############################################################################

##############################################################################
# Start of Service: UpdateIPGeolocationSetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for update_ip_geolocation
#-----------------------------------------------------------------------------
class TestUpdateIpGeolocation():

    #--------------------------------------------------------
    # update_ip_geolocation()
    #--------------------------------------------------------
    @responses.activate
    def test_update_ip_geolocation_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/ip_geolocation'
        mock_response = '{"result": {"id": "ip_geolocation", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'
        value = 'true'

        # Invoke method
        response = service.update_ip_geolocation(
            accept=accept,
            value=value,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == value


    #--------------------------------------------------------
    # test_update_ip_geolocation_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_ip_geolocation_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/ip_geolocation'
        mock_response = '{"result": {"id": "ip_geolocation", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.update_ip_geolocation()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: UpdateIPGeolocationSetting
##############################################################################

##############################################################################
# Start of Service: GetServerSideExcludeSetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_server_side_exclude
#-----------------------------------------------------------------------------
class TestGetServerSideExclude():

    #--------------------------------------------------------
    # get_server_side_exclude()
    #--------------------------------------------------------
    @responses.activate
    def test_get_server_side_exclude_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/server_side_exclude'
        mock_response = '{"result": {"id": "server_side_exclude", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'

        # Invoke method
        response = service.get_server_side_exclude(
            accept=accept
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_server_side_exclude_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_server_side_exclude_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/server_side_exclude'
        mock_response = '{"result": {"id": "server_side_exclude", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.get_server_side_exclude()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: GetServerSideExcludeSetting
##############################################################################

##############################################################################
# Start of Service: UpdateServerSideExcludeSetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for update_server_side_exclude
#-----------------------------------------------------------------------------
class TestUpdateServerSideExclude():

    #--------------------------------------------------------
    # update_server_side_exclude()
    #--------------------------------------------------------
    @responses.activate
    def test_update_server_side_exclude_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/server_side_exclude'
        mock_response = '{"result": {"id": "server_side_exclude", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'
        value = 'true'

        # Invoke method
        response = service.update_server_side_exclude(
            accept=accept,
            value=value,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == value


    #--------------------------------------------------------
    # test_update_server_side_exclude_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_server_side_exclude_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/server_side_exclude'
        mock_response = '{"result": {"id": "server_side_exclude", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.update_server_side_exclude()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: UpdateServerSideExcludeSetting
##############################################################################

##############################################################################
# Start of Service: GetHTTPStrictTransportSecuritySetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_security_header
#-----------------------------------------------------------------------------
class TestGetSecurityHeader():

    #--------------------------------------------------------
    # get_security_header()
    #--------------------------------------------------------
    @responses.activate
    def test_get_security_header_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/security_header'
        mock_response = '{"result": {"id": "security_header", "value": {"strict_transport_security": {"enabled": true, "max_age": 86400, "include_subdomains": true, "nosniff": true}}, "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'

        # Invoke method
        response = service.get_security_header(
            accept=accept
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_security_header_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_security_header_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/security_header'
        mock_response = '{"result": {"id": "security_header", "value": {"strict_transport_security": {"enabled": true, "max_age": 86400, "include_subdomains": true, "nosniff": true}}, "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.get_security_header()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: GetHTTPStrictTransportSecuritySetting
##############################################################################

##############################################################################
# Start of Service: UpdateHTTPStrictTransportSecuritySetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for update_security_header
#-----------------------------------------------------------------------------
class TestUpdateSecurityHeader():

    #--------------------------------------------------------
    # update_security_header()
    #--------------------------------------------------------
    @responses.activate
    def test_update_security_header_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/security_header'
        mock_response = '{"result": {"id": "security_header", "value": {"strict_transport_security": {"enabled": true, "max_age": 86400, "include_subdomains": true, "nosniff": true}}, "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Construct a dict representation of a SecurityHeaderSettingValueStrictTransportSecurity model
        security_header_setting_value_strict_transport_security_model =  {
            'enabled': True,
            'max_age': 86400,
            'include_subdomains': True,
            'nosniff': True
        }
        # Construct a dict representation of a SecurityHeaderSettingValue model
        security_header_setting_value_model =  {
            'strict_transport_security': security_header_setting_value_strict_transport_security_model
        }

        # Set up parameter values
        accept = 'testString'
        value = security_header_setting_value_model

        # Invoke method
        response = service.update_security_header(
            accept=accept,
            value=value,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == value


    #--------------------------------------------------------
    # test_update_security_header_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_security_header_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/security_header'
        mock_response = '{"result": {"id": "security_header", "value": {"strict_transport_security": {"enabled": true, "max_age": 86400, "include_subdomains": true, "nosniff": true}}, "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.update_security_header()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: UpdateHTTPStrictTransportSecuritySetting
##############################################################################

##############################################################################
# Start of Service: GetMobileRedirectSetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_mobile_redirect
#-----------------------------------------------------------------------------
class TestGetMobileRedirect():

    #--------------------------------------------------------
    # get_mobile_redirect()
    #--------------------------------------------------------
    @responses.activate
    def test_get_mobile_redirect_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/mobile_redirect'
        mock_response = '{"result": {"id": "mobile_redirect", "value": {"status": "true", "mobile_subdomain": "m", "strip_uri": false}, "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'

        # Invoke method
        response = service.get_mobile_redirect(
            accept=accept
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_mobile_redirect_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_mobile_redirect_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/mobile_redirect'
        mock_response = '{"result": {"id": "mobile_redirect", "value": {"status": "true", "mobile_subdomain": "m", "strip_uri": false}, "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.get_mobile_redirect()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: GetMobileRedirectSetting
##############################################################################

##############################################################################
# Start of Service: UpdateMobileRedirectSetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for update_mobile_redirect
#-----------------------------------------------------------------------------
class TestUpdateMobileRedirect():

    #--------------------------------------------------------
    # update_mobile_redirect()
    #--------------------------------------------------------
    @responses.activate
    def test_update_mobile_redirect_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/mobile_redirect'
        mock_response = '{"result": {"id": "mobile_redirect", "value": {"status": "true", "mobile_subdomain": "m", "strip_uri": false}, "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Construct a dict representation of a MobileRedirecSettingValue model
        mobile_redirec_setting_value_model =  {
            'status': 'true',
            'mobile_subdomain': 'm',
            'strip_uri': False
        }

        # Set up parameter values
        accept = 'testString'
        value = mobile_redirec_setting_value_model

        # Invoke method
        response = service.update_mobile_redirect(
            accept=accept,
            value=value,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == value


    #--------------------------------------------------------
    # test_update_mobile_redirect_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_mobile_redirect_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/mobile_redirect'
        mock_response = '{"result": {"id": "mobile_redirect", "value": {"status": "true", "mobile_subdomain": "m", "strip_uri": false}, "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.update_mobile_redirect()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: UpdateMobileRedirectSetting
##############################################################################

##############################################################################
# Start of Service: GetPrefetchURLsFromHeaderSetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_prefetch_preload
#-----------------------------------------------------------------------------
class TestGetPrefetchPreload():

    #--------------------------------------------------------
    # get_prefetch_preload()
    #--------------------------------------------------------
    @responses.activate
    def test_get_prefetch_preload_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/prefetch_preload'
        mock_response = '{"result": {"id": "prefetch_preload", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'

        # Invoke method
        response = service.get_prefetch_preload(
            accept=accept
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_prefetch_preload_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_prefetch_preload_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/prefetch_preload'
        mock_response = '{"result": {"id": "prefetch_preload", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.get_prefetch_preload()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: GetPrefetchURLsFromHeaderSetting
##############################################################################

##############################################################################
# Start of Service: UpdatePrefetchURLsFromHeaderSetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for update_prefetch_preload
#-----------------------------------------------------------------------------
class TestUpdatePrefetchPreload():

    #--------------------------------------------------------
    # update_prefetch_preload()
    #--------------------------------------------------------
    @responses.activate
    def test_update_prefetch_preload_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/prefetch_preload'
        mock_response = '{"result": {"id": "prefetch_preload", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'
        value = 'true'

        # Invoke method
        response = service.update_prefetch_preload(
            accept=accept,
            value=value,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == value


    #--------------------------------------------------------
    # test_update_prefetch_preload_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_prefetch_preload_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/prefetch_preload'
        mock_response = '{"result": {"id": "prefetch_preload", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.update_prefetch_preload()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: UpdatePrefetchURLsFromHeaderSetting
##############################################################################

##############################################################################
# Start of Service: GetHttp2Setting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_http2
#-----------------------------------------------------------------------------
class TestGetHttp2():

    #--------------------------------------------------------
    # get_http2()
    #--------------------------------------------------------
    @responses.activate
    def test_get_http2_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/http2'
        mock_response = '{"result": {"id": "http2", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'

        # Invoke method
        response = service.get_http2(
            accept=accept
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_http2_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_http2_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/http2'
        mock_response = '{"result": {"id": "http2", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.get_http2()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: GetHttp2Setting
##############################################################################

##############################################################################
# Start of Service: UpdateHttp2Setting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for update_http2
#-----------------------------------------------------------------------------
class TestUpdateHttp2():

    #--------------------------------------------------------
    # update_http2()
    #--------------------------------------------------------
    @responses.activate
    def test_update_http2_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/http2'
        mock_response = '{"result": {"id": "http2", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'
        value = 'true'

        # Invoke method
        response = service.update_http2(
            accept=accept,
            value=value,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == value


    #--------------------------------------------------------
    # test_update_http2_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_http2_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/http2'
        mock_response = '{"result": {"id": "http2", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.update_http2()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: UpdateHttp2Setting
##############################################################################

##############################################################################
# Start of Service: GetIPv6CompatibilitySetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_ipv6
#-----------------------------------------------------------------------------
class TestGetIpv6():

    #--------------------------------------------------------
    # get_ipv6()
    #--------------------------------------------------------
    @responses.activate
    def test_get_ipv6_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/ipv6'
        mock_response = '{"result": {"id": "ipv6", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'

        # Invoke method
        response = service.get_ipv6(
            accept=accept
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_ipv6_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_ipv6_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/ipv6'
        mock_response = '{"result": {"id": "ipv6", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.get_ipv6()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: GetIPv6CompatibilitySetting
##############################################################################

##############################################################################
# Start of Service: UpdateIPv6CompatibilitySetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for update_ipv6
#-----------------------------------------------------------------------------
class TestUpdateIpv6():

    #--------------------------------------------------------
    # update_ipv6()
    #--------------------------------------------------------
    @responses.activate
    def test_update_ipv6_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/ipv6'
        mock_response = '{"result": {"id": "ipv6", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'
        value = 'true'

        # Invoke method
        response = service.update_ipv6(
            accept=accept,
            value=value,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == value


    #--------------------------------------------------------
    # test_update_ipv6_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_ipv6_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/ipv6'
        mock_response = '{"result": {"id": "ipv6", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.update_ipv6()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: UpdateIPv6CompatibilitySetting
##############################################################################

##############################################################################
# Start of Service: GetWebSocketsSetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_web_sockets
#-----------------------------------------------------------------------------
class TestGetWebSockets():

    #--------------------------------------------------------
    # get_web_sockets()
    #--------------------------------------------------------
    @responses.activate
    def test_get_web_sockets_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/websockets'
        mock_response = '{"result": {"id": "websockets", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'

        # Invoke method
        response = service.get_web_sockets(
            accept=accept
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_web_sockets_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_web_sockets_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/websockets'
        mock_response = '{"result": {"id": "websockets", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.get_web_sockets()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: GetWebSocketsSetting
##############################################################################

##############################################################################
# Start of Service: UpdateWebSocketsSetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for update_web_sockets
#-----------------------------------------------------------------------------
class TestUpdateWebSockets():

    #--------------------------------------------------------
    # update_web_sockets()
    #--------------------------------------------------------
    @responses.activate
    def test_update_web_sockets_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/websockets'
        mock_response = '{"result": {"id": "websockets", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'
        value = 'true'

        # Invoke method
        response = service.update_web_sockets(
            accept=accept,
            value=value,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == value


    #--------------------------------------------------------
    # test_update_web_sockets_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_web_sockets_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/websockets'
        mock_response = '{"result": {"id": "websockets", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.update_web_sockets()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: UpdateWebSocketsSetting
##############################################################################

##############################################################################
# Start of Service: GetPseudoIPv4Setting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_pseudo_ipv4
#-----------------------------------------------------------------------------
class TestGetPseudoIpv4():

    #--------------------------------------------------------
    # get_pseudo_ipv4()
    #--------------------------------------------------------
    @responses.activate
    def test_get_pseudo_ipv4_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/pseudo_ipv4'
        mock_response = '{"result": {"id": "pseudo_ipv4", "value": "add_header", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'

        # Invoke method
        response = service.get_pseudo_ipv4(
            accept=accept
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_pseudo_ipv4_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_pseudo_ipv4_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/pseudo_ipv4'
        mock_response = '{"result": {"id": "pseudo_ipv4", "value": "add_header", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.get_pseudo_ipv4()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: GetPseudoIPv4Setting
##############################################################################

##############################################################################
# Start of Service: UpdatePseudoIPv4Setting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for update_pseudo_ipv4
#-----------------------------------------------------------------------------
class TestUpdatePseudoIpv4():

    #--------------------------------------------------------
    # update_pseudo_ipv4()
    #--------------------------------------------------------
    @responses.activate
    def test_update_pseudo_ipv4_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/pseudo_ipv4'
        mock_response = '{"result": {"id": "pseudo_ipv4", "value": "add_header", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'
        value = 'add_header'

        # Invoke method
        response = service.update_pseudo_ipv4(
            accept=accept,
            value=value,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == value


    #--------------------------------------------------------
    # test_update_pseudo_ipv4_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_pseudo_ipv4_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/pseudo_ipv4'
        mock_response = '{"result": {"id": "pseudo_ipv4", "value": "add_header", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.update_pseudo_ipv4()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: UpdatePseudoIPv4Setting
##############################################################################

##############################################################################
# Start of Service: GetResponseBufferingSetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_response_buffering
#-----------------------------------------------------------------------------
class TestGetResponseBuffering():

    #--------------------------------------------------------
    # get_response_buffering()
    #--------------------------------------------------------
    @responses.activate
    def test_get_response_buffering_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/response_buffering'
        mock_response = '{"result": {"id": "response_buffering", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'

        # Invoke method
        response = service.get_response_buffering(
            accept=accept
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_response_buffering_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_response_buffering_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/response_buffering'
        mock_response = '{"result": {"id": "response_buffering", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.get_response_buffering()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: GetResponseBufferingSetting
##############################################################################

##############################################################################
# Start of Service: UpdateResponseBufferingSetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for update_response_buffering
#-----------------------------------------------------------------------------
class TestUpdateResponseBuffering():

    #--------------------------------------------------------
    # update_response_buffering()
    #--------------------------------------------------------
    @responses.activate
    def test_update_response_buffering_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/response_buffering'
        mock_response = '{"result": {"id": "response_buffering", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'
        value = 'true'

        # Invoke method
        response = service.update_response_buffering(
            accept=accept,
            value=value,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == value


    #--------------------------------------------------------
    # test_update_response_buffering_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_response_buffering_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/response_buffering'
        mock_response = '{"result": {"id": "response_buffering", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.update_response_buffering()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: UpdateResponseBufferingSetting
##############################################################################

##############################################################################
# Start of Service: GetHotlinkProtectionSetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_hotlink_protection
#-----------------------------------------------------------------------------
class TestGetHotlinkProtection():

    #--------------------------------------------------------
    # get_hotlink_protection()
    #--------------------------------------------------------
    @responses.activate
    def test_get_hotlink_protection_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/hotlink_protection'
        mock_response = '{"result": {"id": "hotlink_protection", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'

        # Invoke method
        response = service.get_hotlink_protection(
            accept=accept
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_hotlink_protection_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_hotlink_protection_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/hotlink_protection'
        mock_response = '{"result": {"id": "hotlink_protection", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.get_hotlink_protection()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: GetHotlinkProtectionSetting
##############################################################################

##############################################################################
# Start of Service: UpdateHotlinkProtectionSetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for update_hotlink_protection
#-----------------------------------------------------------------------------
class TestUpdateHotlinkProtection():

    #--------------------------------------------------------
    # update_hotlink_protection()
    #--------------------------------------------------------
    @responses.activate
    def test_update_hotlink_protection_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/hotlink_protection'
        mock_response = '{"result": {"id": "hotlink_protection", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'
        value = 'true'

        # Invoke method
        response = service.update_hotlink_protection(
            accept=accept,
            value=value,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == value


    #--------------------------------------------------------
    # test_update_hotlink_protection_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_hotlink_protection_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/hotlink_protection'
        mock_response = '{"result": {"id": "hotlink_protection", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.update_hotlink_protection()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: UpdateHotlinkProtectionSetting
##############################################################################

##############################################################################
# Start of Service: GetMaximumUploadSizeSetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_max_upload
#-----------------------------------------------------------------------------
class TestGetMaxUpload():

    #--------------------------------------------------------
    # get_max_upload()
    #--------------------------------------------------------
    @responses.activate
    def test_get_max_upload_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/max_upload'
        mock_response = '{"result": {"id": "max_upload", "value": 300, "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'

        # Invoke method
        response = service.get_max_upload(
            accept=accept
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_max_upload_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_max_upload_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/max_upload'
        mock_response = '{"result": {"id": "max_upload", "value": 300, "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.get_max_upload()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: GetMaximumUploadSizeSetting
##############################################################################

##############################################################################
# Start of Service: UpdateMaximumUploadSizeSetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for update_max_upload
#-----------------------------------------------------------------------------
class TestUpdateMaxUpload():

    #--------------------------------------------------------
    # update_max_upload()
    #--------------------------------------------------------
    @responses.activate
    def test_update_max_upload_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/max_upload'
        mock_response = '{"result": {"id": "max_upload", "value": 300, "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'
        value = 300

        # Invoke method
        response = service.update_max_upload(
            accept=accept,
            value=value,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == value


    #--------------------------------------------------------
    # test_update_max_upload_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_max_upload_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/max_upload'
        mock_response = '{"result": {"id": "max_upload", "value": 300, "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.update_max_upload()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: UpdateMaximumUploadSizeSetting
##############################################################################

##############################################################################
# Start of Service: GetTLSClientAuthSetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_tls_client_auth
#-----------------------------------------------------------------------------
class TestGetTlsClientAuth():

    #--------------------------------------------------------
    # get_tls_client_auth()
    #--------------------------------------------------------
    @responses.activate
    def test_get_tls_client_auth_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/tls_client_auth'
        mock_response = '{"result": {"id": "tls_client_auth", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'

        # Invoke method
        response = service.get_tls_client_auth(
            accept=accept
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_tls_client_auth_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_tls_client_auth_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/tls_client_auth'
        mock_response = '{"result": {"id": "tls_client_auth", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.get_tls_client_auth()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: GetTLSClientAuthSetting
##############################################################################

##############################################################################
# Start of Service: UpdateTLSClientAuthSetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for update_tls_client_auth
#-----------------------------------------------------------------------------
class TestUpdateTlsClientAuth():

    #--------------------------------------------------------
    # update_tls_client_auth()
    #--------------------------------------------------------
    @responses.activate
    def test_update_tls_client_auth_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/tls_client_auth'
        mock_response = '{"result": {"id": "tls_client_auth", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'
        value = 'true'

        # Invoke method
        response = service.update_tls_client_auth(
            accept=accept,
            value=value,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == value


    #--------------------------------------------------------
    # test_update_tls_client_auth_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_tls_client_auth_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/tls_client_auth'
        mock_response = '{"result": {"id": "tls_client_auth", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.update_tls_client_auth()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: UpdateTLSClientAuthSetting
##############################################################################

##############################################################################
# Start of Service: GetBrowserCheckSetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_browser_check
#-----------------------------------------------------------------------------
class TestGetBrowserCheck():

    #--------------------------------------------------------
    # get_browser_check()
    #--------------------------------------------------------
    @responses.activate
    def test_get_browser_check_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/browser_check'
        mock_response = '{"result": {"id": "browser_check", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'

        # Invoke method
        response = service.get_browser_check(
            accept=accept
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_browser_check_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_browser_check_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/browser_check'
        mock_response = '{"result": {"id": "browser_check", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.get_browser_check()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: GetBrowserCheckSetting
##############################################################################

##############################################################################
# Start of Service: UpdateBrowserCheckSetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for update_browser_check
#-----------------------------------------------------------------------------
class TestUpdateBrowserCheck():

    #--------------------------------------------------------
    # update_browser_check()
    #--------------------------------------------------------
    @responses.activate
    def test_update_browser_check_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/browser_check'
        mock_response = '{"result": {"id": "browser_check", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'
        value = 'true'

        # Invoke method
        response = service.update_browser_check(
            accept=accept,
            value=value,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == value


    #--------------------------------------------------------
    # test_update_browser_check_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_browser_check_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/browser_check'
        mock_response = '{"result": {"id": "browser_check", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.update_browser_check()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: UpdateBrowserCheckSetting
##############################################################################

##############################################################################
# Start of Service: GetEnableErrorPagesOnSetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_enable_error_pages_on
#-----------------------------------------------------------------------------
class TestGetEnableErrorPagesOn():

    #--------------------------------------------------------
    # get_enable_error_pages_on()
    #--------------------------------------------------------
    @responses.activate
    def test_get_enable_error_pages_on_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/origin_error_page_pass_thru'
        responses.add(responses.GET,
                      url,
                      status=200)

        # Invoke method
        response = service.get_enable_error_pages_on()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_enable_error_pages_on_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_enable_error_pages_on_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/origin_error_page_pass_thru'
        responses.add(responses.GET,
                      url,
                      status=200)

        # Invoke method
        response = service.get_enable_error_pages_on()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: GetEnableErrorPagesOnSetting
##############################################################################

##############################################################################
# Start of Service: UpdateEnableErrorPagesOnSetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for update_enable_error_pages_on
#-----------------------------------------------------------------------------
class TestUpdateEnableErrorPagesOn():

    #--------------------------------------------------------
    # update_enable_error_pages_on()
    #--------------------------------------------------------
    @responses.activate
    def test_update_enable_error_pages_on_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/origin_error_page_pass_thru'
        mock_response = '{"result": {"id": "origin_error_page_pass_thru", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'
        value = 'true'

        # Invoke method
        response = service.update_enable_error_pages_on(
            accept=accept,
            value=value,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == value


    #--------------------------------------------------------
    # test_update_enable_error_pages_on_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_enable_error_pages_on_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/origin_error_page_pass_thru'
        mock_response = '{"result": {"id": "origin_error_page_pass_thru", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.update_enable_error_pages_on()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: UpdateEnableErrorPagesOnSetting
##############################################################################

##############################################################################
# Start of Service: GetWebApplicationFirewallSetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_web_application_firewall
#-----------------------------------------------------------------------------
class TestGetWebApplicationFirewall():

    #--------------------------------------------------------
    # get_web_application_firewall()
    #--------------------------------------------------------
    @responses.activate
    def test_get_web_application_firewall_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/waf'
        mock_response = '{"result": {"id": "waf", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'

        # Invoke method
        response = service.get_web_application_firewall(
            accept=accept
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_web_application_firewall_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_web_application_firewall_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/waf'
        mock_response = '{"result": {"id": "waf", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.get_web_application_firewall()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: GetWebApplicationFirewallSetting
##############################################################################

##############################################################################
# Start of Service: UpdateWebApplicationFirewallSetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for update_web_application_firewall
#-----------------------------------------------------------------------------
class TestUpdateWebApplicationFirewall():

    #--------------------------------------------------------
    # update_web_application_firewall()
    #--------------------------------------------------------
    @responses.activate
    def test_update_web_application_firewall_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/waf'
        mock_response = '{"result": {"id": "waf", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'
        value = 'true'

        # Invoke method
        response = service.update_web_application_firewall(
            accept=accept,
            value=value,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == value


    #--------------------------------------------------------
    # test_update_web_application_firewall_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_web_application_firewall_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/waf'
        mock_response = '{"result": {"id": "waf", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.update_web_application_firewall()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: UpdateWebApplicationFirewallSetting
##############################################################################

