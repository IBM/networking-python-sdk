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
from ibm_cloud_networking_services.global_load_balancer_events_v1 import *

crn = 'testString'

service = GlobalLoadBalancerEventsV1(
    authenticator=NoAuthAuthenticator(),
    crn=crn
    )

base_url = 'https://api.cis.cloud.ibm.com'
service.set_service_url(base_url)

##############################################################################
# Start of Service: GlobalLoadBalancerEvents
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_load_balancer_events
#-----------------------------------------------------------------------------
class TestGetLoadBalancerEvents():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_load_balancer_events()
    #--------------------------------------------------------
    @responses.activate
    def test_get_load_balancer_events_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/load_balancers/events')
        mock_response = '{"success": true, "result": [{"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "timestamp": "2019-01-01T12:00:00", "pool": [{"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "name": "some-pool", "healthy": true, "changed": true, "minimum_origins": 1}], "origins": [{"name": "f1aba936b94213e5b8dca0c0dbf1f9cc", "address": "1.2.3.4", "ip": "1.2.3.4", "enabled": true, "healthy": true, "failure_reason": "No failures", "changed": true}]}], "result_info": {"page": 1, "per_page": 20, "count": 1, "total_count": 2000}, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_load_balancer_events()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_load_balancer_events_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_load_balancer_events_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/load_balancers/events')
        mock_response = '{"success": true, "result": [{"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "timestamp": "2019-01-01T12:00:00", "pool": [{"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "name": "some-pool", "healthy": true, "changed": true, "minimum_origins": 1}], "origins": [{"name": "f1aba936b94213e5b8dca0c0dbf1f9cc", "address": "1.2.3.4", "ip": "1.2.3.4", "enabled": true, "healthy": true, "failure_reason": "No failures", "changed": true}]}], "result_info": {"page": 1, "per_page": 20, "count": 1, "total_count": 2000}, "errors": [["errors"]], "messages": [["messages"]]}'
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
                service.get_load_balancer_events(**req_copy)



# endregion
##############################################################################
# End of Service: GlobalLoadBalancerEvents
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
#-----------------------------------------------------------------------------
# Test Class for ListEventsRespResultInfo
#-----------------------------------------------------------------------------
class TestListEventsRespResultInfo():

    #--------------------------------------------------------
    # Test serialization/deserialization for ListEventsRespResultInfo
    #--------------------------------------------------------
    def test_list_events_resp_result_info_serialization(self):

        # Construct a json representation of a ListEventsRespResultInfo model
        list_events_resp_result_info_model_json = {}
        list_events_resp_result_info_model_json['page'] = 1
        list_events_resp_result_info_model_json['per_page'] = 20
        list_events_resp_result_info_model_json['count'] = 1
        list_events_resp_result_info_model_json['total_count'] = 2000

        # Construct a model instance of ListEventsRespResultInfo by calling from_dict on the json representation
        list_events_resp_result_info_model = ListEventsRespResultInfo.from_dict(list_events_resp_result_info_model_json)
        assert list_events_resp_result_info_model != False

        # Construct a model instance of ListEventsRespResultInfo by calling from_dict on the json representation
        list_events_resp_result_info_model_dict = ListEventsRespResultInfo.from_dict(list_events_resp_result_info_model_json).__dict__
        list_events_resp_result_info_model2 = ListEventsRespResultInfo(**list_events_resp_result_info_model_dict)

        # Verify the model instances are equivalent
        assert list_events_resp_result_info_model == list_events_resp_result_info_model2

        # Convert model instance back to dict and verify no loss of data
        list_events_resp_result_info_model_json2 = list_events_resp_result_info_model.to_dict()
        assert list_events_resp_result_info_model_json2 == list_events_resp_result_info_model_json

#-----------------------------------------------------------------------------
# Test Class for ListEventsRespResultItem
#-----------------------------------------------------------------------------
class TestListEventsRespResultItem():

    #--------------------------------------------------------
    # Test serialization/deserialization for ListEventsRespResultItem
    #--------------------------------------------------------
    def test_list_events_resp_result_item_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        list_events_resp_result_item_origins_item_model = {} # ListEventsRespResultItemOriginsItem
        list_events_resp_result_item_origins_item_model['name'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'
        list_events_resp_result_item_origins_item_model['address'] = '1.2.3.4'
        list_events_resp_result_item_origins_item_model['ip'] = '1.2.3.4'
        list_events_resp_result_item_origins_item_model['enabled'] = True
        list_events_resp_result_item_origins_item_model['healthy'] = True
        list_events_resp_result_item_origins_item_model['failure_reason'] = 'No failures'
        list_events_resp_result_item_origins_item_model['changed'] = True

        list_events_resp_result_item_pool_item_model = {} # ListEventsRespResultItemPoolItem
        list_events_resp_result_item_pool_item_model['id'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'
        list_events_resp_result_item_pool_item_model['name'] = 'some-pool'
        list_events_resp_result_item_pool_item_model['healthy'] = True
        list_events_resp_result_item_pool_item_model['changed'] = True
        list_events_resp_result_item_pool_item_model['minimum_origins'] = 1

        # Construct a json representation of a ListEventsRespResultItem model
        list_events_resp_result_item_model_json = {}
        list_events_resp_result_item_model_json['id'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'
        list_events_resp_result_item_model_json['timestamp'] = '2020-01-28T18:40:40.123456Z'
        list_events_resp_result_item_model_json['pool'] = [list_events_resp_result_item_pool_item_model]
        list_events_resp_result_item_model_json['origins'] = [list_events_resp_result_item_origins_item_model]

        # Construct a model instance of ListEventsRespResultItem by calling from_dict on the json representation
        list_events_resp_result_item_model = ListEventsRespResultItem.from_dict(list_events_resp_result_item_model_json)
        assert list_events_resp_result_item_model != False

        # Construct a model instance of ListEventsRespResultItem by calling from_dict on the json representation
        list_events_resp_result_item_model_dict = ListEventsRespResultItem.from_dict(list_events_resp_result_item_model_json).__dict__
        list_events_resp_result_item_model2 = ListEventsRespResultItem(**list_events_resp_result_item_model_dict)

        # Verify the model instances are equivalent
        assert list_events_resp_result_item_model == list_events_resp_result_item_model2

        # Convert model instance back to dict and verify no loss of data
        list_events_resp_result_item_model_json2 = list_events_resp_result_item_model.to_dict()
        assert list_events_resp_result_item_model_json2 == list_events_resp_result_item_model_json

#-----------------------------------------------------------------------------
# Test Class for ListEventsRespResultItemOriginsItem
#-----------------------------------------------------------------------------
class TestListEventsRespResultItemOriginsItem():

    #--------------------------------------------------------
    # Test serialization/deserialization for ListEventsRespResultItemOriginsItem
    #--------------------------------------------------------
    def test_list_events_resp_result_item_origins_item_serialization(self):

        # Construct a json representation of a ListEventsRespResultItemOriginsItem model
        list_events_resp_result_item_origins_item_model_json = {}
        list_events_resp_result_item_origins_item_model_json['name'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'
        list_events_resp_result_item_origins_item_model_json['address'] = '1.2.3.4'
        list_events_resp_result_item_origins_item_model_json['ip'] = '1.2.3.4'
        list_events_resp_result_item_origins_item_model_json['enabled'] = True
        list_events_resp_result_item_origins_item_model_json['healthy'] = True
        list_events_resp_result_item_origins_item_model_json['failure_reason'] = 'No failures'
        list_events_resp_result_item_origins_item_model_json['changed'] = True

        # Construct a model instance of ListEventsRespResultItemOriginsItem by calling from_dict on the json representation
        list_events_resp_result_item_origins_item_model = ListEventsRespResultItemOriginsItem.from_dict(list_events_resp_result_item_origins_item_model_json)
        assert list_events_resp_result_item_origins_item_model != False

        # Construct a model instance of ListEventsRespResultItemOriginsItem by calling from_dict on the json representation
        list_events_resp_result_item_origins_item_model_dict = ListEventsRespResultItemOriginsItem.from_dict(list_events_resp_result_item_origins_item_model_json).__dict__
        list_events_resp_result_item_origins_item_model2 = ListEventsRespResultItemOriginsItem(**list_events_resp_result_item_origins_item_model_dict)

        # Verify the model instances are equivalent
        assert list_events_resp_result_item_origins_item_model == list_events_resp_result_item_origins_item_model2

        # Convert model instance back to dict and verify no loss of data
        list_events_resp_result_item_origins_item_model_json2 = list_events_resp_result_item_origins_item_model.to_dict()
        assert list_events_resp_result_item_origins_item_model_json2 == list_events_resp_result_item_origins_item_model_json

#-----------------------------------------------------------------------------
# Test Class for ListEventsRespResultItemPoolItem
#-----------------------------------------------------------------------------
class TestListEventsRespResultItemPoolItem():

    #--------------------------------------------------------
    # Test serialization/deserialization for ListEventsRespResultItemPoolItem
    #--------------------------------------------------------
    def test_list_events_resp_result_item_pool_item_serialization(self):

        # Construct a json representation of a ListEventsRespResultItemPoolItem model
        list_events_resp_result_item_pool_item_model_json = {}
        list_events_resp_result_item_pool_item_model_json['id'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'
        list_events_resp_result_item_pool_item_model_json['name'] = 'some-pool'
        list_events_resp_result_item_pool_item_model_json['healthy'] = True
        list_events_resp_result_item_pool_item_model_json['changed'] = True
        list_events_resp_result_item_pool_item_model_json['minimum_origins'] = 1

        # Construct a model instance of ListEventsRespResultItemPoolItem by calling from_dict on the json representation
        list_events_resp_result_item_pool_item_model = ListEventsRespResultItemPoolItem.from_dict(list_events_resp_result_item_pool_item_model_json)
        assert list_events_resp_result_item_pool_item_model != False

        # Construct a model instance of ListEventsRespResultItemPoolItem by calling from_dict on the json representation
        list_events_resp_result_item_pool_item_model_dict = ListEventsRespResultItemPoolItem.from_dict(list_events_resp_result_item_pool_item_model_json).__dict__
        list_events_resp_result_item_pool_item_model2 = ListEventsRespResultItemPoolItem(**list_events_resp_result_item_pool_item_model_dict)

        # Verify the model instances are equivalent
        assert list_events_resp_result_item_pool_item_model == list_events_resp_result_item_pool_item_model2

        # Convert model instance back to dict and verify no loss of data
        list_events_resp_result_item_pool_item_model_json2 = list_events_resp_result_item_pool_item_model.to_dict()
        assert list_events_resp_result_item_pool_item_model_json2 == list_events_resp_result_item_pool_item_model_json

#-----------------------------------------------------------------------------
# Test Class for ListEventsResp
#-----------------------------------------------------------------------------
class TestListEventsResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for ListEventsResp
    #--------------------------------------------------------
    def test_list_events_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        list_events_resp_result_item_origins_item_model = {} # ListEventsRespResultItemOriginsItem
        list_events_resp_result_item_origins_item_model['name'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'
        list_events_resp_result_item_origins_item_model['address'] = '1.2.3.4'
        list_events_resp_result_item_origins_item_model['ip'] = '1.2.3.4'
        list_events_resp_result_item_origins_item_model['enabled'] = True
        list_events_resp_result_item_origins_item_model['healthy'] = True
        list_events_resp_result_item_origins_item_model['failure_reason'] = 'No failures'
        list_events_resp_result_item_origins_item_model['changed'] = True

        list_events_resp_result_item_pool_item_model = {} # ListEventsRespResultItemPoolItem
        list_events_resp_result_item_pool_item_model['id'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'
        list_events_resp_result_item_pool_item_model['name'] = 'some-pool'
        list_events_resp_result_item_pool_item_model['healthy'] = True
        list_events_resp_result_item_pool_item_model['changed'] = True
        list_events_resp_result_item_pool_item_model['minimum_origins'] = 1

        list_events_resp_result_info_model = {} # ListEventsRespResultInfo
        list_events_resp_result_info_model['page'] = 1
        list_events_resp_result_info_model['per_page'] = 20
        list_events_resp_result_info_model['count'] = 1
        list_events_resp_result_info_model['total_count'] = 2000

        list_events_resp_result_item_model = {} # ListEventsRespResultItem
        list_events_resp_result_item_model['id'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'
        list_events_resp_result_item_model['timestamp'] = '2020-01-28T18:40:40.123456Z'
        list_events_resp_result_item_model['pool'] = [list_events_resp_result_item_pool_item_model]
        list_events_resp_result_item_model['origins'] = [list_events_resp_result_item_origins_item_model]

        # Construct a json representation of a ListEventsResp model
        list_events_resp_model_json = {}
        list_events_resp_model_json['success'] = True
        list_events_resp_model_json['result'] = [list_events_resp_result_item_model]
        list_events_resp_model_json['result_info'] = list_events_resp_result_info_model
        list_events_resp_model_json['errors'] = [['testString']]
        list_events_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of ListEventsResp by calling from_dict on the json representation
        list_events_resp_model = ListEventsResp.from_dict(list_events_resp_model_json)
        assert list_events_resp_model != False

        # Construct a model instance of ListEventsResp by calling from_dict on the json representation
        list_events_resp_model_dict = ListEventsResp.from_dict(list_events_resp_model_json).__dict__
        list_events_resp_model2 = ListEventsResp(**list_events_resp_model_dict)

        # Verify the model instances are equivalent
        assert list_events_resp_model == list_events_resp_model2

        # Convert model instance back to dict and verify no loss of data
        list_events_resp_model_json2 = list_events_resp_model.to_dict()
        assert list_events_resp_model_json2 == list_events_resp_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
