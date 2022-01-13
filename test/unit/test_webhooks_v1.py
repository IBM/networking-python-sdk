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
Unit Tests for WebhooksV1
"""

from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import os
import pytest
import re
import responses
import urllib
from ibm_cloud_networking_services.webhooks_v1 import *

crn = 'testString'

_service = WebhooksV1(
    authenticator=NoAuthAuthenticator(),
    crn=crn
)

_base_url = 'https://api.cis.cloud.ibm.com'
_service.set_service_url(_base_url)

##############################################################################
# Start of Service: AlertWebhooks
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

        service = WebhooksV1.new_instance(
            crn=crn,
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, WebhooksV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = WebhooksV1.new_instance(
                crn=crn,
            )

    def test_new_instance_without_required_params(self):
        """
        new_instance_without_required_params()
        """
        with pytest.raises(TypeError, match='new_instance\\(\\) missing \\d required positional arguments?: \'.*\''):
            service = WebhooksV1.new_instance()

    def test_new_instance_required_param_none(self):
        """
        new_instance_required_param_none()
        """
        with pytest.raises(ValueError, match='crn must be provided'):
            service = WebhooksV1.new_instance(
                crn=None,
            )
class TestGetAlertWebhooks():
    """
    Test Class for get_alert_webhooks
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
    def test_get_alert_webhooks_all_params(self):
        """
        get_alert_webhooks()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/alerting/destinations/webhooks')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "6d16fcab-3e80-44b3-b59b-a3716237832e", "name": "My Slack Alert Webhook", "url": "https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd", "type": "generic", "created_at": "2021-09-15T16:33:31.834209Z", "last_success": "2021-09-15T16:33:31.834209Z", "last_failure": "2021-09-15T16:33:31.834209Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.get_alert_webhooks()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_alert_webhooks_all_params_with_retries(self):
        # Enable retries and run test_get_alert_webhooks_all_params.
        _service.enable_retries()
        self.test_get_alert_webhooks_all_params()

        # Disable retries and run test_get_alert_webhooks_all_params.
        _service.disable_retries()
        self.test_get_alert_webhooks_all_params()

    @responses.activate
    def test_get_alert_webhooks_value_error(self):
        """
        test_get_alert_webhooks_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/alerting/destinations/webhooks')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "6d16fcab-3e80-44b3-b59b-a3716237832e", "name": "My Slack Alert Webhook", "url": "https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd", "type": "generic", "created_at": "2021-09-15T16:33:31.834209Z", "last_success": "2021-09-15T16:33:31.834209Z", "last_failure": "2021-09-15T16:33:31.834209Z"}]}'
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
                _service.get_alert_webhooks(**req_copy)


    def test_get_alert_webhooks_value_error_with_retries(self):
        # Enable retries and run test_get_alert_webhooks_value_error.
        _service.enable_retries()
        self.test_get_alert_webhooks_value_error()

        # Disable retries and run test_get_alert_webhooks_value_error.
        _service.disable_retries()
        self.test_get_alert_webhooks_value_error()

class TestCreateAlertWebhook():
    """
    Test Class for create_alert_webhook
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
    def test_create_alert_webhook_all_params(self):
        """
        create_alert_webhook()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/alerting/destinations/webhooks')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "6d16fcab-3e80-44b3-b59b-a3716237832e"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        name = 'My Slack Alert Webhook'
        url = 'https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd'
        secret = 'ff1d9b80-b51d-4a06-bf67-6752fae1eb74'

        # Invoke method
        response = _service.create_alert_webhook(
            name=name,
            url=url,
            secret=secret,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'My Slack Alert Webhook'
        assert req_body['url'] == 'https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd'
        assert req_body['secret'] == 'ff1d9b80-b51d-4a06-bf67-6752fae1eb74'

    def test_create_alert_webhook_all_params_with_retries(self):
        # Enable retries and run test_create_alert_webhook_all_params.
        _service.enable_retries()
        self.test_create_alert_webhook_all_params()

        # Disable retries and run test_create_alert_webhook_all_params.
        _service.disable_retries()
        self.test_create_alert_webhook_all_params()

    @responses.activate
    def test_create_alert_webhook_required_params(self):
        """
        test_create_alert_webhook_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/alerting/destinations/webhooks')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "6d16fcab-3e80-44b3-b59b-a3716237832e"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.create_alert_webhook()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_create_alert_webhook_required_params_with_retries(self):
        # Enable retries and run test_create_alert_webhook_required_params.
        _service.enable_retries()
        self.test_create_alert_webhook_required_params()

        # Disable retries and run test_create_alert_webhook_required_params.
        _service.disable_retries()
        self.test_create_alert_webhook_required_params()

    @responses.activate
    def test_create_alert_webhook_value_error(self):
        """
        test_create_alert_webhook_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/alerting/destinations/webhooks')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "6d16fcab-3e80-44b3-b59b-a3716237832e"}}'
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
                _service.create_alert_webhook(**req_copy)


    def test_create_alert_webhook_value_error_with_retries(self):
        # Enable retries and run test_create_alert_webhook_value_error.
        _service.enable_retries()
        self.test_create_alert_webhook_value_error()

        # Disable retries and run test_create_alert_webhook_value_error.
        _service.disable_retries()
        self.test_create_alert_webhook_value_error()

class TestGetAlertWebhook():
    """
    Test Class for get_alert_webhook
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
    def test_get_alert_webhook_all_params(self):
        """
        get_alert_webhook()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/alerting/destinations/webhooks/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "6d16fcab-3e80-44b3-b59b-a3716237832e", "name": "My Slack Alert Webhook", "url": "https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd", "type": "generic", "created_at": "2021-09-15T16:33:31.834209Z", "last_success": "2021-09-15T16:33:31.834209Z", "last_failure": "2021-09-15T16:33:31.834209Z"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        webhook_id = 'testString'

        # Invoke method
        response = _service.get_alert_webhook(
            webhook_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_alert_webhook_all_params_with_retries(self):
        # Enable retries and run test_get_alert_webhook_all_params.
        _service.enable_retries()
        self.test_get_alert_webhook_all_params()

        # Disable retries and run test_get_alert_webhook_all_params.
        _service.disable_retries()
        self.test_get_alert_webhook_all_params()

    @responses.activate
    def test_get_alert_webhook_value_error(self):
        """
        test_get_alert_webhook_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/alerting/destinations/webhooks/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "6d16fcab-3e80-44b3-b59b-a3716237832e", "name": "My Slack Alert Webhook", "url": "https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd", "type": "generic", "created_at": "2021-09-15T16:33:31.834209Z", "last_success": "2021-09-15T16:33:31.834209Z", "last_failure": "2021-09-15T16:33:31.834209Z"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        webhook_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "webhook_id": webhook_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_alert_webhook(**req_copy)


    def test_get_alert_webhook_value_error_with_retries(self):
        # Enable retries and run test_get_alert_webhook_value_error.
        _service.enable_retries()
        self.test_get_alert_webhook_value_error()

        # Disable retries and run test_get_alert_webhook_value_error.
        _service.disable_retries()
        self.test_get_alert_webhook_value_error()

class TestUpdateAlertWebhook():
    """
    Test Class for update_alert_webhook
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
    def test_update_alert_webhook_all_params(self):
        """
        update_alert_webhook()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/alerting/destinations/webhooks/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "6d16fcab-3e80-44b3-b59b-a3716237832e"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        webhook_id = 'testString'
        name = 'My Slack Alert Webhook'
        url = 'https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd'
        secret = 'ff1d9b80-b51d-4a06-bf67-6752fae1eb74'

        # Invoke method
        response = _service.update_alert_webhook(
            webhook_id,
            name=name,
            url=url,
            secret=secret,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'My Slack Alert Webhook'
        assert req_body['url'] == 'https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd'
        assert req_body['secret'] == 'ff1d9b80-b51d-4a06-bf67-6752fae1eb74'

    def test_update_alert_webhook_all_params_with_retries(self):
        # Enable retries and run test_update_alert_webhook_all_params.
        _service.enable_retries()
        self.test_update_alert_webhook_all_params()

        # Disable retries and run test_update_alert_webhook_all_params.
        _service.disable_retries()
        self.test_update_alert_webhook_all_params()

    @responses.activate
    def test_update_alert_webhook_required_params(self):
        """
        test_update_alert_webhook_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/alerting/destinations/webhooks/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "6d16fcab-3e80-44b3-b59b-a3716237832e"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        webhook_id = 'testString'

        # Invoke method
        response = _service.update_alert_webhook(
            webhook_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_alert_webhook_required_params_with_retries(self):
        # Enable retries and run test_update_alert_webhook_required_params.
        _service.enable_retries()
        self.test_update_alert_webhook_required_params()

        # Disable retries and run test_update_alert_webhook_required_params.
        _service.disable_retries()
        self.test_update_alert_webhook_required_params()

    @responses.activate
    def test_update_alert_webhook_value_error(self):
        """
        test_update_alert_webhook_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/alerting/destinations/webhooks/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "6d16fcab-3e80-44b3-b59b-a3716237832e"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        webhook_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "webhook_id": webhook_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_alert_webhook(**req_copy)


    def test_update_alert_webhook_value_error_with_retries(self):
        # Enable retries and run test_update_alert_webhook_value_error.
        _service.enable_retries()
        self.test_update_alert_webhook_value_error()

        # Disable retries and run test_update_alert_webhook_value_error.
        _service.disable_retries()
        self.test_update_alert_webhook_value_error()

class TestDeleteAlertWebhook():
    """
    Test Class for delete_alert_webhook
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
    def test_delete_alert_webhook_all_params(self):
        """
        delete_alert_webhook()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/alerting/destinations/webhooks/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "6d16fcab-3e80-44b3-b59b-a3716237832e"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        webhook_id = 'testString'

        # Invoke method
        response = _service.delete_alert_webhook(
            webhook_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_delete_alert_webhook_all_params_with_retries(self):
        # Enable retries and run test_delete_alert_webhook_all_params.
        _service.enable_retries()
        self.test_delete_alert_webhook_all_params()

        # Disable retries and run test_delete_alert_webhook_all_params.
        _service.disable_retries()
        self.test_delete_alert_webhook_all_params()

    @responses.activate
    def test_delete_alert_webhook_value_error(self):
        """
        test_delete_alert_webhook_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/alerting/destinations/webhooks/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "6d16fcab-3e80-44b3-b59b-a3716237832e"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        webhook_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "webhook_id": webhook_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_alert_webhook(**req_copy)


    def test_delete_alert_webhook_value_error_with_retries(self):
        # Enable retries and run test_delete_alert_webhook_value_error.
        _service.enable_retries()
        self.test_delete_alert_webhook_value_error()

        # Disable retries and run test_delete_alert_webhook_value_error.
        _service.disable_retries()
        self.test_delete_alert_webhook_value_error()

# endregion
##############################################################################
# End of Service: AlertWebhooks
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestModel_GetAlertWebhookRespResult():
    """
    Test Class for GetAlertWebhookRespResult
    """

    def test_get_alert_webhook_resp_result_serialization(self):
        """
        Test serialization/deserialization for GetAlertWebhookRespResult
        """

        # Construct a json representation of a GetAlertWebhookRespResult model
        get_alert_webhook_resp_result_model_json = {}
        get_alert_webhook_resp_result_model_json['id'] = '6d16fcab-3e80-44b3-b59b-a3716237832e'
        get_alert_webhook_resp_result_model_json['name'] = 'My Slack Alert Webhook'
        get_alert_webhook_resp_result_model_json['url'] = 'https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd'
        get_alert_webhook_resp_result_model_json['type'] = 'generic'
        get_alert_webhook_resp_result_model_json['created_at'] = '2021-09-15T16:33:31.834209Z'
        get_alert_webhook_resp_result_model_json['last_success'] = '2021-09-15T16:33:31.834209Z'
        get_alert_webhook_resp_result_model_json['last_failure'] = '2021-09-15T16:33:31.834209Z'

        # Construct a model instance of GetAlertWebhookRespResult by calling from_dict on the json representation
        get_alert_webhook_resp_result_model = GetAlertWebhookRespResult.from_dict(get_alert_webhook_resp_result_model_json)
        assert get_alert_webhook_resp_result_model != False

        # Construct a model instance of GetAlertWebhookRespResult by calling from_dict on the json representation
        get_alert_webhook_resp_result_model_dict = GetAlertWebhookRespResult.from_dict(get_alert_webhook_resp_result_model_json).__dict__
        get_alert_webhook_resp_result_model2 = GetAlertWebhookRespResult(**get_alert_webhook_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert get_alert_webhook_resp_result_model == get_alert_webhook_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        get_alert_webhook_resp_result_model_json2 = get_alert_webhook_resp_result_model.to_dict()
        assert get_alert_webhook_resp_result_model_json2 == get_alert_webhook_resp_result_model_json

class TestModel_ListAlertWebhooksRespResultItem():
    """
    Test Class for ListAlertWebhooksRespResultItem
    """

    def test_list_alert_webhooks_resp_result_item_serialization(self):
        """
        Test serialization/deserialization for ListAlertWebhooksRespResultItem
        """

        # Construct a json representation of a ListAlertWebhooksRespResultItem model
        list_alert_webhooks_resp_result_item_model_json = {}
        list_alert_webhooks_resp_result_item_model_json['id'] = '6d16fcab-3e80-44b3-b59b-a3716237832e'
        list_alert_webhooks_resp_result_item_model_json['name'] = 'My Slack Alert Webhook'
        list_alert_webhooks_resp_result_item_model_json['url'] = 'https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd'
        list_alert_webhooks_resp_result_item_model_json['type'] = 'generic'
        list_alert_webhooks_resp_result_item_model_json['created_at'] = '2021-09-15T16:33:31.834209Z'
        list_alert_webhooks_resp_result_item_model_json['last_success'] = '2021-09-15T16:33:31.834209Z'
        list_alert_webhooks_resp_result_item_model_json['last_failure'] = '2021-09-15T16:33:31.834209Z'

        # Construct a model instance of ListAlertWebhooksRespResultItem by calling from_dict on the json representation
        list_alert_webhooks_resp_result_item_model = ListAlertWebhooksRespResultItem.from_dict(list_alert_webhooks_resp_result_item_model_json)
        assert list_alert_webhooks_resp_result_item_model != False

        # Construct a model instance of ListAlertWebhooksRespResultItem by calling from_dict on the json representation
        list_alert_webhooks_resp_result_item_model_dict = ListAlertWebhooksRespResultItem.from_dict(list_alert_webhooks_resp_result_item_model_json).__dict__
        list_alert_webhooks_resp_result_item_model2 = ListAlertWebhooksRespResultItem(**list_alert_webhooks_resp_result_item_model_dict)

        # Verify the model instances are equivalent
        assert list_alert_webhooks_resp_result_item_model == list_alert_webhooks_resp_result_item_model2

        # Convert model instance back to dict and verify no loss of data
        list_alert_webhooks_resp_result_item_model_json2 = list_alert_webhooks_resp_result_item_model.to_dict()
        assert list_alert_webhooks_resp_result_item_model_json2 == list_alert_webhooks_resp_result_item_model_json

class TestModel_WebhookSuccessRespResult():
    """
    Test Class for WebhookSuccessRespResult
    """

    def test_webhook_success_resp_result_serialization(self):
        """
        Test serialization/deserialization for WebhookSuccessRespResult
        """

        # Construct a json representation of a WebhookSuccessRespResult model
        webhook_success_resp_result_model_json = {}
        webhook_success_resp_result_model_json['id'] = '6d16fcab-3e80-44b3-b59b-a3716237832e'

        # Construct a model instance of WebhookSuccessRespResult by calling from_dict on the json representation
        webhook_success_resp_result_model = WebhookSuccessRespResult.from_dict(webhook_success_resp_result_model_json)
        assert webhook_success_resp_result_model != False

        # Construct a model instance of WebhookSuccessRespResult by calling from_dict on the json representation
        webhook_success_resp_result_model_dict = WebhookSuccessRespResult.from_dict(webhook_success_resp_result_model_json).__dict__
        webhook_success_resp_result_model2 = WebhookSuccessRespResult(**webhook_success_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert webhook_success_resp_result_model == webhook_success_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        webhook_success_resp_result_model_json2 = webhook_success_resp_result_model.to_dict()
        assert webhook_success_resp_result_model_json2 == webhook_success_resp_result_model_json

class TestModel_GetAlertWebhookResp():
    """
    Test Class for GetAlertWebhookResp
    """

    def test_get_alert_webhook_resp_serialization(self):
        """
        Test serialization/deserialization for GetAlertWebhookResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        get_alert_webhook_resp_result_model = {} # GetAlertWebhookRespResult
        get_alert_webhook_resp_result_model['id'] = '6d16fcab-3e80-44b3-b59b-a3716237832e'
        get_alert_webhook_resp_result_model['name'] = 'My Slack Alert Webhook'
        get_alert_webhook_resp_result_model['url'] = 'https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd'
        get_alert_webhook_resp_result_model['type'] = 'generic'
        get_alert_webhook_resp_result_model['created_at'] = '2021-09-15T16:33:31.834209Z'
        get_alert_webhook_resp_result_model['last_success'] = '2021-09-15T16:33:31.834209Z'
        get_alert_webhook_resp_result_model['last_failure'] = '2021-09-15T16:33:31.834209Z'

        # Construct a json representation of a GetAlertWebhookResp model
        get_alert_webhook_resp_model_json = {}
        get_alert_webhook_resp_model_json['success'] = True
        get_alert_webhook_resp_model_json['errors'] = [['testString']]
        get_alert_webhook_resp_model_json['messages'] = [['testString']]
        get_alert_webhook_resp_model_json['result'] = get_alert_webhook_resp_result_model

        # Construct a model instance of GetAlertWebhookResp by calling from_dict on the json representation
        get_alert_webhook_resp_model = GetAlertWebhookResp.from_dict(get_alert_webhook_resp_model_json)
        assert get_alert_webhook_resp_model != False

        # Construct a model instance of GetAlertWebhookResp by calling from_dict on the json representation
        get_alert_webhook_resp_model_dict = GetAlertWebhookResp.from_dict(get_alert_webhook_resp_model_json).__dict__
        get_alert_webhook_resp_model2 = GetAlertWebhookResp(**get_alert_webhook_resp_model_dict)

        # Verify the model instances are equivalent
        assert get_alert_webhook_resp_model == get_alert_webhook_resp_model2

        # Convert model instance back to dict and verify no loss of data
        get_alert_webhook_resp_model_json2 = get_alert_webhook_resp_model.to_dict()
        assert get_alert_webhook_resp_model_json2 == get_alert_webhook_resp_model_json

class TestModel_ListAlertWebhooksResp():
    """
    Test Class for ListAlertWebhooksResp
    """

    def test_list_alert_webhooks_resp_serialization(self):
        """
        Test serialization/deserialization for ListAlertWebhooksResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        list_alert_webhooks_resp_result_item_model = {} # ListAlertWebhooksRespResultItem
        list_alert_webhooks_resp_result_item_model['id'] = '6d16fcab-3e80-44b3-b59b-a3716237832e'
        list_alert_webhooks_resp_result_item_model['name'] = 'My Slack Alert Webhook'
        list_alert_webhooks_resp_result_item_model['url'] = 'https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd'
        list_alert_webhooks_resp_result_item_model['type'] = 'generic'
        list_alert_webhooks_resp_result_item_model['created_at'] = '2021-09-15T16:33:31.834209Z'
        list_alert_webhooks_resp_result_item_model['last_success'] = '2021-09-15T16:33:31.834209Z'
        list_alert_webhooks_resp_result_item_model['last_failure'] = '2021-09-15T16:33:31.834209Z'

        # Construct a json representation of a ListAlertWebhooksResp model
        list_alert_webhooks_resp_model_json = {}
        list_alert_webhooks_resp_model_json['success'] = True
        list_alert_webhooks_resp_model_json['errors'] = [['testString']]
        list_alert_webhooks_resp_model_json['messages'] = [['testString']]
        list_alert_webhooks_resp_model_json['result'] = [list_alert_webhooks_resp_result_item_model]

        # Construct a model instance of ListAlertWebhooksResp by calling from_dict on the json representation
        list_alert_webhooks_resp_model = ListAlertWebhooksResp.from_dict(list_alert_webhooks_resp_model_json)
        assert list_alert_webhooks_resp_model != False

        # Construct a model instance of ListAlertWebhooksResp by calling from_dict on the json representation
        list_alert_webhooks_resp_model_dict = ListAlertWebhooksResp.from_dict(list_alert_webhooks_resp_model_json).__dict__
        list_alert_webhooks_resp_model2 = ListAlertWebhooksResp(**list_alert_webhooks_resp_model_dict)

        # Verify the model instances are equivalent
        assert list_alert_webhooks_resp_model == list_alert_webhooks_resp_model2

        # Convert model instance back to dict and verify no loss of data
        list_alert_webhooks_resp_model_json2 = list_alert_webhooks_resp_model.to_dict()
        assert list_alert_webhooks_resp_model_json2 == list_alert_webhooks_resp_model_json

class TestModel_WebhookSuccessResp():
    """
    Test Class for WebhookSuccessResp
    """

    def test_webhook_success_resp_serialization(self):
        """
        Test serialization/deserialization for WebhookSuccessResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        webhook_success_resp_result_model = {} # WebhookSuccessRespResult
        webhook_success_resp_result_model['id'] = '6d16fcab-3e80-44b3-b59b-a3716237832e'

        # Construct a json representation of a WebhookSuccessResp model
        webhook_success_resp_model_json = {}
        webhook_success_resp_model_json['success'] = True
        webhook_success_resp_model_json['errors'] = [['testString']]
        webhook_success_resp_model_json['messages'] = [['testString']]
        webhook_success_resp_model_json['result'] = webhook_success_resp_result_model

        # Construct a model instance of WebhookSuccessResp by calling from_dict on the json representation
        webhook_success_resp_model = WebhookSuccessResp.from_dict(webhook_success_resp_model_json)
        assert webhook_success_resp_model != False

        # Construct a model instance of WebhookSuccessResp by calling from_dict on the json representation
        webhook_success_resp_model_dict = WebhookSuccessResp.from_dict(webhook_success_resp_model_json).__dict__
        webhook_success_resp_model2 = WebhookSuccessResp(**webhook_success_resp_model_dict)

        # Verify the model instances are equivalent
        assert webhook_success_resp_model == webhook_success_resp_model2

        # Convert model instance back to dict and verify no loss of data
        webhook_success_resp_model_json2 = webhook_success_resp_model.to_dict()
        assert webhook_success_resp_model_json2 == webhook_success_resp_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
