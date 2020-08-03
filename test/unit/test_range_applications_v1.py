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
import requests
import responses
from ibm_cloud_networking_services.range_applications_v1 import *

crn = 'testString'
zone_identifier = 'testString'

service = RangeApplicationsV1(
    authenticator=NoAuthAuthenticator(),
    crn=crn,
    zone_identifier=zone_identifier
    )

base_url = 'https://api.cis.cloud.ibm.com'
service.set_service_url(base_url)

##############################################################################
# Start of Service: RangeApplications
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_range_apps
#-----------------------------------------------------------------------------
class TestListRangeApps():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # list_range_apps()
    #--------------------------------------------------------
    @responses.activate
    def test_list_range_apps_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/range/apps')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "ea95132c15732412d22c1476fa83f27a", "protocol": "tcp/22", "dns": {"type": "CNAME", "name": "ssh.example.com"}, "origin_direct": ["origin_direct"], "ip_firewall": true, "proxy_protocol": "v1", "edge_ips": {"type": "dynamic", "connectivity": "ipv4"}, "tls": "flexible", "traffic_type": "direct", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        page = 38
        per_page = 1
        order = 'protocol'
        direction = 'asc'

        # Invoke method
        response = service.list_range_apps(
            page=page,
            per_page=per_page,
            order=order,
            direction=direction,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'page={}'.format(page) in query_string
        assert 'per_page={}'.format(per_page) in query_string
        assert 'order={}'.format(order) in query_string
        assert 'direction={}'.format(direction) in query_string


    #--------------------------------------------------------
    # test_list_range_apps_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_range_apps_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/range/apps')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "ea95132c15732412d22c1476fa83f27a", "protocol": "tcp/22", "dns": {"type": "CNAME", "name": "ssh.example.com"}, "origin_direct": ["origin_direct"], "ip_firewall": true, "proxy_protocol": "v1", "edge_ips": {"type": "dynamic", "connectivity": "ipv4"}, "tls": "flexible", "traffic_type": "direct", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_range_apps()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_list_range_apps_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_list_range_apps_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/range/apps')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "ea95132c15732412d22c1476fa83f27a", "protocol": "tcp/22", "dns": {"type": "CNAME", "name": "ssh.example.com"}, "origin_direct": ["origin_direct"], "ip_firewall": true, "proxy_protocol": "v1", "edge_ips": {"type": "dynamic", "connectivity": "ipv4"}, "tls": "flexible", "traffic_type": "direct", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00"}]}'
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
                service.list_range_apps(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for create_range_app
#-----------------------------------------------------------------------------
class TestCreateRangeApp():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # create_range_app()
    #--------------------------------------------------------
    @responses.activate
    def test_create_range_app_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/range/apps')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "ea95132c15732412d22c1476fa83f27a", "protocol": "tcp/22", "dns": {"type": "CNAME", "name": "ssh.example.com"}, "origin_direct": ["origin_direct"], "ip_firewall": true, "proxy_protocol": "v1", "edge_ips": {"type": "dynamic", "connectivity": "ipv4"}, "tls": "flexible", "traffic_type": "direct", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a RangeAppReqDns model
        range_app_req_dns_model = {}
        range_app_req_dns_model['type'] = 'CNAME'
        range_app_req_dns_model['name'] = 'ssh.example.com'

        # Construct a dict representation of a RangeAppReqOriginDns model
        range_app_req_origin_dns_model = {}
        range_app_req_origin_dns_model['name'] = 'origin.net'

        # Construct a dict representation of a RangeAppReqEdgeIps model
        range_app_req_edge_ips_model = {}
        range_app_req_edge_ips_model['type'] = 'dynamic'
        range_app_req_edge_ips_model['connectivity'] = 'all'

        # Set up parameter values
        protocol = 'tcp/22'
        dns = range_app_req_dns_model
        origin_direct = ['testString']
        origin_dns = range_app_req_origin_dns_model
        origin_port = 22
        ip_firewall = True
        proxy_protocol = 'off'
        edge_ips = range_app_req_edge_ips_model
        traffic_type = 'direct'
        tls = 'off'

        # Invoke method
        response = service.create_range_app(
            protocol,
            dns,
            origin_direct=origin_direct,
            origin_dns=origin_dns,
            origin_port=origin_port,
            ip_firewall=ip_firewall,
            proxy_protocol=proxy_protocol,
            edge_ips=edge_ips,
            traffic_type=traffic_type,
            tls=tls,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['protocol'] == 'tcp/22'
        assert req_body['dns'] == range_app_req_dns_model
        assert req_body['origin_direct'] == ['testString']
        assert req_body['origin_dns'] == range_app_req_origin_dns_model
        assert req_body['origin_port'] == 22
        assert req_body['ip_firewall'] == True
        assert req_body['proxy_protocol'] == 'off'
        assert req_body['edge_ips'] == range_app_req_edge_ips_model
        assert req_body['traffic_type'] == 'direct'
        assert req_body['tls'] == 'off'


    #--------------------------------------------------------
    # test_create_range_app_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_create_range_app_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/range/apps')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "ea95132c15732412d22c1476fa83f27a", "protocol": "tcp/22", "dns": {"type": "CNAME", "name": "ssh.example.com"}, "origin_direct": ["origin_direct"], "ip_firewall": true, "proxy_protocol": "v1", "edge_ips": {"type": "dynamic", "connectivity": "ipv4"}, "tls": "flexible", "traffic_type": "direct", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a RangeAppReqDns model
        range_app_req_dns_model = {}
        range_app_req_dns_model['type'] = 'CNAME'
        range_app_req_dns_model['name'] = 'ssh.example.com'

        # Construct a dict representation of a RangeAppReqOriginDns model
        range_app_req_origin_dns_model = {}
        range_app_req_origin_dns_model['name'] = 'origin.net'

        # Construct a dict representation of a RangeAppReqEdgeIps model
        range_app_req_edge_ips_model = {}
        range_app_req_edge_ips_model['type'] = 'dynamic'
        range_app_req_edge_ips_model['connectivity'] = 'all'

        # Set up parameter values
        protocol = 'tcp/22'
        dns = range_app_req_dns_model
        origin_direct = ['testString']
        origin_dns = range_app_req_origin_dns_model
        origin_port = 22
        ip_firewall = True
        proxy_protocol = 'off'
        edge_ips = range_app_req_edge_ips_model
        traffic_type = 'direct'
        tls = 'off'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "protocol": protocol,
            "dns": dns,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.create_range_app(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_range_app
#-----------------------------------------------------------------------------
class TestGetRangeApp():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_range_app()
    #--------------------------------------------------------
    @responses.activate
    def test_get_range_app_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/range/apps/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "ea95132c15732412d22c1476fa83f27a", "protocol": "tcp/22", "dns": {"type": "CNAME", "name": "ssh.example.com"}, "origin_direct": ["origin_direct"], "ip_firewall": true, "proxy_protocol": "v1", "edge_ips": {"type": "dynamic", "connectivity": "ipv4"}, "tls": "flexible", "traffic_type": "direct", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        app_identifier = 'testString'

        # Invoke method
        response = service.get_range_app(
            app_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_range_app_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_range_app_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/range/apps/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "ea95132c15732412d22c1476fa83f27a", "protocol": "tcp/22", "dns": {"type": "CNAME", "name": "ssh.example.com"}, "origin_direct": ["origin_direct"], "ip_firewall": true, "proxy_protocol": "v1", "edge_ips": {"type": "dynamic", "connectivity": "ipv4"}, "tls": "flexible", "traffic_type": "direct", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        app_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "app_identifier": app_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_range_app(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_range_app
#-----------------------------------------------------------------------------
class TestUpdateRangeApp():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_range_app()
    #--------------------------------------------------------
    @responses.activate
    def test_update_range_app_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/range/apps/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "ea95132c15732412d22c1476fa83f27a", "protocol": "tcp/22", "dns": {"type": "CNAME", "name": "ssh.example.com"}, "origin_direct": ["origin_direct"], "ip_firewall": true, "proxy_protocol": "v1", "edge_ips": {"type": "dynamic", "connectivity": "ipv4"}, "tls": "flexible", "traffic_type": "direct", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a RangeAppReqDns model
        range_app_req_dns_model = {}
        range_app_req_dns_model['type'] = 'CNAME'
        range_app_req_dns_model['name'] = 'ssh.example.com'

        # Construct a dict representation of a RangeAppReqOriginDns model
        range_app_req_origin_dns_model = {}
        range_app_req_origin_dns_model['name'] = 'origin.net'

        # Construct a dict representation of a RangeAppReqEdgeIps model
        range_app_req_edge_ips_model = {}
        range_app_req_edge_ips_model['type'] = 'dynamic'
        range_app_req_edge_ips_model['connectivity'] = 'all'

        # Set up parameter values
        app_identifier = 'testString'
        protocol = 'tcp/22'
        dns = range_app_req_dns_model
        origin_direct = ['testString']
        origin_dns = range_app_req_origin_dns_model
        origin_port = 22
        ip_firewall = True
        proxy_protocol = 'off'
        edge_ips = range_app_req_edge_ips_model
        traffic_type = 'direct'
        tls = 'off'

        # Invoke method
        response = service.update_range_app(
            app_identifier,
            protocol,
            dns,
            origin_direct=origin_direct,
            origin_dns=origin_dns,
            origin_port=origin_port,
            ip_firewall=ip_firewall,
            proxy_protocol=proxy_protocol,
            edge_ips=edge_ips,
            traffic_type=traffic_type,
            tls=tls,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['protocol'] == 'tcp/22'
        assert req_body['dns'] == range_app_req_dns_model
        assert req_body['origin_direct'] == ['testString']
        assert req_body['origin_dns'] == range_app_req_origin_dns_model
        assert req_body['origin_port'] == 22
        assert req_body['ip_firewall'] == True
        assert req_body['proxy_protocol'] == 'off'
        assert req_body['edge_ips'] == range_app_req_edge_ips_model
        assert req_body['traffic_type'] == 'direct'
        assert req_body['tls'] == 'off'


    #--------------------------------------------------------
    # test_update_range_app_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_range_app_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/range/apps/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "ea95132c15732412d22c1476fa83f27a", "protocol": "tcp/22", "dns": {"type": "CNAME", "name": "ssh.example.com"}, "origin_direct": ["origin_direct"], "ip_firewall": true, "proxy_protocol": "v1", "edge_ips": {"type": "dynamic", "connectivity": "ipv4"}, "tls": "flexible", "traffic_type": "direct", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a RangeAppReqDns model
        range_app_req_dns_model = {}
        range_app_req_dns_model['type'] = 'CNAME'
        range_app_req_dns_model['name'] = 'ssh.example.com'

        # Construct a dict representation of a RangeAppReqOriginDns model
        range_app_req_origin_dns_model = {}
        range_app_req_origin_dns_model['name'] = 'origin.net'

        # Construct a dict representation of a RangeAppReqEdgeIps model
        range_app_req_edge_ips_model = {}
        range_app_req_edge_ips_model['type'] = 'dynamic'
        range_app_req_edge_ips_model['connectivity'] = 'all'

        # Set up parameter values
        app_identifier = 'testString'
        protocol = 'tcp/22'
        dns = range_app_req_dns_model
        origin_direct = ['testString']
        origin_dns = range_app_req_origin_dns_model
        origin_port = 22
        ip_firewall = True
        proxy_protocol = 'off'
        edge_ips = range_app_req_edge_ips_model
        traffic_type = 'direct'
        tls = 'off'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "app_identifier": app_identifier,
            "protocol": protocol,
            "dns": dns,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.update_range_app(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for delete_range_app
#-----------------------------------------------------------------------------
class TestDeleteRangeApp():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # delete_range_app()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_range_app_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/range/apps/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "ea95132c15732412d22c1476fa83f27a", "protocol": "tcp/22", "dns": {"type": "CNAME", "name": "ssh.example.com"}, "origin_direct": ["origin_direct"], "ip_firewall": true, "proxy_protocol": "v1", "edge_ips": {"type": "dynamic", "connectivity": "ipv4"}, "tls": "flexible", "traffic_type": "direct", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        app_identifier = 'testString'

        # Invoke method
        response = service.delete_range_app(
            app_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_delete_range_app_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_range_app_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/range/apps/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "ea95132c15732412d22c1476fa83f27a", "protocol": "tcp/22", "dns": {"type": "CNAME", "name": "ssh.example.com"}, "origin_direct": ["origin_direct"], "ip_firewall": true, "proxy_protocol": "v1", "edge_ips": {"type": "dynamic", "connectivity": "ipv4"}, "tls": "flexible", "traffic_type": "direct", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        app_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "app_identifier": app_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_range_app(**req_copy)



# endregion
##############################################################################
# End of Service: RangeApplications
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
#-----------------------------------------------------------------------------
# Test Class for RangeAppReqDns
#-----------------------------------------------------------------------------
class TestRangeAppReqDns():

    #--------------------------------------------------------
    # Test serialization/deserialization for RangeAppReqDns
    #--------------------------------------------------------
    def test_range_app_req_dns_serialization(self):

        # Construct a json representation of a RangeAppReqDns model
        range_app_req_dns_model_json = {}
        range_app_req_dns_model_json['type'] = 'CNAME'
        range_app_req_dns_model_json['name'] = 'ssh.example.com'

        # Construct a model instance of RangeAppReqDns by calling from_dict on the json representation
        range_app_req_dns_model = RangeAppReqDns.from_dict(range_app_req_dns_model_json)
        assert range_app_req_dns_model != False

        # Construct a model instance of RangeAppReqDns by calling from_dict on the json representation
        range_app_req_dns_model_dict = RangeAppReqDns.from_dict(range_app_req_dns_model_json).__dict__
        range_app_req_dns_model2 = RangeAppReqDns(**range_app_req_dns_model_dict)

        # Verify the model instances are equivalent
        assert range_app_req_dns_model == range_app_req_dns_model2

        # Convert model instance back to dict and verify no loss of data
        range_app_req_dns_model_json2 = range_app_req_dns_model.to_dict()
        assert range_app_req_dns_model_json2 == range_app_req_dns_model_json

#-----------------------------------------------------------------------------
# Test Class for RangeAppReqEdgeIps
#-----------------------------------------------------------------------------
class TestRangeAppReqEdgeIps():

    #--------------------------------------------------------
    # Test serialization/deserialization for RangeAppReqEdgeIps
    #--------------------------------------------------------
    def test_range_app_req_edge_ips_serialization(self):

        # Construct a json representation of a RangeAppReqEdgeIps model
        range_app_req_edge_ips_model_json = {}
        range_app_req_edge_ips_model_json['type'] = 'dynamic'
        range_app_req_edge_ips_model_json['connectivity'] = 'all'

        # Construct a model instance of RangeAppReqEdgeIps by calling from_dict on the json representation
        range_app_req_edge_ips_model = RangeAppReqEdgeIps.from_dict(range_app_req_edge_ips_model_json)
        assert range_app_req_edge_ips_model != False

        # Construct a model instance of RangeAppReqEdgeIps by calling from_dict on the json representation
        range_app_req_edge_ips_model_dict = RangeAppReqEdgeIps.from_dict(range_app_req_edge_ips_model_json).__dict__
        range_app_req_edge_ips_model2 = RangeAppReqEdgeIps(**range_app_req_edge_ips_model_dict)

        # Verify the model instances are equivalent
        assert range_app_req_edge_ips_model == range_app_req_edge_ips_model2

        # Convert model instance back to dict and verify no loss of data
        range_app_req_edge_ips_model_json2 = range_app_req_edge_ips_model.to_dict()
        assert range_app_req_edge_ips_model_json2 == range_app_req_edge_ips_model_json

#-----------------------------------------------------------------------------
# Test Class for RangeAppReqOriginDns
#-----------------------------------------------------------------------------
class TestRangeAppReqOriginDns():

    #--------------------------------------------------------
    # Test serialization/deserialization for RangeAppReqOriginDns
    #--------------------------------------------------------
    def test_range_app_req_origin_dns_serialization(self):

        # Construct a json representation of a RangeAppReqOriginDns model
        range_app_req_origin_dns_model_json = {}
        range_app_req_origin_dns_model_json['name'] = 'origin.net'

        # Construct a model instance of RangeAppReqOriginDns by calling from_dict on the json representation
        range_app_req_origin_dns_model = RangeAppReqOriginDns.from_dict(range_app_req_origin_dns_model_json)
        assert range_app_req_origin_dns_model != False

        # Construct a model instance of RangeAppReqOriginDns by calling from_dict on the json representation
        range_app_req_origin_dns_model_dict = RangeAppReqOriginDns.from_dict(range_app_req_origin_dns_model_json).__dict__
        range_app_req_origin_dns_model2 = RangeAppReqOriginDns(**range_app_req_origin_dns_model_dict)

        # Verify the model instances are equivalent
        assert range_app_req_origin_dns_model == range_app_req_origin_dns_model2

        # Convert model instance back to dict and verify no loss of data
        range_app_req_origin_dns_model_json2 = range_app_req_origin_dns_model.to_dict()
        assert range_app_req_origin_dns_model_json2 == range_app_req_origin_dns_model_json

#-----------------------------------------------------------------------------
# Test Class for RangeApplicationObjectDns
#-----------------------------------------------------------------------------
class TestRangeApplicationObjectDns():

    #--------------------------------------------------------
    # Test serialization/deserialization for RangeApplicationObjectDns
    #--------------------------------------------------------
    def test_range_application_object_dns_serialization(self):

        # Construct a json representation of a RangeApplicationObjectDns model
        range_application_object_dns_model_json = {}
        range_application_object_dns_model_json['type'] = 'CNAME'
        range_application_object_dns_model_json['name'] = 'ssh.example.com'

        # Construct a model instance of RangeApplicationObjectDns by calling from_dict on the json representation
        range_application_object_dns_model = RangeApplicationObjectDns.from_dict(range_application_object_dns_model_json)
        assert range_application_object_dns_model != False

        # Construct a model instance of RangeApplicationObjectDns by calling from_dict on the json representation
        range_application_object_dns_model_dict = RangeApplicationObjectDns.from_dict(range_application_object_dns_model_json).__dict__
        range_application_object_dns_model2 = RangeApplicationObjectDns(**range_application_object_dns_model_dict)

        # Verify the model instances are equivalent
        assert range_application_object_dns_model == range_application_object_dns_model2

        # Convert model instance back to dict and verify no loss of data
        range_application_object_dns_model_json2 = range_application_object_dns_model.to_dict()
        assert range_application_object_dns_model_json2 == range_application_object_dns_model_json

#-----------------------------------------------------------------------------
# Test Class for RangeApplicationObjectEdgeIps
#-----------------------------------------------------------------------------
class TestRangeApplicationObjectEdgeIps():

    #--------------------------------------------------------
    # Test serialization/deserialization for RangeApplicationObjectEdgeIps
    #--------------------------------------------------------
    def test_range_application_object_edge_ips_serialization(self):

        # Construct a json representation of a RangeApplicationObjectEdgeIps model
        range_application_object_edge_ips_model_json = {}
        range_application_object_edge_ips_model_json['type'] = 'dynamic'
        range_application_object_edge_ips_model_json['connectivity'] = 'ipv4'

        # Construct a model instance of RangeApplicationObjectEdgeIps by calling from_dict on the json representation
        range_application_object_edge_ips_model = RangeApplicationObjectEdgeIps.from_dict(range_application_object_edge_ips_model_json)
        assert range_application_object_edge_ips_model != False

        # Construct a model instance of RangeApplicationObjectEdgeIps by calling from_dict on the json representation
        range_application_object_edge_ips_model_dict = RangeApplicationObjectEdgeIps.from_dict(range_application_object_edge_ips_model_json).__dict__
        range_application_object_edge_ips_model2 = RangeApplicationObjectEdgeIps(**range_application_object_edge_ips_model_dict)

        # Verify the model instances are equivalent
        assert range_application_object_edge_ips_model == range_application_object_edge_ips_model2

        # Convert model instance back to dict and verify no loss of data
        range_application_object_edge_ips_model_json2 = range_application_object_edge_ips_model.to_dict()
        assert range_application_object_edge_ips_model_json2 == range_application_object_edge_ips_model_json

#-----------------------------------------------------------------------------
# Test Class for RangeApplicationObject
#-----------------------------------------------------------------------------
class TestRangeApplicationObject():

    #--------------------------------------------------------
    # Test serialization/deserialization for RangeApplicationObject
    #--------------------------------------------------------
    def test_range_application_object_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        range_application_object_dns_model = {} # RangeApplicationObjectDns
        range_application_object_dns_model['type'] = 'CNAME'
        range_application_object_dns_model['name'] = 'ssh.example.com'

        range_application_object_edge_ips_model = {} # RangeApplicationObjectEdgeIps
        range_application_object_edge_ips_model['type'] = 'dynamic'
        range_application_object_edge_ips_model['connectivity'] = 'ipv4'

        # Construct a json representation of a RangeApplicationObject model
        range_application_object_model_json = {}
        range_application_object_model_json['id'] = 'ea95132c15732412d22c1476fa83f27a'
        range_application_object_model_json['protocol'] = 'tcp/22'
        range_application_object_model_json['dns'] = range_application_object_dns_model
        range_application_object_model_json['origin_direct'] = ['testString']
        range_application_object_model_json['ip_firewall'] = True
        range_application_object_model_json['proxy_protocol'] = 'v1'
        range_application_object_model_json['edge_ips'] = range_application_object_edge_ips_model
        range_application_object_model_json['tls'] = 'flexible'
        range_application_object_model_json['traffic_type'] = 'direct'
        range_application_object_model_json['created_on'] = '2020-01-28T18:40:40.123456Z'
        range_application_object_model_json['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of RangeApplicationObject by calling from_dict on the json representation
        range_application_object_model = RangeApplicationObject.from_dict(range_application_object_model_json)
        assert range_application_object_model != False

        # Construct a model instance of RangeApplicationObject by calling from_dict on the json representation
        range_application_object_model_dict = RangeApplicationObject.from_dict(range_application_object_model_json).__dict__
        range_application_object_model2 = RangeApplicationObject(**range_application_object_model_dict)

        # Verify the model instances are equivalent
        assert range_application_object_model == range_application_object_model2

        # Convert model instance back to dict and verify no loss of data
        range_application_object_model_json2 = range_application_object_model.to_dict()
        assert range_application_object_model_json2 == range_application_object_model_json

#-----------------------------------------------------------------------------
# Test Class for RangeApplicationResp
#-----------------------------------------------------------------------------
class TestRangeApplicationResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for RangeApplicationResp
    #--------------------------------------------------------
    def test_range_application_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        range_application_object_dns_model = {} # RangeApplicationObjectDns
        range_application_object_dns_model['type'] = 'CNAME'
        range_application_object_dns_model['name'] = 'ssh.example.com'

        range_application_object_edge_ips_model = {} # RangeApplicationObjectEdgeIps
        range_application_object_edge_ips_model['type'] = 'dynamic'
        range_application_object_edge_ips_model['connectivity'] = 'ipv4'

        range_application_object_model = {} # RangeApplicationObject
        range_application_object_model['id'] = 'ea95132c15732412d22c1476fa83f27a'
        range_application_object_model['protocol'] = 'tcp/22'
        range_application_object_model['dns'] = range_application_object_dns_model
        range_application_object_model['origin_direct'] = ['testString']
        range_application_object_model['ip_firewall'] = True
        range_application_object_model['proxy_protocol'] = 'v1'
        range_application_object_model['edge_ips'] = range_application_object_edge_ips_model
        range_application_object_model['tls'] = 'flexible'
        range_application_object_model['traffic_type'] = 'direct'
        range_application_object_model['created_on'] = '2020-01-28T18:40:40.123456Z'
        range_application_object_model['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a json representation of a RangeApplicationResp model
        range_application_resp_model_json = {}
        range_application_resp_model_json['success'] = True
        range_application_resp_model_json['errors'] = [['testString']]
        range_application_resp_model_json['messages'] = [['testString']]
        range_application_resp_model_json['result'] = range_application_object_model

        # Construct a model instance of RangeApplicationResp by calling from_dict on the json representation
        range_application_resp_model = RangeApplicationResp.from_dict(range_application_resp_model_json)
        assert range_application_resp_model != False

        # Construct a model instance of RangeApplicationResp by calling from_dict on the json representation
        range_application_resp_model_dict = RangeApplicationResp.from_dict(range_application_resp_model_json).__dict__
        range_application_resp_model2 = RangeApplicationResp(**range_application_resp_model_dict)

        # Verify the model instances are equivalent
        assert range_application_resp_model == range_application_resp_model2

        # Convert model instance back to dict and verify no loss of data
        range_application_resp_model_json2 = range_application_resp_model.to_dict()
        assert range_application_resp_model_json2 == range_application_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for RangeApplications
#-----------------------------------------------------------------------------
class TestRangeApplications():

    #--------------------------------------------------------
    # Test serialization/deserialization for RangeApplications
    #--------------------------------------------------------
    def test_range_applications_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        range_application_object_dns_model = {} # RangeApplicationObjectDns
        range_application_object_dns_model['type'] = 'CNAME'
        range_application_object_dns_model['name'] = 'ssh.example.com'

        range_application_object_edge_ips_model = {} # RangeApplicationObjectEdgeIps
        range_application_object_edge_ips_model['type'] = 'dynamic'
        range_application_object_edge_ips_model['connectivity'] = 'ipv4'

        range_application_object_model = {} # RangeApplicationObject
        range_application_object_model['id'] = 'ea95132c15732412d22c1476fa83f27a'
        range_application_object_model['protocol'] = 'tcp/22'
        range_application_object_model['dns'] = range_application_object_dns_model
        range_application_object_model['origin_direct'] = ['testString']
        range_application_object_model['ip_firewall'] = True
        range_application_object_model['proxy_protocol'] = 'v1'
        range_application_object_model['edge_ips'] = range_application_object_edge_ips_model
        range_application_object_model['tls'] = 'flexible'
        range_application_object_model['traffic_type'] = 'direct'
        range_application_object_model['created_on'] = '2020-01-28T18:40:40.123456Z'
        range_application_object_model['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a json representation of a RangeApplications model
        range_applications_model_json = {}
        range_applications_model_json['success'] = True
        range_applications_model_json['errors'] = [['testString']]
        range_applications_model_json['messages'] = [['testString']]
        range_applications_model_json['result'] = [range_application_object_model]

        # Construct a model instance of RangeApplications by calling from_dict on the json representation
        range_applications_model = RangeApplications.from_dict(range_applications_model_json)
        assert range_applications_model != False

        # Construct a model instance of RangeApplications by calling from_dict on the json representation
        range_applications_model_dict = RangeApplications.from_dict(range_applications_model_json).__dict__
        range_applications_model2 = RangeApplications(**range_applications_model_dict)

        # Verify the model instances are equivalent
        assert range_applications_model == range_applications_model2

        # Convert model instance back to dict and verify no loss of data
        range_applications_model_json2 = range_applications_model.to_dict()
        assert range_applications_model_json2 == range_applications_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
