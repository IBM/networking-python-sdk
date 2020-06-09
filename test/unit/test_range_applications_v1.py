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

base_url = 'https://api.cis.cloud.ibm.com/'
service.set_service_url(base_url)

##############################################################################
# Start of Service: ListRangeApplications
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_range_apps
#-----------------------------------------------------------------------------
class TestListRangeApps():

    #--------------------------------------------------------
    # list_range_apps()
    #--------------------------------------------------------
    @responses.activate
    def test_list_range_apps_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/range/apps'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "ea95132c15732412d22c1476fa83f27a", "protocol": "tcp/22", "dns": {"type": "CNAME", "name": "ssh.example.com"}, "origin_direct": ["origin_direct"], "ip_firewall": true, "proxy_protocol": "v1", "edge_ips": {"type": "dynamic", "connectivity": "ipv4"}, "tls": "flexible", "traffic_type": "direct", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        page = 38
        per_page = 38
        order = 'protocol'
        direction = 'asc'

        # Invoke method
        response = service.list_range_apps(
            page=page,
            per_page=per_page,
            order=order,
            direction=direction
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
        url = base_url + '/v1/testString/zones/testString/range/apps'
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


# endregion
##############################################################################
# End of Service: ListRangeApplications
##############################################################################

##############################################################################
# Start of Service: GetRangeApplication
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_range_app
#-----------------------------------------------------------------------------
class TestGetRangeApp():

    #--------------------------------------------------------
    # get_range_app()
    #--------------------------------------------------------
    @responses.activate
    def test_get_range_app_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/range/apps/testString'
        mock_response = '{"id": "ea95132c15732412d22c1476fa83f27a", "protocol": "tcp/22", "dns": {"type": "CNAME", "name": "ssh.example.com"}, "origin_direct": ["origin_direct"], "ip_firewall": true, "proxy_protocol": "v1", "edge_ips": {"type": "dynamic", "connectivity": "ipv4"}, "tls": "flexible", "traffic_type": "direct", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        app_identifier = 'testString'

        # Invoke method
        response = service.get_range_app(
            app_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_range_app_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_range_app_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/range/apps/testString'
        mock_response = '{"id": "ea95132c15732412d22c1476fa83f27a", "protocol": "tcp/22", "dns": {"type": "CNAME", "name": "ssh.example.com"}, "origin_direct": ["origin_direct"], "ip_firewall": true, "proxy_protocol": "v1", "edge_ips": {"type": "dynamic", "connectivity": "ipv4"}, "tls": "flexible", "traffic_type": "direct", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        app_identifier = 'testString'

        # Invoke method
        response = service.get_range_app(
            app_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: GetRangeApplication
##############################################################################

##############################################################################
# Start of Service: CreateARangeApplication
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for create_range_app
#-----------------------------------------------------------------------------
class TestCreateRangeApp():

    #--------------------------------------------------------
    # create_range_app()
    #--------------------------------------------------------
    @responses.activate
    def test_create_range_app_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/range/apps'
        mock_response = '{"id": "ea95132c15732412d22c1476fa83f27a", "protocol": "tcp/22", "dns": {"type": "CNAME", "name": "ssh.example.com"}, "origin_direct": ["origin_direct"], "ip_firewall": true, "proxy_protocol": "v1", "edge_ips": {"type": "dynamic", "connectivity": "ipv4"}, "tls": "flexible", "traffic_type": "direct", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a RangeAppReqDns model
        range_app_req_dns_model =  {
            'type': 'CNAME',
            'name': 'ssh.example.com'
        }
        # Construct a dict representation of a RangeAppReqOriginDns model
        range_app_req_origin_dns_model =  {
            'name': 'origin.net'
        }
        # Construct a dict representation of a RangeAppReqEdgeIps model
        range_app_req_edge_ips_model =  {
            'type': 'dynamic',
            'connectivity': 'all'
        }

        # Set up parameter values
        protocol = 'tcp/22'
        dns = range_app_req_dns_model
        origin_direct = ['testString']
        origin_dns = range_app_req_origin_dns_model
        origin_port = 22
        ip_firewall = True
        proxy_protocol = 'false'
        edge_ips = range_app_req_edge_ips_model
        traffic_type = 'direct'
        tls = 'false'

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
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['protocol'] == protocol
        assert req_body['dns'] == dns
        assert req_body['origin_direct'] == origin_direct
        assert req_body['origin_dns'] == origin_dns
        assert req_body['origin_port'] == origin_port
        assert req_body['ip_firewall'] == ip_firewall
        assert req_body['proxy_protocol'] == proxy_protocol
        assert req_body['edge_ips'] == edge_ips
        assert req_body['traffic_type'] == traffic_type
        assert req_body['tls'] == tls


    #--------------------------------------------------------
    # test_create_range_app_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_range_app_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/range/apps'
        mock_response = '{"id": "ea95132c15732412d22c1476fa83f27a", "protocol": "tcp/22", "dns": {"type": "CNAME", "name": "ssh.example.com"}, "origin_direct": ["origin_direct"], "ip_firewall": true, "proxy_protocol": "v1", "edge_ips": {"type": "dynamic", "connectivity": "ipv4"}, "tls": "flexible", "traffic_type": "direct", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a RangeAppReqDns model
        range_app_req_dns_model =  {
            'type': 'CNAME',
            'name': 'ssh.example.com'
        }
        # Construct a dict representation of a RangeAppReqOriginDns model
        range_app_req_origin_dns_model =  {
            'name': 'origin.net'
        }
        # Construct a dict representation of a RangeAppReqEdgeIps model
        range_app_req_edge_ips_model =  {
            'type': 'dynamic',
            'connectivity': 'all'
        }

        # Set up parameter values
        protocol = 'tcp/22'
        dns = range_app_req_dns_model
        origin_direct = ['testString']
        origin_dns = range_app_req_origin_dns_model
        origin_port = 22
        ip_firewall = True
        proxy_protocol = 'false'
        edge_ips = range_app_req_edge_ips_model
        traffic_type = 'direct'
        tls = 'false'

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
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['protocol'] == protocol
        assert req_body['dns'] == dns
        assert req_body['origin_direct'] == origin_direct
        assert req_body['origin_dns'] == origin_dns
        assert req_body['origin_port'] == origin_port
        assert req_body['ip_firewall'] == ip_firewall
        assert req_body['proxy_protocol'] == proxy_protocol
        assert req_body['edge_ips'] == edge_ips
        assert req_body['traffic_type'] == traffic_type
        assert req_body['tls'] == tls


# endregion
##############################################################################
# End of Service: CreateARangeApplication
##############################################################################

##############################################################################
# Start of Service: UpdateARangeApplication
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for update_range_app
#-----------------------------------------------------------------------------
class TestUpdateRangeApp():

    #--------------------------------------------------------
    # update_range_app()
    #--------------------------------------------------------
    @responses.activate
    def test_update_range_app_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/range/apps/testString'
        mock_response = '{"id": "ea95132c15732412d22c1476fa83f27a", "protocol": "tcp/22", "dns": {"type": "CNAME", "name": "ssh.example.com"}, "origin_direct": ["origin_direct"], "ip_firewall": true, "proxy_protocol": "v1", "edge_ips": {"type": "dynamic", "connectivity": "ipv4"}, "tls": "flexible", "traffic_type": "direct", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a RangeAppReqDns model
        range_app_req_dns_model =  {
            'type': 'CNAME',
            'name': 'ssh.example.com'
        }
        # Construct a dict representation of a RangeAppReqOriginDns model
        range_app_req_origin_dns_model =  {
            'name': 'origin.net'
        }
        # Construct a dict representation of a RangeAppReqEdgeIps model
        range_app_req_edge_ips_model =  {
            'type': 'dynamic',
            'connectivity': 'all'
        }

        # Set up parameter values
        app_identifier = 'testString'
        protocol = 'tcp/22'
        dns = range_app_req_dns_model
        origin_direct = ['testString']
        origin_dns = range_app_req_origin_dns_model
        origin_port = 22
        ip_firewall = True
        proxy_protocol = 'false'
        edge_ips = range_app_req_edge_ips_model
        traffic_type = 'direct'
        tls = 'false'

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
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['protocol'] == protocol
        assert req_body['dns'] == dns
        assert req_body['origin_direct'] == origin_direct
        assert req_body['origin_dns'] == origin_dns
        assert req_body['origin_port'] == origin_port
        assert req_body['ip_firewall'] == ip_firewall
        assert req_body['proxy_protocol'] == proxy_protocol
        assert req_body['edge_ips'] == edge_ips
        assert req_body['traffic_type'] == traffic_type
        assert req_body['tls'] == tls


    #--------------------------------------------------------
    # test_update_range_app_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_range_app_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/range/apps/testString'
        mock_response = '{"id": "ea95132c15732412d22c1476fa83f27a", "protocol": "tcp/22", "dns": {"type": "CNAME", "name": "ssh.example.com"}, "origin_direct": ["origin_direct"], "ip_firewall": true, "proxy_protocol": "v1", "edge_ips": {"type": "dynamic", "connectivity": "ipv4"}, "tls": "flexible", "traffic_type": "direct", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a RangeAppReqDns model
        range_app_req_dns_model =  {
            'type': 'CNAME',
            'name': 'ssh.example.com'
        }
        # Construct a dict representation of a RangeAppReqOriginDns model
        range_app_req_origin_dns_model =  {
            'name': 'origin.net'
        }
        # Construct a dict representation of a RangeAppReqEdgeIps model
        range_app_req_edge_ips_model =  {
            'type': 'dynamic',
            'connectivity': 'all'
        }

        # Set up parameter values
        app_identifier = 'testString'
        protocol = 'tcp/22'
        dns = range_app_req_dns_model
        origin_direct = ['testString']
        origin_dns = range_app_req_origin_dns_model
        origin_port = 22
        ip_firewall = True
        proxy_protocol = 'false'
        edge_ips = range_app_req_edge_ips_model
        traffic_type = 'direct'
        tls = 'false'

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
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['protocol'] == protocol
        assert req_body['dns'] == dns
        assert req_body['origin_direct'] == origin_direct
        assert req_body['origin_dns'] == origin_dns
        assert req_body['origin_port'] == origin_port
        assert req_body['ip_firewall'] == ip_firewall
        assert req_body['proxy_protocol'] == proxy_protocol
        assert req_body['edge_ips'] == edge_ips
        assert req_body['traffic_type'] == traffic_type
        assert req_body['tls'] == tls


# endregion
##############################################################################
# End of Service: UpdateARangeApplication
##############################################################################

##############################################################################
# Start of Service: DeleteARangeApplication
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for delete_range_app
#-----------------------------------------------------------------------------
class TestDeleteRangeApp():

    #--------------------------------------------------------
    # delete_range_app()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_range_app_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/range/apps/testString'
        mock_response = '{"id": "ea95132c15732412d22c1476fa83f27a"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        app_identifier = 'testString'

        # Invoke method
        response = service.delete_range_app(
            app_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_delete_range_app_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_range_app_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/range/apps/testString'
        mock_response = '{"id": "ea95132c15732412d22c1476fa83f27a"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        app_identifier = 'testString'

        # Invoke method
        response = service.delete_range_app(
            app_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: DeleteARangeApplication
##############################################################################

