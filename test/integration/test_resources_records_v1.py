# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.

"""
Integration test code to execute dns records api
"""

import os
import unittest
from ibm_cloud_networking_services import DnsZonesV1
from ibm_cloud_networking_services import ResourceRecordsV1


class TestResourceRecordsV1(unittest.TestCase):
    """The Resourse records V1 service test class."""

    def setUp(self):
        """ test case setup """
        self.instance_id = os.getenv("INSTANCE_ID")
        self.zone_id = ""
        # create zone class object
        self.zone = DnsZonesV1.new_instance(service_name="pdns_services")
        # create resource record service class object
        self.record = ResourceRecordsV1.new_instance(
            service_name="pdns_services")
        self._create_dns_zones()

    def tearDown(self):
        """ tear down """
        # Delete the resources
        self._clean_dns_resource_records()
        print("Clean up complete")

    def _create_dns_zones(self):
        name = "test.example36.com"
        label = "us-south"
        resp = self.zone.create_dnszone(
            instance_id=self.instance_id, name=name, label=label)
        assert resp is not None
        assert resp.status_code == 200
        self.zone_id = resp.get_result().get("id")

    def _clean_dns_resource_records(self):
        # list all dns resource records
        response = self.record.list_resource_records(
            instance_id=self.instance_id, dnszone_id=self.zone_id)
        assert response is not None
        assert response.status_code == 200
        result = response.get_result().get("resource_records")
        for record in result:
            # delete resource record
            self.record.delete_resource_record(
                instance_id=self.instance_id, dnszone_id=self.zone_id, record_id=record.get("id"))

        # delete dns zones
        response = self.zone.list_dnszones(instance_id=self.instance_id)
        assert response is not None
        assert response.status_code == 200
        result = response.get_result().get("dnszones")
        for zone in result:
            self.zone.delete_dnszone(
                instance_id=self.instance_id, dnszone_id=zone.get("id"))

    def test_1_resource_records_actions(self):
        """ DNS record actions """
        record_type = 'A'
        name = 'test.example.com'
        content = '2.2.2.2'
        ttl = 60
        rdata = {
            'ip': content
        }
        # create resource record
        resp = self.record.create_resource_record(
            instance_id=self.instance_id, dnszone_id=self.zone_id, type=record_type, ttl=ttl, name=name, rdata=rdata)
        assert resp is not None
        assert resp.status_code == 200
        record_id = resp.get_result().get("id")

        # update resource record
        name = 'test.example43.com'
        content = '2.2.2.3'
        ttl = 60
        rdata = {
            'ip': content
        }
        resp = self.record.update_resource_record(
            instance_id=self.instance_id, dnszone_id=self.zone_id, record_id=record_id,
            type=record_type, ttl=ttl, name=name, rdata=rdata)
        assert resp is not None
        assert resp.status_code == 200

        # get resource record
        resp = self.record.get_resource_record(
            instance_id=self.instance_id, dnszone_id=self.zone_id, record_id=record_id)
        assert resp is not None
        assert resp.status_code == 200

        # delete resource record
        resp = self.record.delete_resource_record(
            instance_id=self.instance_id, dnszone_id=self.zone_id, record_id=record_id)
        assert resp is not None
        assert resp.status_code == 204

    def test_2_resource_records_actions(self):
        """ DNS record AAAA actions """
        record_type = 'AAAA'
        name = 'test.example.com'
        ttl = 60
        rdata = {
            'ip': '2001::1'
        }
        # create resource record
        resp = self.record.create_resource_record(
            instance_id=self.instance_id, dnszone_id=self.zone_id, type=record_type, ttl=ttl, name=name, rdata=rdata)
        assert resp is not None
        assert resp.status_code == 200
        record_id = resp.get_result().get("id")

        # update resource record
        name = 'test.example43.com'
        ttl = 120
        rdata = {
            'ip': '2002::2'
        }
        resp = self.record.update_resource_record(
            instance_id=self.instance_id, dnszone_id=self.zone_id, record_id=record_id,
            type=record_type, ttl=ttl, name=name, rdata=rdata)
        assert resp is not None
        assert resp.status_code == 200

        # get resource record
        resp = self.record.get_resource_record(
            instance_id=self.instance_id, dnszone_id=self.zone_id, record_id=record_id)
        assert resp is not None
        assert resp.status_code == 200

        # delete resource record
        resp = self.record.delete_resource_record(
            instance_id=self.instance_id, dnszone_id=self.zone_id, record_id=record_id)
        assert resp is not None
        assert resp.status_code == 204

    def test_3_resource_records_actions(self):
        """ DNS record CNAME actions """
        record_type = 'CNAME'
        name = 'test.example56.com'
        ttl = 60
        rdata = {
            'cname': 'test.example56.com'
        }
        # create resource record
        resp = self.record.create_resource_record(
            instance_id=self.instance_id, dnszone_id=self.zone_id, type=record_type, ttl=ttl, name=name, rdata=rdata)
        assert resp is not None
        assert resp.status_code == 200
        record_id = resp.get_result().get("id")

        # update resource record
        name = 'test.example43.com'
        ttl = 120
        rdata = {
            'cname': 'test.example43.com'
        }
        resp = self.record.update_resource_record(
            instance_id=self.instance_id, dnszone_id=self.zone_id, record_id=record_id,
            type=record_type, ttl=ttl, name=name, rdata=rdata)
        assert resp is not None
        assert resp.status_code == 200

        # get resource record
        resp = self.record.get_resource_record(
            instance_id=self.instance_id, dnszone_id=self.zone_id, record_id=record_id)
        assert resp is not None
        assert resp.status_code == 200

        # delete resource record
        resp = self.record.delete_resource_record(
            instance_id=self.instance_id, dnszone_id=self.zone_id, record_id=record_id)
        assert resp is not None
        assert resp.status_code == 204

    def test_4_resource_records_actions(self):
        """ DNS record MX actions """
        record_type = 'MX'
        name = 'test.example76.com'
        ttl = 60
        rdata = {
            'exchange': 'mail.test.example76.com',
            'preference': 256
        }
        # create resource record
        resp = self.record.create_resource_record(
            instance_id=self.instance_id, dnszone_id=self.zone_id, type=record_type, ttl=ttl, name=name, rdata=rdata)
        assert resp is not None
        assert resp.status_code == 200
        record_id = resp.get_result().get("id")

        # update resource record
        name = 'test.example43.com'
        ttl = 120
        rdata = {
            'exchange': 'mail.test.example43.com',
            'preference': 256
        }
        resp = self.record.update_resource_record(
            instance_id=self.instance_id, dnszone_id=self.zone_id, record_id=record_id,
            type=record_type, ttl=ttl, name=name, rdata=rdata)
        assert resp is not None
        assert resp.status_code == 200

        # get resource record
        resp = self.record.get_resource_record(
            instance_id=self.instance_id, dnszone_id=self.zone_id, record_id=record_id)
        assert resp is not None
        assert resp.status_code == 200

        # delete resource record
        resp = self.record.delete_resource_record(
            instance_id=self.instance_id, dnszone_id=self.zone_id, record_id=record_id)
        assert resp is not None
        assert resp.status_code == 204

    def test_5_resource_records_actions(self):
        """ DNS record SRV actions """
        record_type = 'SRV'
        name = 'test.example76.com'
        ttl = 60
        rdata = {
            "priority": 100,
            "weight": 100,
            "port": 8000,
            "target": "test.example76.com"
        }
        service_name = "_sip"
        protocol = "udp"
        # create resource record
        resp = self.record.create_resource_record(
            instance_id=self.instance_id, dnszone_id=self.zone_id, type=record_type,
            ttl=ttl, name=name, rdata=rdata, service=service_name, protocol=protocol)
        assert resp is not None
        assert resp.status_code == 200
        record_id = resp.get_result().get("id")

        # update resource record
        name = 'test.example43.com'
        ttl = 120
        rdata = {
            "priority": 200,
            "weight": 200,
            "port": 8001,
            "target": "test.example43.com"
        }
        service_name = "_sip"
        protocol = "tcp"
        resp = self.record.update_resource_record(
            instance_id=self.instance_id, dnszone_id=self.zone_id, record_id=record_id,
            type=record_type, ttl=ttl, name=name, rdata=rdata, service=service_name, protocol=protocol)
        assert resp is not None
        assert resp.status_code == 200

        # get resource record
        resp = self.record.get_resource_record(
            instance_id=self.instance_id, dnszone_id=self.zone_id, record_id=record_id)
        assert resp is not None
        assert resp.status_code == 200

        # delete resource record
        resp = self.record.delete_resource_record(
            instance_id=self.instance_id, dnszone_id=self.zone_id, record_id=record_id)
        assert resp is not None
        assert resp.status_code == 204

    def test_6_resource_records_actions(self):
        """ DNS record PTR actions """

        record_type = 'A'
        name = 'example76'
        content = '2.2.2.2'
        ttl = 60
        rdata = {
            'ip': content
        }
        # create resource record
        resp = self.record.create_resource_record(
            instance_id=self.instance_id, dnszone_id=self.zone_id, type=record_type, ttl=ttl, name=name, rdata=rdata)
        assert resp is not None
        assert resp.status_code == 200

        record_type = 'A'
        name = 'example43'
        content = '2.2.2.3'
        ttl = 60
        rdata = {
            'ip': content
        }
        # create resource record
        resp = self.record.create_resource_record(
            instance_id=self.instance_id, dnszone_id=self.zone_id, type=record_type, ttl=ttl, name=name, rdata=rdata)
        assert resp is not None
        assert resp.status_code == 200

        record_type = 'PTR'
        name = '2.2.2.2'
        ttl = 60
        rdata = {
            "ptrdname": "example76.test.example36.com"
        }
        # create resource record
        resp = self.record.create_resource_record(
            instance_id=self.instance_id, dnszone_id=self.zone_id, type=record_type,
            ttl=ttl, rdata=rdata, name=name)
        assert resp is not None
        assert resp.status_code == 200
        record_id = resp.get_result().get("id")

        # update resource record
        ttl = 120
        resp = self.record.update_resource_record(
            instance_id=self.instance_id, dnszone_id=self.zone_id, record_id=record_id, ttl=ttl)
        assert resp is not None
        assert resp.status_code == 200

        # get resource record
        resp = self.record.get_resource_record(
            instance_id=self.instance_id, dnszone_id=self.zone_id, record_id=record_id)
        assert resp is not None
        assert resp.status_code == 200

        # delete resource record
        resp = self.record.delete_resource_record(
            instance_id=self.instance_id, dnszone_id=self.zone_id, record_id=record_id)
        assert resp is not None
        assert resp.status_code == 204

    def test_7_resource_records_actions(self):
        """ DNS record TXT actions """
        record_type = 'TXT'
        name = 'test.example76.com'
        ttl = 60
        rdata = {
            'text': 'this a text record'
        }
        # create resource record
        resp = self.record.create_resource_record(
            instance_id=self.instance_id, dnszone_id=self.zone_id, type=record_type,
            ttl=ttl, name=name, rdata=rdata)
        assert resp is not None
        assert resp.status_code == 200
        record_id = resp.get_result().get("id")

        # update resource record
        name = 'test.example43.com'
        ttl = 120
        rdata = {
            'text': 'this a text record update'
        }
        resp = self.record.update_resource_record(
            instance_id=self.instance_id, dnszone_id=self.zone_id, record_id=record_id,
            type=record_type, ttl=ttl, name=name, rdata=rdata)
        assert resp is not None
        assert resp.status_code == 200

        # get resource record
        resp = self.record.get_resource_record(
            instance_id=self.instance_id, dnszone_id=self.zone_id, record_id=record_id)
        assert resp is not None
        assert resp.status_code == 200

        # delete resource record
        resp = self.record.delete_resource_record(
            instance_id=self.instance_id, dnszone_id=self.zone_id, record_id=record_id)
        assert resp is not None
        assert resp.status_code == 204


if __name__ == '__main__':
    unittest.main()
