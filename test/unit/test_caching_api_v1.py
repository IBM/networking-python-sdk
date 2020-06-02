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
import responses
from ibm_cloud_networking_services import CachingApiV1

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
# Start of Service: PurgeAll
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for purge_all
#-----------------------------------------------------------------------------
class TestPurgeAll():

    #--------------------------------------------------------
    # purge_all()
    #--------------------------------------------------------
    @responses.activate
    def test_purge_all_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/purge_cache/purge_all'
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
    # test_purge_all_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_purge_all_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/purge_cache/purge_all'
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


# endregion
##############################################################################
# End of Service: PurgeAll
##############################################################################

##############################################################################
# Start of Service: PurgeByURLs
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for purge_by_urls
#-----------------------------------------------------------------------------
class TestPurgeByUrls():

    #--------------------------------------------------------
    # purge_by_urls()
    #--------------------------------------------------------
    @responses.activate
    def test_purge_by_urls_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/purge_cache/purge_by_urls'
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
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['files'] == files


    #--------------------------------------------------------
    # test_purge_by_urls_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_purge_by_urls_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/purge_cache/purge_by_urls'
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


# endregion
##############################################################################
# End of Service: PurgeByURLs
##############################################################################

##############################################################################
# Start of Service: PurgeByTags
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for purge_by_cache_tags
#-----------------------------------------------------------------------------
class TestPurgeByCacheTags():

    #--------------------------------------------------------
    # purge_by_cache_tags()
    #--------------------------------------------------------
    @responses.activate
    def test_purge_by_cache_tags_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/purge_cache/purge_by_cache_tags'
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
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['tags'] == tags


    #--------------------------------------------------------
    # test_purge_by_cache_tags_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_purge_by_cache_tags_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/purge_cache/purge_by_cache_tags'
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


# endregion
##############################################################################
# End of Service: PurgeByTags
##############################################################################

##############################################################################
# Start of Service: PurgeByHosts
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for purge_by_hosts
#-----------------------------------------------------------------------------
class TestPurgeByHosts():

    #--------------------------------------------------------
    # purge_by_hosts()
    #--------------------------------------------------------
    @responses.activate
    def test_purge_by_hosts_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/purge_cache/purge_by_hosts'
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
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['hosts'] == hosts


    #--------------------------------------------------------
    # test_purge_by_hosts_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_purge_by_hosts_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/purge_cache/purge_by_hosts'
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


# endregion
##############################################################################
# End of Service: PurgeByHosts
##############################################################################

##############################################################################
# Start of Service: CacheLevel
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_cache_level
#-----------------------------------------------------------------------------
class TestGetCacheLevel():

    #--------------------------------------------------------
    # get_cache_level()
    #--------------------------------------------------------
    @responses.activate
    def test_get_cache_level_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/cache_level'
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
    # test_get_cache_level_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_cache_level_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/cache_level'
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


#-----------------------------------------------------------------------------
# Test Class for update_cache_level
#-----------------------------------------------------------------------------
class TestUpdateCacheLevel():

    #--------------------------------------------------------
    # update_cache_level()
    #--------------------------------------------------------
    @responses.activate
    def test_update_cache_level_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/cache_level'
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
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == value


    #--------------------------------------------------------
    # test_update_cache_level_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_cache_level_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/cache_level'
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


# endregion
##############################################################################
# End of Service: CacheLevel
##############################################################################

##############################################################################
# Start of Service: BrowserCacheTTL
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_browser_cache_ttl
#-----------------------------------------------------------------------------
class TestGetBrowserCacheTtl():

    #--------------------------------------------------------
    # get_browser_cache_ttl()
    #--------------------------------------------------------
    @responses.activate
    def test_get_browser_cache_ttl_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/browser_cache_ttl'
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
    # test_get_browser_cache_ttl_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_browser_cache_ttl_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/browser_cache_ttl'
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


#-----------------------------------------------------------------------------
# Test Class for update_browser_cache_ttl
#-----------------------------------------------------------------------------
class TestUpdateBrowserCacheTtl():

    #--------------------------------------------------------
    # update_browser_cache_ttl()
    #--------------------------------------------------------
    @responses.activate
    def test_update_browser_cache_ttl_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/browser_cache_ttl'
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
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == value


    #--------------------------------------------------------
    # test_update_browser_cache_ttl_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_browser_cache_ttl_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/browser_cache_ttl'
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


# endregion
##############################################################################
# End of Service: BrowserCacheTTL
##############################################################################

##############################################################################
# Start of Service: DevelopmentMode
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_development_mode
#-----------------------------------------------------------------------------
class TestGetDevelopmentMode():

    #--------------------------------------------------------
    # get_development_mode()
    #--------------------------------------------------------
    @responses.activate
    def test_get_development_mode_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/development_mode'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "development_mode", "value": "false", "editable": true, "modified_on": "2014-01-01T05:20:00.12345Z"}}'
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
    # test_get_development_mode_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_development_mode_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/development_mode'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "development_mode", "value": "false", "editable": true, "modified_on": "2014-01-01T05:20:00.12345Z"}}'
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


#-----------------------------------------------------------------------------
# Test Class for update_development_mode
#-----------------------------------------------------------------------------
class TestUpdateDevelopmentMode():

    #--------------------------------------------------------
    # update_development_mode()
    #--------------------------------------------------------
    @responses.activate
    def test_update_development_mode_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/development_mode'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "development_mode", "value": "false", "editable": true, "modified_on": "2014-01-01T05:20:00.12345Z"}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        value = 'false'

        # Invoke method
        response = service.update_development_mode(
            value=value,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == value


    #--------------------------------------------------------
    # test_update_development_mode_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_development_mode_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/development_mode'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "development_mode", "value": "false", "editable": true, "modified_on": "2014-01-01T05:20:00.12345Z"}}'
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


# endregion
##############################################################################
# End of Service: DevelopmentMode
##############################################################################

##############################################################################
# Start of Service: EnableQueryStringSort
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_query_string_sort
#-----------------------------------------------------------------------------
class TestGetQueryStringSort():

    #--------------------------------------------------------
    # get_query_string_sort()
    #--------------------------------------------------------
    @responses.activate
    def test_get_query_string_sort_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/sort_query_string_for_cache'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "sort_query_string_for_cache", "value": "false", "editable": true, "modified_on": "2014-01-01T05:20:00.12345Z"}}'
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
    # test_get_query_string_sort_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_query_string_sort_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/sort_query_string_for_cache'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "sort_query_string_for_cache", "value": "false", "editable": true, "modified_on": "2014-01-01T05:20:00.12345Z"}}'
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


#-----------------------------------------------------------------------------
# Test Class for update_query_string_sort
#-----------------------------------------------------------------------------
class TestUpdateQueryStringSort():

    #--------------------------------------------------------
    # update_query_string_sort()
    #--------------------------------------------------------
    @responses.activate
    def test_update_query_string_sort_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/sort_query_string_for_cache'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "sort_query_string_for_cache", "value": "false", "editable": true, "modified_on": "2014-01-01T05:20:00.12345Z"}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        value = 'false'

        # Invoke method
        response = service.update_query_string_sort(
            value=value,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == value


    #--------------------------------------------------------
    # test_update_query_string_sort_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_query_string_sort_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/sort_query_string_for_cache'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "sort_query_string_for_cache", "value": "false", "editable": true, "modified_on": "2014-01-01T05:20:00.12345Z"}}'
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


# endregion
##############################################################################
# End of Service: EnableQueryStringSort
##############################################################################

