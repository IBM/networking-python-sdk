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
import re
import responses
from ibm_cloud_networking_services.caching_api_v1 import *

crn = 'testString'
zone_id = 'testString'

service = CachingApiV1(
    authenticator=NoAuthAuthenticator(),
    crn=crn,
    zone_id=zone_id
    )

base_url = 'https://api.cis.cloud.ibm.com'
service.set_service_url(base_url)

##############################################################################
# Start of Service: CacheSettings
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for purge_all
#-----------------------------------------------------------------------------
class TestPurgeAll():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # purge_all()
    #--------------------------------------------------------
    @responses.activate
    def test_purge_all_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/purge_cache/purge_all')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "62d26b178b67c0eda0613891f3f51b0a"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.purge_all()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_purge_all_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_purge_all_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/purge_cache/purge_all')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "62d26b178b67c0eda0613891f3f51b0a"}}'
        responses.add(responses.PUT,
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
                service.purge_all(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for purge_by_urls
#-----------------------------------------------------------------------------
class TestPurgeByUrls():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # purge_by_urls()
    #--------------------------------------------------------
    @responses.activate
    def test_purge_by_urls_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/purge_cache/purge_by_urls')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "62d26b178b67c0eda0613891f3f51b0a"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        files = ['http://www.example.com/cat_picture.jpg']

        # Invoke method
        response = service.purge_by_urls(
            files=files,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['files'] == ['http://www.example.com/cat_picture.jpg']


    #--------------------------------------------------------
    # test_purge_by_urls_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_purge_by_urls_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/purge_cache/purge_by_urls')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "62d26b178b67c0eda0613891f3f51b0a"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.purge_by_urls()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_purge_by_urls_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_purge_by_urls_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/purge_cache/purge_by_urls')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "62d26b178b67c0eda0613891f3f51b0a"}}'
        responses.add(responses.PUT,
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
                service.purge_by_urls(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for purge_by_cache_tags
#-----------------------------------------------------------------------------
class TestPurgeByCacheTags():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # purge_by_cache_tags()
    #--------------------------------------------------------
    @responses.activate
    def test_purge_by_cache_tags_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/purge_cache/purge_by_cache_tags')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "62d26b178b67c0eda0613891f3f51b0a"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        tags = ['some-tag']

        # Invoke method
        response = service.purge_by_cache_tags(
            tags=tags,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['tags'] == ['some-tag']


    #--------------------------------------------------------
    # test_purge_by_cache_tags_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_purge_by_cache_tags_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/purge_cache/purge_by_cache_tags')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "62d26b178b67c0eda0613891f3f51b0a"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.purge_by_cache_tags()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_purge_by_cache_tags_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_purge_by_cache_tags_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/purge_cache/purge_by_cache_tags')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "62d26b178b67c0eda0613891f3f51b0a"}}'
        responses.add(responses.PUT,
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
                service.purge_by_cache_tags(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for purge_by_hosts
#-----------------------------------------------------------------------------
class TestPurgeByHosts():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # purge_by_hosts()
    #--------------------------------------------------------
    @responses.activate
    def test_purge_by_hosts_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/purge_cache/purge_by_hosts')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "62d26b178b67c0eda0613891f3f51b0a"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        hosts = ['www.example.com']

        # Invoke method
        response = service.purge_by_hosts(
            hosts=hosts,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['hosts'] == ['www.example.com']


    #--------------------------------------------------------
    # test_purge_by_hosts_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_purge_by_hosts_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/purge_cache/purge_by_hosts')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "62d26b178b67c0eda0613891f3f51b0a"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.purge_by_hosts()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_purge_by_hosts_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_purge_by_hosts_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/purge_cache/purge_by_hosts')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "62d26b178b67c0eda0613891f3f51b0a"}}'
        responses.add(responses.PUT,
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
                service.purge_by_hosts(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_browser_cache_ttl
#-----------------------------------------------------------------------------
class TestGetBrowserCacheTtl():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_browser_cache_ttl()
    #--------------------------------------------------------
    @responses.activate
    def test_get_browser_cache_ttl_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/browser_cache_ttl')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "browser_cache_ttl", "value": 14400, "editable": true, "modified_on": "2014-01-01T05:20:00.12345Z"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_browser_cache_ttl()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_browser_cache_ttl_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_browser_cache_ttl_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/browser_cache_ttl')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "browser_cache_ttl", "value": 14400, "editable": true, "modified_on": "2014-01-01T05:20:00.12345Z"}}'
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
                service.get_browser_cache_ttl(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_browser_cache_ttl
#-----------------------------------------------------------------------------
class TestUpdateBrowserCacheTtl():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_browser_cache_ttl()
    #--------------------------------------------------------
    @responses.activate
    def test_update_browser_cache_ttl_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/browser_cache_ttl')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "browser_cache_ttl", "value": 14400, "editable": true, "modified_on": "2014-01-01T05:20:00.12345Z"}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        value = 14400

        # Invoke method
        response = service.update_browser_cache_ttl(
            value=value,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 14400


    #--------------------------------------------------------
    # test_update_browser_cache_ttl_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_browser_cache_ttl_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/browser_cache_ttl')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "browser_cache_ttl", "value": 14400, "editable": true, "modified_on": "2014-01-01T05:20:00.12345Z"}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.update_browser_cache_ttl()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_browser_cache_ttl_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_browser_cache_ttl_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/browser_cache_ttl')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "browser_cache_ttl", "value": 14400, "editable": true, "modified_on": "2014-01-01T05:20:00.12345Z"}}'
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
                service.update_browser_cache_ttl(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_development_mode
#-----------------------------------------------------------------------------
class TestGetDevelopmentMode():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_development_mode()
    #--------------------------------------------------------
    @responses.activate
    def test_get_development_mode_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/development_mode')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "development_mode", "value": "off", "editable": true, "modified_on": "2014-01-01T05:20:00.12345Z"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_development_mode()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_development_mode_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_development_mode_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/development_mode')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "development_mode", "value": "off", "editable": true, "modified_on": "2014-01-01T05:20:00.12345Z"}}'
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
                service.get_development_mode(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_development_mode
#-----------------------------------------------------------------------------
class TestUpdateDevelopmentMode():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_development_mode()
    #--------------------------------------------------------
    @responses.activate
    def test_update_development_mode_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/development_mode')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "development_mode", "value": "off", "editable": true, "modified_on": "2014-01-01T05:20:00.12345Z"}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        value = 'off'

        # Invoke method
        response = service.update_development_mode(
            value=value,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'off'


    #--------------------------------------------------------
    # test_update_development_mode_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_development_mode_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/development_mode')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "development_mode", "value": "off", "editable": true, "modified_on": "2014-01-01T05:20:00.12345Z"}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.update_development_mode()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_development_mode_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_development_mode_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/development_mode')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "development_mode", "value": "off", "editable": true, "modified_on": "2014-01-01T05:20:00.12345Z"}}'
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
                service.update_development_mode(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_query_string_sort
#-----------------------------------------------------------------------------
class TestGetQueryStringSort():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_query_string_sort()
    #--------------------------------------------------------
    @responses.activate
    def test_get_query_string_sort_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/sort_query_string_for_cache')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "sort_query_string_for_cache", "value": "off", "editable": true, "modified_on": "2014-01-01T05:20:00.12345Z"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_query_string_sort()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_query_string_sort_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_query_string_sort_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/sort_query_string_for_cache')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "sort_query_string_for_cache", "value": "off", "editable": true, "modified_on": "2014-01-01T05:20:00.12345Z"}}'
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
                service.get_query_string_sort(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_query_string_sort
#-----------------------------------------------------------------------------
class TestUpdateQueryStringSort():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_query_string_sort()
    #--------------------------------------------------------
    @responses.activate
    def test_update_query_string_sort_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/sort_query_string_for_cache')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "sort_query_string_for_cache", "value": "off", "editable": true, "modified_on": "2014-01-01T05:20:00.12345Z"}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        value = 'off'

        # Invoke method
        response = service.update_query_string_sort(
            value=value,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'off'


    #--------------------------------------------------------
    # test_update_query_string_sort_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_query_string_sort_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/sort_query_string_for_cache')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "sort_query_string_for_cache", "value": "off", "editable": true, "modified_on": "2014-01-01T05:20:00.12345Z"}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.update_query_string_sort()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_query_string_sort_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_query_string_sort_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/sort_query_string_for_cache')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "sort_query_string_for_cache", "value": "off", "editable": true, "modified_on": "2014-01-01T05:20:00.12345Z"}}'
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
                service.update_query_string_sort(**req_copy)



# endregion
##############################################################################
# End of Service: CacheSettings
##############################################################################

##############################################################################
# Start of Service: CacheLevel
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_cache_level
#-----------------------------------------------------------------------------
class TestGetCacheLevel():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_cache_level()
    #--------------------------------------------------------
    @responses.activate
    def test_get_cache_level_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/cache_level')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "cache_level", "value": "aggressive", "editable": true, "modified_on": "2014-01-01T05:20:00.12345Z"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_cache_level()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_cache_level_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_cache_level_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/cache_level')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "cache_level", "value": "aggressive", "editable": true, "modified_on": "2014-01-01T05:20:00.12345Z"}}'
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
                service.get_cache_level(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_cache_level
#-----------------------------------------------------------------------------
class TestUpdateCacheLevel():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_cache_level()
    #--------------------------------------------------------
    @responses.activate
    def test_update_cache_level_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/cache_level')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "cache_level", "value": "aggressive", "editable": true, "modified_on": "2014-01-01T05:20:00.12345Z"}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        value = 'aggressive'

        # Invoke method
        response = service.update_cache_level(
            value=value,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'aggressive'


    #--------------------------------------------------------
    # test_update_cache_level_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_cache_level_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/cache_level')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "cache_level", "value": "aggressive", "editable": true, "modified_on": "2014-01-01T05:20:00.12345Z"}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.update_cache_level()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_cache_level_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_cache_level_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/cache_level')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "cache_level", "value": "aggressive", "editable": true, "modified_on": "2014-01-01T05:20:00.12345Z"}}'
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
                service.update_cache_level(**req_copy)



# endregion
##############################################################################
# End of Service: CacheLevel
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
#-----------------------------------------------------------------------------
# Test Class for BrowserTTLResponseResult
#-----------------------------------------------------------------------------
class TestBrowserTTLResponseResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for BrowserTTLResponseResult
    #--------------------------------------------------------
    def test_browser_ttl_response_result_serialization(self):

        # Construct a json representation of a BrowserTTLResponseResult model
        browser_ttl_response_result_model_json = {}
        browser_ttl_response_result_model_json['id'] = 'browser_cache_ttl'
        browser_ttl_response_result_model_json['value'] = 14400
        browser_ttl_response_result_model_json['editable'] = True
        browser_ttl_response_result_model_json['modified_on'] = '2014-01-01T05:20:00.12345Z'

        # Construct a model instance of BrowserTTLResponseResult by calling from_dict on the json representation
        browser_ttl_response_result_model = BrowserTTLResponseResult.from_dict(browser_ttl_response_result_model_json)
        assert browser_ttl_response_result_model != False

        # Construct a model instance of BrowserTTLResponseResult by calling from_dict on the json representation
        browser_ttl_response_result_model_dict = BrowserTTLResponseResult.from_dict(browser_ttl_response_result_model_json).__dict__
        browser_ttl_response_result_model2 = BrowserTTLResponseResult(**browser_ttl_response_result_model_dict)

        # Verify the model instances are equivalent
        assert browser_ttl_response_result_model == browser_ttl_response_result_model2

        # Convert model instance back to dict and verify no loss of data
        browser_ttl_response_result_model_json2 = browser_ttl_response_result_model.to_dict()
        assert browser_ttl_response_result_model_json2 == browser_ttl_response_result_model_json

#-----------------------------------------------------------------------------
# Test Class for CacheLevelResponseResult
#-----------------------------------------------------------------------------
class TestCacheLevelResponseResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for CacheLevelResponseResult
    #--------------------------------------------------------
    def test_cache_level_response_result_serialization(self):

        # Construct a json representation of a CacheLevelResponseResult model
        cache_level_response_result_model_json = {}
        cache_level_response_result_model_json['id'] = 'cache_level'
        cache_level_response_result_model_json['value'] = 'aggressive'
        cache_level_response_result_model_json['editable'] = True
        cache_level_response_result_model_json['modified_on'] = '2014-01-01T05:20:00.12345Z'

        # Construct a model instance of CacheLevelResponseResult by calling from_dict on the json representation
        cache_level_response_result_model = CacheLevelResponseResult.from_dict(cache_level_response_result_model_json)
        assert cache_level_response_result_model != False

        # Construct a model instance of CacheLevelResponseResult by calling from_dict on the json representation
        cache_level_response_result_model_dict = CacheLevelResponseResult.from_dict(cache_level_response_result_model_json).__dict__
        cache_level_response_result_model2 = CacheLevelResponseResult(**cache_level_response_result_model_dict)

        # Verify the model instances are equivalent
        assert cache_level_response_result_model == cache_level_response_result_model2

        # Convert model instance back to dict and verify no loss of data
        cache_level_response_result_model_json2 = cache_level_response_result_model.to_dict()
        assert cache_level_response_result_model_json2 == cache_level_response_result_model_json

#-----------------------------------------------------------------------------
# Test Class for DeveopmentModeResponseResult
#-----------------------------------------------------------------------------
class TestDeveopmentModeResponseResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for DeveopmentModeResponseResult
    #--------------------------------------------------------
    def test_deveopment_mode_response_result_serialization(self):

        # Construct a json representation of a DeveopmentModeResponseResult model
        deveopment_mode_response_result_model_json = {}
        deveopment_mode_response_result_model_json['id'] = 'development_mode'
        deveopment_mode_response_result_model_json['value'] = 'off'
        deveopment_mode_response_result_model_json['editable'] = True
        deveopment_mode_response_result_model_json['modified_on'] = '2014-01-01T05:20:00.12345Z'

        # Construct a model instance of DeveopmentModeResponseResult by calling from_dict on the json representation
        deveopment_mode_response_result_model = DeveopmentModeResponseResult.from_dict(deveopment_mode_response_result_model_json)
        assert deveopment_mode_response_result_model != False

        # Construct a model instance of DeveopmentModeResponseResult by calling from_dict on the json representation
        deveopment_mode_response_result_model_dict = DeveopmentModeResponseResult.from_dict(deveopment_mode_response_result_model_json).__dict__
        deveopment_mode_response_result_model2 = DeveopmentModeResponseResult(**deveopment_mode_response_result_model_dict)

        # Verify the model instances are equivalent
        assert deveopment_mode_response_result_model == deveopment_mode_response_result_model2

        # Convert model instance back to dict and verify no loss of data
        deveopment_mode_response_result_model_json2 = deveopment_mode_response_result_model.to_dict()
        assert deveopment_mode_response_result_model_json2 == deveopment_mode_response_result_model_json

#-----------------------------------------------------------------------------
# Test Class for EnableQueryStringSortResponseResult
#-----------------------------------------------------------------------------
class TestEnableQueryStringSortResponseResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for EnableQueryStringSortResponseResult
    #--------------------------------------------------------
    def test_enable_query_string_sort_response_result_serialization(self):

        # Construct a json representation of a EnableQueryStringSortResponseResult model
        enable_query_string_sort_response_result_model_json = {}
        enable_query_string_sort_response_result_model_json['id'] = 'sort_query_string_for_cache'
        enable_query_string_sort_response_result_model_json['value'] = 'off'
        enable_query_string_sort_response_result_model_json['editable'] = True
        enable_query_string_sort_response_result_model_json['modified_on'] = '2014-01-01T05:20:00.12345Z'

        # Construct a model instance of EnableQueryStringSortResponseResult by calling from_dict on the json representation
        enable_query_string_sort_response_result_model = EnableQueryStringSortResponseResult.from_dict(enable_query_string_sort_response_result_model_json)
        assert enable_query_string_sort_response_result_model != False

        # Construct a model instance of EnableQueryStringSortResponseResult by calling from_dict on the json representation
        enable_query_string_sort_response_result_model_dict = EnableQueryStringSortResponseResult.from_dict(enable_query_string_sort_response_result_model_json).__dict__
        enable_query_string_sort_response_result_model2 = EnableQueryStringSortResponseResult(**enable_query_string_sort_response_result_model_dict)

        # Verify the model instances are equivalent
        assert enable_query_string_sort_response_result_model == enable_query_string_sort_response_result_model2

        # Convert model instance back to dict and verify no loss of data
        enable_query_string_sort_response_result_model_json2 = enable_query_string_sort_response_result_model.to_dict()
        assert enable_query_string_sort_response_result_model_json2 == enable_query_string_sort_response_result_model_json

#-----------------------------------------------------------------------------
# Test Class for PurgeAllResponseResult
#-----------------------------------------------------------------------------
class TestPurgeAllResponseResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for PurgeAllResponseResult
    #--------------------------------------------------------
    def test_purge_all_response_result_serialization(self):

        # Construct a json representation of a PurgeAllResponseResult model
        purge_all_response_result_model_json = {}
        purge_all_response_result_model_json['id'] = '62d26b178b67c0eda0613891f3f51b0a'

        # Construct a model instance of PurgeAllResponseResult by calling from_dict on the json representation
        purge_all_response_result_model = PurgeAllResponseResult.from_dict(purge_all_response_result_model_json)
        assert purge_all_response_result_model != False

        # Construct a model instance of PurgeAllResponseResult by calling from_dict on the json representation
        purge_all_response_result_model_dict = PurgeAllResponseResult.from_dict(purge_all_response_result_model_json).__dict__
        purge_all_response_result_model2 = PurgeAllResponseResult(**purge_all_response_result_model_dict)

        # Verify the model instances are equivalent
        assert purge_all_response_result_model == purge_all_response_result_model2

        # Convert model instance back to dict and verify no loss of data
        purge_all_response_result_model_json2 = purge_all_response_result_model.to_dict()
        assert purge_all_response_result_model_json2 == purge_all_response_result_model_json

#-----------------------------------------------------------------------------
# Test Class for BrowserTTLResponse
#-----------------------------------------------------------------------------
class TestBrowserTTLResponse():

    #--------------------------------------------------------
    # Test serialization/deserialization for BrowserTTLResponse
    #--------------------------------------------------------
    def test_browser_ttl_response_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        browser_ttl_response_result_model = {} # BrowserTTLResponseResult
        browser_ttl_response_result_model['id'] = 'browser_cache_ttl'
        browser_ttl_response_result_model['value'] = 14400
        browser_ttl_response_result_model['editable'] = True
        browser_ttl_response_result_model['modified_on'] = '2014-01-01T05:20:00.12345Z'

        # Construct a json representation of a BrowserTTLResponse model
        browser_ttl_response_model_json = {}
        browser_ttl_response_model_json['success'] = True
        browser_ttl_response_model_json['errors'] = [['testString']]
        browser_ttl_response_model_json['messages'] = [['testString']]
        browser_ttl_response_model_json['result'] = browser_ttl_response_result_model

        # Construct a model instance of BrowserTTLResponse by calling from_dict on the json representation
        browser_ttl_response_model = BrowserTTLResponse.from_dict(browser_ttl_response_model_json)
        assert browser_ttl_response_model != False

        # Construct a model instance of BrowserTTLResponse by calling from_dict on the json representation
        browser_ttl_response_model_dict = BrowserTTLResponse.from_dict(browser_ttl_response_model_json).__dict__
        browser_ttl_response_model2 = BrowserTTLResponse(**browser_ttl_response_model_dict)

        # Verify the model instances are equivalent
        assert browser_ttl_response_model == browser_ttl_response_model2

        # Convert model instance back to dict and verify no loss of data
        browser_ttl_response_model_json2 = browser_ttl_response_model.to_dict()
        assert browser_ttl_response_model_json2 == browser_ttl_response_model_json

#-----------------------------------------------------------------------------
# Test Class for CacheLevelResponse
#-----------------------------------------------------------------------------
class TestCacheLevelResponse():

    #--------------------------------------------------------
    # Test serialization/deserialization for CacheLevelResponse
    #--------------------------------------------------------
    def test_cache_level_response_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        cache_level_response_result_model = {} # CacheLevelResponseResult
        cache_level_response_result_model['id'] = 'cache_level'
        cache_level_response_result_model['value'] = 'aggressive'
        cache_level_response_result_model['editable'] = True
        cache_level_response_result_model['modified_on'] = '2014-01-01T05:20:00.12345Z'

        # Construct a json representation of a CacheLevelResponse model
        cache_level_response_model_json = {}
        cache_level_response_model_json['success'] = True
        cache_level_response_model_json['errors'] = [['testString']]
        cache_level_response_model_json['messages'] = [['testString']]
        cache_level_response_model_json['result'] = cache_level_response_result_model

        # Construct a model instance of CacheLevelResponse by calling from_dict on the json representation
        cache_level_response_model = CacheLevelResponse.from_dict(cache_level_response_model_json)
        assert cache_level_response_model != False

        # Construct a model instance of CacheLevelResponse by calling from_dict on the json representation
        cache_level_response_model_dict = CacheLevelResponse.from_dict(cache_level_response_model_json).__dict__
        cache_level_response_model2 = CacheLevelResponse(**cache_level_response_model_dict)

        # Verify the model instances are equivalent
        assert cache_level_response_model == cache_level_response_model2

        # Convert model instance back to dict and verify no loss of data
        cache_level_response_model_json2 = cache_level_response_model.to_dict()
        assert cache_level_response_model_json2 == cache_level_response_model_json

#-----------------------------------------------------------------------------
# Test Class for DeveopmentModeResponse
#-----------------------------------------------------------------------------
class TestDeveopmentModeResponse():

    #--------------------------------------------------------
    # Test serialization/deserialization for DeveopmentModeResponse
    #--------------------------------------------------------
    def test_deveopment_mode_response_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        deveopment_mode_response_result_model = {} # DeveopmentModeResponseResult
        deveopment_mode_response_result_model['id'] = 'development_mode'
        deveopment_mode_response_result_model['value'] = 'off'
        deveopment_mode_response_result_model['editable'] = True
        deveopment_mode_response_result_model['modified_on'] = '2014-01-01T05:20:00.12345Z'

        # Construct a json representation of a DeveopmentModeResponse model
        deveopment_mode_response_model_json = {}
        deveopment_mode_response_model_json['success'] = True
        deveopment_mode_response_model_json['errors'] = [['testString']]
        deveopment_mode_response_model_json['messages'] = [['testString']]
        deveopment_mode_response_model_json['result'] = deveopment_mode_response_result_model

        # Construct a model instance of DeveopmentModeResponse by calling from_dict on the json representation
        deveopment_mode_response_model = DeveopmentModeResponse.from_dict(deveopment_mode_response_model_json)
        assert deveopment_mode_response_model != False

        # Construct a model instance of DeveopmentModeResponse by calling from_dict on the json representation
        deveopment_mode_response_model_dict = DeveopmentModeResponse.from_dict(deveopment_mode_response_model_json).__dict__
        deveopment_mode_response_model2 = DeveopmentModeResponse(**deveopment_mode_response_model_dict)

        # Verify the model instances are equivalent
        assert deveopment_mode_response_model == deveopment_mode_response_model2

        # Convert model instance back to dict and verify no loss of data
        deveopment_mode_response_model_json2 = deveopment_mode_response_model.to_dict()
        assert deveopment_mode_response_model_json2 == deveopment_mode_response_model_json

#-----------------------------------------------------------------------------
# Test Class for EnableQueryStringSortResponse
#-----------------------------------------------------------------------------
class TestEnableQueryStringSortResponse():

    #--------------------------------------------------------
    # Test serialization/deserialization for EnableQueryStringSortResponse
    #--------------------------------------------------------
    def test_enable_query_string_sort_response_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        enable_query_string_sort_response_result_model = {} # EnableQueryStringSortResponseResult
        enable_query_string_sort_response_result_model['id'] = 'sort_query_string_for_cache'
        enable_query_string_sort_response_result_model['value'] = 'off'
        enable_query_string_sort_response_result_model['editable'] = True
        enable_query_string_sort_response_result_model['modified_on'] = '2014-01-01T05:20:00.12345Z'

        # Construct a json representation of a EnableQueryStringSortResponse model
        enable_query_string_sort_response_model_json = {}
        enable_query_string_sort_response_model_json['success'] = True
        enable_query_string_sort_response_model_json['errors'] = [['testString']]
        enable_query_string_sort_response_model_json['messages'] = [['testString']]
        enable_query_string_sort_response_model_json['result'] = enable_query_string_sort_response_result_model

        # Construct a model instance of EnableQueryStringSortResponse by calling from_dict on the json representation
        enable_query_string_sort_response_model = EnableQueryStringSortResponse.from_dict(enable_query_string_sort_response_model_json)
        assert enable_query_string_sort_response_model != False

        # Construct a model instance of EnableQueryStringSortResponse by calling from_dict on the json representation
        enable_query_string_sort_response_model_dict = EnableQueryStringSortResponse.from_dict(enable_query_string_sort_response_model_json).__dict__
        enable_query_string_sort_response_model2 = EnableQueryStringSortResponse(**enable_query_string_sort_response_model_dict)

        # Verify the model instances are equivalent
        assert enable_query_string_sort_response_model == enable_query_string_sort_response_model2

        # Convert model instance back to dict and verify no loss of data
        enable_query_string_sort_response_model_json2 = enable_query_string_sort_response_model.to_dict()
        assert enable_query_string_sort_response_model_json2 == enable_query_string_sort_response_model_json

#-----------------------------------------------------------------------------
# Test Class for PurgeAllResponse
#-----------------------------------------------------------------------------
class TestPurgeAllResponse():

    #--------------------------------------------------------
    # Test serialization/deserialization for PurgeAllResponse
    #--------------------------------------------------------
    def test_purge_all_response_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        purge_all_response_result_model = {} # PurgeAllResponseResult
        purge_all_response_result_model['id'] = '62d26b178b67c0eda0613891f3f51b0a'

        # Construct a json representation of a PurgeAllResponse model
        purge_all_response_model_json = {}
        purge_all_response_model_json['success'] = True
        purge_all_response_model_json['errors'] = [['testString']]
        purge_all_response_model_json['messages'] = [['testString']]
        purge_all_response_model_json['result'] = purge_all_response_result_model

        # Construct a model instance of PurgeAllResponse by calling from_dict on the json representation
        purge_all_response_model = PurgeAllResponse.from_dict(purge_all_response_model_json)
        assert purge_all_response_model != False

        # Construct a model instance of PurgeAllResponse by calling from_dict on the json representation
        purge_all_response_model_dict = PurgeAllResponse.from_dict(purge_all_response_model_json).__dict__
        purge_all_response_model2 = PurgeAllResponse(**purge_all_response_model_dict)

        # Verify the model instances are equivalent
        assert purge_all_response_model == purge_all_response_model2

        # Convert model instance back to dict and verify no loss of data
        purge_all_response_model_json2 = purge_all_response_model.to_dict()
        assert purge_all_response_model_json2 == purge_all_response_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
