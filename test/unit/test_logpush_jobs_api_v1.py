# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2026.
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
Unit Tests for LogpushJobsApiV1
"""

from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import os
import pytest
import re
import responses
import urllib
from ibm_cloud_networking_services.logpush_jobs_api_v1 import *

crn = 'testString'
dataset = 'testString'
zone_id = 'testString'

_service = LogpushJobsApiV1(
    authenticator=NoAuthAuthenticator(),
    crn=crn,
    dataset=dataset,
    zone_id=zone_id,
)

_base_url = 'https://api.cis.cloud.ibm.com'
_service.set_service_url(_base_url)


def preprocess_url(operation_path: str):
    """
    Returns the request url associated with the specified operation path.
    This will be base_url concatenated with a quoted version of operation_path.
    The returned request URL is used to register the mock response so it needs
    to match the request URL that is formed by the requests library.
    """

    # Form the request URL from the base URL and operation path.
    request_url = _base_url + operation_path

    # If the request url does NOT end with a /, then just return it as-is.
    # Otherwise, return a regular expression that matches one or more trailing /.
    if not request_url.endswith('/'):
        return request_url
    return re.compile(request_url.rstrip('/') + '/+')


##############################################################################
# Start of Service: LogpushJobs
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = LogpushJobsApiV1.new_instance(
            crn=crn,
            dataset=dataset,
            zone_id=zone_id,
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, LogpushJobsApiV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = LogpushJobsApiV1.new_instance(
                crn=crn,
                dataset=dataset,
                zone_id=zone_id,
                service_name='TEST_SERVICE_NOT_FOUND',
            )

    def test_new_instance_without_required_params(self):
        """
        new_instance_without_required_params()
        """
        with pytest.raises(TypeError, match='new_instance\\(\\) missing \\d required positional arguments?: \'.*\''):
            service = LogpushJobsApiV1.new_instance()

    def test_new_instance_required_param_none(self):
        """
        new_instance_required_param_none()
        """
        with pytest.raises(ValueError, match='crn must be provided'):
            service = LogpushJobsApiV1.new_instance(
                crn=None,
                dataset=None,
                zone_id=None,
            )


class TestGetLogpushJobsV2:
    """
    Test Class for get_logpush_jobs_v2
    """

    @responses.activate
    def test_get_logpush_jobs_v2_all_params(self):
        """
        get_logpush_jobs_v2()
        """
        # Set up mock
        url = preprocess_url('/v2/testString/zones/testString/logpush/jobs')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": 5850, "name": "My log push job", "enabled": false, "dataset": "firewall_events", "frequency": "high", "logpull_options": "timestamps=rfc3339&timestamps=rfc3339", "destination_conf": "cos://cos-bucket001?region=us-south&instance-id=231f5467-3072-4cb9-9e39-a906fa3032ea", "last_complete": "2022-01-15T16:33:31.834209Z", "last_error": "2022-01-15T16:33:31.834209Z", "error_message": "error_message"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_logpush_jobs_v2()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_logpush_jobs_v2_all_params_with_retries(self):
        # Enable retries and run test_get_logpush_jobs_v2_all_params.
        _service.enable_retries()
        self.test_get_logpush_jobs_v2_all_params()

        # Disable retries and run test_get_logpush_jobs_v2_all_params.
        _service.disable_retries()
        self.test_get_logpush_jobs_v2_all_params()

    @responses.activate
    def test_get_logpush_jobs_v2_value_error(self):
        """
        test_get_logpush_jobs_v2_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/testString/zones/testString/logpush/jobs')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": 5850, "name": "My log push job", "enabled": false, "dataset": "firewall_events", "frequency": "high", "logpull_options": "timestamps=rfc3339&timestamps=rfc3339", "destination_conf": "cos://cos-bucket001?region=us-south&instance-id=231f5467-3072-4cb9-9e39-a906fa3032ea", "last_complete": "2022-01-15T16:33:31.834209Z", "last_error": "2022-01-15T16:33:31.834209Z", "error_message": "error_message"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_logpush_jobs_v2(**req_copy)

    def test_get_logpush_jobs_v2_value_error_with_retries(self):
        # Enable retries and run test_get_logpush_jobs_v2_value_error.
        _service.enable_retries()
        self.test_get_logpush_jobs_v2_value_error()

        # Disable retries and run test_get_logpush_jobs_v2_value_error.
        _service.disable_retries()
        self.test_get_logpush_jobs_v2_value_error()


class TestCreateLogpushJobV2:
    """
    Test Class for create_logpush_job_v2
    """

    @responses.activate
    def test_create_logpush_job_v2_all_params(self):
        """
        create_logpush_job_v2()
        """
        # Set up mock
        url = preprocess_url('/v2/testString/zones/testString/logpush/jobs')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": 5850, "name": "My log push job", "enabled": false, "dataset": "firewall_events", "frequency": "high", "logpull_options": "timestamps=rfc3339&timestamps=rfc3339", "destination_conf": "cos://cos-bucket001?region=us-south&instance-id=231f5467-3072-4cb9-9e39-a906fa3032ea", "last_complete": "2022-01-15T16:33:31.834209Z", "last_error": "2022-01-15T16:33:31.834209Z", "error_message": "error_message"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a CreateLogpushJobV2RequestLogpushJobCosReq model
        create_logpush_job_v2_request_model = {}
        create_logpush_job_v2_request_model['name'] = 'My log push job'
        create_logpush_job_v2_request_model['enabled'] = False
        create_logpush_job_v2_request_model['logpull_options'] = 'timestamps=rfc3339&timestamps=rfc3339'
        create_logpush_job_v2_request_model['cos'] = {'bucket_name': 'cos-bucket001', 'region': 'us-south', 'id': '231f5467-3072-4cb9-9e39-a906fa3032ea'}
        create_logpush_job_v2_request_model['ownership_challenge'] = '00000000000000000000000000000000'
        create_logpush_job_v2_request_model['dataset'] = 'http_requests'
        create_logpush_job_v2_request_model['frequency'] = 'high'

        # Set up parameter values
        create_logpush_job_v2_request = create_logpush_job_v2_request_model

        # Invoke method
        response = _service.create_logpush_job_v2(
            create_logpush_job_v2_request=create_logpush_job_v2_request,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == create_logpush_job_v2_request

    def test_create_logpush_job_v2_all_params_with_retries(self):
        # Enable retries and run test_create_logpush_job_v2_all_params.
        _service.enable_retries()
        self.test_create_logpush_job_v2_all_params()

        # Disable retries and run test_create_logpush_job_v2_all_params.
        _service.disable_retries()
        self.test_create_logpush_job_v2_all_params()

    @responses.activate
    def test_create_logpush_job_v2_required_params(self):
        """
        test_create_logpush_job_v2_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/testString/zones/testString/logpush/jobs')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": 5850, "name": "My log push job", "enabled": false, "dataset": "firewall_events", "frequency": "high", "logpull_options": "timestamps=rfc3339&timestamps=rfc3339", "destination_conf": "cos://cos-bucket001?region=us-south&instance-id=231f5467-3072-4cb9-9e39-a906fa3032ea", "last_complete": "2022-01-15T16:33:31.834209Z", "last_error": "2022-01-15T16:33:31.834209Z", "error_message": "error_message"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.create_logpush_job_v2()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_create_logpush_job_v2_required_params_with_retries(self):
        # Enable retries and run test_create_logpush_job_v2_required_params.
        _service.enable_retries()
        self.test_create_logpush_job_v2_required_params()

        # Disable retries and run test_create_logpush_job_v2_required_params.
        _service.disable_retries()
        self.test_create_logpush_job_v2_required_params()

    @responses.activate
    def test_create_logpush_job_v2_value_error(self):
        """
        test_create_logpush_job_v2_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/testString/zones/testString/logpush/jobs')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": 5850, "name": "My log push job", "enabled": false, "dataset": "firewall_events", "frequency": "high", "logpull_options": "timestamps=rfc3339&timestamps=rfc3339", "destination_conf": "cos://cos-bucket001?region=us-south&instance-id=231f5467-3072-4cb9-9e39-a906fa3032ea", "last_complete": "2022-01-15T16:33:31.834209Z", "last_error": "2022-01-15T16:33:31.834209Z", "error_message": "error_message"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_logpush_job_v2(**req_copy)

    def test_create_logpush_job_v2_value_error_with_retries(self):
        # Enable retries and run test_create_logpush_job_v2_value_error.
        _service.enable_retries()
        self.test_create_logpush_job_v2_value_error()

        # Disable retries and run test_create_logpush_job_v2_value_error.
        _service.disable_retries()
        self.test_create_logpush_job_v2_value_error()


class TestGetLogpushJobV2:
    """
    Test Class for get_logpush_job_v2
    """

    @responses.activate
    def test_get_logpush_job_v2_all_params(self):
        """
        get_logpush_job_v2()
        """
        # Set up mock
        url = preprocess_url('/v2/testString/zones/testString/logpush/jobs/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": 5850, "name": "My log push job", "enabled": false, "dataset": "firewall_events", "frequency": "high", "logpull_options": "timestamps=rfc3339&timestamps=rfc3339", "destination_conf": "cos://cos-bucket001?region=us-south&instance-id=231f5467-3072-4cb9-9e39-a906fa3032ea", "last_complete": "2022-01-15T16:33:31.834209Z", "last_error": "2022-01-15T16:33:31.834209Z", "error_message": "error_message"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        job_id = 'testString'

        # Invoke method
        response = _service.get_logpush_job_v2(
            job_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_logpush_job_v2_all_params_with_retries(self):
        # Enable retries and run test_get_logpush_job_v2_all_params.
        _service.enable_retries()
        self.test_get_logpush_job_v2_all_params()

        # Disable retries and run test_get_logpush_job_v2_all_params.
        _service.disable_retries()
        self.test_get_logpush_job_v2_all_params()

    @responses.activate
    def test_get_logpush_job_v2_value_error(self):
        """
        test_get_logpush_job_v2_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/testString/zones/testString/logpush/jobs/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": 5850, "name": "My log push job", "enabled": false, "dataset": "firewall_events", "frequency": "high", "logpull_options": "timestamps=rfc3339&timestamps=rfc3339", "destination_conf": "cos://cos-bucket001?region=us-south&instance-id=231f5467-3072-4cb9-9e39-a906fa3032ea", "last_complete": "2022-01-15T16:33:31.834209Z", "last_error": "2022-01-15T16:33:31.834209Z", "error_message": "error_message"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        job_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "job_id": job_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_logpush_job_v2(**req_copy)

    def test_get_logpush_job_v2_value_error_with_retries(self):
        # Enable retries and run test_get_logpush_job_v2_value_error.
        _service.enable_retries()
        self.test_get_logpush_job_v2_value_error()

        # Disable retries and run test_get_logpush_job_v2_value_error.
        _service.disable_retries()
        self.test_get_logpush_job_v2_value_error()


class TestUpdateLogpushJobV2:
    """
    Test Class for update_logpush_job_v2
    """

    @responses.activate
    def test_update_logpush_job_v2_all_params(self):
        """
        update_logpush_job_v2()
        """
        # Set up mock
        url = preprocess_url('/v2/testString/zones/testString/logpush/jobs/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": 5850, "name": "My log push job", "enabled": false, "dataset": "firewall_events", "frequency": "high", "logpull_options": "timestamps=rfc3339&timestamps=rfc3339", "destination_conf": "cos://cos-bucket001?region=us-south&instance-id=231f5467-3072-4cb9-9e39-a906fa3032ea", "last_complete": "2022-01-15T16:33:31.834209Z", "last_error": "2022-01-15T16:33:31.834209Z", "error_message": "error_message"}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a UpdateLogpushJobV2RequestLogpushJobsUpdateCosReq model
        update_logpush_job_v2_request_model = {}
        update_logpush_job_v2_request_model['enabled'] = False
        update_logpush_job_v2_request_model['logpull_options'] = 'timestamps=rfc3339&timestamps=rfc3339'
        update_logpush_job_v2_request_model['cos'] = {'bucket_name': 'cos-bucket001', 'region': 'us-south', 'id': '231f5467-3072-4cb9-9e39-a906fa3032ea'}
        update_logpush_job_v2_request_model['ownership_challenge'] = '00000000000000000000000000000000'
        update_logpush_job_v2_request_model['frequency'] = 'high'

        # Set up parameter values
        job_id = 'testString'
        update_logpush_job_v2_request = update_logpush_job_v2_request_model

        # Invoke method
        response = _service.update_logpush_job_v2(
            job_id,
            update_logpush_job_v2_request=update_logpush_job_v2_request,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == update_logpush_job_v2_request

    def test_update_logpush_job_v2_all_params_with_retries(self):
        # Enable retries and run test_update_logpush_job_v2_all_params.
        _service.enable_retries()
        self.test_update_logpush_job_v2_all_params()

        # Disable retries and run test_update_logpush_job_v2_all_params.
        _service.disable_retries()
        self.test_update_logpush_job_v2_all_params()

    @responses.activate
    def test_update_logpush_job_v2_required_params(self):
        """
        test_update_logpush_job_v2_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/testString/zones/testString/logpush/jobs/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": 5850, "name": "My log push job", "enabled": false, "dataset": "firewall_events", "frequency": "high", "logpull_options": "timestamps=rfc3339&timestamps=rfc3339", "destination_conf": "cos://cos-bucket001?region=us-south&instance-id=231f5467-3072-4cb9-9e39-a906fa3032ea", "last_complete": "2022-01-15T16:33:31.834209Z", "last_error": "2022-01-15T16:33:31.834209Z", "error_message": "error_message"}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        job_id = 'testString'

        # Invoke method
        response = _service.update_logpush_job_v2(
            job_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_logpush_job_v2_required_params_with_retries(self):
        # Enable retries and run test_update_logpush_job_v2_required_params.
        _service.enable_retries()
        self.test_update_logpush_job_v2_required_params()

        # Disable retries and run test_update_logpush_job_v2_required_params.
        _service.disable_retries()
        self.test_update_logpush_job_v2_required_params()

    @responses.activate
    def test_update_logpush_job_v2_value_error(self):
        """
        test_update_logpush_job_v2_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/testString/zones/testString/logpush/jobs/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": 5850, "name": "My log push job", "enabled": false, "dataset": "firewall_events", "frequency": "high", "logpull_options": "timestamps=rfc3339&timestamps=rfc3339", "destination_conf": "cos://cos-bucket001?region=us-south&instance-id=231f5467-3072-4cb9-9e39-a906fa3032ea", "last_complete": "2022-01-15T16:33:31.834209Z", "last_error": "2022-01-15T16:33:31.834209Z", "error_message": "error_message"}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        job_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "job_id": job_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_logpush_job_v2(**req_copy)

    def test_update_logpush_job_v2_value_error_with_retries(self):
        # Enable retries and run test_update_logpush_job_v2_value_error.
        _service.enable_retries()
        self.test_update_logpush_job_v2_value_error()

        # Disable retries and run test_update_logpush_job_v2_value_error.
        _service.disable_retries()
        self.test_update_logpush_job_v2_value_error()


class TestDeleteLogpushJobV2:
    """
    Test Class for delete_logpush_job_v2
    """

    @responses.activate
    def test_delete_logpush_job_v2_all_params(self):
        """
        delete_logpush_job_v2()
        """
        # Set up mock
        url = preprocess_url('/v2/testString/zones/testString/logpush/jobs/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"anyKey": "anyValue"}}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        job_id = 'testString'

        # Invoke method
        response = _service.delete_logpush_job_v2(
            job_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_delete_logpush_job_v2_all_params_with_retries(self):
        # Enable retries and run test_delete_logpush_job_v2_all_params.
        _service.enable_retries()
        self.test_delete_logpush_job_v2_all_params()

        # Disable retries and run test_delete_logpush_job_v2_all_params.
        _service.disable_retries()
        self.test_delete_logpush_job_v2_all_params()

    @responses.activate
    def test_delete_logpush_job_v2_value_error(self):
        """
        test_delete_logpush_job_v2_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/testString/zones/testString/logpush/jobs/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"anyKey": "anyValue"}}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        job_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "job_id": job_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_logpush_job_v2(**req_copy)

    def test_delete_logpush_job_v2_value_error_with_retries(self):
        # Enable retries and run test_delete_logpush_job_v2_value_error.
        _service.enable_retries()
        self.test_delete_logpush_job_v2_value_error()

        # Disable retries and run test_delete_logpush_job_v2_value_error.
        _service.disable_retries()
        self.test_delete_logpush_job_v2_value_error()


class TestGetLogpushOwnershipV2:
    """
    Test Class for get_logpush_ownership_v2
    """

    @responses.activate
    def test_get_logpush_ownership_v2_all_params(self):
        """
        get_logpush_ownership_v2()
        """
        # Set up mock
        url = preprocess_url('/v2/testString/zones/testString/logpush/ownership')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"filename": "logs/challenge-filename.txt", "valid": true, "messages": "messages"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        cos = {'bucket_name': 'cos-bucket001', 'region': 'us-south', 'id': '231f5467-3072-4cb9-9e39-a906fa3032ea'}

        # Invoke method
        response = _service.get_logpush_ownership_v2(
            cos=cos,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['cos'] == {'bucket_name': 'cos-bucket001', 'region': 'us-south', 'id': '231f5467-3072-4cb9-9e39-a906fa3032ea'}

    def test_get_logpush_ownership_v2_all_params_with_retries(self):
        # Enable retries and run test_get_logpush_ownership_v2_all_params.
        _service.enable_retries()
        self.test_get_logpush_ownership_v2_all_params()

        # Disable retries and run test_get_logpush_ownership_v2_all_params.
        _service.disable_retries()
        self.test_get_logpush_ownership_v2_all_params()

    @responses.activate
    def test_get_logpush_ownership_v2_required_params(self):
        """
        test_get_logpush_ownership_v2_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/testString/zones/testString/logpush/ownership')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"filename": "logs/challenge-filename.txt", "valid": true, "messages": "messages"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_logpush_ownership_v2()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_logpush_ownership_v2_required_params_with_retries(self):
        # Enable retries and run test_get_logpush_ownership_v2_required_params.
        _service.enable_retries()
        self.test_get_logpush_ownership_v2_required_params()

        # Disable retries and run test_get_logpush_ownership_v2_required_params.
        _service.disable_retries()
        self.test_get_logpush_ownership_v2_required_params()

    @responses.activate
    def test_get_logpush_ownership_v2_value_error(self):
        """
        test_get_logpush_ownership_v2_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/testString/zones/testString/logpush/ownership')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"filename": "logs/challenge-filename.txt", "valid": true, "messages": "messages"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_logpush_ownership_v2(**req_copy)

    def test_get_logpush_ownership_v2_value_error_with_retries(self):
        # Enable retries and run test_get_logpush_ownership_v2_value_error.
        _service.enable_retries()
        self.test_get_logpush_ownership_v2_value_error()

        # Disable retries and run test_get_logpush_ownership_v2_value_error.
        _service.disable_retries()
        self.test_get_logpush_ownership_v2_value_error()


class TestValidateLogpushOwnershipChallengeV2:
    """
    Test Class for validate_logpush_ownership_challenge_v2
    """

    @responses.activate
    def test_validate_logpush_ownership_challenge_v2_all_params(self):
        """
        validate_logpush_ownership_challenge_v2()
        """
        # Set up mock
        url = preprocess_url('/v2/testString/zones/testString/logpush/ownership/validate')
        mock_response = '{"valid": true}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        cos = {'bucket_name': 'cos-bucket001', 'region': 'us-south', 'id': '231f5467-3072-4cb9-9e39-a906fa3032ea'}
        ownership_challenge = '00000000000000000000'

        # Invoke method
        response = _service.validate_logpush_ownership_challenge_v2(
            cos=cos,
            ownership_challenge=ownership_challenge,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['cos'] == {'bucket_name': 'cos-bucket001', 'region': 'us-south', 'id': '231f5467-3072-4cb9-9e39-a906fa3032ea'}
        assert req_body['ownership_challenge'] == '00000000000000000000'

    def test_validate_logpush_ownership_challenge_v2_all_params_with_retries(self):
        # Enable retries and run test_validate_logpush_ownership_challenge_v2_all_params.
        _service.enable_retries()
        self.test_validate_logpush_ownership_challenge_v2_all_params()

        # Disable retries and run test_validate_logpush_ownership_challenge_v2_all_params.
        _service.disable_retries()
        self.test_validate_logpush_ownership_challenge_v2_all_params()

    @responses.activate
    def test_validate_logpush_ownership_challenge_v2_required_params(self):
        """
        test_validate_logpush_ownership_challenge_v2_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/testString/zones/testString/logpush/ownership/validate')
        mock_response = '{"valid": true}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.validate_logpush_ownership_challenge_v2()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_validate_logpush_ownership_challenge_v2_required_params_with_retries(self):
        # Enable retries and run test_validate_logpush_ownership_challenge_v2_required_params.
        _service.enable_retries()
        self.test_validate_logpush_ownership_challenge_v2_required_params()

        # Disable retries and run test_validate_logpush_ownership_challenge_v2_required_params.
        _service.disable_retries()
        self.test_validate_logpush_ownership_challenge_v2_required_params()

    @responses.activate
    def test_validate_logpush_ownership_challenge_v2_value_error(self):
        """
        test_validate_logpush_ownership_challenge_v2_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/testString/zones/testString/logpush/ownership/validate')
        mock_response = '{"valid": true}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.validate_logpush_ownership_challenge_v2(**req_copy)

    def test_validate_logpush_ownership_challenge_v2_value_error_with_retries(self):
        # Enable retries and run test_validate_logpush_ownership_challenge_v2_value_error.
        _service.enable_retries()
        self.test_validate_logpush_ownership_challenge_v2_value_error()

        # Disable retries and run test_validate_logpush_ownership_challenge_v2_value_error.
        _service.disable_retries()
        self.test_validate_logpush_ownership_challenge_v2_value_error()


class TestListFieldsForDatasetV2:
    """
    Test Class for list_fields_for_dataset_v2
    """

    @responses.activate
    def test_list_fields_for_dataset_v2_all_params(self):
        """
        list_fields_for_dataset_v2()
        """
        # Set up mock
        url = preprocess_url('/v2/testString/zones/testString/logpush/datasets/testString/fields')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"anyKey": "anyValue"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.list_fields_for_dataset_v2()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_fields_for_dataset_v2_all_params_with_retries(self):
        # Enable retries and run test_list_fields_for_dataset_v2_all_params.
        _service.enable_retries()
        self.test_list_fields_for_dataset_v2_all_params()

        # Disable retries and run test_list_fields_for_dataset_v2_all_params.
        _service.disable_retries()
        self.test_list_fields_for_dataset_v2_all_params()

    @responses.activate
    def test_list_fields_for_dataset_v2_value_error(self):
        """
        test_list_fields_for_dataset_v2_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/testString/zones/testString/logpush/datasets/testString/fields')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"anyKey": "anyValue"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_fields_for_dataset_v2(**req_copy)

    def test_list_fields_for_dataset_v2_value_error_with_retries(self):
        # Enable retries and run test_list_fields_for_dataset_v2_value_error.
        _service.enable_retries()
        self.test_list_fields_for_dataset_v2_value_error()

        # Disable retries and run test_list_fields_for_dataset_v2_value_error.
        _service.disable_retries()
        self.test_list_fields_for_dataset_v2_value_error()


class TestListLogpushJobsForDatasetV2:
    """
    Test Class for list_logpush_jobs_for_dataset_v2
    """

    @responses.activate
    def test_list_logpush_jobs_for_dataset_v2_all_params(self):
        """
        list_logpush_jobs_for_dataset_v2()
        """
        # Set up mock
        url = preprocess_url('/v2/testString/zones/testString/logpush/datasets/testString/jobs')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": 5850, "name": "My log push job", "enabled": false, "dataset": "firewall_events", "frequency": "high", "logpull_options": "timestamps=rfc3339&timestamps=rfc3339", "destination_conf": "cos://cos-bucket001?region=us-south&instance-id=231f5467-3072-4cb9-9e39-a906fa3032ea", "last_complete": "2022-01-15T16:33:31.834209Z", "last_error": "2022-01-15T16:33:31.834209Z", "error_message": "error_message"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.list_logpush_jobs_for_dataset_v2()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_logpush_jobs_for_dataset_v2_all_params_with_retries(self):
        # Enable retries and run test_list_logpush_jobs_for_dataset_v2_all_params.
        _service.enable_retries()
        self.test_list_logpush_jobs_for_dataset_v2_all_params()

        # Disable retries and run test_list_logpush_jobs_for_dataset_v2_all_params.
        _service.disable_retries()
        self.test_list_logpush_jobs_for_dataset_v2_all_params()

    @responses.activate
    def test_list_logpush_jobs_for_dataset_v2_value_error(self):
        """
        test_list_logpush_jobs_for_dataset_v2_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/testString/zones/testString/logpush/datasets/testString/jobs')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": 5850, "name": "My log push job", "enabled": false, "dataset": "firewall_events", "frequency": "high", "logpull_options": "timestamps=rfc3339&timestamps=rfc3339", "destination_conf": "cos://cos-bucket001?region=us-south&instance-id=231f5467-3072-4cb9-9e39-a906fa3032ea", "last_complete": "2022-01-15T16:33:31.834209Z", "last_error": "2022-01-15T16:33:31.834209Z", "error_message": "error_message"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_logpush_jobs_for_dataset_v2(**req_copy)

    def test_list_logpush_jobs_for_dataset_v2_value_error_with_retries(self):
        # Enable retries and run test_list_logpush_jobs_for_dataset_v2_value_error.
        _service.enable_retries()
        self.test_list_logpush_jobs_for_dataset_v2_value_error()

        # Disable retries and run test_list_logpush_jobs_for_dataset_v2_value_error.
        _service.disable_retries()
        self.test_list_logpush_jobs_for_dataset_v2_value_error()


class TestGetLogsRetention:
    """
    Test Class for get_logs_retention
    """

    @responses.activate
    def test_get_logs_retention_all_params(self):
        """
        get_logs_retention()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/logs/retention')
        mock_response = '{"result": {"flag": true}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_logs_retention()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_logs_retention_all_params_with_retries(self):
        # Enable retries and run test_get_logs_retention_all_params.
        _service.enable_retries()
        self.test_get_logs_retention_all_params()

        # Disable retries and run test_get_logs_retention_all_params.
        _service.disable_retries()
        self.test_get_logs_retention_all_params()

    @responses.activate
    def test_get_logs_retention_value_error(self):
        """
        test_get_logs_retention_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/logs/retention')
        mock_response = '{"result": {"flag": true}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_logs_retention(**req_copy)

    def test_get_logs_retention_value_error_with_retries(self):
        # Enable retries and run test_get_logs_retention_value_error.
        _service.enable_retries()
        self.test_get_logs_retention_value_error()

        # Disable retries and run test_get_logs_retention_value_error.
        _service.disable_retries()
        self.test_get_logs_retention_value_error()


class TestCreateLogRetention:
    """
    Test Class for create_log_retention
    """

    @responses.activate
    def test_create_log_retention_all_params(self):
        """
        create_log_retention()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/logs/retention')
        mock_response = '{"result": {"flag": true}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        flag = False

        # Invoke method
        response = _service.create_log_retention(
            flag=flag,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['flag'] == False

    def test_create_log_retention_all_params_with_retries(self):
        # Enable retries and run test_create_log_retention_all_params.
        _service.enable_retries()
        self.test_create_log_retention_all_params()

        # Disable retries and run test_create_log_retention_all_params.
        _service.disable_retries()
        self.test_create_log_retention_all_params()

    @responses.activate
    def test_create_log_retention_required_params(self):
        """
        test_create_log_retention_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/logs/retention')
        mock_response = '{"result": {"flag": true}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.create_log_retention()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_create_log_retention_required_params_with_retries(self):
        # Enable retries and run test_create_log_retention_required_params.
        _service.enable_retries()
        self.test_create_log_retention_required_params()

        # Disable retries and run test_create_log_retention_required_params.
        _service.disable_retries()
        self.test_create_log_retention_required_params()

    @responses.activate
    def test_create_log_retention_value_error(self):
        """
        test_create_log_retention_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/logs/retention')
        mock_response = '{"result": {"flag": true}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_log_retention(**req_copy)

    def test_create_log_retention_value_error_with_retries(self):
        # Enable retries and run test_create_log_retention_value_error.
        _service.enable_retries()
        self.test_create_log_retention_value_error()

        # Disable retries and run test_create_log_retention_value_error.
        _service.disable_retries()
        self.test_create_log_retention_value_error()


# endregion
##############################################################################
# End of Service: LogpushJobs
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region


class TestModel_LogRetentionRespResult:
    """
    Test Class for LogRetentionRespResult
    """

    def test_log_retention_resp_result_serialization(self):
        """
        Test serialization/deserialization for LogRetentionRespResult
        """

        # Construct a json representation of a LogRetentionRespResult model
        log_retention_resp_result_model_json = {}
        log_retention_resp_result_model_json['flag'] = True

        # Construct a model instance of LogRetentionRespResult by calling from_dict on the json representation
        log_retention_resp_result_model = LogRetentionRespResult.from_dict(log_retention_resp_result_model_json)
        assert log_retention_resp_result_model != False

        # Construct a model instance of LogRetentionRespResult by calling from_dict on the json representation
        log_retention_resp_result_model_dict = LogRetentionRespResult.from_dict(log_retention_resp_result_model_json).__dict__
        log_retention_resp_result_model2 = LogRetentionRespResult(**log_retention_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert log_retention_resp_result_model == log_retention_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        log_retention_resp_result_model_json2 = log_retention_resp_result_model.to_dict()
        assert log_retention_resp_result_model_json2 == log_retention_resp_result_model_json


class TestModel_LogpushJobIbmclReqIbmcl:
    """
    Test Class for LogpushJobIbmclReqIbmcl
    """

    def test_logpush_job_ibmcl_req_ibmcl_serialization(self):
        """
        Test serialization/deserialization for LogpushJobIbmclReqIbmcl
        """

        # Construct a json representation of a LogpushJobIbmclReqIbmcl model
        logpush_job_ibmcl_req_ibmcl_model_json = {}
        logpush_job_ibmcl_req_ibmcl_model_json['instance_id'] = '90d208cc-e1dd-4fb2-a938-358e5996f056'
        logpush_job_ibmcl_req_ibmcl_model_json['region'] = 'eu-es'
        logpush_job_ibmcl_req_ibmcl_model_json['api_key'] = 'XXXXXXXXXXXXXX'

        # Construct a model instance of LogpushJobIbmclReqIbmcl by calling from_dict on the json representation
        logpush_job_ibmcl_req_ibmcl_model = LogpushJobIbmclReqIbmcl.from_dict(logpush_job_ibmcl_req_ibmcl_model_json)
        assert logpush_job_ibmcl_req_ibmcl_model != False

        # Construct a model instance of LogpushJobIbmclReqIbmcl by calling from_dict on the json representation
        logpush_job_ibmcl_req_ibmcl_model_dict = LogpushJobIbmclReqIbmcl.from_dict(logpush_job_ibmcl_req_ibmcl_model_json).__dict__
        logpush_job_ibmcl_req_ibmcl_model2 = LogpushJobIbmclReqIbmcl(**logpush_job_ibmcl_req_ibmcl_model_dict)

        # Verify the model instances are equivalent
        assert logpush_job_ibmcl_req_ibmcl_model == logpush_job_ibmcl_req_ibmcl_model2

        # Convert model instance back to dict and verify no loss of data
        logpush_job_ibmcl_req_ibmcl_model_json2 = logpush_job_ibmcl_req_ibmcl_model.to_dict()
        assert logpush_job_ibmcl_req_ibmcl_model_json2 == logpush_job_ibmcl_req_ibmcl_model_json


class TestModel_LogpushJobsUpdateIbmclReqIbmcl:
    """
    Test Class for LogpushJobsUpdateIbmclReqIbmcl
    """

    def test_logpush_jobs_update_ibmcl_req_ibmcl_serialization(self):
        """
        Test serialization/deserialization for LogpushJobsUpdateIbmclReqIbmcl
        """

        # Construct a json representation of a LogpushJobsUpdateIbmclReqIbmcl model
        logpush_jobs_update_ibmcl_req_ibmcl_model_json = {}
        logpush_jobs_update_ibmcl_req_ibmcl_model_json['instance_id'] = '90d208cc-e1dd-4fb2-a938-358e5996f056'
        logpush_jobs_update_ibmcl_req_ibmcl_model_json['region'] = 'eu-es'
        logpush_jobs_update_ibmcl_req_ibmcl_model_json['api_key'] = 'XXXXXXXXXXXXXX'

        # Construct a model instance of LogpushJobsUpdateIbmclReqIbmcl by calling from_dict on the json representation
        logpush_jobs_update_ibmcl_req_ibmcl_model = LogpushJobsUpdateIbmclReqIbmcl.from_dict(logpush_jobs_update_ibmcl_req_ibmcl_model_json)
        assert logpush_jobs_update_ibmcl_req_ibmcl_model != False

        # Construct a model instance of LogpushJobsUpdateIbmclReqIbmcl by calling from_dict on the json representation
        logpush_jobs_update_ibmcl_req_ibmcl_model_dict = LogpushJobsUpdateIbmclReqIbmcl.from_dict(logpush_jobs_update_ibmcl_req_ibmcl_model_json).__dict__
        logpush_jobs_update_ibmcl_req_ibmcl_model2 = LogpushJobsUpdateIbmclReqIbmcl(**logpush_jobs_update_ibmcl_req_ibmcl_model_dict)

        # Verify the model instances are equivalent
        assert logpush_jobs_update_ibmcl_req_ibmcl_model == logpush_jobs_update_ibmcl_req_ibmcl_model2

        # Convert model instance back to dict and verify no loss of data
        logpush_jobs_update_ibmcl_req_ibmcl_model_json2 = logpush_jobs_update_ibmcl_req_ibmcl_model.to_dict()
        assert logpush_jobs_update_ibmcl_req_ibmcl_model_json2 == logpush_jobs_update_ibmcl_req_ibmcl_model_json


class TestModel_DeleteLogpushJobResp:
    """
    Test Class for DeleteLogpushJobResp
    """

    def test_delete_logpush_job_resp_serialization(self):
        """
        Test serialization/deserialization for DeleteLogpushJobResp
        """

        # Construct a json representation of a DeleteLogpushJobResp model
        delete_logpush_job_resp_model_json = {}
        delete_logpush_job_resp_model_json['success'] = True
        delete_logpush_job_resp_model_json['errors'] = [['testString']]
        delete_logpush_job_resp_model_json['messages'] = [['testString']]
        delete_logpush_job_resp_model_json['result'] = {'anyKey': 'anyValue'}

        # Construct a model instance of DeleteLogpushJobResp by calling from_dict on the json representation
        delete_logpush_job_resp_model = DeleteLogpushJobResp.from_dict(delete_logpush_job_resp_model_json)
        assert delete_logpush_job_resp_model != False

        # Construct a model instance of DeleteLogpushJobResp by calling from_dict on the json representation
        delete_logpush_job_resp_model_dict = DeleteLogpushJobResp.from_dict(delete_logpush_job_resp_model_json).__dict__
        delete_logpush_job_resp_model2 = DeleteLogpushJobResp(**delete_logpush_job_resp_model_dict)

        # Verify the model instances are equivalent
        assert delete_logpush_job_resp_model == delete_logpush_job_resp_model2

        # Convert model instance back to dict and verify no loss of data
        delete_logpush_job_resp_model_json2 = delete_logpush_job_resp_model.to_dict()
        assert delete_logpush_job_resp_model_json2 == delete_logpush_job_resp_model_json


class TestModel_ListFieldsResp:
    """
    Test Class for ListFieldsResp
    """

    def test_list_fields_resp_serialization(self):
        """
        Test serialization/deserialization for ListFieldsResp
        """

        # Construct a json representation of a ListFieldsResp model
        list_fields_resp_model_json = {}
        list_fields_resp_model_json['success'] = True
        list_fields_resp_model_json['errors'] = [['testString']]
        list_fields_resp_model_json['messages'] = [['testString']]
        list_fields_resp_model_json['result'] = {}

        # Construct a model instance of ListFieldsResp by calling from_dict on the json representation
        list_fields_resp_model = ListFieldsResp.from_dict(list_fields_resp_model_json)
        assert list_fields_resp_model != False

        # Construct a model instance of ListFieldsResp by calling from_dict on the json representation
        list_fields_resp_model_dict = ListFieldsResp.from_dict(list_fields_resp_model_json).__dict__
        list_fields_resp_model2 = ListFieldsResp(**list_fields_resp_model_dict)

        # Verify the model instances are equivalent
        assert list_fields_resp_model == list_fields_resp_model2

        # Convert model instance back to dict and verify no loss of data
        list_fields_resp_model_json2 = list_fields_resp_model.to_dict()
        assert list_fields_resp_model_json2 == list_fields_resp_model_json


class TestModel_ListLogpushJobsResp:
    """
    Test Class for ListLogpushJobsResp
    """

    def test_list_logpush_jobs_resp_serialization(self):
        """
        Test serialization/deserialization for ListLogpushJobsResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        logpush_job_pack_model = {}  # LogpushJobPack
        logpush_job_pack_model['id'] = 5850
        logpush_job_pack_model['name'] = 'My log push job'
        logpush_job_pack_model['enabled'] = False
        logpush_job_pack_model['dataset'] = 'firewall_events'
        logpush_job_pack_model['frequency'] = 'high'
        logpush_job_pack_model['logpull_options'] = 'timestamps=rfc3339&timestamps=rfc3339'
        logpush_job_pack_model['destination_conf'] = 'cos://cos-bucket001?region=us-south&instance-id=231f5467-3072-4cb9-9e39-a906fa3032ea'
        logpush_job_pack_model['last_complete'] = '2022-01-15T16:33:31.834209Z'
        logpush_job_pack_model['last_error'] = '2022-01-15T16:33:31.834209Z'
        logpush_job_pack_model['error_message'] = 'testString'

        # Construct a json representation of a ListLogpushJobsResp model
        list_logpush_jobs_resp_model_json = {}
        list_logpush_jobs_resp_model_json['success'] = True
        list_logpush_jobs_resp_model_json['errors'] = [['testString']]
        list_logpush_jobs_resp_model_json['messages'] = [['testString']]
        list_logpush_jobs_resp_model_json['result'] = [logpush_job_pack_model]

        # Construct a model instance of ListLogpushJobsResp by calling from_dict on the json representation
        list_logpush_jobs_resp_model = ListLogpushJobsResp.from_dict(list_logpush_jobs_resp_model_json)
        assert list_logpush_jobs_resp_model != False

        # Construct a model instance of ListLogpushJobsResp by calling from_dict on the json representation
        list_logpush_jobs_resp_model_dict = ListLogpushJobsResp.from_dict(list_logpush_jobs_resp_model_json).__dict__
        list_logpush_jobs_resp_model2 = ListLogpushJobsResp(**list_logpush_jobs_resp_model_dict)

        # Verify the model instances are equivalent
        assert list_logpush_jobs_resp_model == list_logpush_jobs_resp_model2

        # Convert model instance back to dict and verify no loss of data
        list_logpush_jobs_resp_model_json2 = list_logpush_jobs_resp_model.to_dict()
        assert list_logpush_jobs_resp_model_json2 == list_logpush_jobs_resp_model_json


class TestModel_LogRetentionResp:
    """
    Test Class for LogRetentionResp
    """

    def test_log_retention_resp_serialization(self):
        """
        Test serialization/deserialization for LogRetentionResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        log_retention_resp_result_model = {}  # LogRetentionRespResult
        log_retention_resp_result_model['flag'] = True

        # Construct a json representation of a LogRetentionResp model
        log_retention_resp_model_json = {}
        log_retention_resp_model_json['result'] = log_retention_resp_result_model
        log_retention_resp_model_json['success'] = True
        log_retention_resp_model_json['errors'] = [['testString']]
        log_retention_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of LogRetentionResp by calling from_dict on the json representation
        log_retention_resp_model = LogRetentionResp.from_dict(log_retention_resp_model_json)
        assert log_retention_resp_model != False

        # Construct a model instance of LogRetentionResp by calling from_dict on the json representation
        log_retention_resp_model_dict = LogRetentionResp.from_dict(log_retention_resp_model_json).__dict__
        log_retention_resp_model2 = LogRetentionResp(**log_retention_resp_model_dict)

        # Verify the model instances are equivalent
        assert log_retention_resp_model == log_retention_resp_model2

        # Convert model instance back to dict and verify no loss of data
        log_retention_resp_model_json2 = log_retention_resp_model.to_dict()
        assert log_retention_resp_model_json2 == log_retention_resp_model_json


class TestModel_LogpushJobPack:
    """
    Test Class for LogpushJobPack
    """

    def test_logpush_job_pack_serialization(self):
        """
        Test serialization/deserialization for LogpushJobPack
        """

        # Construct a json representation of a LogpushJobPack model
        logpush_job_pack_model_json = {}
        logpush_job_pack_model_json['id'] = 5850
        logpush_job_pack_model_json['name'] = 'My log push job'
        logpush_job_pack_model_json['enabled'] = False
        logpush_job_pack_model_json['dataset'] = 'firewall_events'
        logpush_job_pack_model_json['frequency'] = 'high'
        logpush_job_pack_model_json['logpull_options'] = 'timestamps=rfc3339&timestamps=rfc3339'
        logpush_job_pack_model_json['destination_conf'] = 'cos://cos-bucket001?region=us-south&instance-id=231f5467-3072-4cb9-9e39-a906fa3032ea'
        logpush_job_pack_model_json['last_complete'] = '2022-01-15T16:33:31.834209Z'
        logpush_job_pack_model_json['last_error'] = '2022-01-15T16:33:31.834209Z'
        logpush_job_pack_model_json['error_message'] = 'testString'

        # Construct a model instance of LogpushJobPack by calling from_dict on the json representation
        logpush_job_pack_model = LogpushJobPack.from_dict(logpush_job_pack_model_json)
        assert logpush_job_pack_model != False

        # Construct a model instance of LogpushJobPack by calling from_dict on the json representation
        logpush_job_pack_model_dict = LogpushJobPack.from_dict(logpush_job_pack_model_json).__dict__
        logpush_job_pack_model2 = LogpushJobPack(**logpush_job_pack_model_dict)

        # Verify the model instances are equivalent
        assert logpush_job_pack_model == logpush_job_pack_model2

        # Convert model instance back to dict and verify no loss of data
        logpush_job_pack_model_json2 = logpush_job_pack_model.to_dict()
        assert logpush_job_pack_model_json2 == logpush_job_pack_model_json


class TestModel_LogpushJobsResp:
    """
    Test Class for LogpushJobsResp
    """

    def test_logpush_jobs_resp_serialization(self):
        """
        Test serialization/deserialization for LogpushJobsResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        logpush_job_pack_model = {}  # LogpushJobPack
        logpush_job_pack_model['id'] = 5850
        logpush_job_pack_model['name'] = 'My log push job'
        logpush_job_pack_model['enabled'] = False
        logpush_job_pack_model['dataset'] = 'firewall_events'
        logpush_job_pack_model['frequency'] = 'high'
        logpush_job_pack_model['logpull_options'] = 'timestamps=rfc3339&timestamps=rfc3339'
        logpush_job_pack_model['destination_conf'] = 'cos://cos-bucket001?region=us-south&instance-id=231f5467-3072-4cb9-9e39-a906fa3032ea'
        logpush_job_pack_model['last_complete'] = '2022-01-15T16:33:31.834209Z'
        logpush_job_pack_model['last_error'] = '2022-01-15T16:33:31.834209Z'
        logpush_job_pack_model['error_message'] = 'testString'

        # Construct a json representation of a LogpushJobsResp model
        logpush_jobs_resp_model_json = {}
        logpush_jobs_resp_model_json['success'] = True
        logpush_jobs_resp_model_json['errors'] = [['testString']]
        logpush_jobs_resp_model_json['messages'] = [['testString']]
        logpush_jobs_resp_model_json['result'] = logpush_job_pack_model

        # Construct a model instance of LogpushJobsResp by calling from_dict on the json representation
        logpush_jobs_resp_model = LogpushJobsResp.from_dict(logpush_jobs_resp_model_json)
        assert logpush_jobs_resp_model != False

        # Construct a model instance of LogpushJobsResp by calling from_dict on the json representation
        logpush_jobs_resp_model_dict = LogpushJobsResp.from_dict(logpush_jobs_resp_model_json).__dict__
        logpush_jobs_resp_model2 = LogpushJobsResp(**logpush_jobs_resp_model_dict)

        # Verify the model instances are equivalent
        assert logpush_jobs_resp_model == logpush_jobs_resp_model2

        # Convert model instance back to dict and verify no loss of data
        logpush_jobs_resp_model_json2 = logpush_jobs_resp_model.to_dict()
        assert logpush_jobs_resp_model_json2 == logpush_jobs_resp_model_json


class TestModel_OwnershipChallengeResp:
    """
    Test Class for OwnershipChallengeResp
    """

    def test_ownership_challenge_resp_serialization(self):
        """
        Test serialization/deserialization for OwnershipChallengeResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        ownership_challenge_result_model = {}  # OwnershipChallengeResult
        ownership_challenge_result_model['filename'] = 'logs/challenge-filename.txt'
        ownership_challenge_result_model['valid'] = True
        ownership_challenge_result_model['messages'] = 'testString'

        # Construct a json representation of a OwnershipChallengeResp model
        ownership_challenge_resp_model_json = {}
        ownership_challenge_resp_model_json['success'] = True
        ownership_challenge_resp_model_json['errors'] = [['testString']]
        ownership_challenge_resp_model_json['messages'] = [['testString']]
        ownership_challenge_resp_model_json['result'] = ownership_challenge_result_model

        # Construct a model instance of OwnershipChallengeResp by calling from_dict on the json representation
        ownership_challenge_resp_model = OwnershipChallengeResp.from_dict(ownership_challenge_resp_model_json)
        assert ownership_challenge_resp_model != False

        # Construct a model instance of OwnershipChallengeResp by calling from_dict on the json representation
        ownership_challenge_resp_model_dict = OwnershipChallengeResp.from_dict(ownership_challenge_resp_model_json).__dict__
        ownership_challenge_resp_model2 = OwnershipChallengeResp(**ownership_challenge_resp_model_dict)

        # Verify the model instances are equivalent
        assert ownership_challenge_resp_model == ownership_challenge_resp_model2

        # Convert model instance back to dict and verify no loss of data
        ownership_challenge_resp_model_json2 = ownership_challenge_resp_model.to_dict()
        assert ownership_challenge_resp_model_json2 == ownership_challenge_resp_model_json


class TestModel_OwnershipChallengeResult:
    """
    Test Class for OwnershipChallengeResult
    """

    def test_ownership_challenge_result_serialization(self):
        """
        Test serialization/deserialization for OwnershipChallengeResult
        """

        # Construct a json representation of a OwnershipChallengeResult model
        ownership_challenge_result_model_json = {}
        ownership_challenge_result_model_json['filename'] = 'logs/challenge-filename.txt'
        ownership_challenge_result_model_json['valid'] = True
        ownership_challenge_result_model_json['messages'] = 'testString'

        # Construct a model instance of OwnershipChallengeResult by calling from_dict on the json representation
        ownership_challenge_result_model = OwnershipChallengeResult.from_dict(ownership_challenge_result_model_json)
        assert ownership_challenge_result_model != False

        # Construct a model instance of OwnershipChallengeResult by calling from_dict on the json representation
        ownership_challenge_result_model_dict = OwnershipChallengeResult.from_dict(ownership_challenge_result_model_json).__dict__
        ownership_challenge_result_model2 = OwnershipChallengeResult(**ownership_challenge_result_model_dict)

        # Verify the model instances are equivalent
        assert ownership_challenge_result_model == ownership_challenge_result_model2

        # Convert model instance back to dict and verify no loss of data
        ownership_challenge_result_model_json2 = ownership_challenge_result_model.to_dict()
        assert ownership_challenge_result_model_json2 == ownership_challenge_result_model_json


class TestModel_OwnershipChallengeValidateResult:
    """
    Test Class for OwnershipChallengeValidateResult
    """

    def test_ownership_challenge_validate_result_serialization(self):
        """
        Test serialization/deserialization for OwnershipChallengeValidateResult
        """

        # Construct a json representation of a OwnershipChallengeValidateResult model
        ownership_challenge_validate_result_model_json = {}
        ownership_challenge_validate_result_model_json['valid'] = True

        # Construct a model instance of OwnershipChallengeValidateResult by calling from_dict on the json representation
        ownership_challenge_validate_result_model = OwnershipChallengeValidateResult.from_dict(ownership_challenge_validate_result_model_json)
        assert ownership_challenge_validate_result_model != False

        # Construct a model instance of OwnershipChallengeValidateResult by calling from_dict on the json representation
        ownership_challenge_validate_result_model_dict = OwnershipChallengeValidateResult.from_dict(ownership_challenge_validate_result_model_json).__dict__
        ownership_challenge_validate_result_model2 = OwnershipChallengeValidateResult(**ownership_challenge_validate_result_model_dict)

        # Verify the model instances are equivalent
        assert ownership_challenge_validate_result_model == ownership_challenge_validate_result_model2

        # Convert model instance back to dict and verify no loss of data
        ownership_challenge_validate_result_model_json2 = ownership_challenge_validate_result_model.to_dict()
        assert ownership_challenge_validate_result_model_json2 == ownership_challenge_validate_result_model_json


class TestModel_CreateLogpushJobV2RequestLogpushJobCosReq:
    """
    Test Class for CreateLogpushJobV2RequestLogpushJobCosReq
    """

    def test_create_logpush_job_v2_request_logpush_job_cos_req_serialization(self):
        """
        Test serialization/deserialization for CreateLogpushJobV2RequestLogpushJobCosReq
        """

        # Construct a json representation of a CreateLogpushJobV2RequestLogpushJobCosReq model
        create_logpush_job_v2_request_logpush_job_cos_req_model_json = {}
        create_logpush_job_v2_request_logpush_job_cos_req_model_json['name'] = 'My log push job'
        create_logpush_job_v2_request_logpush_job_cos_req_model_json['enabled'] = False
        create_logpush_job_v2_request_logpush_job_cos_req_model_json['logpull_options'] = 'timestamps=rfc3339&timestamps=rfc3339'
        create_logpush_job_v2_request_logpush_job_cos_req_model_json['cos'] = {'bucket_name': 'cos-bucket001', 'region': 'us-south', 'id': '231f5467-3072-4cb9-9e39-a906fa3032ea'}
        create_logpush_job_v2_request_logpush_job_cos_req_model_json['ownership_challenge'] = '00000000000000000000000000000000'
        create_logpush_job_v2_request_logpush_job_cos_req_model_json['dataset'] = 'http_requests'
        create_logpush_job_v2_request_logpush_job_cos_req_model_json['frequency'] = 'high'

        # Construct a model instance of CreateLogpushJobV2RequestLogpushJobCosReq by calling from_dict on the json representation
        create_logpush_job_v2_request_logpush_job_cos_req_model = CreateLogpushJobV2RequestLogpushJobCosReq.from_dict(create_logpush_job_v2_request_logpush_job_cos_req_model_json)
        assert create_logpush_job_v2_request_logpush_job_cos_req_model != False

        # Construct a model instance of CreateLogpushJobV2RequestLogpushJobCosReq by calling from_dict on the json representation
        create_logpush_job_v2_request_logpush_job_cos_req_model_dict = CreateLogpushJobV2RequestLogpushJobCosReq.from_dict(create_logpush_job_v2_request_logpush_job_cos_req_model_json).__dict__
        create_logpush_job_v2_request_logpush_job_cos_req_model2 = CreateLogpushJobV2RequestLogpushJobCosReq(**create_logpush_job_v2_request_logpush_job_cos_req_model_dict)

        # Verify the model instances are equivalent
        assert create_logpush_job_v2_request_logpush_job_cos_req_model == create_logpush_job_v2_request_logpush_job_cos_req_model2

        # Convert model instance back to dict and verify no loss of data
        create_logpush_job_v2_request_logpush_job_cos_req_model_json2 = create_logpush_job_v2_request_logpush_job_cos_req_model.to_dict()
        assert create_logpush_job_v2_request_logpush_job_cos_req_model_json2 == create_logpush_job_v2_request_logpush_job_cos_req_model_json


class TestModel_CreateLogpushJobV2RequestLogpushJobGenericReq:
    """
    Test Class for CreateLogpushJobV2RequestLogpushJobGenericReq
    """

    def test_create_logpush_job_v2_request_logpush_job_generic_req_serialization(self):
        """
        Test serialization/deserialization for CreateLogpushJobV2RequestLogpushJobGenericReq
        """

        # Construct a json representation of a CreateLogpushJobV2RequestLogpushJobGenericReq model
        create_logpush_job_v2_request_logpush_job_generic_req_model_json = {}
        create_logpush_job_v2_request_logpush_job_generic_req_model_json['name'] = 'My log push job'
        create_logpush_job_v2_request_logpush_job_generic_req_model_json['enabled'] = False
        create_logpush_job_v2_request_logpush_job_generic_req_model_json['logpull_options'] = 'timestamps=rfc3339&timestamps=rfc3339'
        create_logpush_job_v2_request_logpush_job_generic_req_model_json['destination_conf'] = 's3://mybucket/logs?region=us-west-2'
        create_logpush_job_v2_request_logpush_job_generic_req_model_json['dataset'] = 'http_requests'
        create_logpush_job_v2_request_logpush_job_generic_req_model_json['frequency'] = 'high'

        # Construct a model instance of CreateLogpushJobV2RequestLogpushJobGenericReq by calling from_dict on the json representation
        create_logpush_job_v2_request_logpush_job_generic_req_model = CreateLogpushJobV2RequestLogpushJobGenericReq.from_dict(create_logpush_job_v2_request_logpush_job_generic_req_model_json)
        assert create_logpush_job_v2_request_logpush_job_generic_req_model != False

        # Construct a model instance of CreateLogpushJobV2RequestLogpushJobGenericReq by calling from_dict on the json representation
        create_logpush_job_v2_request_logpush_job_generic_req_model_dict = CreateLogpushJobV2RequestLogpushJobGenericReq.from_dict(create_logpush_job_v2_request_logpush_job_generic_req_model_json).__dict__
        create_logpush_job_v2_request_logpush_job_generic_req_model2 = CreateLogpushJobV2RequestLogpushJobGenericReq(**create_logpush_job_v2_request_logpush_job_generic_req_model_dict)

        # Verify the model instances are equivalent
        assert create_logpush_job_v2_request_logpush_job_generic_req_model == create_logpush_job_v2_request_logpush_job_generic_req_model2

        # Convert model instance back to dict and verify no loss of data
        create_logpush_job_v2_request_logpush_job_generic_req_model_json2 = create_logpush_job_v2_request_logpush_job_generic_req_model.to_dict()
        assert create_logpush_job_v2_request_logpush_job_generic_req_model_json2 == create_logpush_job_v2_request_logpush_job_generic_req_model_json


class TestModel_CreateLogpushJobV2RequestLogpushJobIbmclReq:
    """
    Test Class for CreateLogpushJobV2RequestLogpushJobIbmclReq
    """

    def test_create_logpush_job_v2_request_logpush_job_ibmcl_req_serialization(self):
        """
        Test serialization/deserialization for CreateLogpushJobV2RequestLogpushJobIbmclReq
        """

        # Construct dict forms of any model objects needed in order to build this model.

        logpush_job_ibmcl_req_ibmcl_model = {}  # LogpushJobIbmclReqIbmcl
        logpush_job_ibmcl_req_ibmcl_model['instance_id'] = '90d208cc-e1dd-4fb2-a938-358e5996f056'
        logpush_job_ibmcl_req_ibmcl_model['region'] = 'eu-es'
        logpush_job_ibmcl_req_ibmcl_model['api_key'] = 'XXXXXXXXXXXXXX'

        # Construct a json representation of a CreateLogpushJobV2RequestLogpushJobIbmclReq model
        create_logpush_job_v2_request_logpush_job_ibmcl_req_model_json = {}
        create_logpush_job_v2_request_logpush_job_ibmcl_req_model_json['name'] = 'My log push job'
        create_logpush_job_v2_request_logpush_job_ibmcl_req_model_json['enabled'] = False
        create_logpush_job_v2_request_logpush_job_ibmcl_req_model_json['logpull_options'] = 'timestamps=rfc3339&timestamps=rfc3339'
        create_logpush_job_v2_request_logpush_job_ibmcl_req_model_json['ibmcl'] = logpush_job_ibmcl_req_ibmcl_model
        create_logpush_job_v2_request_logpush_job_ibmcl_req_model_json['dataset'] = 'http_requests'
        create_logpush_job_v2_request_logpush_job_ibmcl_req_model_json['frequency'] = 'high'

        # Construct a model instance of CreateLogpushJobV2RequestLogpushJobIbmclReq by calling from_dict on the json representation
        create_logpush_job_v2_request_logpush_job_ibmcl_req_model = CreateLogpushJobV2RequestLogpushJobIbmclReq.from_dict(create_logpush_job_v2_request_logpush_job_ibmcl_req_model_json)
        assert create_logpush_job_v2_request_logpush_job_ibmcl_req_model != False

        # Construct a model instance of CreateLogpushJobV2RequestLogpushJobIbmclReq by calling from_dict on the json representation
        create_logpush_job_v2_request_logpush_job_ibmcl_req_model_dict = CreateLogpushJobV2RequestLogpushJobIbmclReq.from_dict(create_logpush_job_v2_request_logpush_job_ibmcl_req_model_json).__dict__
        create_logpush_job_v2_request_logpush_job_ibmcl_req_model2 = CreateLogpushJobV2RequestLogpushJobIbmclReq(**create_logpush_job_v2_request_logpush_job_ibmcl_req_model_dict)

        # Verify the model instances are equivalent
        assert create_logpush_job_v2_request_logpush_job_ibmcl_req_model == create_logpush_job_v2_request_logpush_job_ibmcl_req_model2

        # Convert model instance back to dict and verify no loss of data
        create_logpush_job_v2_request_logpush_job_ibmcl_req_model_json2 = create_logpush_job_v2_request_logpush_job_ibmcl_req_model.to_dict()
        assert create_logpush_job_v2_request_logpush_job_ibmcl_req_model_json2 == create_logpush_job_v2_request_logpush_job_ibmcl_req_model_json


class TestModel_CreateLogpushJobV2RequestLogpushJobLogdnaReq:
    """
    Test Class for CreateLogpushJobV2RequestLogpushJobLogdnaReq
    """

    def test_create_logpush_job_v2_request_logpush_job_logdna_req_serialization(self):
        """
        Test serialization/deserialization for CreateLogpushJobV2RequestLogpushJobLogdnaReq
        """

        # Construct a json representation of a CreateLogpushJobV2RequestLogpushJobLogdnaReq model
        create_logpush_job_v2_request_logpush_job_logdna_req_model_json = {}
        create_logpush_job_v2_request_logpush_job_logdna_req_model_json['name'] = 'My log push job'
        create_logpush_job_v2_request_logpush_job_logdna_req_model_json['enabled'] = False
        create_logpush_job_v2_request_logpush_job_logdna_req_model_json['logpull_options'] = 'timestamps=rfc3339&timestamps=rfc3339'
        create_logpush_job_v2_request_logpush_job_logdna_req_model_json['logdna'] = {'ingress_key': '8aef12bcd5e5af42', 'region': 'us-south', 'hostname': 'www.example.com'}
        create_logpush_job_v2_request_logpush_job_logdna_req_model_json['dataset'] = 'http_requests'
        create_logpush_job_v2_request_logpush_job_logdna_req_model_json['frequency'] = 'high'

        # Construct a model instance of CreateLogpushJobV2RequestLogpushJobLogdnaReq by calling from_dict on the json representation
        create_logpush_job_v2_request_logpush_job_logdna_req_model = CreateLogpushJobV2RequestLogpushJobLogdnaReq.from_dict(create_logpush_job_v2_request_logpush_job_logdna_req_model_json)
        assert create_logpush_job_v2_request_logpush_job_logdna_req_model != False

        # Construct a model instance of CreateLogpushJobV2RequestLogpushJobLogdnaReq by calling from_dict on the json representation
        create_logpush_job_v2_request_logpush_job_logdna_req_model_dict = CreateLogpushJobV2RequestLogpushJobLogdnaReq.from_dict(create_logpush_job_v2_request_logpush_job_logdna_req_model_json).__dict__
        create_logpush_job_v2_request_logpush_job_logdna_req_model2 = CreateLogpushJobV2RequestLogpushJobLogdnaReq(**create_logpush_job_v2_request_logpush_job_logdna_req_model_dict)

        # Verify the model instances are equivalent
        assert create_logpush_job_v2_request_logpush_job_logdna_req_model == create_logpush_job_v2_request_logpush_job_logdna_req_model2

        # Convert model instance back to dict and verify no loss of data
        create_logpush_job_v2_request_logpush_job_logdna_req_model_json2 = create_logpush_job_v2_request_logpush_job_logdna_req_model.to_dict()
        assert create_logpush_job_v2_request_logpush_job_logdna_req_model_json2 == create_logpush_job_v2_request_logpush_job_logdna_req_model_json


class TestModel_UpdateLogpushJobV2RequestLogpushJobsUpdateCosReq:
    """
    Test Class for UpdateLogpushJobV2RequestLogpushJobsUpdateCosReq
    """

    def test_update_logpush_job_v2_request_logpush_jobs_update_cos_req_serialization(self):
        """
        Test serialization/deserialization for UpdateLogpushJobV2RequestLogpushJobsUpdateCosReq
        """

        # Construct a json representation of a UpdateLogpushJobV2RequestLogpushJobsUpdateCosReq model
        update_logpush_job_v2_request_logpush_jobs_update_cos_req_model_json = {}
        update_logpush_job_v2_request_logpush_jobs_update_cos_req_model_json['enabled'] = False
        update_logpush_job_v2_request_logpush_jobs_update_cos_req_model_json['logpull_options'] = 'timestamps=rfc3339&timestamps=rfc3339'
        update_logpush_job_v2_request_logpush_jobs_update_cos_req_model_json['cos'] = {'bucket_name': 'cos-bucket001', 'region': 'us-south', 'id': '231f5467-3072-4cb9-9e39-a906fa3032ea'}
        update_logpush_job_v2_request_logpush_jobs_update_cos_req_model_json['ownership_challenge'] = '00000000000000000000000000000000'
        update_logpush_job_v2_request_logpush_jobs_update_cos_req_model_json['frequency'] = 'high'

        # Construct a model instance of UpdateLogpushJobV2RequestLogpushJobsUpdateCosReq by calling from_dict on the json representation
        update_logpush_job_v2_request_logpush_jobs_update_cos_req_model = UpdateLogpushJobV2RequestLogpushJobsUpdateCosReq.from_dict(update_logpush_job_v2_request_logpush_jobs_update_cos_req_model_json)
        assert update_logpush_job_v2_request_logpush_jobs_update_cos_req_model != False

        # Construct a model instance of UpdateLogpushJobV2RequestLogpushJobsUpdateCosReq by calling from_dict on the json representation
        update_logpush_job_v2_request_logpush_jobs_update_cos_req_model_dict = UpdateLogpushJobV2RequestLogpushJobsUpdateCosReq.from_dict(update_logpush_job_v2_request_logpush_jobs_update_cos_req_model_json).__dict__
        update_logpush_job_v2_request_logpush_jobs_update_cos_req_model2 = UpdateLogpushJobV2RequestLogpushJobsUpdateCosReq(**update_logpush_job_v2_request_logpush_jobs_update_cos_req_model_dict)

        # Verify the model instances are equivalent
        assert update_logpush_job_v2_request_logpush_jobs_update_cos_req_model == update_logpush_job_v2_request_logpush_jobs_update_cos_req_model2

        # Convert model instance back to dict and verify no loss of data
        update_logpush_job_v2_request_logpush_jobs_update_cos_req_model_json2 = update_logpush_job_v2_request_logpush_jobs_update_cos_req_model.to_dict()
        assert update_logpush_job_v2_request_logpush_jobs_update_cos_req_model_json2 == update_logpush_job_v2_request_logpush_jobs_update_cos_req_model_json


class TestModel_UpdateLogpushJobV2RequestLogpushJobsUpdateGenericReq:
    """
    Test Class for UpdateLogpushJobV2RequestLogpushJobsUpdateGenericReq
    """

    def test_update_logpush_job_v2_request_logpush_jobs_update_generic_req_serialization(self):
        """
        Test serialization/deserialization for UpdateLogpushJobV2RequestLogpushJobsUpdateGenericReq
        """

        # Construct a json representation of a UpdateLogpushJobV2RequestLogpushJobsUpdateGenericReq model
        update_logpush_job_v2_request_logpush_jobs_update_generic_req_model_json = {}
        update_logpush_job_v2_request_logpush_jobs_update_generic_req_model_json['name'] = 'My log push job'
        update_logpush_job_v2_request_logpush_jobs_update_generic_req_model_json['enabled'] = False
        update_logpush_job_v2_request_logpush_jobs_update_generic_req_model_json['logpull_options'] = 'timestamps=rfc3339&timestamps=rfc3339'
        update_logpush_job_v2_request_logpush_jobs_update_generic_req_model_json['destination_conf'] = 's3://mybucket/logs?region=us-west-2'
        update_logpush_job_v2_request_logpush_jobs_update_generic_req_model_json['dataset'] = 'http_requests'
        update_logpush_job_v2_request_logpush_jobs_update_generic_req_model_json['frequency'] = 'high'

        # Construct a model instance of UpdateLogpushJobV2RequestLogpushJobsUpdateGenericReq by calling from_dict on the json representation
        update_logpush_job_v2_request_logpush_jobs_update_generic_req_model = UpdateLogpushJobV2RequestLogpushJobsUpdateGenericReq.from_dict(update_logpush_job_v2_request_logpush_jobs_update_generic_req_model_json)
        assert update_logpush_job_v2_request_logpush_jobs_update_generic_req_model != False

        # Construct a model instance of UpdateLogpushJobV2RequestLogpushJobsUpdateGenericReq by calling from_dict on the json representation
        update_logpush_job_v2_request_logpush_jobs_update_generic_req_model_dict = UpdateLogpushJobV2RequestLogpushJobsUpdateGenericReq.from_dict(update_logpush_job_v2_request_logpush_jobs_update_generic_req_model_json).__dict__
        update_logpush_job_v2_request_logpush_jobs_update_generic_req_model2 = UpdateLogpushJobV2RequestLogpushJobsUpdateGenericReq(**update_logpush_job_v2_request_logpush_jobs_update_generic_req_model_dict)

        # Verify the model instances are equivalent
        assert update_logpush_job_v2_request_logpush_jobs_update_generic_req_model == update_logpush_job_v2_request_logpush_jobs_update_generic_req_model2

        # Convert model instance back to dict and verify no loss of data
        update_logpush_job_v2_request_logpush_jobs_update_generic_req_model_json2 = update_logpush_job_v2_request_logpush_jobs_update_generic_req_model.to_dict()
        assert update_logpush_job_v2_request_logpush_jobs_update_generic_req_model_json2 == update_logpush_job_v2_request_logpush_jobs_update_generic_req_model_json


class TestModel_UpdateLogpushJobV2RequestLogpushJobsUpdateIbmclReq:
    """
    Test Class for UpdateLogpushJobV2RequestLogpushJobsUpdateIbmclReq
    """

    def test_update_logpush_job_v2_request_logpush_jobs_update_ibmcl_req_serialization(self):
        """
        Test serialization/deserialization for UpdateLogpushJobV2RequestLogpushJobsUpdateIbmclReq
        """

        # Construct dict forms of any model objects needed in order to build this model.

        logpush_jobs_update_ibmcl_req_ibmcl_model = {}  # LogpushJobsUpdateIbmclReqIbmcl
        logpush_jobs_update_ibmcl_req_ibmcl_model['instance_id'] = '90d208cc-e1dd-4fb2-a938-358e5996f056'
        logpush_jobs_update_ibmcl_req_ibmcl_model['region'] = 'eu-es'
        logpush_jobs_update_ibmcl_req_ibmcl_model['api_key'] = 'XXXXXXXXXXXXXX'

        # Construct a json representation of a UpdateLogpushJobV2RequestLogpushJobsUpdateIbmclReq model
        update_logpush_job_v2_request_logpush_jobs_update_ibmcl_req_model_json = {}
        update_logpush_job_v2_request_logpush_jobs_update_ibmcl_req_model_json['enabled'] = False
        update_logpush_job_v2_request_logpush_jobs_update_ibmcl_req_model_json['logpull_options'] = 'timestamps=rfc3339&timestamps=rfc3339'
        update_logpush_job_v2_request_logpush_jobs_update_ibmcl_req_model_json['ibmcl'] = logpush_jobs_update_ibmcl_req_ibmcl_model
        update_logpush_job_v2_request_logpush_jobs_update_ibmcl_req_model_json['frequency'] = 'high'

        # Construct a model instance of UpdateLogpushJobV2RequestLogpushJobsUpdateIbmclReq by calling from_dict on the json representation
        update_logpush_job_v2_request_logpush_jobs_update_ibmcl_req_model = UpdateLogpushJobV2RequestLogpushJobsUpdateIbmclReq.from_dict(update_logpush_job_v2_request_logpush_jobs_update_ibmcl_req_model_json)
        assert update_logpush_job_v2_request_logpush_jobs_update_ibmcl_req_model != False

        # Construct a model instance of UpdateLogpushJobV2RequestLogpushJobsUpdateIbmclReq by calling from_dict on the json representation
        update_logpush_job_v2_request_logpush_jobs_update_ibmcl_req_model_dict = UpdateLogpushJobV2RequestLogpushJobsUpdateIbmclReq.from_dict(update_logpush_job_v2_request_logpush_jobs_update_ibmcl_req_model_json).__dict__
        update_logpush_job_v2_request_logpush_jobs_update_ibmcl_req_model2 = UpdateLogpushJobV2RequestLogpushJobsUpdateIbmclReq(**update_logpush_job_v2_request_logpush_jobs_update_ibmcl_req_model_dict)

        # Verify the model instances are equivalent
        assert update_logpush_job_v2_request_logpush_jobs_update_ibmcl_req_model == update_logpush_job_v2_request_logpush_jobs_update_ibmcl_req_model2

        # Convert model instance back to dict and verify no loss of data
        update_logpush_job_v2_request_logpush_jobs_update_ibmcl_req_model_json2 = update_logpush_job_v2_request_logpush_jobs_update_ibmcl_req_model.to_dict()
        assert update_logpush_job_v2_request_logpush_jobs_update_ibmcl_req_model_json2 == update_logpush_job_v2_request_logpush_jobs_update_ibmcl_req_model_json


class TestModel_UpdateLogpushJobV2RequestLogpushJobsUpdateLogdnaReq:
    """
    Test Class for UpdateLogpushJobV2RequestLogpushJobsUpdateLogdnaReq
    """

    def test_update_logpush_job_v2_request_logpush_jobs_update_logdna_req_serialization(self):
        """
        Test serialization/deserialization for UpdateLogpushJobV2RequestLogpushJobsUpdateLogdnaReq
        """

        # Construct a json representation of a UpdateLogpushJobV2RequestLogpushJobsUpdateLogdnaReq model
        update_logpush_job_v2_request_logpush_jobs_update_logdna_req_model_json = {}
        update_logpush_job_v2_request_logpush_jobs_update_logdna_req_model_json['enabled'] = False
        update_logpush_job_v2_request_logpush_jobs_update_logdna_req_model_json['logpull_options'] = 'timestamps=rfc3339&timestamps=rfc3339'
        update_logpush_job_v2_request_logpush_jobs_update_logdna_req_model_json['logdna'] = {'ingress_key': '8aef12bcd5e5af42', 'region': 'us-south', 'hostname': 'www.example.com'}
        update_logpush_job_v2_request_logpush_jobs_update_logdna_req_model_json['frequency'] = 'high'

        # Construct a model instance of UpdateLogpushJobV2RequestLogpushJobsUpdateLogdnaReq by calling from_dict on the json representation
        update_logpush_job_v2_request_logpush_jobs_update_logdna_req_model = UpdateLogpushJobV2RequestLogpushJobsUpdateLogdnaReq.from_dict(update_logpush_job_v2_request_logpush_jobs_update_logdna_req_model_json)
        assert update_logpush_job_v2_request_logpush_jobs_update_logdna_req_model != False

        # Construct a model instance of UpdateLogpushJobV2RequestLogpushJobsUpdateLogdnaReq by calling from_dict on the json representation
        update_logpush_job_v2_request_logpush_jobs_update_logdna_req_model_dict = UpdateLogpushJobV2RequestLogpushJobsUpdateLogdnaReq.from_dict(update_logpush_job_v2_request_logpush_jobs_update_logdna_req_model_json).__dict__
        update_logpush_job_v2_request_logpush_jobs_update_logdna_req_model2 = UpdateLogpushJobV2RequestLogpushJobsUpdateLogdnaReq(**update_logpush_job_v2_request_logpush_jobs_update_logdna_req_model_dict)

        # Verify the model instances are equivalent
        assert update_logpush_job_v2_request_logpush_jobs_update_logdna_req_model == update_logpush_job_v2_request_logpush_jobs_update_logdna_req_model2

        # Convert model instance back to dict and verify no loss of data
        update_logpush_job_v2_request_logpush_jobs_update_logdna_req_model_json2 = update_logpush_job_v2_request_logpush_jobs_update_logdna_req_model.to_dict()
        assert update_logpush_job_v2_request_logpush_jobs_update_logdna_req_model_json2 == update_logpush_job_v2_request_logpush_jobs_update_logdna_req_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
