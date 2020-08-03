# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.

"""
Integration test code to execute dns record client functions
"""

import os
import unittest
from dotenv import load_dotenv, find_dotenv
from ibm_cloud_networking_services import DnsRecordsV1

configFile = "cis.env"

# load the .env file containing your environment variables
try:
    load_dotenv(find_dotenv(filename="cis.env"))
except:
    print('warning: no cis.env file loaded')


class TestDnsRecordV1(unittest.TestCase):
    """ Test class to call dns record sdk functions """

    def setUp(self):
        """ test case setup """
        if not os.path.exists(configFile):
            raise unittest.SkipTest(
                'External configuration not available, skipping...')
        self.crn = os.getenv("CRN")
        self.zone_id = os.getenv("ZONE_ID")
        self.endpoint = os.getenv("API_ENDPOINT")
        # create dns record class object
        self.dns = DnsRecordsV1.new_instance(
            crn=self.crn, zone_identifier=self.zone_id, service_name="cis_services")
        self.dns.set_service_url(self.endpoint)
        self._clean_dns_records()

    def tearDown(self):
        """ tear down """
        # Delete the resources
        print("Clean up complete")

    def _clean_dns_records(self):
        response = self.dns.list_all_dns_records()
        assert response is not None
        assert response.status_code == 200
        resp = response.get_result().get("result")
        for record in resp:
            if "example" in record.get("name"):
                self.dns.delete_dns_record(
                    dnsrecord_identifier=record.get("id"))

    ################## list_all_dns_records ###################

    def test_1_list_all_dns_records(self):
        """ test for success """
        response = self.dns.list_all_dns_records().get_result()
        assert response is not None and response.get('success') is True

    ################### dns record actions ############################
    def test_1_dns_record_actions(self):
        """ test create/get/update/delete dns A record success """
        # create dns A records
        record_type = 'A'
        name = 'example_ip'
        content = '1.1.1.1'
        response = self.dns.create_dns_record(
            type=record_type,
            name=name, content=content)
        assert response is not None
        assert response.status_code == 200
        record_id = response.get_result().get("result")["id"]

        # get dns A record
        response = self.dns.get_dns_record(
            dnsrecord_identifier=record_id)
        assert response.status_code == 200

        # update dns A records
        content = '2.2.2.2'
        response = self.dns.update_dns_record(
            dnsrecord_identifier=record_id, type=record_type,
            name=name, content=content)
        assert response is not None
        assert response.status_code == 200

        # delete dns A records
        response = self.dns.delete_dns_record(
            dnsrecord_identifier=record_id)
        assert response is not None
        assert response.status_code == 200

    def test_2_dns_record_actions(self):
        """ test create/get/update/delete dns AAAA record success """
        # create dns AAAA records
        record_type = 'AAAA'
        name = 'example_ipv6'
        content = '2001::9'
        response = self.dns.create_dns_record(
            type=record_type,
            name=name, content=content)
        assert response is not None
        assert response.status_code == 200
        record_id = response.get_result().get("result")["id"]

        # get dns AAAA record
        response = self.dns.get_dns_record(dnsrecord_identifier=record_id)
        assert response.status_code == 200

        # update dns AAAA records
        content = '2002::10'
        response = self.dns.update_dns_record(
            dnsrecord_identifier=record_id, type=record_type,
            name=name, content=content)
        assert response is not None
        assert response.status_code == 200

        # delete dns AAAA records
        response = self.dns.delete_dns_record(
            dnsrecord_identifier=record_id)
        assert response is not None
        assert response.status_code == 200

    def test_3_dns_record_actions(self):
        """ test create/get/update/delete dns CNAME record success """
        # create dns CNAME records
        record_type = 'CNAME'
        name = 'example_alias'
        content = 'ibm_alias.com'
        response = self.dns.create_dns_record(
            type=record_type,
            name=name, content=content)
        assert response is not None
        assert response.status_code == 200
        record_id = response.get_result().get("result")["id"]

        # get dns CNAME record
        response = self.dns.get_dns_record(
            dnsrecord_identifier=record_id)
        assert response.status_code == 200

        # update dns CNAME records
        content = 'ibm_alias_1.com'
        response = self.dns.update_dns_record(
            dnsrecord_identifier=record_id, type=record_type,
            name=name, content=content)
        assert response is not None
        assert response.status_code == 200

        # delete dns CNAME records
        response = self.dns.delete_dns_record(dnsrecord_identifier=record_id)
        assert response is not None
        assert response.status_code == 200

    def test_4_dns_record_actions(self):
        """ test create/get/update/delete dns MX record success """
        # create dns MX records
        record_type = 'MX'
        name = 'example_mail'
        content = 'mail.dummy.com'
        priority = 3
        response = self.dns.create_dns_record(
            type=record_type,
            name=name, content=content, priority=priority)
        assert response is not None
        assert response.status_code == 200
        record_id = response.get_result().get("result")["id"]

        # get dns MX record
        response = self.dns.get_dns_record(dnsrecord_identifier=record_id)
        assert response.status_code == 200

        # update dns MX records
        content = 'dummy_mail.ibm.com'
        priority = 6
        response = self.dns.update_dns_record(
            dnsrecord_identifier=record_id, type=record_type, name=name, content=content, priority=priority)
        assert response is not None
        assert response.status_code == 200

        # delete dns MX records
        response = self.dns.delete_dns_record(
            dnsrecord_identifier=record_id)
        assert response is not None
        assert response.status_code == 200

    def test_5_dns_record_actions(self):
        """ test create/get/update/delete dns SPF record success """
        # create dns SPF records
        record_type = 'SPF'
        name = 'example_spf'
        content = 'v=spf1 a mx -all'
        response = self.dns.create_dns_record(
            type=record_type,
            name=name, content=content)
        assert response is not None
        assert response.status_code == 200
        record_id = response.get_result().get("result")["id"]

        # get dns SPF record
        response = self.dns.get_dns_record(dnsrecord_identifier=record_id)
        assert response.status_code == 200

        # update dns SPF records
        content = 'v=spf4 a mx -all'
        response = self.dns.update_dns_record(
            dnsrecord_identifier=record_id, type=record_type,
            name=name, content=content)
        assert response is not None
        assert response.status_code == 200

        # delete dns SPF records
        response = self.dns.delete_dns_record(
            dnsrecord_identifier=record_id)
        assert response is not None
        assert response.status_code == 200

    def test_6_dns_record_actions(self):
        """ test create/get/update/delete dns TXT record success """
        # create dns TXT records
        record_type = 'TXT'
        name = 'ibm-example'
        content = 'sample text'
        response = self.dns.create_dns_record(
            type=record_type,
            name=name, content=content)
        assert response is not None
        assert response.status_code == 200
        record_id = response.get_result().get("result")["id"]

        # get dns TXT record
        response = self.dns.get_dns_record(
            dnsrecord_identifier=record_id)
        assert response.status_code == 200

        # update dns TXT records
        content = 'sample text update'
        response = self.dns.update_dns_record(
            dnsrecord_identifier=record_id, type=record_type,
            name=name, content=content)
        assert response is not None
        assert response.status_code == 200

        # delete dns TXT records
        response = self.dns.delete_dns_record(
            dnsrecord_identifier=record_id)
        assert response is not None
        assert response.status_code == 200

    def test_7_dns_record_actions(self):
        """ test create/get/update/delete dns NS record success """
        # create dns NS records
        record_type = 'NS'
        name = 'example_beta'
        content = 'ns765.beta.com'
        response = self.dns.create_dns_record(
            type=record_type,
            name=name, content=content)
        assert response is not None
        assert response.status_code == 200
        record_id = response.get_result().get("result")["id"]

        # get dns NS record
        response = self.dns.get_dns_record(
            dnsrecord_identifier=record_id)
        assert response.status_code == 200

        # update dns NS records
        name = 'example-ns'
        content = 'ns765.name.com'
        response = self.dns.update_dns_record(
            dnsrecord_identifier=record_id, type=record_type,
            name=name, content=content)
        assert response is not None
        assert response.status_code == 200

        # delete dns NS records
        response = self.dns.delete_dns_record(
            dnsrecord_identifier=record_id)
        assert response is not None
        assert response.status_code == 200


if __name__ == '__main__':
    unittest.main()
