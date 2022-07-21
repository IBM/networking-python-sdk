# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.

"""
Integration test code to execute dns zones
"""

import os
import unittest
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_networking_services.dns_svcs_v1 import DnsSvcsV1
from dotenv import load_dotenv, find_dotenv

configFile = "pdns.env"
# load the .env file containing your environment variables
try:
    load_dotenv(find_dotenv(filename=configFile))
except:
    raise unittest.SkipTest('no dns.env file loaded, skipping...')

class TestDNSSvcsV1(unittest.TestCase):
    """The DNS V1 service test class."""
    # @unittest.skip("skipping")  
    def setUp(self):
        """ test case setup """
        if not os.path.exists(configFile):
            raise unittest.SkipTest('External configuration not available, skipping...')
        self.instance_id = os.getenv("DNS_SVCS_INSTANCE_ID")
        # create zone class object
        self.zone = DnsSvcsV1.new_instance(service_name="dns_svcs")
        # Delete the resources
        self._clean_dns_zones()

    def tearDown(self):
        """ tear down """
        # Delete the resources
        self._clean_dns_zones()
        print("Clean up complete")

    def _clean_dns_zones(self):
        response = self.zone.list_dnszones(instance_id=self.instance_id)
        assert response is not None
        assert response.status_code == 200
        result = response.get_result()
        if result is not None:
            zones = result.get("dnszones")
            for zone in zones:
                self.zone.delete_dnszone(
                    instance_id=self.instance_id, dnszone_id=zone.get("id"))

    def test_1_pdns_zone_action(self):
        """ test private dns zone create/delete/update/get functionality """
        name = "test.example36.com"
        label = "us-south"
        resp = self.zone.list_dnszones(instance_id=self.instance_id)
        assert resp is not None
        assert resp.status_code == 200

        # create dns zone
        resp = self.zone.create_dnszone(
            instance_id=self.instance_id, name=name, label=label)
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("instance_id") == self.instance_id
        assert resp.get_result().get("name") == name
        assert resp.get_result().get("label") == label
        zone_id = resp.get_result().get("id")

        # get dns zone
        resp = self.zone.get_dnszone(
            instance_id=self.instance_id, dnszone_id=zone_id)
        assert resp.status_code == 200
        assert resp.get_result().get("instance_id") == self.instance_id
        assert resp.get_result().get("name") == name
        assert resp.get_result().get("label") == label

        # update dns zone
        label = "us-south-1"
        desc = "test instance"
        resp = self.zone.update_dnszone(
            instance_id=self.instance_id, dnszone_id=zone_id, description=desc, label=label)
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("instance_id") == self.instance_id
        assert resp.get_result().get("name") == name
        assert resp.get_result().get("label") == label
        assert resp.get_result().get("description") == desc

        # delete dns zone
        resp = self.zone.delete_dnszone(
            instance_id=self.instance_id, dnszone_id=zone_id)
        assert resp is not None
        assert resp.status_code == 204

    def test_1_pdns_zone_list(self):
        """ test private dns zone list functionality """

        name = "test.example34.com"
        label = "us-south"
        # create dns zone
        resp = self.zone.create_dnszone(
            instance_id=self.instance_id, name=name, label=label)
        assert resp is not None
        assert resp.status_code == 200

        name = "test.example35.com"
        # create dns zone
        resp = self.zone.create_dnszone(
            instance_id=self.instance_id, name=name, label=label)
        assert resp is not None
        assert resp.status_code == 200

        name = "test.example36.com"
        # create dns zone
        resp = self.zone.create_dnszone(
            instance_id=self.instance_id, name=name, label=label)
        assert resp is not None
        assert resp.status_code == 200

        name = "test.example37.com"
        # create dns zone
        resp = self.zone.create_dnszone(
            instance_id=self.instance_id, name=name, label=label)
        assert resp is not None
        assert resp.status_code == 200

        resp = self.zone.list_dnszones(
            instance_id=self.instance_id, offset=1, limit=2)
        assert resp is not None
        assert resp.status_code == 200

    def test_1_pdns_zone_negative(self):
        name = "test.example36.com"
        label = "us-south"
        instance_id = None
        with self.assertRaises(ValueError) as val:
            self.zone.create_dnszone(instance_id=instance_id,
                                     name=name, label=label)
            self.assertEqual(val.exception.msg, 'instance_id must be provided')
        desc = "this is a test"
        dnszone_id = "123456"
        with self.assertRaises(ValueError) as val:
            self.zone.update_dnszone(instance_id=instance_id,
                                     dnszone_id=dnszone_id, description=desc, label=label)
            self.assertEqual(val.exception.msg, 'instance_id must be provided')
        instance_id = "123456"
        dnszone_id = None
        with self.assertRaises(ValueError) as val:
            self.zone.update_dnszone(instance_id=instance_id,
                                     dnszone_id=dnszone_id, description=desc, label=label)
            self.assertEqual(val.exception.msg, 'dnszone_id must be provided')

        instance_id = None
        dnszone_id = "123456"
        with self.assertRaises(ValueError) as val:
            self.zone.delete_dnszone(instance_id=instance_id,
                                     dnszone_id=dnszone_id)
            self.assertEqual(val.exception.msg, 'instance_id must be provided')
        instance_id = "123545"
        dnszone_id = None
        with self.assertRaises(ValueError) as val:
            self.zone.delete_dnszone(instance_id=instance_id,
                                     dnszone_id=dnszone_id)
            self.assertEqual(val.exception.msg, 'dnszone_id must be provided')

        instance_id = None
        dnszone_id = "123456"
        with self.assertRaises(ValueError) as val:
            self.zone.get_dnszone(instance_id=instance_id,
                                  dnszone_id=dnszone_id)
            self.assertEqual(val.exception.msg, 'instance_id must be provided')
        instance_id = "123545"
        dnszone_id = None
        with self.assertRaises(ValueError) as val:
            self.zone.get_dnszone(instance_id=instance_id,
                                  dnszone_id=dnszone_id)
            self.assertEqual(val.exception.msg, 'dnszone_id must be provided')

        instance_id = None
        with self.assertRaises(ValueError) as val:
            self.zone.list_dnszones(instance_id=instance_id)
            self.assertEqual(val.exception.msg, 'instance_id must be provided')


class TestResourceRecordsV1(unittest.TestCase):
    """The Resourse records V1 service test class."""
    # @unittest.skip("skipping")
    def setUp(self):
        """ test case setup """
        if not os.path.exists(configFile):
            raise unittest.SkipTest(
                'External configuration not available, skipping...')
        self.instance_id = os.getenv("DNS_SVCS_INSTANCE_ID")
        self.zone_id = ""
        # create zone class object
        self.zone = DnsSvcsV1.new_instance(service_name="dns_svcs")
        # create resource record service class object
        self.record = DnsSvcsV1.new_instance(
            service_name="dns_svcs")
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
            ttl=ttl, name=name, rdata=rdata)
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
            ttl=ttl, name=name, rdata=rdata)
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
            ttl=ttl, name=name, rdata=rdata)
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
            ttl=ttl, name=name, rdata=rdata)
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
            ttl=ttl, name=name, rdata=rdata, service=service_name, protocol=protocol)
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
            ttl=ttl, name=name, rdata=rdata)
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

    def test_8_import_resource_records_actions(self):
        """ DNS record import actions """
        """ Write a DSN record into tmp file """
        wFile = open("/tmp/records.txt", "w+")
        wFile.write("example.sdk.cistest-load.com. 1 IN A 1.1.1.1")
        wFile.close()
        f = open("/tmp/records.txt", "rb")
        file_content_type = 'testString'
        x_correlation_id = 'testString'
        headers = {}
        resp = self.record.import_resource_records(instance_id=self.instance_id, dnszone_id=self.zone_id,
                                                   file=f, file_content_type=file_content_type,x_correlation_id=x_correlation_id, headers=headers)
        f.close()
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("total_records_parsed") == 1
        try:
            os.remove("/tmp/records.txt")
        except:
            pass

    def test_9_export_resource_records_actions(self):
        """ DNS record import actions """
        """ Create resource record to export """
        record_type = 'TXT'
        name = 'test.example76.com'
        ttl = 60
        rdata = {
            'text': 'this a text record'
        }
        resp = self.record.create_resource_record(instance_id=self.instance_id, dnszone_id=self.zone_id, type=record_type,
                ttl=ttl, name=name, rdata=rdata)
        assert resp is not None
        assert resp.status_code == 200

        resp = self.record.export_resource_records(instance_id=self.instance_id, dnszone_id=self.zone_id, x_correlation_id="test")
        assert resp is not None
        assert resp.status_code == 200


    def test_1_resource_records_negative(self):
        instance_id = None
        dnszone_id = "123456"
        with self.assertRaises(ValueError) as val:
            self.record.create_resource_record(instance_id=instance_id,
                                               dnszone_id=dnszone_id)
            self.assertEqual(val.exception.msg, 'instance_id must be provided')
        instance_id = "123456"
        dnszone_id = None
        with self.assertRaises(ValueError) as val:
            self.record.create_resource_record(instance_id=instance_id,
                                               dnszone_id=dnszone_id)
            self.assertEqual(val.exception.msg, 'dnszone_id must be provided')

        instance_id = None
        dnszone_id = "123456"
        with self.assertRaises(ValueError) as val:
            self.record.update_resource_record(instance_id=instance_id,
                                               dnszone_id=dnszone_id, record_id=None)
            self.assertEqual(val.exception.msg, 'instance_id must be provided')
        instance_id = "123456"
        dnszone_id = None
        with self.assertRaises(ValueError) as val:
            self.record.update_resource_record(instance_id=instance_id,
                                               dnszone_id=dnszone_id, record_id=None)
            self.assertEqual(val.exception.msg, 'dnszone_id must be provided')

        instance_id = "123456"
        dnszone_id = "12345"
        with self.assertRaises(ValueError) as val:
            self.record.update_resource_record(instance_id=instance_id,
                                               dnszone_id=dnszone_id, record_id=None)
            self.assertEqual(val.exception.msg, 'record_id must be provided')

        instance_id = None
        dnszone_id = "123456"
        with self.assertRaises(ValueError) as val:
            self.record.delete_resource_record(instance_id=instance_id,
                                               dnszone_id=dnszone_id, record_id=None)
            self.assertEqual(val.exception.msg, 'instance_id must be provided')
        instance_id = "123456"
        dnszone_id = None
        with self.assertRaises(ValueError) as val:
            self.record.delete_resource_record(instance_id=instance_id,
                                               dnszone_id=dnszone_id, record_id=None)
            self.assertEqual(val.exception.msg, 'dnszone_id must be provided')
        instance_id = "123456"
        dnszone_id = "12345"
        with self.assertRaises(ValueError) as val:
            self.record.delete_resource_record(instance_id=instance_id,
                                               dnszone_id=dnszone_id, record_id=None)
            self.assertEqual(val.exception.msg, 'record_id must be provided')

        instance_id = None
        dnszone_id = "123456"
        with self.assertRaises(ValueError) as val:
            self.record.get_resource_record(instance_id=instance_id,
                                            dnszone_id=dnszone_id, record_id=None)
            self.assertEqual(val.exception.msg, 'instance_id must be provided')
        instance_id = "123456"
        dnszone_id = None
        with self.assertRaises(ValueError) as val:
            self.record.get_resource_record(instance_id=instance_id,
                                            dnszone_id=dnszone_id, record_id=None)
            self.assertEqual(val.exception.msg, 'dnszone_id must be provided')
        instance_id = "123456"
        dnszone_id = "12345"
        with self.assertRaises(ValueError) as val:
            self.record.get_resource_record(instance_id=instance_id,
                                            dnszone_id=dnszone_id, record_id=None)
            self.assertEqual(val.exception.msg, 'record_id must be provided')

        instance_id = None
        dnszone_id = "123456"
        with self.assertRaises(ValueError) as val:
            self.record.list_resource_records(instance_id=instance_id,
                                              dnszone_id=dnszone_id)
            self.assertEqual(val.exception.msg, 'instance_id must be provided')
        instance_id = "123456"
        dnszone_id = None
        with self.assertRaises(ValueError) as val:
            self.record.list_resource_records(instance_id=instance_id,
                                              dnszone_id=dnszone_id)
            self.assertEqual(val.exception.msg, 'dnszone_id must be provided')

        instance_id = "123456"
        dnszone_id = None
        with self.assertRaises(ValueError) as val:
            self.record.import_resource_records(instance_id=instance_id,
                                                  dnszone_id=dnszone_id)
            self.assertEqual(val.exception.msg, 'dnszone_id must be provided')

        instance_id = None
        dnszone_id = "123456"
        with self.assertRaises(ValueError) as val:
            self.record.import_resource_records(instance_id=instance_id,
                                              dnszone_id=dnszone_id)
            self.assertEqual(val.exception.msg, 'instance_id must be provided')
        instance_id = "123456"
        dnszone_id = None
        with self.assertRaises(ValueError) as val:
            self.record.export_resource_records(instance_id=instance_id,
                                                dnszone_id=dnszone_id)
            self.assertEqual(val.exception.msg, 'dnszone_id must be provided')
        instance_id = None
        dnszone_id = "123456"
        with self.assertRaises(ValueError) as val:
            self.record.export_resource_records(instance_id=instance_id,
                                                dnszone_id=dnszone_id)
            self.assertEqual(val.exception.msg, 'instance_id must be provided')
class TestPermittedNetworksForDnsZonesV1(unittest.TestCase):
    """The Permitted Networks for DNS V1 service test class."""
    # @unittest.skip("skipping")
    def setUp(self):
        """ test case setup """
        if not os.path.exists(configFile):
            raise unittest.SkipTest(
                'External configuration not available, skipping...')
        self.instance_id = os.getenv("DNS_SVCS_INSTANCE_ID")
        self.vpc_crn = os.getenv("DNS_SVCS_VPC_CRN")
        self.zone_id = ""
        # create zone class object
        self.zone = DnsSvcsV1.new_instance(service_name="dns_svcs")
        self._create_dns_zones()
        # create permitted nework class object
        self.nw = DnsSvcsV1.new_instance(
            service_name="dns_svcs")

    def tearDown(self):
        """ tear down """
        # Delete the resources
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
        # delete dns zones
        response = self.zone.list_dnszones(instance_id=self.instance_id)
        assert response is not None
        assert response.status_code == 200
        result = response.get_result().get("dnszones")
        for zone in result:
            self.zone.delete_dnszone(
                instance_id=self.instance_id, dnszone_id=zone.get("id"))

    def test_1_permitted_network_actions(self):
        """ test pdns permitted network """
        pnw = {
            'vpc_crn': self.vpc_crn
        }
        # permit = [pnw]
        resp = self.nw.create_permitted_network(
            instance_id=self.instance_id, dnszone_id=self.zone_id, type='vpc', permitted_network=pnw)
        assert resp is not None
        assert resp.status_code == 200
        network_id = resp.get_result().get("id")

        resp = self.nw.get_permitted_network(
            instance_id=self.instance_id, dnszone_id=self.zone_id, permitted_network_id=network_id)
        assert resp is not None
        assert resp.status_code == 200

        resp = self.nw.list_permitted_networks(
            instance_id=self.instance_id, dnszone_id=self.zone_id)
        assert resp is not None
        assert resp.status_code == 200

        resp = self.nw.delete_permitted_network(
            instance_id=self.instance_id, dnszone_id=self.zone_id, permitted_network_id=network_id)
        assert resp is not None
        assert resp.status_code == 202

    def test_1_permitted_network_negative(self):
        instance_id = None
        dnszone_id = "123456"
        with self.assertRaises(ValueError) as val:
            self.nw.create_permitted_network(instance_id=instance_id,
                                             dnszone_id=dnszone_id)
            self.assertEqual(val.exception.msg, 'instance_id must be provided')
        instance_id = "123456"
        dnszone_id = None
        with self.assertRaises(ValueError) as val:
            self.nw.create_permitted_network(instance_id=instance_id,
                                             dnszone_id=dnszone_id)
            self.assertEqual(val.exception.msg, 'dnszone_id must be provided')

        instance_id = None
        dnszone_id = "123456"
        with self.assertRaises(ValueError) as val:
            self.nw.delete_permitted_network(instance_id=instance_id,
                                             dnszone_id=dnszone_id, permitted_network_id=None)
            self.assertEqual(val.exception.msg, 'instance_id must be provided')
        instance_id = "123456"
        dnszone_id = None
        with self.assertRaises(ValueError) as val:
            self.nw.delete_permitted_network(instance_id=instance_id,
                                             dnszone_id=dnszone_id, permitted_network_id=None)
            self.assertEqual(val.exception.msg, 'dnszone_id must be provided')

        instance_id = None
        dnszone_id = "123456"
        with self.assertRaises(ValueError) as val:
            self.nw.get_permitted_network(instance_id=instance_id,
                                          dnszone_id=dnszone_id, permitted_network_id=None)
            self.assertEqual(val.exception.msg, 'instance_id must be provided')
        instance_id = "123456"
        dnszone_id = None
        with self.assertRaises(ValueError) as val:
            self.nw.get_permitted_network(instance_id=instance_id,
                                          dnszone_id=dnszone_id, permitted_network_id=None)
            self.assertEqual(val.exception.msg, 'dnszone_id must be provided')

        instance_id = None
        dnszone_id = "123456"
        with self.assertRaises(ValueError) as val:
            self.nw.list_permitted_networks(instance_id=instance_id,
                                            dnszone_id=dnszone_id)
            self.assertEqual(val.exception.msg, 'instance_id must be provided')
        instance_id = "123456"
        dnszone_id = None
        with self.assertRaises(ValueError) as val:
            self.nw.list_permitted_networks(instance_id=instance_id,
                                            dnszone_id=dnszone_id)
            self.assertEqual(val.exception.msg, 'dnszone_id must be provided')


class TestGlobalLoadBalancersV1 (unittest.TestCase):
    
    """The Global Load Balancers for DNS V1 service test class."""
    # @unittest.skip("skipping")
    def setUp(self):
        """ test case setup """

        if not os.path.exists(configFile):
            raise unittest.SkipTest(
                'External configuration not available, skipping...')

        self.instance_id = os.getenv("DNS_SVCS_INSTANCE_ID")
        self.vpc_crn = os.getenv("DNS_SVCS_VPC_CRN")
        self.subnet_crn = os.getenv("DNS_SVCS_SUBNET_CRN")
        self.zone_id = ""

        # create zone class object
        self.zone = DnsSvcsV1.new_instance(service_name="dns_svcs")

        # create global load balancers record class object
        self.globalLoadBalancers = DnsSvcsV1.new_instance(
            service_name="dns_svcs")
        self._create_dns_zones()

    def tearDown(self):
        """ tear down """
        # Delete Global load balancers
        self._clean_dns_globalloadbalancers()
        print("Clean up complete")

    def _create_dns_zones(self):
        name = "test.example36.com"
        label = "us-south"
        resp = self.zone.create_dnszone(
            instance_id=self.instance_id, name=name, label=label)
        assert resp is not None
        assert resp.status_code == 200
        self.zone_id = resp.get_result().get("id")

    def _clean_dns_globalloadbalancers(self):
        # delete all dns Load Balancer
        response = self.globalLoadBalancers.list_load_balancers(
            instance_id=self.instance_id, dnszone_id=self.zone_id)
        assert response is not None
        assert response.status_code == 200
        loadbalancers = {}
        loadbalancers = response.get_result().get("load_balancers")
        for loadbalancer in loadbalancers:
            self.globalLoadBalancers.delete_load_balancer(
                instance_id=self.instance_id, dnszone_id=self.zone_id, lb_id=loadbalancer.get("id"))
            assert response is not None
        # delete all dns Pools
        response = self.globalLoadBalancers.list_pools(
            instance_id=self.instance_id)
        assert response is not None
        assert response.status_code == 200
        pools = {}
        pools = response.get_result().get("pools")
        for pool in pools:
            self.globalLoadBalancers.delete_pool(
                instance_id=self.instance_id, pool_id=pool.get("id"))
            assert response is not None
        # delete all dns Monitors
        response = self.globalLoadBalancers.list_monitors(
            instance_id=self.instance_id)
        assert response is not None
        assert response.status_code == 200
        monitors = {}
        monitors = response.get_result().get("monitors")
        for monitor in monitors:
            self.globalLoadBalancers.delete_monitor(
                instance_id=self.instance_id, monitor_id=monitor.get("id"))
            assert response is not None
        # delete dns zones
        response = self.zone.list_dnszones(instance_id=self.instance_id)
        assert response is not None
        assert response.status_code == 200
        result = response.get_result().get("dnszones")
        for zone in result:
            self.zone.delete_dnszone(
                instance_id=self.instance_id, dnszone_id=zone.get("id"))

    ################## global load balancers integration test cases ##################
    # @unittest.skip('skipping...')
    def test_1_dns_globalloadbalancers(self):
        """ create,get,update,delete GLB monitor """

        name = 'testmonitor1'
        lbtype = 'HTTP'
        description = 'Creating testmonitor1'
        port = 8080
        interval = 60
        retries = 2
        timeout = 5
        method = 'GET'
        path = "helth"
        header = {"Host": ["example.com"], "X-App-ID": ["abc123"]}
        allow_insecure = True
        expected_body = "alive"
        # Create monitor
        response = self.globalLoadBalancers.create_monitor(
            instance_id=self.instance_id, name=name, type=lbtype, description=description, port=port, interval=interval, retries=retries, timeout=timeout)
        assert response is not None
        assert response.status_code == 200
        self.monitor_id = response.get_result().get("id")
        assert name == response.get_result().get("name")
        assert lbtype == response.get_result().get("type")
        assert description == response.get_result().get("description")
        assert interval == response.get_result().get("interval")
        # Get monitor
        response = self.globalLoadBalancers.get_monitor(
            instance_id=self.instance_id, monitor_id=self.monitor_id)
        assert response is not None
        assert response.status_code == 200

        # Update monitor
        lbtype = 'HTTPS'
        description = 'Updating testmonitor1'
        interval = 70
        timeout = 10
        response = self.globalLoadBalancers.update_monitor(
            instance_id=self.instance_id, monitor_id=self.monitor_id, type=lbtype, description=description, interval=interval, timeout=timeout)
        assert response is not None
        assert response.status_code == 200
        assert lbtype == response.get_result().get("type")
        assert description == response.get_result().get("description")

        """ createcreate,get,update,delete  GLB Pool """

        # Create Pools
        name = "testPool"
        origins = [{"name": "app-server-1",
                    "address": "10.10.10.8", "enabled": True}]
        description = "create testpool"
        enabled = True
        healthy_origins_threshold = 1
        subnets = []
        subnets.append(self.subnet_crn)
        response = self.globalLoadBalancers.create_pool(instance_id=self.instance_id, name=name, origins=origins,
                                                        description=description, enabled=enabled,
                                                        healthy_origins_threshold=healthy_origins_threshold,
                                                        monitor=self.monitor_id, healthcheck_region='us-south',
                                                        healthcheck_subnets=subnets)
        assert response is not None
        assert response.status_code == 200
        self.pool_id = response.get_result().get("id")
        assert name == response.get_result().get("name")
        assert description == response.get_result().get("description")
        assert enabled == response.get_result().get("enabled")
        assert healthy_origins_threshold == response.get_result().get(
            "healthy_origins_threshold")
        # GET pool
        response = self.globalLoadBalancers.get_pool(
            instance_id=self.instance_id, pool_id=self.pool_id)
        assert response is not None
        assert response.status_code == 200
        assert response.get_result().get("healthcheck_subnets")[
            0] == self.subnet_crn
        assert response.get_result().get("healthcheck_vsis")[
            0].get("subnet") == self.subnet_crn
        assert response.get_result().get("healthcheck_vsis")[
            0].get("vpc") == self.vpc_crn

        # Update pool
        name = "updatetestPool"
        description = "update testpool"
        response = self.globalLoadBalancers.update_pool(
            instance_id=self.instance_id, pool_id=self.pool_id, name=name, description=description,
            healthcheck_region='us-south', monitor=self.monitor_id, healthcheck_subnets=subnets)
        assert response is not None
        assert response.status_code == 200
        assert name == response.get_result().get("name")
        assert description == response.get_result().get("description")
        assert response.get_result().get("healthcheck_subnets")[
            0] == self.subnet_crn
        assert response.get_result().get("healthcheck_vsis")[
            0].get("subnet") == self.subnet_crn
        assert response.get_result().get("healthcheck_vsis")[
            0].get("vpc") == self.vpc_crn

        """ create,get,update,list,delete GLB LB """

        name = 'testloadbalancer'
        description = 'Creating testloadbalancer'
        default_pools = [self.pool_id]
        enabled = True
        ttl = 120
        # Create Load balancer
        response = self.globalLoadBalancers.create_load_balancer(instance_id=self.instance_id, dnszone_id=self.zone_id, name=name,
                                                                 fallback_pool=self.pool_id, default_pools=default_pools, description=description, enabled=enabled, ttl=ttl)
        assert response is not None
        assert response.status_code == 200
        self.loadbalancer_id = response.get_result().get("id")
        assert description == response.get_result().get("description")
        assert enabled == response.get_result().get("enabled")
        assert ttl == response.get_result().get("ttl")
        # GET Load balancer
        response = self.globalLoadBalancers.get_load_balancer(
            instance_id=self.instance_id, dnszone_id=self.zone_id, lb_id=self.loadbalancer_id)
        assert response is not None
        assert response.status_code == 200
        # Update Load balancer
        name = "updatetestLoadbalancer"
        description = "update testLoadbalancer"
        response = self.globalLoadBalancers.update_load_balancer(
            instance_id=self.instance_id, dnszone_id=self.zone_id, lb_id=self.loadbalancer_id, name=name, description=description)
        assert response is not None
        assert response.status_code == 200
        assert description == response.get_result().get("description")
        # List Load balancer
        response = self.globalLoadBalancers.list_load_balancers(
            instance_id=self.instance_id, dnszone_id=self.zone_id)
        assert response is not None
        assert response.status_code == 200

        # Delete Load balancer/Pool/Monitor
        response = self.globalLoadBalancers.delete_load_balancer(
            instance_id=self.instance_id, dnszone_id=self.zone_id, lb_id=self.loadbalancer_id)
        assert response is not None
        assert response.status_code == 204
        response = self.globalLoadBalancers.delete_pool(
            instance_id=self.instance_id, pool_id=self.pool_id)
        assert response is not None
        assert response.status_code == 204
        response = self.globalLoadBalancers.delete_monitor(
            instance_id=self.instance_id, monitor_id=self.monitor_id)
        assert response is not None
        assert response.status_code == 204

    def test_2_list_dns_globalloadbalancers(self):

        # List monitor
        for i in range(3):
            name = 'testmonitor'+str(i)
            lbtype = 'HTTP'
            description = 'Creating testmonitor '+str(i)
            response = self.globalLoadBalancers.create_monitor(
                instance_id=self.instance_id, name=name, type=lbtype, description=description)
            assert response is not None
            assert response.status_code == 200
        response = self.globalLoadBalancers.list_monitors(
            instance_id=self.instance_id)
        assert response is not None
        assert response.status_code == 200

        # List Pools
        for i in range(3):
            name = "testPool"+str(i)
            origins = [{"name": "app-server-"+str(i),
                        "address": "10.10.10.8", "enabled": True}]
            description = "create testpool"+str(i)
            enabled = True
            healthy_origins_threshold = 1
            response = self.globalLoadBalancers.create_pool(
                instance_id=self.instance_id, name=name, origins=origins, description=description, enabled=enabled, healthy_origins_threshold=healthy_origins_threshold)
            assert response is not None
            assert response.status_code == 200
        response = self.globalLoadBalancers.list_pools(
            instance_id=self.instance_id)
        assert response is not None
        assert response.status_code == 200

class TestCustomResolversV1(unittest.TestCase):
    """Custom Resolvers for DNS V1 service test class."""

    
    def setUp(self):
        """ test case setup """
        if not os.path.exists(configFile):
            raise unittest.SkipTest('External configuration not available, skipping...')
        self.instance_id = os.getenv("DNS_SVCS_INSTANCE_ID")
        self.subnet_crn = os.getenv("DNS_SVCS_SUBNET_CRN")
        self.subnet_crn_location = os.getenv("DNS_SVCS_CUSTOMER_LOCATION_SUBNET_CRN")

        # Create Custom Resolver class object
        self.cr = DnsSvcsV1.new_instance(service_name="dns_svcs")

    def tearDown(self):
        """ tear down """
        # Delete the resources
        self._clean_dns_custom_resolver()
        print("Clean up complete")

    def _clean_dns_custom_resolver(self):
        # Delete Custom Resolver
        response = self.cr.list_custom_resolvers(instance_id=self.instance_id)
        assert response is not None
        assert response.status_code == 200
        result = response.get_result().get("custom_resolvers")
        for crs in result:
            self.cr.delete_custom_resolver(instance_id=self.instance_id, resolver_id=crs.get("id"))
        
    def test_1_dns_customresolvers(self):
        """ create,get,update,list Custom Resolvers """

        name = 'testcustomresolvers'
        description = "Creating Custom Resolvers"
        location_input_model = {}
        location_input_model['subnet_crn'] = self.subnet_crn_location
        location_input_model['enabled'] = False
        resp = self.cr.create_custom_resolver(instance_id=self.instance_id, name=name,
                                              locations = [location_input_model],description=description)

        assert resp is not None
        assert resp.status_code == 200
        resolver_id = resp.get_result().get("id")
        locations = resp.get_result().get("locations")

        # Get Custom Resolver
        resp = self.cr.get_custom_resolver(instance_id=self.instance_id, resolver_id=resolver_id)
        assert resp is not None
        assert resp.status_code == 200

        # Update Custom Resolver
        name = 'updatecustomresolvers'
        description = "Updating Custom Resolvers"
        resp = self.cr.update_custom_resolver(instance_id=self.instance_id, resolver_id=resolver_id, 
                                              name=name, description=description)
        assert resp is not None
        assert resp.status_code == 200

        # Update location order of Custom Resolver
        resp = self.cr.update_cr_locations_order(instance_id=self.instance_id, resolver_id=resolver_id, 
                                              locations=[locations[0]['id']])
        assert resp is not None
        assert resp.status_code == 200

        # List Custom Resolver
        resp = self.cr.list_custom_resolvers(instance_id=self.instance_id)
        assert resp is not None
        assert resp.status_code == 200

        """ add,update,Custom Resolver Locations """
        # Add Custom Resolver Locations
        resp = self.cr.add_custom_resolver_location(instance_id=self.instance_id, resolver_id=resolver_id,
                                                    subnet_crn=self.subnet_crn_location, enabled=True)
        assert resp is not None
        assert resp.status_code == 200
        location_id = resp.get_result().get("id")


        # Update Custom Resolver Locations
        resp = self.cr.update_custom_resolver_location(instance_id=self.instance_id, resolver_id=resolver_id,
                                                       location_id=location_id, enabled=False)
        assert resp is not None
        assert resp.status_code == 200

        """ create,get,update,list Forwarding rules """
        # Create Forwarding rules
        type1 = 'zone'
        match = "test.example.com"
        forward_to = ["168.20.22.122"]
        resp = self.cr.create_forwarding_rule(instance_id=self.instance_id, resolver_id=resolver_id,
                                              type=type1, match=match, forward_to=forward_to)
        assert resp is not None
        assert resp.status_code == 200
        rule_id = resp.get_result().get("id")

        # Get Forwarding rules
        resp = self.cr.get_forwarding_rule(instance_id=self.instance_id, resolver_id=resolver_id, rule_id=rule_id)
        assert resp is not None
        assert resp.status_code == 200

        # Update Forwarding rules 
        description = "Updating Forwarding rules"
        match = "test.updateexample.com"
        forward_to = ["168.20.22.122", "190.20.22.134"]

        resp = self.cr.update_forwarding_rule(instance_id=self.instance_id, resolver_id=resolver_id, rule_id=rule_id,
                                              description=description, match=match, forward_to=forward_to)
        assert resp is not None
        assert resp.status_code == 200

        # List Forwarding rules
        resp = self.cr.list_forwarding_rules(instance_id=self.instance_id, resolver_id=resolver_id)
        assert resp is not None
        assert resp.status_code == 200

        """ create,get,update,list Secondary Zones """
        # Create secondary zones
        description = "Secondary zone"
        zone = "example.com"
        enabled = False
        transfer_from = ["10.0.0.7"]
        resp = self.cr.create_secondary_zone(instance_id=self.instance_id, resolver_id=resolver_id,
                                             description=description, zone=zone, enabled=enabled, transfer_from=transfer_from)
        secondary_zone_id = resp.get_result().get("id")
        assert resp is not None
        assert resp.status_code == 200

        # List Secondary zones
        offset = 0
        limit = 200
        resp = self.cr.list_secondary_zones(instance_id=self.instance_id, resolver_id=resolver_id,
                                            offset=offset, limit=limit)
        assert resp is not None
        assert resp.status_code == 200

        # Get Secondary zones
        x_correlation_id = "abc123"
        resp = self.cr.get_secondary_zone(instance_id=self.instance_id, resolver_id=resolver_id,
                                           secondary_zone_id=secondary_zone_id, x_correlation_id=x_correlation_id)
        assert resp is not None
        assert resp.status_code == 200

        # Update Secondary zones
        x_correlation_id = "abc123"
        description = "update Secondary zone"
        enabled = False
        transfer_from = ["10.0.0.5"]    
        resp = self.cr.update_secondary_zone(instance_id=self.instance_id, resolver_id=resolver_id, secondary_zone_id=secondary_zone_id, x_correlation_id=x_correlation_id, description=description, enabled=enabled, transfer_from=transfer_from )
        assert resp is not None
        assert resp.status_code == 200

        # Delete Secondary zones
        x_correlation_id = "abc123"
        resp = self.cr.delete_secondary_zone(instance_id=self.instance_id, resolver_id=resolver_id,
                                           secondary_zone_id=secondary_zone_id, x_correlation_id=x_correlation_id )
        assert resp is not None
        assert resp.status_code == 204

        """ Delete Custom Resolver,  Locations, Forwarding rules """ 
        # Delete Forwarding rules
        resp = self.cr.delete_forwarding_rule(instance_id=self.instance_id, resolver_id=resolver_id, rule_id=rule_id)
        assert resp is not None
        assert resp.status_code == 204

        # Delete Custom resolver locations
        resp = self.cr.delete_custom_resolver_location(instance_id=self.instance_id, resolver_id=resolver_id,
                                                       location_id=location_id)
        assert resp is not None
        assert resp.status_code == 204
        
        # Delete Custom Resolver
        resp = self.cr.delete_custom_resolver(instance_id=self.instance_id, resolver_id=resolver_id)
        assert resp is not None
        assert resp.status_code == 204
        
class TestCrossAccountV1(unittest.TestCase):
    """Linked Zones for DNS V1 service test class."""   

    def setUp(self):
        """ test case setup """
        if not os.path.exists(configFile):
            raise unittest.SkipTest('External configuration not available, skipping...')
        self.instance_id = os.getenv("DNS_SVCS_INSTANCE_ID")
        self.owner_instance_id = os.getenv("DNS_SVCS_OWNER_INSTANCE_ID")
        self.owner_zone_id = os.getenv("DNS_SVCS_OWNER_ZONE_ID")
        self.lz_vpc_crn = os.getenv("DNS_SVCS_LZ_VPC_CRN")
        authenticatorV2 = IAMAuthenticator(apikey=os.getenv("DNS_SVCS_OWNER_APIKEY"),
                                           url=os.getenv("DNS_SVCS_AUTH_URL"))
        # Create Linked Zones class object
        self.lz = DnsSvcsV1.new_instance(service_name="dns_svcs")
        self.ar = DnsSvcsV1.new_instance(service_name="dns_svcs")
        self.ar.authenticator = authenticatorV2

    # def tearDown(self):
    #     """ tear down """
    #     # Delete the resources
    #     self._clean_linked_zones()
    #     print("Clean up complete")

    # def _clean_linked_zones(self):
    #     # Delete Linked Zones
    #     response = self.lz.list_linked_zones(instance_id=self.instance_id)
    #     assert response is not None
    #     assert response.status_code == 200
    #     result = response.get_result().get("linked_zones")
    #     for lzs in result:
    #         self.lz.delete_linked_zone(instance_id=self.instance_id, linked_dnszone_id=lzs.get("id"))

    def test_1_dns_linkedzones(self):
        """ create,get,update,list Linked Zones """
        # Create Linked Zones
        description = "Linked zone example"
        label = "dev"
        x_correlation_id = 'create-linked-zone-sdk-at123'
        resp = self.lz.create_linked_zone(instance_id=self.instance_id, owner_instance_id=self.owner_instance_id,
                                         owner_zone_id=self.owner_zone_id, description=description, label=label,
                                         x_correlation_id=x_correlation_id)
        
        linked_dnszone_id = resp.get_result().get("id")
        assert resp is not None
        assert resp.status_code == 200

        # List Linked Zones
        x_correlation_id = 'list-linked-zone-sdk-at123'
        offset = 0
        limit = 200
        resp = self.lz.list_linked_zones(instance_id=self.instance_id, offset=offset,
                                         limit=limit, x_correlation_id=x_correlation_id)
        assert resp is not None
        assert resp.status_code == 200

        # Get Linked Zones
        x_correlation_id = 'get-linked-zone-sdk-at123'
        resp = self.lz.get_linked_zone(instance_id=self.instance_id, linked_dnszone_id=linked_dnszone_id, x_correlation_id=x_correlation_id) 
        assert resp is not None
        assert resp.status_code == 200

        # Update Linked Zones
        description = "Linked zone update example"
        label = "dev1"
        x_correlation_id = 'update-linked-zone-sdk-at123'
        resp = self.lz.update_linked_zone(instance_id=self.instance_id, linked_dnszone_id=linked_dnszone_id, x_correlation_id=x_correlation_id,
                                          description=description, label=label) 
        assert resp is not None
        assert resp.status_code == 200

        # List Access Requests
        x_correlation_id = 'list-access-request-sdk-at123'
        offset = 0
        limit = 200
        resp = self.ar.list_dnszone_access_requests(instance_id=self.owner_instance_id, dnszone_id=self.owner_zone_id, offset=offset,
                                         limit=limit, x_correlation_id=x_correlation_id)
        request_id = resp.get_result().get("access_requests")
        assert resp is not None
        assert resp.status_code == 200

        # Get an access request
        x_correlation_id = 'get-access-request-sdk-at123'
        resp = self.ar.get_dnszone_access_request(instance_id=self.owner_instance_id, dnszone_id=self.owner_zone_id, request_id=request_id[0]["id"],
                                                  x_correlation_id=x_correlation_id)
        assert resp is not None
        assert resp.status_code == 200

        # Update the state of an access request
        x_correlation_id = 'update-access-request-sdk-at123'
        action = 'APPROVE'
        resp = self.ar.update_dnszone_access_request(instance_id=self.owner_instance_id, dnszone_id=self.owner_zone_id, request_id=request_id[0]["id"],
                                                  action=action, x_correlation_id=x_correlation_id)
        assert resp is not None
        assert resp.status_code == 200
        
        # List the permitted networks for a linked zone
        x_correlation_id = 'list-permitted-network-sdk-at123'
        resp = self.lz.list_linked_permitted_networks(instance_id=self.instance_id, linked_dnszone_id=linked_dnszone_id, x_correlation_id=x_correlation_id)
        assert resp is not None
        assert resp.status_code == 200

        # Create a permitted network for a linked zone
        permitted_network_vpc_model = {}
        permitted_network_vpc_model['vpc_crn'] = self.lz_vpc_crn
        x_correlation_id = 'create-permitted-network-sdk-at123'
        type = 'vpc'
        resp = self.lz.create_lz_permitted_network(instance_id=self.instance_id, linked_dnszone_id=linked_dnszone_id, x_correlation_id=x_correlation_id,
                                                   type=type, permitted_network=permitted_network_vpc_model)
        permitted_network_id = resp.get_result().get("id")
        assert resp is not None
        assert resp.status_code == 200

        # Get a permitted network
        x_correlation_id = 'get-permitted-network-sdk-at123'
        resp = self.lz.get_linked_permitted_network(instance_id=self.instance_id, linked_dnszone_id=linked_dnszone_id, x_correlation_id=x_correlation_id, permitted_network_id=permitted_network_id)
        assert resp is not None
        assert resp.status_code == 200
        
        # Remove a permitted network
        x_correlation_id = 'delete-permitted-network-sdk-at123'
        resp = self.lz.delete_lz_permitted_network(instance_id=self.instance_id, linked_dnszone_id=linked_dnszone_id, x_correlation_id=x_correlation_id, permitted_network_id=permitted_network_id)
        assert resp is not None
        assert resp.status_code == 202

        # Delete Linked Zones
        x_correlation_id = 'delete-linked-zone-sdk-at123'
        resp = self.lz.delete_linked_zone(instance_id=self.instance_id, linked_dnszone_id=linked_dnszone_id, x_correlation_id=x_correlation_id)
        assert resp is not None
        assert resp.status_code == 204

if __name__ == '__main__':
    unittest.main()
