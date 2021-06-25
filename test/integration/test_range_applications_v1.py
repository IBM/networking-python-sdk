# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.

"""
Integration test code for Range App Services
"""

import os
import unittest
from dotenv import load_dotenv, find_dotenv
from ibm_cloud_networking_services.range_applications_v1 import RangeApplicationsV1

configFile = "cis.env"

# load the .env file containing your environment variables
try:
    load_dotenv(find_dotenv(filename="cis.env"))
except:
    print('warning: no cis.env file loaded')


class TestRangeApplicationsApiV1(unittest.TestCase):
    """ Range Application API test class """

    @unittest.skip("skipping")

    def setUp(self):
        if not os.path.exists(configFile):
            raise unittest.SkipTest(
                'External configuration not available, skipping...')

        self.crn = os.getenv("CRN")
        self.zone_id = os.getenv("ZONE_ID")
        self.endpoint = os.getenv("API_ENDPOINT")
        self.url = os.getenv("URL")
        self.rapp = RangeApplicationsV1.new_instance(
            crn=self.crn, zone_identifier=self.zone_id, service_name="cis_services")
        self.rapp.set_service_url(self.endpoint)
        self._clean_up_page_apps()

    def tearDown(self):
        """ tear down """
        # Delete the resources
        print("Clean up complete")

    def _clean_up_page_apps(self):
        resp = self.rapp.list_range_apps()

        for id in resp.get_result().get("result"):
            # delete range app
            resp = self.rapp.delete_range_app(app_identifier=id.get("id"))

    def test_1_range_app_origin_direct(self):
        protocol = "tcp/22"
        dns = {
            "type": "CNAME",
            "name": "example." + self.url
        }
        origin_direct = ["tcp://12.1.1.1:22"]
        origin_port = 22
        ip_firewall = True
        proxy_protocol = "off"
        edge_ips = {
            "type": "dynamic",
            "connectivity": "all"
        }
        traffic_type = "direct"
        tls = "off"

        # create range app
        resp = self.rapp.create_range_app(protocol=protocol, dns=dns, origin_direct=origin_direct,
                                          origin_port=origin_port, ip_firewall=ip_firewall, proxy_protocol=proxy_protocol, edge_ips=edge_ips, traffic_type=traffic_type, tls=tls)
        assert resp is not None
        assert resp.status_code == 200

        app_id = resp.get_result().get("result")["id"]

        # get range app
        resp = self.rapp.get_range_app(
            app_identifier=app_id)
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("result")["id"] == app_id

        # update range app
        origin_direct = ["tcp://12.12.12.12:25"]
        resp = self.rapp.update_range_app(app_identifier=app_id, protocol=protocol, dns=dns, origin_direct=origin_direct,
                                          origin_port=origin_port, ip_firewall=ip_firewall, proxy_protocol=proxy_protocol, edge_ips=edge_ips, traffic_type=traffic_type, tls=tls)
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("result").get("origin_direct") == origin_direct

        # delete range app
        resp = self.rapp.delete_range_app(
            app_identifier=app_id)
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("result")["id"] == app_id

    def test_1_range_app_origin_dns(self):
        name = "origin.net"
        protocol = "tcp/22"
        dns = {
            "type": "CNAME",
            "name": "example." + self.url
        }
        origin_dns = {
            "name": name
        }
        origin_port = 22
        ip_firewall = True
        proxy_protocol = "off"
        edge_ips = {
            "type": "dynamic",
            "connectivity": "all"
        }
        traffic_type = "direct"
        tls = "off"

        # create range app
        resp = self.rapp.create_range_app(protocol=protocol, dns=dns, origin_dns=origin_dns,
                                          origin_port=origin_port, ip_firewall=ip_firewall, proxy_protocol=proxy_protocol, edge_ips=edge_ips, traffic_type=traffic_type, tls=tls)
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("result").get("origin_dns").get("name") == name

        app_id = resp.get_result().get("result")["id"]

        # update range app
        name = "origin-example.net"
        origin_dns = {
            "name": name
        }
        resp = self.rapp.update_range_app(app_identifier=app_id, protocol=protocol, dns=dns, origin_dns=origin_dns,
                                          origin_port=origin_port, ip_firewall=ip_firewall, proxy_protocol=proxy_protocol, edge_ips=edge_ips, traffic_type=traffic_type, tls=tls)
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("result").get("origin_dns").get("name") == name

        # get range app
        resp = self.rapp.get_range_app(
            app_identifier=app_id)
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("result")["id"] == app_id

        # delete range app
        resp = self.rapp.delete_range_app(
            app_identifier=app_id)
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("result")["id"] == app_id

    def test_1_list_range_apps(self):
        protocol = "tcp/22"
        origin_port = 22
        ip_firewall = True
        proxy_protocol = "off"
        edge_ips = {
            "type": "dynamic",
            "connectivity": "all"
        }
        traffic_type = "direct"
        tls = "off"

        # create range app
        for i in range(1, 10, 1):
            number = str(i)
            dns = {
                "type": "CNAME",
                "name": "example" + number + "." + self.url
            }
            origin_direct = ["tcp://12.1.1." + number + ":22"]
            resp = self.rapp.create_range_app(protocol=protocol, dns=dns, origin_direct=origin_direct,
                                              origin_port=origin_port, ip_firewall=ip_firewall, proxy_protocol=proxy_protocol, edge_ips=edge_ips, traffic_type=traffic_type, tls=tls)
            assert resp is not None
            assert resp.status_code == 200

        name = "origin1.net"
        protocol = "tcp/22"
        dns = {
            "type": "CNAME",
            "name": "example50." + self.url
        }
        origin_dns = {
            "name": name
        }
        origin_port = 22
        ip_firewall = True
        proxy_protocol = "off"
        edge_ips = {
            "type": "dynamic",
            "connectivity": "all"
        }
        traffic_type = "direct"
        tls = "off"

        # create range app
        resp = self.rapp.create_range_app(protocol=protocol, dns=dns, origin_dns=origin_dns,
                                          origin_port=origin_port, ip_firewall=ip_firewall, proxy_protocol=proxy_protocol, edge_ips=edge_ips, traffic_type=traffic_type, tls=tls)
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("result").get("origin_dns").get("name") == name

        resp = self.rapp.list_range_apps()
        assert resp is not None
        assert resp.status_code == 200

        # list range apps by page and per page input
        resp = self.rapp.list_range_apps(
            page=2, per_page=5, order="created_on", direction="asc")
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("result_info").get("page") == 2
        assert resp.get_result().get("result_info").get("per_page") == 5

        resp = self.rapp.list_range_apps()
        for id in resp.get_result().get("result"):
            # delete range app
            resp = self.rapp.delete_range_app(app_identifier=id.get("id"))

    def test_1_range_app_origin_direct_ip_firewall(self):
        protocol = "tcp/22"
        dns = {
            "type": "CNAME",
            "name": "example." + self.url
        }
        origin_direct = ["tcp://12.1.1.1:22"]
        origin_port = 22
        ip_firewall = False
        proxy_protocol = "off"
        edge_ips = {
            "type": "dynamic",
            "connectivity": "all"
        }
        traffic_type = "direct"
        tls = "off"

        # create range app
        resp = self.rapp.create_range_app(protocol=protocol, dns=dns, origin_direct=origin_direct,
                                          origin_port=origin_port, ip_firewall=ip_firewall, proxy_protocol=proxy_protocol, edge_ips=edge_ips, traffic_type=traffic_type, tls=tls)
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("result").get("ip_firewall") == False

        app_id = resp.get_result().get("result")["id"]

        # get range app
        resp = self.rapp.get_range_app(
            app_identifier=app_id)
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("result")["id"] == app_id

        # update range app
        ip_firewall = True
        resp = self.rapp.update_range_app(app_identifier=app_id, protocol=protocol, dns=dns, origin_direct=origin_direct,
                                          origin_port=origin_port, ip_firewall=ip_firewall, proxy_protocol=proxy_protocol, edge_ips=edge_ips, traffic_type=traffic_type, tls=tls)
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("result").get("ip_firewall") == True

        # delete range app
        resp = self.rapp.delete_range_app(
            app_identifier=app_id)
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("result")["id"] == app_id

    def test_1_range_app_origin_direct_proxy(self):
        protocol = "tcp/22"
        dns = {
            "type": "CNAME",
            "name": "example." + self.url
        }
        origin_direct = ["tcp://12.1.1.1:22"]
        origin_port = 22
        ip_firewall = False
        edge_ips = {
            "type": "dynamic",
            "connectivity": "all"
        }
        traffic_type = "direct"
        tls = "off"
        proxy_protocols = ["off", "v1", "v2"]
        i = 0
        for proxy_protocol in proxy_protocols:
            # create range app
            resp = self.rapp.create_range_app(protocol=protocol, dns=dns, origin_direct=origin_direct,
                                              origin_port=origin_port, ip_firewall=ip_firewall, proxy_protocol=proxy_protocol, edge_ips=edge_ips, traffic_type=traffic_type, tls=tls)
            assert resp is not None
            assert resp.status_code == 200
            assert resp.get_result().get("result").get("proxy_protocol") == proxy_protocol

            app_id = resp.get_result().get("result")["id"]

            # get range app
            resp = self.rapp.get_range_app(app_identifier=app_id)
            assert resp is not None
            assert resp.status_code == 200
            assert resp.get_result().get("result")["id"] == app_id

            # update range app
            i = i + 1
            proxy_protocol = proxy_protocols[i % len(proxy_protocols)]
            resp = self.rapp.update_range_app(app_identifier=app_id, protocol=protocol, dns=dns, origin_direct=origin_direct, origin_port=origin_port,
                                              ip_firewall=ip_firewall, proxy_protocol=proxy_protocol, edge_ips=edge_ips, traffic_type=traffic_type, tls=tls)
            assert resp is not None
            assert resp.status_code == 200
            assert resp.get_result().get("result").get("proxy_protocol") == proxy_protocol

            # delete range app
            resp = self.rapp.delete_range_app(app_identifier=app_id)
            assert resp is not None
            assert resp.status_code == 200
            assert resp.get_result().get("result")["id"] == app_id

    def test_1_range_app_traffic_type(self):

        traffic_types = ["direct", "http", "https"]
        #     "tls": ["off", "flexible", "full", "strict"],
        #     "connectivity": ["ipv4", "ipv6", "all"]

        protocol = "tcp/22"
        dns = {
            "type": "CNAME",
            "name": "example." + self.url
        }
        origin_direct = ["tcp://12.1.1.1:22"]
        origin_port = 22
        ip_firewall = False
        proxy_protocol = "off"
        edge_ips = {
            "type": "dynamic",
            "connectivity": "all"
        }
        tls = "off"
        i = 0
        for traffic_type in traffic_types:

            # create range app
            print("creating app with ", traffic_type)
            resp = self.rapp.create_range_app(protocol=protocol, dns=dns, origin_direct=origin_direct,
                                              origin_port=origin_port, ip_firewall=ip_firewall, proxy_protocol=proxy_protocol, edge_ips=edge_ips, traffic_type=traffic_type, tls=tls)
            assert resp is not None
            assert resp.status_code == 200

            app_id = resp.get_result().get("result")["id"]

            # get range app
            resp = self.rapp.get_range_app(app_identifier=app_id)
            assert resp is not None
            assert resp.status_code == 200
            assert resp.get_result().get("result")["id"] == app_id

            # update range app
            i = i + 1
            traffic_type = traffic_types[i % len(traffic_types)]
            print("updating app with ", traffic_type)
            resp = self.rapp.update_range_app(app_identifier=app_id, protocol=protocol, dns=dns, origin_direct=origin_direct, origin_port=origin_port,
                                              ip_firewall=ip_firewall, proxy_protocol=proxy_protocol, edge_ips=edge_ips, traffic_type=traffic_type, tls=tls)
            assert resp is not None
            assert resp.status_code == 200
            assert resp.get_result().get("result").get("traffic_type") == traffic_type

            # delete range app
            resp = self.rapp.delete_range_app(app_identifier=app_id)
            assert resp is not None
            assert resp.status_code == 200
            assert resp.get_result().get("result")["id"] == app_id

    def test_1_range_app_tls(self):

        tlss = ["off", "flexible", "full", "strict"]
        #     "connectivity": ["ipv4", "ipv6", "all"]

        protocol = "tcp/22"
        dns = {
            "type": "CNAME",
            "name": "example." + self.url
        }
        origin_direct = ["tcp://12.1.1.1:22"]
        origin_port = 22
        ip_firewall = False
        proxy_protocol = "off"
        edge_ips = {
            "type": "dynamic",
            "connectivity": "all"
        }
        traffic_type = "direct"
        i = 0
        for tls in tlss:
            # create range app
            print("creating app with tls", tls)
            resp = self.rapp.create_range_app(protocol=protocol, dns=dns, origin_direct=origin_direct,
                                              origin_port=origin_port, ip_firewall=ip_firewall, proxy_protocol=proxy_protocol, edge_ips=edge_ips, traffic_type=traffic_type, tls=tls)
            assert resp is not None
            assert resp.status_code == 200

            app_id = resp.get_result().get("result")["id"]

            # get range app
            resp = self.rapp.get_range_app(app_identifier=app_id)
            assert resp is not None
            assert resp.status_code == 200
            assert resp.get_result().get("result")["id"] == app_id
            assert resp.get_result().get("result").get("tls") == tls

            # update range app
            i = i + 1
            tls = tlss[i % len(tlss)]
            print("updating app with tls", tls)
            resp = self.rapp.update_range_app(app_identifier=app_id, protocol=protocol, dns=dns, origin_direct=origin_direct, origin_port=origin_port,
                                              ip_firewall=ip_firewall, proxy_protocol=proxy_protocol, edge_ips=edge_ips, traffic_type=traffic_type, tls=tls)
            assert resp is not None
            assert resp.status_code == 200
            assert resp.get_result().get("result").get("tls") == tls

            # delete range app
            resp = self.rapp.delete_range_app(app_identifier=app_id)
            assert resp is not None
            assert resp.status_code == 200
            assert resp.get_result().get("result")["id"] == app_id

    def test_1_range_app_connectivity(self):

        connectivities = ["ipv4", "ipv6", "all"]

        protocol = "tcp/22"
        dns = {
            "type": "CNAME",
            "name": "example." + self.url
        }
        origin_direct = ["tcp://12.1.1.1:22"]
        origin_port = 22
        ip_firewall = False
        proxy_protocol = "off"
        edge_ips = {
            "type": "dynamic",
            "connectivity": "all"
        }
        traffic_type = "direct"
        tls = "off"
        i = 0
        for connectivity in connectivities:
            # create range app
            edge_ips = {
                "type": "dynamic",
                "connectivity": connectivity
            }
            print("creating app with connectivity", connectivity)
            resp = self.rapp.create_range_app(protocol=protocol, dns=dns, origin_direct=origin_direct,
                                              origin_port=origin_port, ip_firewall=ip_firewall, proxy_protocol=proxy_protocol, edge_ips=edge_ips, traffic_type=traffic_type, tls=tls)
            assert resp is not None
            assert resp.status_code == 200

            app_id = resp.get_result().get("result")["id"]

            # get range app
            resp = self.rapp.get_range_app(app_identifier=app_id)
            assert resp is not None
            assert resp.status_code == 200
            assert resp.get_result().get("result")["id"] == app_id
            assert resp.get_result().get("result").get(
                "edge_ips").get("connectivity") == connectivity

            # update range app
            i = i + 1
            connectivity = connectivities[i % len(connectivities)]
            edge_ips = {
                "type": "dynamic",
                "connectivity": connectivity
            }
            print("updating app with tls", tls)
            resp = self.rapp.update_range_app(app_identifier=app_id, protocol=protocol, dns=dns, origin_direct=origin_direct, origin_port=origin_port,
                                              ip_firewall=ip_firewall, proxy_protocol=proxy_protocol, edge_ips=edge_ips, traffic_type=traffic_type, tls=tls)
            assert resp is not None
            assert resp.status_code == 200
            assert resp.get_result().get("result").get(
                "edge_ips").get("connectivity") == connectivity

            # delete range app
            resp = self.rapp.delete_range_app(app_identifier=app_id)
            assert resp is not None
            assert resp.status_code == 200
            assert resp.get_result().get("result")["id"] == app_id


if __name__ == '__main__':
    unittest.main()
