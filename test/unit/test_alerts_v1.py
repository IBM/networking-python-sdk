# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2022.
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

"""
Unit Tests for AlertsV1
"""

from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import os
import pytest
import re
import responses
import urllib
from ibm_cloud_networking_services.alerts_v1 import *

crn = 'testString'

_service = AlertsV1(
    authenticator=NoAuthAuthenticator(),
    crn=crn
)

_base_url = 'https://api.cis.cloud.ibm.com'
_service.set_service_url(_base_url)

##############################################################################
# Start of Service: AlertPolicies
##############################################################################
# region

class TestNewInstance():
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = AlertsV1.new_instance(
            crn=crn,
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, AlertsV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = AlertsV1.new_instance(
                crn=crn,
            )

    def test_new_instance_without_required_params(self):
        """
        new_instance_without_required_params()
        """
        with pytest.raises(TypeError, match='new_instance\\(\\) missing \\d required positional arguments?: \'.*\''):
            service = AlertsV1.new_instance()

    def test_new_instance_required_param_none(self):
        """
        new_instance_required_param_none()
        """
        with pytest.raises(ValueError, match='crn must be provided'):
            service = AlertsV1.new_instance(
                crn=None,
            )
class TestGetAlertPolicies():
    """
    Test Class for get_alert_policies
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_alert_policies_all_params(self):
        """
        get_alert_policies()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/alerting/policies')
        mock_response = '{"success": true, "errors": [{"id": "id"}], "messages": [{"id": "id"}], "result": [{"id": "f0413b106d2c4aa9b1553d5d0209c522", "name": "My Alert Policy", "description": "Description for my alert policy", "enabled": true, "alert_type": "dos_attack_l7", "mechanisms": {"email": [{"id": "id"}], "webhooks": [{"id": "id"}]}, "created": "2021-09-15T16:33:31.834209Z", "modified": "2021-09-15T16:33:31.834209Z", "conditions": {"anyKey": "anyValue"}, "filters": {"anyKey": "anyValue"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.get_alert_policies()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_alert_policies_all_params_with_retries(self):
        # Enable retries and run test_get_alert_policies_all_params.
        _service.enable_retries()
        self.test_get_alert_policies_all_params()

        # Disable retries and run test_get_alert_policies_all_params.
        _service.disable_retries()
        self.test_get_alert_policies_all_params()

    @responses.activate
    def test_get_alert_policies_value_error(self):
        """
        test_get_alert_policies_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/alerting/policies')
        mock_response = '{"success": true, "errors": [{"id": "id"}], "messages": [{"id": "id"}], "result": [{"id": "f0413b106d2c4aa9b1553d5d0209c522", "name": "My Alert Policy", "description": "Description for my alert policy", "enabled": true, "alert_type": "dos_attack_l7", "mechanisms": {"email": [{"id": "id"}], "webhooks": [{"id": "id"}]}, "created": "2021-09-15T16:33:31.834209Z", "modified": "2021-09-15T16:33:31.834209Z", "conditions": {"anyKey": "anyValue"}, "filters": {"anyKey": "anyValue"}}]}'
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
                _service.get_alert_policies(**req_copy)


    def test_get_alert_policies_value_error_with_retries(self):
        # Enable retries and run test_get_alert_policies_value_error.
        _service.enable_retries()
        self.test_get_alert_policies_value_error()

        # Disable retries and run test_get_alert_policies_value_error.
        _service.disable_retries()
        self.test_get_alert_policies_value_error()

class TestCreateAlertPolicy():
    """
    Test Class for create_alert_policy
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_create_alert_policy_all_params(self):
        """
        create_alert_policy()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/alerting/policies')
        mock_response = '{"success": true, "errors": [{"id": "id"}], "messages": [{"id": "id"}], "result": {"id": "f0413b106d2c4aa9b1553d5d0209c522"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a CreateAlertPolicyInputMechanismsEmailItem model
        create_alert_policy_input_mechanisms_email_item_model = {}
        create_alert_policy_input_mechanisms_email_item_model['id'] = 'mynotifications@email.com'

        # Construct a dict representation of a CreateAlertPolicyInputMechanismsWebhooksItem model
        create_alert_policy_input_mechanisms_webhooks_item_model = {}
        create_alert_policy_input_mechanisms_webhooks_item_model['id'] = 'f0413b106d2c4aa9b1553d5d0209c522'

        # Construct a dict representation of a CreateAlertPolicyInputMechanisms model
        create_alert_policy_input_mechanisms_model = {}
        create_alert_policy_input_mechanisms_model['email'] = [create_alert_policy_input_mechanisms_email_item_model]
        create_alert_policy_input_mechanisms_model['webhooks'] = [create_alert_policy_input_mechanisms_webhooks_item_model]

        # Set up parameter values
        name = 'My Alert Policy'
        enabled = True
        alert_type = 'dos_attack_l7'
        mechanisms = create_alert_policy_input_mechanisms_model
        description = 'A description for my alert policy'
        filters = { 'foo': 'bar' }
        conditions = { 'foo': 'bar' }

        # Invoke method
        response = _service.create_alert_policy(
            name=name,
            enabled=enabled,
            alert_type=alert_type,
            mechanisms=mechanisms,
            description=description,
            filters=filters,
            conditions=conditions,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'My Alert Policy'
        assert req_body['enabled'] == True
        assert req_body['alert_type'] == 'dos_attack_l7'
        assert req_body['mechanisms'] == create_alert_policy_input_mechanisms_model
        assert req_body['description'] == 'A description for my alert policy'
        assert req_body['filters'] == { 'foo': 'bar' }
        assert req_body['conditions'] == { 'foo': 'bar' }

    def test_create_alert_policy_all_params_with_retries(self):
        # Enable retries and run test_create_alert_policy_all_params.
        _service.enable_retries()
        self.test_create_alert_policy_all_params()

        # Disable retries and run test_create_alert_policy_all_params.
        _service.disable_retries()
        self.test_create_alert_policy_all_params()

    @responses.activate
    def test_create_alert_policy_required_params(self):
        """
        test_create_alert_policy_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/alerting/policies')
        mock_response = '{"success": true, "errors": [{"id": "id"}], "messages": [{"id": "id"}], "result": {"id": "f0413b106d2c4aa9b1553d5d0209c522"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.create_alert_policy()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_create_alert_policy_required_params_with_retries(self):
        # Enable retries and run test_create_alert_policy_required_params.
        _service.enable_retries()
        self.test_create_alert_policy_required_params()

        # Disable retries and run test_create_alert_policy_required_params.
        _service.disable_retries()
        self.test_create_alert_policy_required_params()

    @responses.activate
    def test_create_alert_policy_value_error(self):
        """
        test_create_alert_policy_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/alerting/policies')
        mock_response = '{"success": true, "errors": [{"id": "id"}], "messages": [{"id": "id"}], "result": {"id": "f0413b106d2c4aa9b1553d5d0209c522"}}'
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
                _service.create_alert_policy(**req_copy)


    def test_create_alert_policy_value_error_with_retries(self):
        # Enable retries and run test_create_alert_policy_value_error.
        _service.enable_retries()
        self.test_create_alert_policy_value_error()

        # Disable retries and run test_create_alert_policy_value_error.
        _service.disable_retries()
        self.test_create_alert_policy_value_error()

class TestGetAlertPolicy():
    """
    Test Class for get_alert_policy
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_alert_policy_all_params(self):
        """
        get_alert_policy()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/alerting/policies/testString')
        mock_response = '{"success": true, "errors": [{"id": "id"}], "messages": [{"id": "id"}], "result": {"id": "f0413b106d2c4aa9b1553d5d0209c522", "name": "My Alert Policy", "description": "Description for my alert policy", "enabled": true, "alert_type": "dos_attack_l7", "mechanisms": {"email": [{"id": "id"}], "webhooks": [{"id": "id"}]}, "created": "2021-09-15T16:33:31.834209Z", "modified": "2021-09-15T16:33:31.834209Z", "conditions": {"anyKey": "anyValue"}, "filters": {"anyKey": "anyValue"}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        policy_id = 'testString'

        # Invoke method
        response = _service.get_alert_policy(
            policy_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_alert_policy_all_params_with_retries(self):
        # Enable retries and run test_get_alert_policy_all_params.
        _service.enable_retries()
        self.test_get_alert_policy_all_params()

        # Disable retries and run test_get_alert_policy_all_params.
        _service.disable_retries()
        self.test_get_alert_policy_all_params()

    @responses.activate
    def test_get_alert_policy_value_error(self):
        """
        test_get_alert_policy_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/alerting/policies/testString')
        mock_response = '{"success": true, "errors": [{"id": "id"}], "messages": [{"id": "id"}], "result": {"id": "f0413b106d2c4aa9b1553d5d0209c522", "name": "My Alert Policy", "description": "Description for my alert policy", "enabled": true, "alert_type": "dos_attack_l7", "mechanisms": {"email": [{"id": "id"}], "webhooks": [{"id": "id"}]}, "created": "2021-09-15T16:33:31.834209Z", "modified": "2021-09-15T16:33:31.834209Z", "conditions": {"anyKey": "anyValue"}, "filters": {"anyKey": "anyValue"}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        policy_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "policy_id": policy_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_alert_policy(**req_copy)


    def test_get_alert_policy_value_error_with_retries(self):
        # Enable retries and run test_get_alert_policy_value_error.
        _service.enable_retries()
        self.test_get_alert_policy_value_error()

        # Disable retries and run test_get_alert_policy_value_error.
        _service.disable_retries()
        self.test_get_alert_policy_value_error()

class TestUpdateAlertPolicy():
    """
    Test Class for update_alert_policy
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_update_alert_policy_all_params(self):
        """
        update_alert_policy()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/alerting/policies/testString')
        mock_response = '{"success": true, "errors": [{"id": "id"}], "messages": [{"id": "id"}], "result": {"id": "f0413b106d2c4aa9b1553d5d0209c522"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a UpdateAlertPolicyInputMechanismsEmailItem model
        update_alert_policy_input_mechanisms_email_item_model = {}
        update_alert_policy_input_mechanisms_email_item_model['id'] = 'mynotifications@email.com'

        # Construct a dict representation of a UpdateAlertPolicyInputMechanismsWebhooksItem model
        update_alert_policy_input_mechanisms_webhooks_item_model = {}
        update_alert_policy_input_mechanisms_webhooks_item_model['id'] = 'f0413b106d2c4aa9b1553d5d0209c522'

        # Construct a dict representation of a UpdateAlertPolicyInputMechanisms model
        update_alert_policy_input_mechanisms_model = {}
        update_alert_policy_input_mechanisms_model['email'] = [update_alert_policy_input_mechanisms_email_item_model]
        update_alert_policy_input_mechanisms_model['webhooks'] = [update_alert_policy_input_mechanisms_webhooks_item_model]

        # Set up parameter values
        policy_id = 'testString'
        name = 'My Alert Policy'
        enabled = True
        alert_type = 'dos_attack_l7'
        mechanisms = update_alert_policy_input_mechanisms_model
        conditions = { 'foo': 'bar' }
        description = 'A description for my alert policy'
        filters = { 'foo': 'bar' }

        # Invoke method
        response = _service.update_alert_policy(
            policy_id,
            name=name,
            enabled=enabled,
            alert_type=alert_type,
            mechanisms=mechanisms,
            conditions=conditions,
            description=description,
            filters=filters,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'My Alert Policy'
        assert req_body['enabled'] == True
        assert req_body['alert_type'] == 'dos_attack_l7'
        assert req_body['mechanisms'] == update_alert_policy_input_mechanisms_model
        assert req_body['conditions'] == { 'foo': 'bar' }
        assert req_body['description'] == 'A description for my alert policy'
        assert req_body['filters'] == { 'foo': 'bar' }

    def test_update_alert_policy_all_params_with_retries(self):
        # Enable retries and run test_update_alert_policy_all_params.
        _service.enable_retries()
        self.test_update_alert_policy_all_params()

        # Disable retries and run test_update_alert_policy_all_params.
        _service.disable_retries()
        self.test_update_alert_policy_all_params()

    @responses.activate
    def test_update_alert_policy_required_params(self):
        """
        test_update_alert_policy_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/alerting/policies/testString')
        mock_response = '{"success": true, "errors": [{"id": "id"}], "messages": [{"id": "id"}], "result": {"id": "f0413b106d2c4aa9b1553d5d0209c522"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        policy_id = 'testString'

        # Invoke method
        response = _service.update_alert_policy(
            policy_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_alert_policy_required_params_with_retries(self):
        # Enable retries and run test_update_alert_policy_required_params.
        _service.enable_retries()
        self.test_update_alert_policy_required_params()

        # Disable retries and run test_update_alert_policy_required_params.
        _service.disable_retries()
        self.test_update_alert_policy_required_params()

    @responses.activate
    def test_update_alert_policy_value_error(self):
        """
        test_update_alert_policy_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/alerting/policies/testString')
        mock_response = '{"success": true, "errors": [{"id": "id"}], "messages": [{"id": "id"}], "result": {"id": "f0413b106d2c4aa9b1553d5d0209c522"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        policy_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "policy_id": policy_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_alert_policy(**req_copy)


    def test_update_alert_policy_value_error_with_retries(self):
        # Enable retries and run test_update_alert_policy_value_error.
        _service.enable_retries()
        self.test_update_alert_policy_value_error()

        # Disable retries and run test_update_alert_policy_value_error.
        _service.disable_retries()
        self.test_update_alert_policy_value_error()

class TestDeleteAlertPolicy():
    """
    Test Class for delete_alert_policy
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_alert_policy_all_params(self):
        """
        delete_alert_policy()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/alerting/policies/testString')
        mock_response = '{"success": true, "errors": [{"id": "id"}], "messages": [{"id": "id"}], "result": {"id": "f0413b106d2c4aa9b1553d5d0209c522"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        policy_id = 'testString'

        # Invoke method
        response = _service.delete_alert_policy(
            policy_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_delete_alert_policy_all_params_with_retries(self):
        # Enable retries and run test_delete_alert_policy_all_params.
        _service.enable_retries()
        self.test_delete_alert_policy_all_params()

        # Disable retries and run test_delete_alert_policy_all_params.
        _service.disable_retries()
        self.test_delete_alert_policy_all_params()

    @responses.activate
    def test_delete_alert_policy_value_error(self):
        """
        test_delete_alert_policy_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/alerting/policies/testString')
        mock_response = '{"success": true, "errors": [{"id": "id"}], "messages": [{"id": "id"}], "result": {"id": "f0413b106d2c4aa9b1553d5d0209c522"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        policy_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "policy_id": policy_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_alert_policy(**req_copy)


    def test_delete_alert_policy_value_error_with_retries(self):
        # Enable retries and run test_delete_alert_policy_value_error.
        _service.enable_retries()
        self.test_delete_alert_policy_value_error()

        # Disable retries and run test_delete_alert_policy_value_error.
        _service.disable_retries()
        self.test_delete_alert_policy_value_error()

# endregion
##############################################################################
# End of Service: AlertPolicies
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestModel_AlertSuccessRespErrorsItem():
    """
    Test Class for AlertSuccessRespErrorsItem
    """

    def test_alert_success_resp_errors_item_serialization(self):
        """
        Test serialization/deserialization for AlertSuccessRespErrorsItem
        """

        # Construct a json representation of a AlertSuccessRespErrorsItem model
        alert_success_resp_errors_item_model_json = {}
        alert_success_resp_errors_item_model_json['id'] = 'testString'

        # Construct a model instance of AlertSuccessRespErrorsItem by calling from_dict on the json representation
        alert_success_resp_errors_item_model = AlertSuccessRespErrorsItem.from_dict(alert_success_resp_errors_item_model_json)
        assert alert_success_resp_errors_item_model != False

        # Construct a model instance of AlertSuccessRespErrorsItem by calling from_dict on the json representation
        alert_success_resp_errors_item_model_dict = AlertSuccessRespErrorsItem.from_dict(alert_success_resp_errors_item_model_json).__dict__
        alert_success_resp_errors_item_model2 = AlertSuccessRespErrorsItem(**alert_success_resp_errors_item_model_dict)

        # Verify the model instances are equivalent
        assert alert_success_resp_errors_item_model == alert_success_resp_errors_item_model2

        # Convert model instance back to dict and verify no loss of data
        alert_success_resp_errors_item_model_json2 = alert_success_resp_errors_item_model.to_dict()
        assert alert_success_resp_errors_item_model_json2 == alert_success_resp_errors_item_model_json

class TestModel_AlertSuccessRespMessagesItem():
    """
    Test Class for AlertSuccessRespMessagesItem
    """

    def test_alert_success_resp_messages_item_serialization(self):
        """
        Test serialization/deserialization for AlertSuccessRespMessagesItem
        """

        # Construct a json representation of a AlertSuccessRespMessagesItem model
        alert_success_resp_messages_item_model_json = {}
        alert_success_resp_messages_item_model_json['id'] = 'testString'

        # Construct a model instance of AlertSuccessRespMessagesItem by calling from_dict on the json representation
        alert_success_resp_messages_item_model = AlertSuccessRespMessagesItem.from_dict(alert_success_resp_messages_item_model_json)
        assert alert_success_resp_messages_item_model != False

        # Construct a model instance of AlertSuccessRespMessagesItem by calling from_dict on the json representation
        alert_success_resp_messages_item_model_dict = AlertSuccessRespMessagesItem.from_dict(alert_success_resp_messages_item_model_json).__dict__
        alert_success_resp_messages_item_model2 = AlertSuccessRespMessagesItem(**alert_success_resp_messages_item_model_dict)

        # Verify the model instances are equivalent
        assert alert_success_resp_messages_item_model == alert_success_resp_messages_item_model2

        # Convert model instance back to dict and verify no loss of data
        alert_success_resp_messages_item_model_json2 = alert_success_resp_messages_item_model.to_dict()
        assert alert_success_resp_messages_item_model_json2 == alert_success_resp_messages_item_model_json

class TestModel_AlertSuccessRespResult():
    """
    Test Class for AlertSuccessRespResult
    """

    def test_alert_success_resp_result_serialization(self):
        """
        Test serialization/deserialization for AlertSuccessRespResult
        """

        # Construct a json representation of a AlertSuccessRespResult model
        alert_success_resp_result_model_json = {}
        alert_success_resp_result_model_json['id'] = 'f0413b106d2c4aa9b1553d5d0209c522'

        # Construct a model instance of AlertSuccessRespResult by calling from_dict on the json representation
        alert_success_resp_result_model = AlertSuccessRespResult.from_dict(alert_success_resp_result_model_json)
        assert alert_success_resp_result_model != False

        # Construct a model instance of AlertSuccessRespResult by calling from_dict on the json representation
        alert_success_resp_result_model_dict = AlertSuccessRespResult.from_dict(alert_success_resp_result_model_json).__dict__
        alert_success_resp_result_model2 = AlertSuccessRespResult(**alert_success_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert alert_success_resp_result_model == alert_success_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        alert_success_resp_result_model_json2 = alert_success_resp_result_model.to_dict()
        assert alert_success_resp_result_model_json2 == alert_success_resp_result_model_json

class TestModel_CreateAlertPolicyInputMechanisms():
    """
    Test Class for CreateAlertPolicyInputMechanisms
    """

    def test_create_alert_policy_input_mechanisms_serialization(self):
        """
        Test serialization/deserialization for CreateAlertPolicyInputMechanisms
        """

        # Construct dict forms of any model objects needed in order to build this model.

        create_alert_policy_input_mechanisms_email_item_model = {} # CreateAlertPolicyInputMechanismsEmailItem
        create_alert_policy_input_mechanisms_email_item_model['id'] = 'mynotifications@email.com'

        create_alert_policy_input_mechanisms_webhooks_item_model = {} # CreateAlertPolicyInputMechanismsWebhooksItem
        create_alert_policy_input_mechanisms_webhooks_item_model['id'] = 'f0413b106d2c4aa9b1553d5d0209c522'

        # Construct a json representation of a CreateAlertPolicyInputMechanisms model
        create_alert_policy_input_mechanisms_model_json = {}
        create_alert_policy_input_mechanisms_model_json['email'] = [create_alert_policy_input_mechanisms_email_item_model]
        create_alert_policy_input_mechanisms_model_json['webhooks'] = [create_alert_policy_input_mechanisms_webhooks_item_model]

        # Construct a model instance of CreateAlertPolicyInputMechanisms by calling from_dict on the json representation
        create_alert_policy_input_mechanisms_model = CreateAlertPolicyInputMechanisms.from_dict(create_alert_policy_input_mechanisms_model_json)
        assert create_alert_policy_input_mechanisms_model != False

        # Construct a model instance of CreateAlertPolicyInputMechanisms by calling from_dict on the json representation
        create_alert_policy_input_mechanisms_model_dict = CreateAlertPolicyInputMechanisms.from_dict(create_alert_policy_input_mechanisms_model_json).__dict__
        create_alert_policy_input_mechanisms_model2 = CreateAlertPolicyInputMechanisms(**create_alert_policy_input_mechanisms_model_dict)

        # Verify the model instances are equivalent
        assert create_alert_policy_input_mechanisms_model == create_alert_policy_input_mechanisms_model2

        # Convert model instance back to dict and verify no loss of data
        create_alert_policy_input_mechanisms_model_json2 = create_alert_policy_input_mechanisms_model.to_dict()
        assert create_alert_policy_input_mechanisms_model_json2 == create_alert_policy_input_mechanisms_model_json

class TestModel_CreateAlertPolicyInputMechanismsEmailItem():
    """
    Test Class for CreateAlertPolicyInputMechanismsEmailItem
    """

    def test_create_alert_policy_input_mechanisms_email_item_serialization(self):
        """
        Test serialization/deserialization for CreateAlertPolicyInputMechanismsEmailItem
        """

        # Construct a json representation of a CreateAlertPolicyInputMechanismsEmailItem model
        create_alert_policy_input_mechanisms_email_item_model_json = {}
        create_alert_policy_input_mechanisms_email_item_model_json['id'] = 'testString'

        # Construct a model instance of CreateAlertPolicyInputMechanismsEmailItem by calling from_dict on the json representation
        create_alert_policy_input_mechanisms_email_item_model = CreateAlertPolicyInputMechanismsEmailItem.from_dict(create_alert_policy_input_mechanisms_email_item_model_json)
        assert create_alert_policy_input_mechanisms_email_item_model != False

        # Construct a model instance of CreateAlertPolicyInputMechanismsEmailItem by calling from_dict on the json representation
        create_alert_policy_input_mechanisms_email_item_model_dict = CreateAlertPolicyInputMechanismsEmailItem.from_dict(create_alert_policy_input_mechanisms_email_item_model_json).__dict__
        create_alert_policy_input_mechanisms_email_item_model2 = CreateAlertPolicyInputMechanismsEmailItem(**create_alert_policy_input_mechanisms_email_item_model_dict)

        # Verify the model instances are equivalent
        assert create_alert_policy_input_mechanisms_email_item_model == create_alert_policy_input_mechanisms_email_item_model2

        # Convert model instance back to dict and verify no loss of data
        create_alert_policy_input_mechanisms_email_item_model_json2 = create_alert_policy_input_mechanisms_email_item_model.to_dict()
        assert create_alert_policy_input_mechanisms_email_item_model_json2 == create_alert_policy_input_mechanisms_email_item_model_json

class TestModel_CreateAlertPolicyInputMechanismsWebhooksItem():
    """
    Test Class for CreateAlertPolicyInputMechanismsWebhooksItem
    """

    def test_create_alert_policy_input_mechanisms_webhooks_item_serialization(self):
        """
        Test serialization/deserialization for CreateAlertPolicyInputMechanismsWebhooksItem
        """

        # Construct a json representation of a CreateAlertPolicyInputMechanismsWebhooksItem model
        create_alert_policy_input_mechanisms_webhooks_item_model_json = {}
        create_alert_policy_input_mechanisms_webhooks_item_model_json['id'] = 'testString'

        # Construct a model instance of CreateAlertPolicyInputMechanismsWebhooksItem by calling from_dict on the json representation
        create_alert_policy_input_mechanisms_webhooks_item_model = CreateAlertPolicyInputMechanismsWebhooksItem.from_dict(create_alert_policy_input_mechanisms_webhooks_item_model_json)
        assert create_alert_policy_input_mechanisms_webhooks_item_model != False

        # Construct a model instance of CreateAlertPolicyInputMechanismsWebhooksItem by calling from_dict on the json representation
        create_alert_policy_input_mechanisms_webhooks_item_model_dict = CreateAlertPolicyInputMechanismsWebhooksItem.from_dict(create_alert_policy_input_mechanisms_webhooks_item_model_json).__dict__
        create_alert_policy_input_mechanisms_webhooks_item_model2 = CreateAlertPolicyInputMechanismsWebhooksItem(**create_alert_policy_input_mechanisms_webhooks_item_model_dict)

        # Verify the model instances are equivalent
        assert create_alert_policy_input_mechanisms_webhooks_item_model == create_alert_policy_input_mechanisms_webhooks_item_model2

        # Convert model instance back to dict and verify no loss of data
        create_alert_policy_input_mechanisms_webhooks_item_model_json2 = create_alert_policy_input_mechanisms_webhooks_item_model.to_dict()
        assert create_alert_policy_input_mechanisms_webhooks_item_model_json2 == create_alert_policy_input_mechanisms_webhooks_item_model_json

class TestModel_GetAlertPolicyRespErrorsItem():
    """
    Test Class for GetAlertPolicyRespErrorsItem
    """

    def test_get_alert_policy_resp_errors_item_serialization(self):
        """
        Test serialization/deserialization for GetAlertPolicyRespErrorsItem
        """

        # Construct a json representation of a GetAlertPolicyRespErrorsItem model
        get_alert_policy_resp_errors_item_model_json = {}
        get_alert_policy_resp_errors_item_model_json['id'] = 'testString'

        # Construct a model instance of GetAlertPolicyRespErrorsItem by calling from_dict on the json representation
        get_alert_policy_resp_errors_item_model = GetAlertPolicyRespErrorsItem.from_dict(get_alert_policy_resp_errors_item_model_json)
        assert get_alert_policy_resp_errors_item_model != False

        # Construct a model instance of GetAlertPolicyRespErrorsItem by calling from_dict on the json representation
        get_alert_policy_resp_errors_item_model_dict = GetAlertPolicyRespErrorsItem.from_dict(get_alert_policy_resp_errors_item_model_json).__dict__
        get_alert_policy_resp_errors_item_model2 = GetAlertPolicyRespErrorsItem(**get_alert_policy_resp_errors_item_model_dict)

        # Verify the model instances are equivalent
        assert get_alert_policy_resp_errors_item_model == get_alert_policy_resp_errors_item_model2

        # Convert model instance back to dict and verify no loss of data
        get_alert_policy_resp_errors_item_model_json2 = get_alert_policy_resp_errors_item_model.to_dict()
        assert get_alert_policy_resp_errors_item_model_json2 == get_alert_policy_resp_errors_item_model_json

class TestModel_GetAlertPolicyRespMessagesItem():
    """
    Test Class for GetAlertPolicyRespMessagesItem
    """

    def test_get_alert_policy_resp_messages_item_serialization(self):
        """
        Test serialization/deserialization for GetAlertPolicyRespMessagesItem
        """

        # Construct a json representation of a GetAlertPolicyRespMessagesItem model
        get_alert_policy_resp_messages_item_model_json = {}
        get_alert_policy_resp_messages_item_model_json['id'] = 'testString'

        # Construct a model instance of GetAlertPolicyRespMessagesItem by calling from_dict on the json representation
        get_alert_policy_resp_messages_item_model = GetAlertPolicyRespMessagesItem.from_dict(get_alert_policy_resp_messages_item_model_json)
        assert get_alert_policy_resp_messages_item_model != False

        # Construct a model instance of GetAlertPolicyRespMessagesItem by calling from_dict on the json representation
        get_alert_policy_resp_messages_item_model_dict = GetAlertPolicyRespMessagesItem.from_dict(get_alert_policy_resp_messages_item_model_json).__dict__
        get_alert_policy_resp_messages_item_model2 = GetAlertPolicyRespMessagesItem(**get_alert_policy_resp_messages_item_model_dict)

        # Verify the model instances are equivalent
        assert get_alert_policy_resp_messages_item_model == get_alert_policy_resp_messages_item_model2

        # Convert model instance back to dict and verify no loss of data
        get_alert_policy_resp_messages_item_model_json2 = get_alert_policy_resp_messages_item_model.to_dict()
        assert get_alert_policy_resp_messages_item_model_json2 == get_alert_policy_resp_messages_item_model_json

class TestModel_GetAlertPolicyRespResult():
    """
    Test Class for GetAlertPolicyRespResult
    """

    def test_get_alert_policy_resp_result_serialization(self):
        """
        Test serialization/deserialization for GetAlertPolicyRespResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        get_alert_policy_resp_result_mechanisms_email_item_model = {} # GetAlertPolicyRespResultMechanismsEmailItem
        get_alert_policy_resp_result_mechanisms_email_item_model['id'] = 'mynotifications@email.com'

        get_alert_policy_resp_result_mechanisms_webhooks_item_model = {} # GetAlertPolicyRespResultMechanismsWebhooksItem
        get_alert_policy_resp_result_mechanisms_webhooks_item_model['id'] = 'f0413b106d2c4aa9b1553d5d0209c522'

        get_alert_policy_resp_result_mechanisms_model = {} # GetAlertPolicyRespResultMechanisms
        get_alert_policy_resp_result_mechanisms_model['email'] = [get_alert_policy_resp_result_mechanisms_email_item_model]
        get_alert_policy_resp_result_mechanisms_model['webhooks'] = [get_alert_policy_resp_result_mechanisms_webhooks_item_model]

        # Construct a json representation of a GetAlertPolicyRespResult model
        get_alert_policy_resp_result_model_json = {}
        get_alert_policy_resp_result_model_json['id'] = 'f0413b106d2c4aa9b1553d5d0209c522'
        get_alert_policy_resp_result_model_json['name'] = 'My Alert Policy'
        get_alert_policy_resp_result_model_json['description'] = 'Description for my alert policy'
        get_alert_policy_resp_result_model_json['enabled'] = True
        get_alert_policy_resp_result_model_json['alert_type'] = 'dos_attack_l7'
        get_alert_policy_resp_result_model_json['mechanisms'] = get_alert_policy_resp_result_mechanisms_model
        get_alert_policy_resp_result_model_json['created'] = '2021-09-15T16:33:31.834209Z'
        get_alert_policy_resp_result_model_json['modified'] = '2021-09-15T16:33:31.834209Z'
        get_alert_policy_resp_result_model_json['conditions'] = { 'foo': 'bar' }
        get_alert_policy_resp_result_model_json['filters'] = { 'foo': 'bar' }

        # Construct a model instance of GetAlertPolicyRespResult by calling from_dict on the json representation
        get_alert_policy_resp_result_model = GetAlertPolicyRespResult.from_dict(get_alert_policy_resp_result_model_json)
        assert get_alert_policy_resp_result_model != False

        # Construct a model instance of GetAlertPolicyRespResult by calling from_dict on the json representation
        get_alert_policy_resp_result_model_dict = GetAlertPolicyRespResult.from_dict(get_alert_policy_resp_result_model_json).__dict__
        get_alert_policy_resp_result_model2 = GetAlertPolicyRespResult(**get_alert_policy_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert get_alert_policy_resp_result_model == get_alert_policy_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        get_alert_policy_resp_result_model_json2 = get_alert_policy_resp_result_model.to_dict()
        assert get_alert_policy_resp_result_model_json2 == get_alert_policy_resp_result_model_json

class TestModel_GetAlertPolicyRespResultMechanisms():
    """
    Test Class for GetAlertPolicyRespResultMechanisms
    """

    def test_get_alert_policy_resp_result_mechanisms_serialization(self):
        """
        Test serialization/deserialization for GetAlertPolicyRespResultMechanisms
        """

        # Construct dict forms of any model objects needed in order to build this model.

        get_alert_policy_resp_result_mechanisms_email_item_model = {} # GetAlertPolicyRespResultMechanismsEmailItem
        get_alert_policy_resp_result_mechanisms_email_item_model['id'] = 'mynotifications@email.com'

        get_alert_policy_resp_result_mechanisms_webhooks_item_model = {} # GetAlertPolicyRespResultMechanismsWebhooksItem
        get_alert_policy_resp_result_mechanisms_webhooks_item_model['id'] = 'f0413b106d2c4aa9b1553d5d0209c522'

        # Construct a json representation of a GetAlertPolicyRespResultMechanisms model
        get_alert_policy_resp_result_mechanisms_model_json = {}
        get_alert_policy_resp_result_mechanisms_model_json['email'] = [get_alert_policy_resp_result_mechanisms_email_item_model]
        get_alert_policy_resp_result_mechanisms_model_json['webhooks'] = [get_alert_policy_resp_result_mechanisms_webhooks_item_model]

        # Construct a model instance of GetAlertPolicyRespResultMechanisms by calling from_dict on the json representation
        get_alert_policy_resp_result_mechanisms_model = GetAlertPolicyRespResultMechanisms.from_dict(get_alert_policy_resp_result_mechanisms_model_json)
        assert get_alert_policy_resp_result_mechanisms_model != False

        # Construct a model instance of GetAlertPolicyRespResultMechanisms by calling from_dict on the json representation
        get_alert_policy_resp_result_mechanisms_model_dict = GetAlertPolicyRespResultMechanisms.from_dict(get_alert_policy_resp_result_mechanisms_model_json).__dict__
        get_alert_policy_resp_result_mechanisms_model2 = GetAlertPolicyRespResultMechanisms(**get_alert_policy_resp_result_mechanisms_model_dict)

        # Verify the model instances are equivalent
        assert get_alert_policy_resp_result_mechanisms_model == get_alert_policy_resp_result_mechanisms_model2

        # Convert model instance back to dict and verify no loss of data
        get_alert_policy_resp_result_mechanisms_model_json2 = get_alert_policy_resp_result_mechanisms_model.to_dict()
        assert get_alert_policy_resp_result_mechanisms_model_json2 == get_alert_policy_resp_result_mechanisms_model_json

class TestModel_GetAlertPolicyRespResultMechanismsEmailItem():
    """
    Test Class for GetAlertPolicyRespResultMechanismsEmailItem
    """

    def test_get_alert_policy_resp_result_mechanisms_email_item_serialization(self):
        """
        Test serialization/deserialization for GetAlertPolicyRespResultMechanismsEmailItem
        """

        # Construct a json representation of a GetAlertPolicyRespResultMechanismsEmailItem model
        get_alert_policy_resp_result_mechanisms_email_item_model_json = {}
        get_alert_policy_resp_result_mechanisms_email_item_model_json['id'] = 'testString'

        # Construct a model instance of GetAlertPolicyRespResultMechanismsEmailItem by calling from_dict on the json representation
        get_alert_policy_resp_result_mechanisms_email_item_model = GetAlertPolicyRespResultMechanismsEmailItem.from_dict(get_alert_policy_resp_result_mechanisms_email_item_model_json)
        assert get_alert_policy_resp_result_mechanisms_email_item_model != False

        # Construct a model instance of GetAlertPolicyRespResultMechanismsEmailItem by calling from_dict on the json representation
        get_alert_policy_resp_result_mechanisms_email_item_model_dict = GetAlertPolicyRespResultMechanismsEmailItem.from_dict(get_alert_policy_resp_result_mechanisms_email_item_model_json).__dict__
        get_alert_policy_resp_result_mechanisms_email_item_model2 = GetAlertPolicyRespResultMechanismsEmailItem(**get_alert_policy_resp_result_mechanisms_email_item_model_dict)

        # Verify the model instances are equivalent
        assert get_alert_policy_resp_result_mechanisms_email_item_model == get_alert_policy_resp_result_mechanisms_email_item_model2

        # Convert model instance back to dict and verify no loss of data
        get_alert_policy_resp_result_mechanisms_email_item_model_json2 = get_alert_policy_resp_result_mechanisms_email_item_model.to_dict()
        assert get_alert_policy_resp_result_mechanisms_email_item_model_json2 == get_alert_policy_resp_result_mechanisms_email_item_model_json

class TestModel_GetAlertPolicyRespResultMechanismsWebhooksItem():
    """
    Test Class for GetAlertPolicyRespResultMechanismsWebhooksItem
    """

    def test_get_alert_policy_resp_result_mechanisms_webhooks_item_serialization(self):
        """
        Test serialization/deserialization for GetAlertPolicyRespResultMechanismsWebhooksItem
        """

        # Construct a json representation of a GetAlertPolicyRespResultMechanismsWebhooksItem model
        get_alert_policy_resp_result_mechanisms_webhooks_item_model_json = {}
        get_alert_policy_resp_result_mechanisms_webhooks_item_model_json['id'] = 'testString'

        # Construct a model instance of GetAlertPolicyRespResultMechanismsWebhooksItem by calling from_dict on the json representation
        get_alert_policy_resp_result_mechanisms_webhooks_item_model = GetAlertPolicyRespResultMechanismsWebhooksItem.from_dict(get_alert_policy_resp_result_mechanisms_webhooks_item_model_json)
        assert get_alert_policy_resp_result_mechanisms_webhooks_item_model != False

        # Construct a model instance of GetAlertPolicyRespResultMechanismsWebhooksItem by calling from_dict on the json representation
        get_alert_policy_resp_result_mechanisms_webhooks_item_model_dict = GetAlertPolicyRespResultMechanismsWebhooksItem.from_dict(get_alert_policy_resp_result_mechanisms_webhooks_item_model_json).__dict__
        get_alert_policy_resp_result_mechanisms_webhooks_item_model2 = GetAlertPolicyRespResultMechanismsWebhooksItem(**get_alert_policy_resp_result_mechanisms_webhooks_item_model_dict)

        # Verify the model instances are equivalent
        assert get_alert_policy_resp_result_mechanisms_webhooks_item_model == get_alert_policy_resp_result_mechanisms_webhooks_item_model2

        # Convert model instance back to dict and verify no loss of data
        get_alert_policy_resp_result_mechanisms_webhooks_item_model_json2 = get_alert_policy_resp_result_mechanisms_webhooks_item_model.to_dict()
        assert get_alert_policy_resp_result_mechanisms_webhooks_item_model_json2 == get_alert_policy_resp_result_mechanisms_webhooks_item_model_json

class TestModel_ListAlertPoliciesRespErrorsItem():
    """
    Test Class for ListAlertPoliciesRespErrorsItem
    """

    def test_list_alert_policies_resp_errors_item_serialization(self):
        """
        Test serialization/deserialization for ListAlertPoliciesRespErrorsItem
        """

        # Construct a json representation of a ListAlertPoliciesRespErrorsItem model
        list_alert_policies_resp_errors_item_model_json = {}
        list_alert_policies_resp_errors_item_model_json['id'] = 'testString'

        # Construct a model instance of ListAlertPoliciesRespErrorsItem by calling from_dict on the json representation
        list_alert_policies_resp_errors_item_model = ListAlertPoliciesRespErrorsItem.from_dict(list_alert_policies_resp_errors_item_model_json)
        assert list_alert_policies_resp_errors_item_model != False

        # Construct a model instance of ListAlertPoliciesRespErrorsItem by calling from_dict on the json representation
        list_alert_policies_resp_errors_item_model_dict = ListAlertPoliciesRespErrorsItem.from_dict(list_alert_policies_resp_errors_item_model_json).__dict__
        list_alert_policies_resp_errors_item_model2 = ListAlertPoliciesRespErrorsItem(**list_alert_policies_resp_errors_item_model_dict)

        # Verify the model instances are equivalent
        assert list_alert_policies_resp_errors_item_model == list_alert_policies_resp_errors_item_model2

        # Convert model instance back to dict and verify no loss of data
        list_alert_policies_resp_errors_item_model_json2 = list_alert_policies_resp_errors_item_model.to_dict()
        assert list_alert_policies_resp_errors_item_model_json2 == list_alert_policies_resp_errors_item_model_json

class TestModel_ListAlertPoliciesRespMessagesItem():
    """
    Test Class for ListAlertPoliciesRespMessagesItem
    """

    def test_list_alert_policies_resp_messages_item_serialization(self):
        """
        Test serialization/deserialization for ListAlertPoliciesRespMessagesItem
        """

        # Construct a json representation of a ListAlertPoliciesRespMessagesItem model
        list_alert_policies_resp_messages_item_model_json = {}
        list_alert_policies_resp_messages_item_model_json['id'] = 'testString'

        # Construct a model instance of ListAlertPoliciesRespMessagesItem by calling from_dict on the json representation
        list_alert_policies_resp_messages_item_model = ListAlertPoliciesRespMessagesItem.from_dict(list_alert_policies_resp_messages_item_model_json)
        assert list_alert_policies_resp_messages_item_model != False

        # Construct a model instance of ListAlertPoliciesRespMessagesItem by calling from_dict on the json representation
        list_alert_policies_resp_messages_item_model_dict = ListAlertPoliciesRespMessagesItem.from_dict(list_alert_policies_resp_messages_item_model_json).__dict__
        list_alert_policies_resp_messages_item_model2 = ListAlertPoliciesRespMessagesItem(**list_alert_policies_resp_messages_item_model_dict)

        # Verify the model instances are equivalent
        assert list_alert_policies_resp_messages_item_model == list_alert_policies_resp_messages_item_model2

        # Convert model instance back to dict and verify no loss of data
        list_alert_policies_resp_messages_item_model_json2 = list_alert_policies_resp_messages_item_model.to_dict()
        assert list_alert_policies_resp_messages_item_model_json2 == list_alert_policies_resp_messages_item_model_json

class TestModel_ListAlertPoliciesRespResultItem():
    """
    Test Class for ListAlertPoliciesRespResultItem
    """

    def test_list_alert_policies_resp_result_item_serialization(self):
        """
        Test serialization/deserialization for ListAlertPoliciesRespResultItem
        """

        # Construct dict forms of any model objects needed in order to build this model.

        list_alert_policies_resp_result_item_mechanisms_email_item_model = {} # ListAlertPoliciesRespResultItemMechanismsEmailItem
        list_alert_policies_resp_result_item_mechanisms_email_item_model['id'] = 'mynotifications@email.com'

        list_alert_policies_resp_result_item_mechanisms_webhooks_item_model = {} # ListAlertPoliciesRespResultItemMechanismsWebhooksItem
        list_alert_policies_resp_result_item_mechanisms_webhooks_item_model['id'] = 'f0413b106d2c4aa9b1553d5d0209c522'

        list_alert_policies_resp_result_item_mechanisms_model = {} # ListAlertPoliciesRespResultItemMechanisms
        list_alert_policies_resp_result_item_mechanisms_model['email'] = [list_alert_policies_resp_result_item_mechanisms_email_item_model]
        list_alert_policies_resp_result_item_mechanisms_model['webhooks'] = [list_alert_policies_resp_result_item_mechanisms_webhooks_item_model]

        # Construct a json representation of a ListAlertPoliciesRespResultItem model
        list_alert_policies_resp_result_item_model_json = {}
        list_alert_policies_resp_result_item_model_json['id'] = 'f0413b106d2c4aa9b1553d5d0209c522'
        list_alert_policies_resp_result_item_model_json['name'] = 'My Alert Policy'
        list_alert_policies_resp_result_item_model_json['description'] = 'Description for my alert policy'
        list_alert_policies_resp_result_item_model_json['enabled'] = True
        list_alert_policies_resp_result_item_model_json['alert_type'] = 'dos_attack_l7'
        list_alert_policies_resp_result_item_model_json['mechanisms'] = list_alert_policies_resp_result_item_mechanisms_model
        list_alert_policies_resp_result_item_model_json['created'] = '2021-09-15T16:33:31.834209Z'
        list_alert_policies_resp_result_item_model_json['modified'] = '2021-09-15T16:33:31.834209Z'
        list_alert_policies_resp_result_item_model_json['conditions'] = { 'foo': 'bar' }
        list_alert_policies_resp_result_item_model_json['filters'] = { 'foo': 'bar' }

        # Construct a model instance of ListAlertPoliciesRespResultItem by calling from_dict on the json representation
        list_alert_policies_resp_result_item_model = ListAlertPoliciesRespResultItem.from_dict(list_alert_policies_resp_result_item_model_json)
        assert list_alert_policies_resp_result_item_model != False

        # Construct a model instance of ListAlertPoliciesRespResultItem by calling from_dict on the json representation
        list_alert_policies_resp_result_item_model_dict = ListAlertPoliciesRespResultItem.from_dict(list_alert_policies_resp_result_item_model_json).__dict__
        list_alert_policies_resp_result_item_model2 = ListAlertPoliciesRespResultItem(**list_alert_policies_resp_result_item_model_dict)

        # Verify the model instances are equivalent
        assert list_alert_policies_resp_result_item_model == list_alert_policies_resp_result_item_model2

        # Convert model instance back to dict and verify no loss of data
        list_alert_policies_resp_result_item_model_json2 = list_alert_policies_resp_result_item_model.to_dict()
        assert list_alert_policies_resp_result_item_model_json2 == list_alert_policies_resp_result_item_model_json

class TestModel_ListAlertPoliciesRespResultItemMechanisms():
    """
    Test Class for ListAlertPoliciesRespResultItemMechanisms
    """

    def test_list_alert_policies_resp_result_item_mechanisms_serialization(self):
        """
        Test serialization/deserialization for ListAlertPoliciesRespResultItemMechanisms
        """

        # Construct dict forms of any model objects needed in order to build this model.

        list_alert_policies_resp_result_item_mechanisms_email_item_model = {} # ListAlertPoliciesRespResultItemMechanismsEmailItem
        list_alert_policies_resp_result_item_mechanisms_email_item_model['id'] = 'mynotifications@email.com'

        list_alert_policies_resp_result_item_mechanisms_webhooks_item_model = {} # ListAlertPoliciesRespResultItemMechanismsWebhooksItem
        list_alert_policies_resp_result_item_mechanisms_webhooks_item_model['id'] = 'f0413b106d2c4aa9b1553d5d0209c522'

        # Construct a json representation of a ListAlertPoliciesRespResultItemMechanisms model
        list_alert_policies_resp_result_item_mechanisms_model_json = {}
        list_alert_policies_resp_result_item_mechanisms_model_json['email'] = [list_alert_policies_resp_result_item_mechanisms_email_item_model]
        list_alert_policies_resp_result_item_mechanisms_model_json['webhooks'] = [list_alert_policies_resp_result_item_mechanisms_webhooks_item_model]

        # Construct a model instance of ListAlertPoliciesRespResultItemMechanisms by calling from_dict on the json representation
        list_alert_policies_resp_result_item_mechanisms_model = ListAlertPoliciesRespResultItemMechanisms.from_dict(list_alert_policies_resp_result_item_mechanisms_model_json)
        assert list_alert_policies_resp_result_item_mechanisms_model != False

        # Construct a model instance of ListAlertPoliciesRespResultItemMechanisms by calling from_dict on the json representation
        list_alert_policies_resp_result_item_mechanisms_model_dict = ListAlertPoliciesRespResultItemMechanisms.from_dict(list_alert_policies_resp_result_item_mechanisms_model_json).__dict__
        list_alert_policies_resp_result_item_mechanisms_model2 = ListAlertPoliciesRespResultItemMechanisms(**list_alert_policies_resp_result_item_mechanisms_model_dict)

        # Verify the model instances are equivalent
        assert list_alert_policies_resp_result_item_mechanisms_model == list_alert_policies_resp_result_item_mechanisms_model2

        # Convert model instance back to dict and verify no loss of data
        list_alert_policies_resp_result_item_mechanisms_model_json2 = list_alert_policies_resp_result_item_mechanisms_model.to_dict()
        assert list_alert_policies_resp_result_item_mechanisms_model_json2 == list_alert_policies_resp_result_item_mechanisms_model_json

class TestModel_ListAlertPoliciesRespResultItemMechanismsEmailItem():
    """
    Test Class for ListAlertPoliciesRespResultItemMechanismsEmailItem
    """

    def test_list_alert_policies_resp_result_item_mechanisms_email_item_serialization(self):
        """
        Test serialization/deserialization for ListAlertPoliciesRespResultItemMechanismsEmailItem
        """

        # Construct a json representation of a ListAlertPoliciesRespResultItemMechanismsEmailItem model
        list_alert_policies_resp_result_item_mechanisms_email_item_model_json = {}
        list_alert_policies_resp_result_item_mechanisms_email_item_model_json['id'] = 'testString'

        # Construct a model instance of ListAlertPoliciesRespResultItemMechanismsEmailItem by calling from_dict on the json representation
        list_alert_policies_resp_result_item_mechanisms_email_item_model = ListAlertPoliciesRespResultItemMechanismsEmailItem.from_dict(list_alert_policies_resp_result_item_mechanisms_email_item_model_json)
        assert list_alert_policies_resp_result_item_mechanisms_email_item_model != False

        # Construct a model instance of ListAlertPoliciesRespResultItemMechanismsEmailItem by calling from_dict on the json representation
        list_alert_policies_resp_result_item_mechanisms_email_item_model_dict = ListAlertPoliciesRespResultItemMechanismsEmailItem.from_dict(list_alert_policies_resp_result_item_mechanisms_email_item_model_json).__dict__
        list_alert_policies_resp_result_item_mechanisms_email_item_model2 = ListAlertPoliciesRespResultItemMechanismsEmailItem(**list_alert_policies_resp_result_item_mechanisms_email_item_model_dict)

        # Verify the model instances are equivalent
        assert list_alert_policies_resp_result_item_mechanisms_email_item_model == list_alert_policies_resp_result_item_mechanisms_email_item_model2

        # Convert model instance back to dict and verify no loss of data
        list_alert_policies_resp_result_item_mechanisms_email_item_model_json2 = list_alert_policies_resp_result_item_mechanisms_email_item_model.to_dict()
        assert list_alert_policies_resp_result_item_mechanisms_email_item_model_json2 == list_alert_policies_resp_result_item_mechanisms_email_item_model_json

class TestModel_ListAlertPoliciesRespResultItemMechanismsWebhooksItem():
    """
    Test Class for ListAlertPoliciesRespResultItemMechanismsWebhooksItem
    """

    def test_list_alert_policies_resp_result_item_mechanisms_webhooks_item_serialization(self):
        """
        Test serialization/deserialization for ListAlertPoliciesRespResultItemMechanismsWebhooksItem
        """

        # Construct a json representation of a ListAlertPoliciesRespResultItemMechanismsWebhooksItem model
        list_alert_policies_resp_result_item_mechanisms_webhooks_item_model_json = {}
        list_alert_policies_resp_result_item_mechanisms_webhooks_item_model_json['id'] = 'testString'

        # Construct a model instance of ListAlertPoliciesRespResultItemMechanismsWebhooksItem by calling from_dict on the json representation
        list_alert_policies_resp_result_item_mechanisms_webhooks_item_model = ListAlertPoliciesRespResultItemMechanismsWebhooksItem.from_dict(list_alert_policies_resp_result_item_mechanisms_webhooks_item_model_json)
        assert list_alert_policies_resp_result_item_mechanisms_webhooks_item_model != False

        # Construct a model instance of ListAlertPoliciesRespResultItemMechanismsWebhooksItem by calling from_dict on the json representation
        list_alert_policies_resp_result_item_mechanisms_webhooks_item_model_dict = ListAlertPoliciesRespResultItemMechanismsWebhooksItem.from_dict(list_alert_policies_resp_result_item_mechanisms_webhooks_item_model_json).__dict__
        list_alert_policies_resp_result_item_mechanisms_webhooks_item_model2 = ListAlertPoliciesRespResultItemMechanismsWebhooksItem(**list_alert_policies_resp_result_item_mechanisms_webhooks_item_model_dict)

        # Verify the model instances are equivalent
        assert list_alert_policies_resp_result_item_mechanisms_webhooks_item_model == list_alert_policies_resp_result_item_mechanisms_webhooks_item_model2

        # Convert model instance back to dict and verify no loss of data
        list_alert_policies_resp_result_item_mechanisms_webhooks_item_model_json2 = list_alert_policies_resp_result_item_mechanisms_webhooks_item_model.to_dict()
        assert list_alert_policies_resp_result_item_mechanisms_webhooks_item_model_json2 == list_alert_policies_resp_result_item_mechanisms_webhooks_item_model_json

class TestModel_UpdateAlertPolicyInputMechanisms():
    """
    Test Class for UpdateAlertPolicyInputMechanisms
    """

    def test_update_alert_policy_input_mechanisms_serialization(self):
        """
        Test serialization/deserialization for UpdateAlertPolicyInputMechanisms
        """

        # Construct dict forms of any model objects needed in order to build this model.

        update_alert_policy_input_mechanisms_email_item_model = {} # UpdateAlertPolicyInputMechanismsEmailItem
        update_alert_policy_input_mechanisms_email_item_model['id'] = 'mynotifications@email.com'

        update_alert_policy_input_mechanisms_webhooks_item_model = {} # UpdateAlertPolicyInputMechanismsWebhooksItem
        update_alert_policy_input_mechanisms_webhooks_item_model['id'] = 'f0413b106d2c4aa9b1553d5d0209c522'

        # Construct a json representation of a UpdateAlertPolicyInputMechanisms model
        update_alert_policy_input_mechanisms_model_json = {}
        update_alert_policy_input_mechanisms_model_json['email'] = [update_alert_policy_input_mechanisms_email_item_model]
        update_alert_policy_input_mechanisms_model_json['webhooks'] = [update_alert_policy_input_mechanisms_webhooks_item_model]

        # Construct a model instance of UpdateAlertPolicyInputMechanisms by calling from_dict on the json representation
        update_alert_policy_input_mechanisms_model = UpdateAlertPolicyInputMechanisms.from_dict(update_alert_policy_input_mechanisms_model_json)
        assert update_alert_policy_input_mechanisms_model != False

        # Construct a model instance of UpdateAlertPolicyInputMechanisms by calling from_dict on the json representation
        update_alert_policy_input_mechanisms_model_dict = UpdateAlertPolicyInputMechanisms.from_dict(update_alert_policy_input_mechanisms_model_json).__dict__
        update_alert_policy_input_mechanisms_model2 = UpdateAlertPolicyInputMechanisms(**update_alert_policy_input_mechanisms_model_dict)

        # Verify the model instances are equivalent
        assert update_alert_policy_input_mechanisms_model == update_alert_policy_input_mechanisms_model2

        # Convert model instance back to dict and verify no loss of data
        update_alert_policy_input_mechanisms_model_json2 = update_alert_policy_input_mechanisms_model.to_dict()
        assert update_alert_policy_input_mechanisms_model_json2 == update_alert_policy_input_mechanisms_model_json

class TestModel_UpdateAlertPolicyInputMechanismsEmailItem():
    """
    Test Class for UpdateAlertPolicyInputMechanismsEmailItem
    """

    def test_update_alert_policy_input_mechanisms_email_item_serialization(self):
        """
        Test serialization/deserialization for UpdateAlertPolicyInputMechanismsEmailItem
        """

        # Construct a json representation of a UpdateAlertPolicyInputMechanismsEmailItem model
        update_alert_policy_input_mechanisms_email_item_model_json = {}
        update_alert_policy_input_mechanisms_email_item_model_json['id'] = 'testString'

        # Construct a model instance of UpdateAlertPolicyInputMechanismsEmailItem by calling from_dict on the json representation
        update_alert_policy_input_mechanisms_email_item_model = UpdateAlertPolicyInputMechanismsEmailItem.from_dict(update_alert_policy_input_mechanisms_email_item_model_json)
        assert update_alert_policy_input_mechanisms_email_item_model != False

        # Construct a model instance of UpdateAlertPolicyInputMechanismsEmailItem by calling from_dict on the json representation
        update_alert_policy_input_mechanisms_email_item_model_dict = UpdateAlertPolicyInputMechanismsEmailItem.from_dict(update_alert_policy_input_mechanisms_email_item_model_json).__dict__
        update_alert_policy_input_mechanisms_email_item_model2 = UpdateAlertPolicyInputMechanismsEmailItem(**update_alert_policy_input_mechanisms_email_item_model_dict)

        # Verify the model instances are equivalent
        assert update_alert_policy_input_mechanisms_email_item_model == update_alert_policy_input_mechanisms_email_item_model2

        # Convert model instance back to dict and verify no loss of data
        update_alert_policy_input_mechanisms_email_item_model_json2 = update_alert_policy_input_mechanisms_email_item_model.to_dict()
        assert update_alert_policy_input_mechanisms_email_item_model_json2 == update_alert_policy_input_mechanisms_email_item_model_json

class TestModel_UpdateAlertPolicyInputMechanismsWebhooksItem():
    """
    Test Class for UpdateAlertPolicyInputMechanismsWebhooksItem
    """

    def test_update_alert_policy_input_mechanisms_webhooks_item_serialization(self):
        """
        Test serialization/deserialization for UpdateAlertPolicyInputMechanismsWebhooksItem
        """

        # Construct a json representation of a UpdateAlertPolicyInputMechanismsWebhooksItem model
        update_alert_policy_input_mechanisms_webhooks_item_model_json = {}
        update_alert_policy_input_mechanisms_webhooks_item_model_json['id'] = 'testString'

        # Construct a model instance of UpdateAlertPolicyInputMechanismsWebhooksItem by calling from_dict on the json representation
        update_alert_policy_input_mechanisms_webhooks_item_model = UpdateAlertPolicyInputMechanismsWebhooksItem.from_dict(update_alert_policy_input_mechanisms_webhooks_item_model_json)
        assert update_alert_policy_input_mechanisms_webhooks_item_model != False

        # Construct a model instance of UpdateAlertPolicyInputMechanismsWebhooksItem by calling from_dict on the json representation
        update_alert_policy_input_mechanisms_webhooks_item_model_dict = UpdateAlertPolicyInputMechanismsWebhooksItem.from_dict(update_alert_policy_input_mechanisms_webhooks_item_model_json).__dict__
        update_alert_policy_input_mechanisms_webhooks_item_model2 = UpdateAlertPolicyInputMechanismsWebhooksItem(**update_alert_policy_input_mechanisms_webhooks_item_model_dict)

        # Verify the model instances are equivalent
        assert update_alert_policy_input_mechanisms_webhooks_item_model == update_alert_policy_input_mechanisms_webhooks_item_model2

        # Convert model instance back to dict and verify no loss of data
        update_alert_policy_input_mechanisms_webhooks_item_model_json2 = update_alert_policy_input_mechanisms_webhooks_item_model.to_dict()
        assert update_alert_policy_input_mechanisms_webhooks_item_model_json2 == update_alert_policy_input_mechanisms_webhooks_item_model_json

class TestModel_AlertSuccessResp():
    """
    Test Class for AlertSuccessResp
    """

    def test_alert_success_resp_serialization(self):
        """
        Test serialization/deserialization for AlertSuccessResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        alert_success_resp_errors_item_model = {} # AlertSuccessRespErrorsItem
        alert_success_resp_errors_item_model['id'] = 'testString'

        alert_success_resp_messages_item_model = {} # AlertSuccessRespMessagesItem
        alert_success_resp_messages_item_model['id'] = 'testString'

        alert_success_resp_result_model = {} # AlertSuccessRespResult
        alert_success_resp_result_model['id'] = 'f0413b106d2c4aa9b1553d5d0209c522'

        # Construct a json representation of a AlertSuccessResp model
        alert_success_resp_model_json = {}
        alert_success_resp_model_json['success'] = True
        alert_success_resp_model_json['errors'] = [alert_success_resp_errors_item_model]
        alert_success_resp_model_json['messages'] = [alert_success_resp_messages_item_model]
        alert_success_resp_model_json['result'] = alert_success_resp_result_model

        # Construct a model instance of AlertSuccessResp by calling from_dict on the json representation
        alert_success_resp_model = AlertSuccessResp.from_dict(alert_success_resp_model_json)
        assert alert_success_resp_model != False

        # Construct a model instance of AlertSuccessResp by calling from_dict on the json representation
        alert_success_resp_model_dict = AlertSuccessResp.from_dict(alert_success_resp_model_json).__dict__
        alert_success_resp_model2 = AlertSuccessResp(**alert_success_resp_model_dict)

        # Verify the model instances are equivalent
        assert alert_success_resp_model == alert_success_resp_model2

        # Convert model instance back to dict and verify no loss of data
        alert_success_resp_model_json2 = alert_success_resp_model.to_dict()
        assert alert_success_resp_model_json2 == alert_success_resp_model_json

class TestModel_GetAlertPolicyResp():
    """
    Test Class for GetAlertPolicyResp
    """

    def test_get_alert_policy_resp_serialization(self):
        """
        Test serialization/deserialization for GetAlertPolicyResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        get_alert_policy_resp_errors_item_model = {} # GetAlertPolicyRespErrorsItem
        get_alert_policy_resp_errors_item_model['id'] = 'testString'

        get_alert_policy_resp_messages_item_model = {} # GetAlertPolicyRespMessagesItem
        get_alert_policy_resp_messages_item_model['id'] = 'testString'

        get_alert_policy_resp_result_mechanisms_email_item_model = {} # GetAlertPolicyRespResultMechanismsEmailItem
        get_alert_policy_resp_result_mechanisms_email_item_model['id'] = 'mynotifications@email.com'

        get_alert_policy_resp_result_mechanisms_webhooks_item_model = {} # GetAlertPolicyRespResultMechanismsWebhooksItem
        get_alert_policy_resp_result_mechanisms_webhooks_item_model['id'] = 'f0413b106d2c4aa9b1553d5d0209c522'

        get_alert_policy_resp_result_mechanisms_model = {} # GetAlertPolicyRespResultMechanisms
        get_alert_policy_resp_result_mechanisms_model['email'] = [get_alert_policy_resp_result_mechanisms_email_item_model]
        get_alert_policy_resp_result_mechanisms_model['webhooks'] = [get_alert_policy_resp_result_mechanisms_webhooks_item_model]

        get_alert_policy_resp_result_model = {} # GetAlertPolicyRespResult
        get_alert_policy_resp_result_model['id'] = 'f0413b106d2c4aa9b1553d5d0209c522'
        get_alert_policy_resp_result_model['name'] = 'My Alert Policy'
        get_alert_policy_resp_result_model['description'] = 'Description for my alert policy'
        get_alert_policy_resp_result_model['enabled'] = True
        get_alert_policy_resp_result_model['alert_type'] = 'dos_attack_l7'
        get_alert_policy_resp_result_model['mechanisms'] = get_alert_policy_resp_result_mechanisms_model
        get_alert_policy_resp_result_model['created'] = '2021-09-15T16:33:31.834209Z'
        get_alert_policy_resp_result_model['modified'] = '2021-09-15T16:33:31.834209Z'
        get_alert_policy_resp_result_model['conditions'] = { 'foo': 'bar' }
        get_alert_policy_resp_result_model['filters'] = { 'foo': 'bar' }

        # Construct a json representation of a GetAlertPolicyResp model
        get_alert_policy_resp_model_json = {}
        get_alert_policy_resp_model_json['success'] = True
        get_alert_policy_resp_model_json['errors'] = [get_alert_policy_resp_errors_item_model]
        get_alert_policy_resp_model_json['messages'] = [get_alert_policy_resp_messages_item_model]
        get_alert_policy_resp_model_json['result'] = get_alert_policy_resp_result_model

        # Construct a model instance of GetAlertPolicyResp by calling from_dict on the json representation
        get_alert_policy_resp_model = GetAlertPolicyResp.from_dict(get_alert_policy_resp_model_json)
        assert get_alert_policy_resp_model != False

        # Construct a model instance of GetAlertPolicyResp by calling from_dict on the json representation
        get_alert_policy_resp_model_dict = GetAlertPolicyResp.from_dict(get_alert_policy_resp_model_json).__dict__
        get_alert_policy_resp_model2 = GetAlertPolicyResp(**get_alert_policy_resp_model_dict)

        # Verify the model instances are equivalent
        assert get_alert_policy_resp_model == get_alert_policy_resp_model2

        # Convert model instance back to dict and verify no loss of data
        get_alert_policy_resp_model_json2 = get_alert_policy_resp_model.to_dict()
        assert get_alert_policy_resp_model_json2 == get_alert_policy_resp_model_json

class TestModel_ListAlertPoliciesResp():
    """
    Test Class for ListAlertPoliciesResp
    """

    def test_list_alert_policies_resp_serialization(self):
        """
        Test serialization/deserialization for ListAlertPoliciesResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        list_alert_policies_resp_errors_item_model = {} # ListAlertPoliciesRespErrorsItem
        list_alert_policies_resp_errors_item_model['id'] = 'testString'

        list_alert_policies_resp_messages_item_model = {} # ListAlertPoliciesRespMessagesItem
        list_alert_policies_resp_messages_item_model['id'] = 'testString'

        list_alert_policies_resp_result_item_mechanisms_email_item_model = {} # ListAlertPoliciesRespResultItemMechanismsEmailItem
        list_alert_policies_resp_result_item_mechanisms_email_item_model['id'] = 'mynotifications@email.com'

        list_alert_policies_resp_result_item_mechanisms_webhooks_item_model = {} # ListAlertPoliciesRespResultItemMechanismsWebhooksItem
        list_alert_policies_resp_result_item_mechanisms_webhooks_item_model['id'] = 'f0413b106d2c4aa9b1553d5d0209c522'

        list_alert_policies_resp_result_item_mechanisms_model = {} # ListAlertPoliciesRespResultItemMechanisms
        list_alert_policies_resp_result_item_mechanisms_model['email'] = [list_alert_policies_resp_result_item_mechanisms_email_item_model]
        list_alert_policies_resp_result_item_mechanisms_model['webhooks'] = [list_alert_policies_resp_result_item_mechanisms_webhooks_item_model]

        list_alert_policies_resp_result_item_model = {} # ListAlertPoliciesRespResultItem
        list_alert_policies_resp_result_item_model['id'] = 'f0413b106d2c4aa9b1553d5d0209c522'
        list_alert_policies_resp_result_item_model['name'] = 'My Alert Policy'
        list_alert_policies_resp_result_item_model['description'] = 'Description for my alert policy'
        list_alert_policies_resp_result_item_model['enabled'] = True
        list_alert_policies_resp_result_item_model['alert_type'] = 'dos_attack_l7'
        list_alert_policies_resp_result_item_model['mechanisms'] = list_alert_policies_resp_result_item_mechanisms_model
        list_alert_policies_resp_result_item_model['created'] = '2021-09-15T16:33:31.834209Z'
        list_alert_policies_resp_result_item_model['modified'] = '2021-09-15T16:33:31.834209Z'
        list_alert_policies_resp_result_item_model['conditions'] = { 'foo': 'bar' }
        list_alert_policies_resp_result_item_model['filters'] = { 'foo': 'bar' }

        # Construct a json representation of a ListAlertPoliciesResp model
        list_alert_policies_resp_model_json = {}
        list_alert_policies_resp_model_json['success'] = True
        list_alert_policies_resp_model_json['errors'] = [list_alert_policies_resp_errors_item_model]
        list_alert_policies_resp_model_json['messages'] = [list_alert_policies_resp_messages_item_model]
        list_alert_policies_resp_model_json['result'] = [list_alert_policies_resp_result_item_model]

        # Construct a model instance of ListAlertPoliciesResp by calling from_dict on the json representation
        list_alert_policies_resp_model = ListAlertPoliciesResp.from_dict(list_alert_policies_resp_model_json)
        assert list_alert_policies_resp_model != False

        # Construct a model instance of ListAlertPoliciesResp by calling from_dict on the json representation
        list_alert_policies_resp_model_dict = ListAlertPoliciesResp.from_dict(list_alert_policies_resp_model_json).__dict__
        list_alert_policies_resp_model2 = ListAlertPoliciesResp(**list_alert_policies_resp_model_dict)

        # Verify the model instances are equivalent
        assert list_alert_policies_resp_model == list_alert_policies_resp_model2

        # Convert model instance back to dict and verify no loss of data
        list_alert_policies_resp_model_json2 = list_alert_policies_resp_model.to_dict()
        assert list_alert_policies_resp_model_json2 == list_alert_policies_resp_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
