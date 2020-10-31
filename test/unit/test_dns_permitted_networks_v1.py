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
import requests
import responses
from ibm_cloud_networking_services.dns_permitted_networks_v1 import *


service = DnsPermittedNetworksV1(
    authenticator=NoAuthAuthenticator()
    )

base_url = 'https://api.dns-svcs.cloud.ibm.com/v1'
service.set_service_url(base_url)

##############################################################################
# Start of Service: PermittedNetwork
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_permitted_networks
#-----------------------------------------------------------------------------
class TestListPermittedNetworks():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # list_permitted_networks()
    #--------------------------------------------------------
    @responses.activate
    def test_list_permitted_networks_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/dnszones/testString/permitted_networks')
        mock_response = '{"permitted_networks": [{"id": "fecd0173-3919-456b-b202-3029dfa1b0f7", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "permitted_network": {"vpc_crn": "crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6"}, "type": "vpc", "state": "ACTIVE"}], "offset": 0, "limit": 10, "total_count": 200, "first": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:252926c6-7d0c-4d37-861a-1faca0041785/permitted_networks?limit=10"}, "next": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:252926c6-7d0c-4d37-861a-1faca0041785/permitted_networks?offset=1&limit=10"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        x_correlation_id = 'testString'
        offset = 'testString'
        limit = 'testString'

        # Invoke method
        response = service.list_permitted_networks(
            instance_id,
            dnszone_id,
            x_correlation_id=x_correlation_id,
            offset=offset,
            limit=limit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'offset={}'.format(offset) in query_string
        assert 'limit={}'.format(limit) in query_string


    #--------------------------------------------------------
    # test_list_permitted_networks_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_permitted_networks_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/dnszones/testString/permitted_networks')
        mock_response = '{"permitted_networks": [{"id": "fecd0173-3919-456b-b202-3029dfa1b0f7", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "permitted_network": {"vpc_crn": "crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6"}, "type": "vpc", "state": "ACTIVE"}], "offset": 0, "limit": 10, "total_count": 200, "first": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:252926c6-7d0c-4d37-861a-1faca0041785/permitted_networks?limit=10"}, "next": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:252926c6-7d0c-4d37-861a-1faca0041785/permitted_networks?offset=1&limit=10"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'

        # Invoke method
        response = service.list_permitted_networks(
            instance_id,
            dnszone_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_list_permitted_networks_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_list_permitted_networks_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/dnszones/testString/permitted_networks')
        mock_response = '{"permitted_networks": [{"id": "fecd0173-3919-456b-b202-3029dfa1b0f7", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "permitted_network": {"vpc_crn": "crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6"}, "type": "vpc", "state": "ACTIVE"}], "offset": 0, "limit": 10, "total_count": 200, "first": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:252926c6-7d0c-4d37-861a-1faca0041785/permitted_networks?limit=10"}, "next": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:252926c6-7d0c-4d37-861a-1faca0041785/permitted_networks?offset=1&limit=10"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "dnszone_id": dnszone_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.list_permitted_networks(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for create_permitted_network
#-----------------------------------------------------------------------------
class TestCreatePermittedNetwork():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # create_permitted_network()
    #--------------------------------------------------------
    @responses.activate
    def test_create_permitted_network_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/dnszones/testString/permitted_networks')
        mock_response = '{"id": "fecd0173-3919-456b-b202-3029dfa1b0f7", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "permitted_network": {"vpc_crn": "crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6"}, "type": "vpc", "state": "ACTIVE"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a PermittedNetworkVpc model
        permitted_network_vpc_model = {}
        permitted_network_vpc_model['vpc_crn'] = 'crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6'

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        type = 'vpc'
        permitted_network = permitted_network_vpc_model
        x_correlation_id = 'testString'

        # Invoke method
        response = service.create_permitted_network(
            instance_id,
            dnszone_id,
            type=type,
            permitted_network=permitted_network,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['type'] == 'vpc'
        assert req_body['permitted_network'] == permitted_network_vpc_model


    #--------------------------------------------------------
    # test_create_permitted_network_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_permitted_network_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/dnszones/testString/permitted_networks')
        mock_response = '{"id": "fecd0173-3919-456b-b202-3029dfa1b0f7", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "permitted_network": {"vpc_crn": "crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6"}, "type": "vpc", "state": "ACTIVE"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'

        # Invoke method
        response = service.create_permitted_network(
            instance_id,
            dnszone_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_create_permitted_network_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_create_permitted_network_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/dnszones/testString/permitted_networks')
        mock_response = '{"id": "fecd0173-3919-456b-b202-3029dfa1b0f7", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "permitted_network": {"vpc_crn": "crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6"}, "type": "vpc", "state": "ACTIVE"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "dnszone_id": dnszone_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.create_permitted_network(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for delete_permitted_network
#-----------------------------------------------------------------------------
class TestDeletePermittedNetwork():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # delete_permitted_network()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_permitted_network_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/dnszones/testString/permitted_networks/testString')
        mock_response = '{"id": "fecd0173-3919-456b-b202-3029dfa1b0f7", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "permitted_network": {"vpc_crn": "crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6"}, "type": "vpc", "state": "ACTIVE"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        permitted_network_id = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = service.delete_permitted_network(
            instance_id,
            dnszone_id,
            permitted_network_id,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


    #--------------------------------------------------------
    # test_delete_permitted_network_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_permitted_network_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/dnszones/testString/permitted_networks/testString')
        mock_response = '{"id": "fecd0173-3919-456b-b202-3029dfa1b0f7", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "permitted_network": {"vpc_crn": "crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6"}, "type": "vpc", "state": "ACTIVE"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        permitted_network_id = 'testString'

        # Invoke method
        response = service.delete_permitted_network(
            instance_id,
            dnszone_id,
            permitted_network_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


    #--------------------------------------------------------
    # test_delete_permitted_network_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_permitted_network_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/dnszones/testString/permitted_networks/testString')
        mock_response = '{"id": "fecd0173-3919-456b-b202-3029dfa1b0f7", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "permitted_network": {"vpc_crn": "crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6"}, "type": "vpc", "state": "ACTIVE"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        permitted_network_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "dnszone_id": dnszone_id,
            "permitted_network_id": permitted_network_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_permitted_network(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_permitted_network
#-----------------------------------------------------------------------------
class TestGetPermittedNetwork():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_permitted_network()
    #--------------------------------------------------------
    @responses.activate
    def test_get_permitted_network_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/dnszones/testString/permitted_networks/testString')
        mock_response = '{"id": "fecd0173-3919-456b-b202-3029dfa1b0f7", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "permitted_network": {"vpc_crn": "crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6"}, "type": "vpc", "state": "ACTIVE"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        permitted_network_id = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = service.get_permitted_network(
            instance_id,
            dnszone_id,
            permitted_network_id,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_permitted_network_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_permitted_network_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/dnszones/testString/permitted_networks/testString')
        mock_response = '{"id": "fecd0173-3919-456b-b202-3029dfa1b0f7", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "permitted_network": {"vpc_crn": "crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6"}, "type": "vpc", "state": "ACTIVE"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        permitted_network_id = 'testString'

        # Invoke method
        response = service.get_permitted_network(
            instance_id,
            dnszone_id,
            permitted_network_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_permitted_network_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_permitted_network_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/dnszones/testString/permitted_networks/testString')
        mock_response = '{"id": "fecd0173-3919-456b-b202-3029dfa1b0f7", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "permitted_network": {"vpc_crn": "crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6"}, "type": "vpc", "state": "ACTIVE"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        permitted_network_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "dnszone_id": dnszone_id,
            "permitted_network_id": permitted_network_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_permitted_network(**req_copy)



# endregion
##############################################################################
# End of Service: PermittedNetwork
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
#-----------------------------------------------------------------------------
# Test Class for FirstHref
#-----------------------------------------------------------------------------
class TestFirstHref():

    #--------------------------------------------------------
    # Test serialization/deserialization for FirstHref
    #--------------------------------------------------------
    def test_first_href_serialization(self):

        # Construct a json representation of a FirstHref model
        first_href_model_json = {}
        first_href_model_json['href'] = 'https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:252926c6-7d0c-4d37-861a-1faca0041785/permitted_networks?limit=10'

        # Construct a model instance of FirstHref by calling from_dict on the json representation
        first_href_model = FirstHref.from_dict(first_href_model_json)
        assert first_href_model != False

        # Construct a model instance of FirstHref by calling from_dict on the json representation
        first_href_model_dict = FirstHref.from_dict(first_href_model_json).__dict__
        first_href_model2 = FirstHref(**first_href_model_dict)

        # Verify the model instances are equivalent
        assert first_href_model == first_href_model2

        # Convert model instance back to dict and verify no loss of data
        first_href_model_json2 = first_href_model.to_dict()
        assert first_href_model_json2 == first_href_model_json

#-----------------------------------------------------------------------------
# Test Class for ListPermittedNetworks
#-----------------------------------------------------------------------------
class TestListPermittedNetworks():

    #--------------------------------------------------------
    # Test serialization/deserialization for ListPermittedNetworks
    #--------------------------------------------------------
    def test_list_permitted_networks_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        permitted_network_vpc_model = {} # PermittedNetworkVpc
        permitted_network_vpc_model['vpc_crn'] = 'crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6'

        first_href_model = {} # FirstHref
        first_href_model['href'] = 'https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:252926c6-7d0c-4d37-861a-1faca0041785/permitted_networks?limit=10'

        next_href_model = {} # NextHref
        next_href_model['href'] = 'https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:252926c6-7d0c-4d37-861a-1faca0041785/permitted_networks?offset=1&limit=10'

        permitted_network_model = {} # PermittedNetwork
        permitted_network_model['id'] = 'fecd0173-3919-456b-b202-3029dfa1b0f7'
        permitted_network_model['created_on'] = '2019-01-01T05:20:00.12345Z'
        permitted_network_model['modified_on'] = '2019-01-01T05:20:00.12345Z'
        permitted_network_model['permitted_network'] = permitted_network_vpc_model
        permitted_network_model['type'] = 'vpc'
        permitted_network_model['state'] = 'ACTIVE'

        # Construct a json representation of a ListPermittedNetworks model
        list_permitted_networks_model_json = {}
        list_permitted_networks_model_json['permitted_networks'] = [permitted_network_model]
        list_permitted_networks_model_json['offset'] = 0
        list_permitted_networks_model_json['limit'] = 10
        list_permitted_networks_model_json['total_count'] = 200
        list_permitted_networks_model_json['first'] = first_href_model
        list_permitted_networks_model_json['next'] = next_href_model

        # Construct a model instance of ListPermittedNetworks by calling from_dict on the json representation
        list_permitted_networks_model = ListPermittedNetworks.from_dict(list_permitted_networks_model_json)
        assert list_permitted_networks_model != False

        # Construct a model instance of ListPermittedNetworks by calling from_dict on the json representation
        list_permitted_networks_model_dict = ListPermittedNetworks.from_dict(list_permitted_networks_model_json).__dict__
        list_permitted_networks_model2 = ListPermittedNetworks(**list_permitted_networks_model_dict)

        # Verify the model instances are equivalent
        assert list_permitted_networks_model == list_permitted_networks_model2

        # Convert model instance back to dict and verify no loss of data
        list_permitted_networks_model_json2 = list_permitted_networks_model.to_dict()
        assert list_permitted_networks_model_json2 == list_permitted_networks_model_json

#-----------------------------------------------------------------------------
# Test Class for NextHref
#-----------------------------------------------------------------------------
class TestNextHref():

    #--------------------------------------------------------
    # Test serialization/deserialization for NextHref
    #--------------------------------------------------------
    def test_next_href_serialization(self):

        # Construct a json representation of a NextHref model
        next_href_model_json = {}
        next_href_model_json['href'] = 'https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:252926c6-7d0c-4d37-861a-1faca0041785/permitted_networks?offset=1&limit=10'

        # Construct a model instance of NextHref by calling from_dict on the json representation
        next_href_model = NextHref.from_dict(next_href_model_json)
        assert next_href_model != False

        # Construct a model instance of NextHref by calling from_dict on the json representation
        next_href_model_dict = NextHref.from_dict(next_href_model_json).__dict__
        next_href_model2 = NextHref(**next_href_model_dict)

        # Verify the model instances are equivalent
        assert next_href_model == next_href_model2

        # Convert model instance back to dict and verify no loss of data
        next_href_model_json2 = next_href_model.to_dict()
        assert next_href_model_json2 == next_href_model_json

#-----------------------------------------------------------------------------
# Test Class for PermittedNetwork
#-----------------------------------------------------------------------------
class TestPermittedNetwork():

    #--------------------------------------------------------
    # Test serialization/deserialization for PermittedNetwork
    #--------------------------------------------------------
    def test_permitted_network_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        permitted_network_vpc_model = {} # PermittedNetworkVpc
        permitted_network_vpc_model['vpc_crn'] = 'crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6'

        # Construct a json representation of a PermittedNetwork model
        permitted_network_model_json = {}
        permitted_network_model_json['id'] = 'fecd0173-3919-456b-b202-3029dfa1b0f7'
        permitted_network_model_json['created_on'] = '2019-01-01T05:20:00.12345Z'
        permitted_network_model_json['modified_on'] = '2019-01-01T05:20:00.12345Z'
        permitted_network_model_json['permitted_network'] = permitted_network_vpc_model
        permitted_network_model_json['type'] = 'vpc'
        permitted_network_model_json['state'] = 'ACTIVE'

        # Construct a model instance of PermittedNetwork by calling from_dict on the json representation
        permitted_network_model = PermittedNetwork.from_dict(permitted_network_model_json)
        assert permitted_network_model != False

        # Construct a model instance of PermittedNetwork by calling from_dict on the json representation
        permitted_network_model_dict = PermittedNetwork.from_dict(permitted_network_model_json).__dict__
        permitted_network_model2 = PermittedNetwork(**permitted_network_model_dict)

        # Verify the model instances are equivalent
        assert permitted_network_model == permitted_network_model2

        # Convert model instance back to dict and verify no loss of data
        permitted_network_model_json2 = permitted_network_model.to_dict()
        assert permitted_network_model_json2 == permitted_network_model_json

#-----------------------------------------------------------------------------
# Test Class for PermittedNetworkVpc
#-----------------------------------------------------------------------------
class TestPermittedNetworkVpc():

    #--------------------------------------------------------
    # Test serialization/deserialization for PermittedNetworkVpc
    #--------------------------------------------------------
    def test_permitted_network_vpc_serialization(self):

        # Construct a json representation of a PermittedNetworkVpc model
        permitted_network_vpc_model_json = {}
        permitted_network_vpc_model_json['vpc_crn'] = 'crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6'

        # Construct a model instance of PermittedNetworkVpc by calling from_dict on the json representation
        permitted_network_vpc_model = PermittedNetworkVpc.from_dict(permitted_network_vpc_model_json)
        assert permitted_network_vpc_model != False

        # Construct a model instance of PermittedNetworkVpc by calling from_dict on the json representation
        permitted_network_vpc_model_dict = PermittedNetworkVpc.from_dict(permitted_network_vpc_model_json).__dict__
        permitted_network_vpc_model2 = PermittedNetworkVpc(**permitted_network_vpc_model_dict)

        # Verify the model instances are equivalent
        assert permitted_network_vpc_model == permitted_network_vpc_model2

        # Convert model instance back to dict and verify no loss of data
        permitted_network_vpc_model_json2 = permitted_network_vpc_model.to_dict()
        assert permitted_network_vpc_model_json2 == permitted_network_vpc_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
