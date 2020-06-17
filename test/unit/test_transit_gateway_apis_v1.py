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
from ibm_cloud_sdk_core.utils import date_to_string
import inspect
import json
import pytest
import requests
import responses
from ibm_cloud_networking_services.transit_gateway_apis_v1 import *

version = date.fromtimestamp(1580236840.123456)

service = TransitGatewayApisV1(
    authenticator=NoAuthAuthenticator(),
    version=version
    )

base_url = 'https://transit.cloud.ibm.com/v1'
service.set_service_url(base_url)

##############################################################################
# Start of Service: TransitGateways
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_transit_gateways
#-----------------------------------------------------------------------------
class TestListTransitGateways():

    #--------------------------------------------------------
    # list_transit_gateways()
    #--------------------------------------------------------
    @responses.activate
    def test_list_transit_gateways_all_params(self):
        # Set up mock
        url = base_url + '/transit_gateways'
        mock_response = '{"transit_gateways": [{"id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "crn": "crn:v1:bluemix:public:transit:dal03:a/57a7d05f36894e3cb9b46a43556d903e::gateway:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "name": "my-transit-gateway-in-TransitGateway", "global": true, "location": "us-south", "created_at": "2019-01-01T12:00:00", "resource_group": {"id": "56969d60-43e9-465c-883c-b9f7363e78e8", "href": "https://resource-manager.bluemix.net/v1/resource_groups/56969d60-43e9-465c-883c-b9f7363e78e8"}, "status": "available", "updated_at": "2019-01-01T12:00:00"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_transit_gateways()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_list_transit_gateways_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_list_transit_gateways_value_error(self):
        # Set up mock
        url = base_url + '/transit_gateways'
        mock_response = '{"transit_gateways": [{"id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "crn": "crn:v1:bluemix:public:transit:dal03:a/57a7d05f36894e3cb9b46a43556d903e::gateway:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "name": "my-transit-gateway-in-TransitGateway", "global": true, "location": "us-south", "created_at": "2019-01-01T12:00:00", "resource_group": {"id": "56969d60-43e9-465c-883c-b9f7363e78e8", "href": "https://resource-manager.bluemix.net/v1/resource_groups/56969d60-43e9-465c-883c-b9f7363e78e8"}, "status": "available", "updated_at": "2019-01-01T12:00:00"}]}'
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
                service.list_transit_gateways(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for create_transit_gateway
#-----------------------------------------------------------------------------
class TestCreateTransitGateway():

    #--------------------------------------------------------
    # create_transit_gateway()
    #--------------------------------------------------------
    @responses.activate
    def test_create_transit_gateway_all_params(self):
        # Set up mock
        url = base_url + '/transit_gateways'
        mock_response = '{"id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "crn": "crn:v1:bluemix:public:transit:dal03:a/57a7d05f36894e3cb9b46a43556d903e::gateway:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "name": "my-transit-gateway-in-TransitGateway", "global": true, "location": "us-south", "created_at": "2019-01-01T12:00:00", "resource_group": {"id": "56969d60-43e9-465c-883c-b9f7363e78e8", "href": "https://resource-manager.bluemix.net/v1/resource_groups/56969d60-43e9-465c-883c-b9f7363e78e8"}, "status": "available", "updated_at": "2019-01-01T12:00:00"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a ResourceGroupIdentity model
        resource_group_identity_model = {}
        resource_group_identity_model['id'] = '56969d60-43e9-465c-883c-b9f7363e78e8'

        # Set up parameter values
        location = 'us-south'
        name = 'Transit_Service_BWTN_SJ_DL'
        global_ = True
        resource_group = resource_group_identity_model

        # Invoke method
        response = service.create_transit_gateway(
            location,
            name,
            global_=global_,
            resource_group=resource_group,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['location'] == 'us-south'
        assert req_body['name'] == 'Transit_Service_BWTN_SJ_DL'
        assert req_body['global'] == True
        assert req_body['resource_group'] == resource_group_identity_model


    #--------------------------------------------------------
    # test_create_transit_gateway_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_create_transit_gateway_value_error(self):
        # Set up mock
        url = base_url + '/transit_gateways'
        mock_response = '{"id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "crn": "crn:v1:bluemix:public:transit:dal03:a/57a7d05f36894e3cb9b46a43556d903e::gateway:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "name": "my-transit-gateway-in-TransitGateway", "global": true, "location": "us-south", "created_at": "2019-01-01T12:00:00", "resource_group": {"id": "56969d60-43e9-465c-883c-b9f7363e78e8", "href": "https://resource-manager.bluemix.net/v1/resource_groups/56969d60-43e9-465c-883c-b9f7363e78e8"}, "status": "available", "updated_at": "2019-01-01T12:00:00"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a ResourceGroupIdentity model
        resource_group_identity_model = {}
        resource_group_identity_model['id'] = '56969d60-43e9-465c-883c-b9f7363e78e8'

        # Set up parameter values
        location = 'us-south'
        name = 'Transit_Service_BWTN_SJ_DL'
        global_ = True
        resource_group = resource_group_identity_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "location": location,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.create_transit_gateway(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for delete_transit_gateway
#-----------------------------------------------------------------------------
class TestDeleteTransitGateway():

    #--------------------------------------------------------
    # delete_transit_gateway()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_transit_gateway_all_params(self):
        # Set up mock
        url = base_url + '/transit_gateways/testString'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.delete_transit_gateway(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    #--------------------------------------------------------
    # test_delete_transit_gateway_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_transit_gateway_value_error(self):
        # Set up mock
        url = base_url + '/transit_gateways/testString'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_transit_gateway(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for detail_transit_gateway
#-----------------------------------------------------------------------------
class TestDetailTransitGateway():

    #--------------------------------------------------------
    # detail_transit_gateway()
    #--------------------------------------------------------
    @responses.activate
    def test_detail_transit_gateway_all_params(self):
        # Set up mock
        url = base_url + '/transit_gateways/testString'
        mock_response = '{"id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "crn": "crn:v1:bluemix:public:transit:dal03:a/57a7d05f36894e3cb9b46a43556d903e::gateway:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "name": "my-transit-gateway-in-TransitGateway", "global": true, "location": "us-south", "created_at": "2019-01-01T12:00:00", "resource_group": {"id": "56969d60-43e9-465c-883c-b9f7363e78e8", "href": "https://resource-manager.bluemix.net/v1/resource_groups/56969d60-43e9-465c-883c-b9f7363e78e8"}, "status": "available", "updated_at": "2019-01-01T12:00:00"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.detail_transit_gateway(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_detail_transit_gateway_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_detail_transit_gateway_value_error(self):
        # Set up mock
        url = base_url + '/transit_gateways/testString'
        mock_response = '{"id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "crn": "crn:v1:bluemix:public:transit:dal03:a/57a7d05f36894e3cb9b46a43556d903e::gateway:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "name": "my-transit-gateway-in-TransitGateway", "global": true, "location": "us-south", "created_at": "2019-01-01T12:00:00", "resource_group": {"id": "56969d60-43e9-465c-883c-b9f7363e78e8", "href": "https://resource-manager.bluemix.net/v1/resource_groups/56969d60-43e9-465c-883c-b9f7363e78e8"}, "status": "available", "updated_at": "2019-01-01T12:00:00"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.detail_transit_gateway(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_transit_gateway
#-----------------------------------------------------------------------------
class TestUpdateTransitGateway():

    #--------------------------------------------------------
    # update_transit_gateway()
    #--------------------------------------------------------
    @responses.activate
    def test_update_transit_gateway_all_params(self):
        # Set up mock
        url = base_url + '/transit_gateways/testString'
        mock_response = '{"id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "crn": "crn:v1:bluemix:public:transit:dal03:a/57a7d05f36894e3cb9b46a43556d903e::gateway:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "name": "my-transit-gateway-in-TransitGateway", "global": true, "location": "us-south", "created_at": "2019-01-01T12:00:00", "resource_group": {"id": "56969d60-43e9-465c-883c-b9f7363e78e8", "href": "https://resource-manager.bluemix.net/v1/resource_groups/56969d60-43e9-465c-883c-b9f7363e78e8"}, "status": "available", "updated_at": "2019-01-01T12:00:00"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        global_ = True
        name = 'my-transit-gateway'

        # Invoke method
        response = service.update_transit_gateway(
            id,
            global_=global_,
            name=name,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['global'] == True
        assert req_body['name'] == 'my-transit-gateway'


    #--------------------------------------------------------
    # test_update_transit_gateway_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_transit_gateway_value_error(self):
        # Set up mock
        url = base_url + '/transit_gateways/testString'
        mock_response = '{"id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "crn": "crn:v1:bluemix:public:transit:dal03:a/57a7d05f36894e3cb9b46a43556d903e::gateway:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "name": "my-transit-gateway-in-TransitGateway", "global": true, "location": "us-south", "created_at": "2019-01-01T12:00:00", "resource_group": {"id": "56969d60-43e9-465c-883c-b9f7363e78e8", "href": "https://resource-manager.bluemix.net/v1/resource_groups/56969d60-43e9-465c-883c-b9f7363e78e8"}, "status": "available", "updated_at": "2019-01-01T12:00:00"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        global_ = True
        name = 'my-transit-gateway'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.update_transit_gateway(**req_copy)



# endregion
##############################################################################
# End of Service: TransitGateways
##############################################################################

##############################################################################
# Start of Service: TransitGatewaysNetworkConnections
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_transit_gateway_connections
#-----------------------------------------------------------------------------
class TestListTransitGatewayConnections():

    #--------------------------------------------------------
    # list_transit_gateway_connections()
    #--------------------------------------------------------
    @responses.activate
    def test_list_transit_gateway_connections_all_params(self):
        # Set up mock
        url = base_url + '/transit_gateways/testString/connections'
        mock_response = '{"connections": [{"name": "Transit_Service_BWTN_SJ_DL", "network_id": "crn:v1:bluemix:public:is:us-south:a/123456::vpc:4727d842-f94f-4a2d-824a-9bc9b02c523b", "network_type": "vpc", "id": "1a15dca5-7e33-45e1-b7c5-bc690e569531-connection_id", "created_at": "2019-01-01T12:00:00", "status": "attached", "updated_at": "2019-01-01T12:00:00"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        transit_gateway_id = 'testString'

        # Invoke method
        response = service.list_transit_gateway_connections(
            transit_gateway_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_list_transit_gateway_connections_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_list_transit_gateway_connections_value_error(self):
        # Set up mock
        url = base_url + '/transit_gateways/testString/connections'
        mock_response = '{"connections": [{"name": "Transit_Service_BWTN_SJ_DL", "network_id": "crn:v1:bluemix:public:is:us-south:a/123456::vpc:4727d842-f94f-4a2d-824a-9bc9b02c523b", "network_type": "vpc", "id": "1a15dca5-7e33-45e1-b7c5-bc690e569531-connection_id", "created_at": "2019-01-01T12:00:00", "status": "attached", "updated_at": "2019-01-01T12:00:00"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        transit_gateway_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "transit_gateway_id": transit_gateway_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.list_transit_gateway_connections(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for create_transit_gateway_connection
#-----------------------------------------------------------------------------
class TestCreateTransitGatewayConnection():

    #--------------------------------------------------------
    # create_transit_gateway_connection()
    #--------------------------------------------------------
    @responses.activate
    def test_create_transit_gateway_connection_all_params(self):
        # Set up mock
        url = base_url + '/transit_gateways/testString/connections'
        mock_response = '{"name": "Transit_Service_BWTN_SJ_DL", "network_id": "crn:v1:bluemix:public:is:us-south:a/123456::vpc:4727d842-f94f-4a2d-824a-9bc9b02c523b", "network_type": "vpc", "id": "1a15dca5-7e33-45e1-b7c5-bc690e569531-connection_id", "created_at": "2019-01-01T12:00:00", "status": "attached", "updated_at": "2019-01-01T12:00:00"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        transit_gateway_id = 'testString'
        network_type = 'vpc'
        name = 'Transit_Service_BWTN_SJ_DL'
        network_id = 'crn:v1:bluemix:public:is:us-south:a/123456::vpc:4727d842-f94f-4a2d-824a-9bc9b02c523b'

        # Invoke method
        response = service.create_transit_gateway_connection(
            transit_gateway_id,
            network_type,
            name=name,
            network_id=network_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['network_type'] == 'vpc'
        assert req_body['name'] == 'Transit_Service_BWTN_SJ_DL'
        assert req_body['network_id'] == 'crn:v1:bluemix:public:is:us-south:a/123456::vpc:4727d842-f94f-4a2d-824a-9bc9b02c523b'


    #--------------------------------------------------------
    # test_create_transit_gateway_connection_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_create_transit_gateway_connection_value_error(self):
        # Set up mock
        url = base_url + '/transit_gateways/testString/connections'
        mock_response = '{"name": "Transit_Service_BWTN_SJ_DL", "network_id": "crn:v1:bluemix:public:is:us-south:a/123456::vpc:4727d842-f94f-4a2d-824a-9bc9b02c523b", "network_type": "vpc", "id": "1a15dca5-7e33-45e1-b7c5-bc690e569531-connection_id", "created_at": "2019-01-01T12:00:00", "status": "attached", "updated_at": "2019-01-01T12:00:00"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        transit_gateway_id = 'testString'
        network_type = 'vpc'
        name = 'Transit_Service_BWTN_SJ_DL'
        network_id = 'crn:v1:bluemix:public:is:us-south:a/123456::vpc:4727d842-f94f-4a2d-824a-9bc9b02c523b'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "transit_gateway_id": transit_gateway_id,
            "network_type": network_type,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.create_transit_gateway_connection(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for delete_transit_gateway_connection
#-----------------------------------------------------------------------------
class TestDeleteTransitGatewayConnection():

    #--------------------------------------------------------
    # delete_transit_gateway_connection()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_transit_gateway_connection_all_params(self):
        # Set up mock
        url = base_url + '/transit_gateways/testString/connections/testString'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        transit_gateway_id = 'testString'
        id = 'testString'

        # Invoke method
        response = service.delete_transit_gateway_connection(
            transit_gateway_id,
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    #--------------------------------------------------------
    # test_delete_transit_gateway_connection_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_transit_gateway_connection_value_error(self):
        # Set up mock
        url = base_url + '/transit_gateways/testString/connections/testString'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        transit_gateway_id = 'testString'
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "transit_gateway_id": transit_gateway_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_transit_gateway_connection(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for detail_transit_gateway_connection
#-----------------------------------------------------------------------------
class TestDetailTransitGatewayConnection():

    #--------------------------------------------------------
    # detail_transit_gateway_connection()
    #--------------------------------------------------------
    @responses.activate
    def test_detail_transit_gateway_connection_all_params(self):
        # Set up mock
        url = base_url + '/transit_gateways/testString/connections/testString'
        mock_response = '{"name": "Transit_Service_BWTN_SJ_DL", "network_id": "crn:v1:bluemix:public:is:us-south:a/123456::vpc:4727d842-f94f-4a2d-824a-9bc9b02c523b", "network_type": "vpc", "id": "1a15dca5-7e33-45e1-b7c5-bc690e569531-connection_id", "created_at": "2019-01-01T12:00:00", "status": "attached", "updated_at": "2019-01-01T12:00:00"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        transit_gateway_id = 'testString'
        id = 'testString'

        # Invoke method
        response = service.detail_transit_gateway_connection(
            transit_gateway_id,
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_detail_transit_gateway_connection_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_detail_transit_gateway_connection_value_error(self):
        # Set up mock
        url = base_url + '/transit_gateways/testString/connections/testString'
        mock_response = '{"name": "Transit_Service_BWTN_SJ_DL", "network_id": "crn:v1:bluemix:public:is:us-south:a/123456::vpc:4727d842-f94f-4a2d-824a-9bc9b02c523b", "network_type": "vpc", "id": "1a15dca5-7e33-45e1-b7c5-bc690e569531-connection_id", "created_at": "2019-01-01T12:00:00", "status": "attached", "updated_at": "2019-01-01T12:00:00"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        transit_gateway_id = 'testString'
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "transit_gateway_id": transit_gateway_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.detail_transit_gateway_connection(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_transit_gateway_connection
#-----------------------------------------------------------------------------
class TestUpdateTransitGatewayConnection():

    #--------------------------------------------------------
    # update_transit_gateway_connection()
    #--------------------------------------------------------
    @responses.activate
    def test_update_transit_gateway_connection_all_params(self):
        # Set up mock
        url = base_url + '/transit_gateways/testString/connections/testString'
        mock_response = '{"name": "Transit_Service_BWTN_SJ_DL", "network_id": "crn:v1:bluemix:public:is:us-south:a/123456::vpc:4727d842-f94f-4a2d-824a-9bc9b02c523b", "network_type": "vpc", "id": "1a15dca5-7e33-45e1-b7c5-bc690e569531-connection_id", "created_at": "2019-01-01T12:00:00", "status": "attached", "updated_at": "2019-01-01T12:00:00"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        transit_gateway_id = 'testString'
        id = 'testString'
        name = 'Transit_Service_BWTN_SJ_DL'

        # Invoke method
        response = service.update_transit_gateway_connection(
            transit_gateway_id,
            id,
            name=name,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'Transit_Service_BWTN_SJ_DL'


    #--------------------------------------------------------
    # test_update_transit_gateway_connection_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_transit_gateway_connection_value_error(self):
        # Set up mock
        url = base_url + '/transit_gateways/testString/connections/testString'
        mock_response = '{"name": "Transit_Service_BWTN_SJ_DL", "network_id": "crn:v1:bluemix:public:is:us-south:a/123456::vpc:4727d842-f94f-4a2d-824a-9bc9b02c523b", "network_type": "vpc", "id": "1a15dca5-7e33-45e1-b7c5-bc690e569531-connection_id", "created_at": "2019-01-01T12:00:00", "status": "attached", "updated_at": "2019-01-01T12:00:00"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        transit_gateway_id = 'testString'
        id = 'testString'
        name = 'Transit_Service_BWTN_SJ_DL'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "transit_gateway_id": transit_gateway_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.update_transit_gateway_connection(**req_copy)



# endregion
##############################################################################
# End of Service: TransitGatewaysNetworkConnections
##############################################################################

##############################################################################
# Start of Service: TransitLocation
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_gateway_locations
#-----------------------------------------------------------------------------
class TestListGatewayLocations():

    #--------------------------------------------------------
    # list_gateway_locations()
    #--------------------------------------------------------
    @responses.activate
    def test_list_gateway_locations_all_params(self):
        # Set up mock
        url = base_url + '/locations'
        mock_response = '{"locations": [{"billing_location": "us", "name": "us-south", "type": "region"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_gateway_locations()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_list_gateway_locations_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_list_gateway_locations_value_error(self):
        # Set up mock
        url = base_url + '/locations'
        mock_response = '{"locations": [{"billing_location": "us", "name": "us-south", "type": "region"}]}'
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
                service.list_gateway_locations(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for detail_gateway_location
#-----------------------------------------------------------------------------
class TestDetailGatewayLocation():

    #--------------------------------------------------------
    # detail_gateway_location()
    #--------------------------------------------------------
    @responses.activate
    def test_detail_gateway_location_all_params(self):
        # Set up mock
        url = base_url + '/locations/testString'
        mock_response = '{"billing_location": "us", "name": "us-south", "type": "region", "local_connection_locations": [{"display_name": "Dallas", "name": "us-south", "type": "region"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        name = 'testString'

        # Invoke method
        response = service.detail_gateway_location(
            name,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_detail_gateway_location_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_detail_gateway_location_value_error(self):
        # Set up mock
        url = base_url + '/locations/testString'
        mock_response = '{"billing_location": "us", "name": "us-south", "type": "region", "local_connection_locations": [{"display_name": "Dallas", "name": "us-south", "type": "region"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        name = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.detail_gateway_location(**req_copy)



# endregion
##############################################################################
# End of Service: TransitLocation
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
#-----------------------------------------------------------------------------
# Test Class for ResourceGroupIdentity
#-----------------------------------------------------------------------------
class TestResourceGroupIdentity():

    #--------------------------------------------------------
    # Test serialization/deserialization for ResourceGroupIdentity
    #--------------------------------------------------------
    def test_resource_group_identity_serialization(self):

        # Construct a json representation of a ResourceGroupIdentity model
        resource_group_identity_model_json = {}
        resource_group_identity_model_json['id'] = '56969d60-43e9-465c-883c-b9f7363e78e8'

        # Construct a model instance of ResourceGroupIdentity by calling from_dict on the json representation
        resource_group_identity_model = ResourceGroupIdentity.from_dict(resource_group_identity_model_json)
        assert resource_group_identity_model != False

        # Construct a model instance of ResourceGroupIdentity by calling from_dict on the json representation
        resource_group_identity_model_dict = ResourceGroupIdentity.from_dict(resource_group_identity_model_json).__dict__
        resource_group_identity_model2 = ResourceGroupIdentity(**resource_group_identity_model_dict)

        # Verify the model instances are equivalent
        assert resource_group_identity_model == resource_group_identity_model2

        # Convert model instance back to dict and verify no loss of data
        resource_group_identity_model_json2 = resource_group_identity_model.to_dict()
        assert resource_group_identity_model_json2 == resource_group_identity_model_json

#-----------------------------------------------------------------------------
# Test Class for ResourceGroupReference
#-----------------------------------------------------------------------------
class TestResourceGroupReference():

    #--------------------------------------------------------
    # Test serialization/deserialization for ResourceGroupReference
    #--------------------------------------------------------
    def test_resource_group_reference_serialization(self):

        # Construct a json representation of a ResourceGroupReference model
        resource_group_reference_model_json = {}
        resource_group_reference_model_json['id'] = '56969d60-43e9-465c-883c-b9f7363e78e8'
        resource_group_reference_model_json['href'] = 'https://resource-manager.bluemix.net/v1/resource_groups/56969d60-43e9-465c-883c-b9f7363e78e8'

        # Construct a model instance of ResourceGroupReference by calling from_dict on the json representation
        resource_group_reference_model = ResourceGroupReference.from_dict(resource_group_reference_model_json)
        assert resource_group_reference_model != False

        # Construct a model instance of ResourceGroupReference by calling from_dict on the json representation
        resource_group_reference_model_dict = ResourceGroupReference.from_dict(resource_group_reference_model_json).__dict__
        resource_group_reference_model2 = ResourceGroupReference(**resource_group_reference_model_dict)

        # Verify the model instances are equivalent
        assert resource_group_reference_model == resource_group_reference_model2

        # Convert model instance back to dict and verify no loss of data
        resource_group_reference_model_json2 = resource_group_reference_model.to_dict()
        assert resource_group_reference_model_json2 == resource_group_reference_model_json

#-----------------------------------------------------------------------------
# Test Class for TSCollection
#-----------------------------------------------------------------------------
class TestTSCollection():

    #--------------------------------------------------------
    # Test serialization/deserialization for TSCollection
    #--------------------------------------------------------
    def test_ts_collection_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        ts_location_basic_model = {} # TSLocationBasic
        ts_location_basic_model['billing_location'] = 'us'
        ts_location_basic_model['name'] = 'us-south'
        ts_location_basic_model['type'] = 'region'

        # Construct a json representation of a TSCollection model
        ts_collection_model_json = {}
        ts_collection_model_json['locations'] = [ts_location_basic_model]

        # Construct a model instance of TSCollection by calling from_dict on the json representation
        ts_collection_model = TSCollection.from_dict(ts_collection_model_json)
        assert ts_collection_model != False

        # Construct a model instance of TSCollection by calling from_dict on the json representation
        ts_collection_model_dict = TSCollection.from_dict(ts_collection_model_json).__dict__
        ts_collection_model2 = TSCollection(**ts_collection_model_dict)

        # Verify the model instances are equivalent
        assert ts_collection_model == ts_collection_model2

        # Convert model instance back to dict and verify no loss of data
        ts_collection_model_json2 = ts_collection_model.to_dict()
        assert ts_collection_model_json2 == ts_collection_model_json

#-----------------------------------------------------------------------------
# Test Class for TSLocalLocation
#-----------------------------------------------------------------------------
class TestTSLocalLocation():

    #--------------------------------------------------------
    # Test serialization/deserialization for TSLocalLocation
    #--------------------------------------------------------
    def test_ts_local_location_serialization(self):

        # Construct a json representation of a TSLocalLocation model
        ts_local_location_model_json = {}
        ts_local_location_model_json['display_name'] = 'Dallas'
        ts_local_location_model_json['name'] = 'us-south'
        ts_local_location_model_json['type'] = 'region'

        # Construct a model instance of TSLocalLocation by calling from_dict on the json representation
        ts_local_location_model = TSLocalLocation.from_dict(ts_local_location_model_json)
        assert ts_local_location_model != False

        # Construct a model instance of TSLocalLocation by calling from_dict on the json representation
        ts_local_location_model_dict = TSLocalLocation.from_dict(ts_local_location_model_json).__dict__
        ts_local_location_model2 = TSLocalLocation(**ts_local_location_model_dict)

        # Verify the model instances are equivalent
        assert ts_local_location_model == ts_local_location_model2

        # Convert model instance back to dict and verify no loss of data
        ts_local_location_model_json2 = ts_local_location_model.to_dict()
        assert ts_local_location_model_json2 == ts_local_location_model_json

#-----------------------------------------------------------------------------
# Test Class for TSLocation
#-----------------------------------------------------------------------------
class TestTSLocation():

    #--------------------------------------------------------
    # Test serialization/deserialization for TSLocation
    #--------------------------------------------------------
    def test_ts_location_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        ts_local_location_model = {} # TSLocalLocation
        ts_local_location_model['display_name'] = 'Dallas'
        ts_local_location_model['name'] = 'us-south'
        ts_local_location_model['type'] = 'region'

        # Construct a json representation of a TSLocation model
        ts_location_model_json = {}
        ts_location_model_json['billing_location'] = 'us'
        ts_location_model_json['name'] = 'us-south'
        ts_location_model_json['type'] = 'region'
        ts_location_model_json['local_connection_locations'] = [ts_local_location_model]

        # Construct a model instance of TSLocation by calling from_dict on the json representation
        ts_location_model = TSLocation.from_dict(ts_location_model_json)
        assert ts_location_model != False

        # Construct a model instance of TSLocation by calling from_dict on the json representation
        ts_location_model_dict = TSLocation.from_dict(ts_location_model_json).__dict__
        ts_location_model2 = TSLocation(**ts_location_model_dict)

        # Verify the model instances are equivalent
        assert ts_location_model == ts_location_model2

        # Convert model instance back to dict and verify no loss of data
        ts_location_model_json2 = ts_location_model.to_dict()
        assert ts_location_model_json2 == ts_location_model_json

#-----------------------------------------------------------------------------
# Test Class for TSLocationBasic
#-----------------------------------------------------------------------------
class TestTSLocationBasic():

    #--------------------------------------------------------
    # Test serialization/deserialization for TSLocationBasic
    #--------------------------------------------------------
    def test_ts_location_basic_serialization(self):

        # Construct a json representation of a TSLocationBasic model
        ts_location_basic_model_json = {}
        ts_location_basic_model_json['billing_location'] = 'us'
        ts_location_basic_model_json['name'] = 'us-south'
        ts_location_basic_model_json['type'] = 'region'

        # Construct a model instance of TSLocationBasic by calling from_dict on the json representation
        ts_location_basic_model = TSLocationBasic.from_dict(ts_location_basic_model_json)
        assert ts_location_basic_model != False

        # Construct a model instance of TSLocationBasic by calling from_dict on the json representation
        ts_location_basic_model_dict = TSLocationBasic.from_dict(ts_location_basic_model_json).__dict__
        ts_location_basic_model2 = TSLocationBasic(**ts_location_basic_model_dict)

        # Verify the model instances are equivalent
        assert ts_location_basic_model == ts_location_basic_model2

        # Convert model instance back to dict and verify no loss of data
        ts_location_basic_model_json2 = ts_location_basic_model.to_dict()
        assert ts_location_basic_model_json2 == ts_location_basic_model_json

#-----------------------------------------------------------------------------
# Test Class for TransitGateway
#-----------------------------------------------------------------------------
class TestTransitGateway():

    #--------------------------------------------------------
    # Test serialization/deserialization for TransitGateway
    #--------------------------------------------------------
    def test_transit_gateway_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        resource_group_reference_model = {} # ResourceGroupReference
        resource_group_reference_model['id'] = '56969d60-43e9-465c-883c-b9f7363e78e8'
        resource_group_reference_model['href'] = 'https://resource-manager.bluemix.net/v1/resource_groups/56969d60-43e9-465c-883c-b9f7363e78e8'

        # Construct a json representation of a TransitGateway model
        transit_gateway_model_json = {}
        transit_gateway_model_json['id'] = 'ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4'
        transit_gateway_model_json['crn'] = 'crn:v1:bluemix:public:transit:dal03:a/57a7d05f36894e3cb9b46a43556d903e::gateway:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4'
        transit_gateway_model_json['name'] = 'my-transit-gateway-in-TransitGateway'
        transit_gateway_model_json['global'] = True
        transit_gateway_model_json['location'] = 'us-south'
        transit_gateway_model_json['created_at'] = '2020-01-28T18:40:40.123456Z'
        transit_gateway_model_json['resource_group'] = resource_group_reference_model
        transit_gateway_model_json['status'] = 'available'
        transit_gateway_model_json['updated_at'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of TransitGateway by calling from_dict on the json representation
        transit_gateway_model = TransitGateway.from_dict(transit_gateway_model_json)
        assert transit_gateway_model != False

        # Construct a model instance of TransitGateway by calling from_dict on the json representation
        transit_gateway_model_dict = TransitGateway.from_dict(transit_gateway_model_json).__dict__
        transit_gateway_model2 = TransitGateway(**transit_gateway_model_dict)

        # Verify the model instances are equivalent
        assert transit_gateway_model == transit_gateway_model2

        # Convert model instance back to dict and verify no loss of data
        transit_gateway_model_json2 = transit_gateway_model.to_dict()
        assert transit_gateway_model_json2 == transit_gateway_model_json

#-----------------------------------------------------------------------------
# Test Class for TransitGatewayCollection
#-----------------------------------------------------------------------------
class TestTransitGatewayCollection():

    #--------------------------------------------------------
    # Test serialization/deserialization for TransitGatewayCollection
    #--------------------------------------------------------
    def test_transit_gateway_collection_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        resource_group_reference_model = {} # ResourceGroupReference
        resource_group_reference_model['id'] = '56969d60-43e9-465c-883c-b9f7363e78e8'
        resource_group_reference_model['href'] = 'https://resource-manager.bluemix.net/v1/resource_groups/56969d60-43e9-465c-883c-b9f7363e78e8'

        transit_gateway_model = {} # TransitGateway
        transit_gateway_model['id'] = 'ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4'
        transit_gateway_model['crn'] = 'crn:v1:bluemix:public:transit:dal03:a/57a7d05f36894e3cb9b46a43556d903e::gateway:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4'
        transit_gateway_model['name'] = 'my-transit-gateway-in-TransitGateway'
        transit_gateway_model['global'] = True
        transit_gateway_model['location'] = 'us-south'
        transit_gateway_model['created_at'] = '2020-01-28T18:40:40.123456Z'
        transit_gateway_model['resource_group'] = resource_group_reference_model
        transit_gateway_model['status'] = 'available'
        transit_gateway_model['updated_at'] = '2020-01-28T18:40:40.123456Z'

        # Construct a json representation of a TransitGatewayCollection model
        transit_gateway_collection_model_json = {}
        transit_gateway_collection_model_json['transit_gateways'] = [transit_gateway_model]

        # Construct a model instance of TransitGatewayCollection by calling from_dict on the json representation
        transit_gateway_collection_model = TransitGatewayCollection.from_dict(transit_gateway_collection_model_json)
        assert transit_gateway_collection_model != False

        # Construct a model instance of TransitGatewayCollection by calling from_dict on the json representation
        transit_gateway_collection_model_dict = TransitGatewayCollection.from_dict(transit_gateway_collection_model_json).__dict__
        transit_gateway_collection_model2 = TransitGatewayCollection(**transit_gateway_collection_model_dict)

        # Verify the model instances are equivalent
        assert transit_gateway_collection_model == transit_gateway_collection_model2

        # Convert model instance back to dict and verify no loss of data
        transit_gateway_collection_model_json2 = transit_gateway_collection_model.to_dict()
        assert transit_gateway_collection_model_json2 == transit_gateway_collection_model_json

#-----------------------------------------------------------------------------
# Test Class for TransitGatewayConnectionCollection
#-----------------------------------------------------------------------------
class TestTransitGatewayConnectionCollection():

    #--------------------------------------------------------
    # Test serialization/deserialization for TransitGatewayConnectionCollection
    #--------------------------------------------------------
    def test_transit_gateway_connection_collection_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        transit_gateway_connection_cust_model = {} # TransitGatewayConnectionCust
        transit_gateway_connection_cust_model['name'] = 'Transit_Service_BWTN_SJ_DL'
        transit_gateway_connection_cust_model['network_id'] = 'crn:v1:bluemix:public:is:us-south:a/123456::vpc:4727d842-f94f-4a2d-824a-9bc9b02c523b'
        transit_gateway_connection_cust_model['network_type'] = 'vpc'
        transit_gateway_connection_cust_model['id'] = '1a15dca5-7e33-45e1-b7c5-bc690e569531-connection_id'
        transit_gateway_connection_cust_model['created_at'] = '2020-01-28T18:40:40.123456Z'
        transit_gateway_connection_cust_model['status'] = 'attached'
        transit_gateway_connection_cust_model['updated_at'] = '2020-01-28T18:40:40.123456Z'

        # Construct a json representation of a TransitGatewayConnectionCollection model
        transit_gateway_connection_collection_model_json = {}
        transit_gateway_connection_collection_model_json['connections'] = [transit_gateway_connection_cust_model]

        # Construct a model instance of TransitGatewayConnectionCollection by calling from_dict on the json representation
        transit_gateway_connection_collection_model = TransitGatewayConnectionCollection.from_dict(transit_gateway_connection_collection_model_json)
        assert transit_gateway_connection_collection_model != False

        # Construct a model instance of TransitGatewayConnectionCollection by calling from_dict on the json representation
        transit_gateway_connection_collection_model_dict = TransitGatewayConnectionCollection.from_dict(transit_gateway_connection_collection_model_json).__dict__
        transit_gateway_connection_collection_model2 = TransitGatewayConnectionCollection(**transit_gateway_connection_collection_model_dict)

        # Verify the model instances are equivalent
        assert transit_gateway_connection_collection_model == transit_gateway_connection_collection_model2

        # Convert model instance back to dict and verify no loss of data
        transit_gateway_connection_collection_model_json2 = transit_gateway_connection_collection_model.to_dict()
        assert transit_gateway_connection_collection_model_json2 == transit_gateway_connection_collection_model_json

#-----------------------------------------------------------------------------
# Test Class for TransitGatewayConnectionCust
#-----------------------------------------------------------------------------
class TestTransitGatewayConnectionCust():

    #--------------------------------------------------------
    # Test serialization/deserialization for TransitGatewayConnectionCust
    #--------------------------------------------------------
    def test_transit_gateway_connection_cust_serialization(self):

        # Construct a json representation of a TransitGatewayConnectionCust model
        transit_gateway_connection_cust_model_json = {}
        transit_gateway_connection_cust_model_json['name'] = 'Transit_Service_BWTN_SJ_DL'
        transit_gateway_connection_cust_model_json['network_id'] = 'crn:v1:bluemix:public:is:us-south:a/123456::vpc:4727d842-f94f-4a2d-824a-9bc9b02c523b'
        transit_gateway_connection_cust_model_json['network_type'] = 'vpc'
        transit_gateway_connection_cust_model_json['id'] = '1a15dca5-7e33-45e1-b7c5-bc690e569531-connection_id'
        transit_gateway_connection_cust_model_json['created_at'] = '2020-01-28T18:40:40.123456Z'
        transit_gateway_connection_cust_model_json['status'] = 'attached'
        transit_gateway_connection_cust_model_json['updated_at'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of TransitGatewayConnectionCust by calling from_dict on the json representation
        transit_gateway_connection_cust_model = TransitGatewayConnectionCust.from_dict(transit_gateway_connection_cust_model_json)
        assert transit_gateway_connection_cust_model != False

        # Construct a model instance of TransitGatewayConnectionCust by calling from_dict on the json representation
        transit_gateway_connection_cust_model_dict = TransitGatewayConnectionCust.from_dict(transit_gateway_connection_cust_model_json).__dict__
        transit_gateway_connection_cust_model2 = TransitGatewayConnectionCust(**transit_gateway_connection_cust_model_dict)

        # Verify the model instances are equivalent
        assert transit_gateway_connection_cust_model == transit_gateway_connection_cust_model2

        # Convert model instance back to dict and verify no loss of data
        transit_gateway_connection_cust_model_json2 = transit_gateway_connection_cust_model.to_dict()
        assert transit_gateway_connection_cust_model_json2 == transit_gateway_connection_cust_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
