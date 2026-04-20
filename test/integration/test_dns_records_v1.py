# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2026.

"""
Integration test code to execute dns record client functions
"""

import os
import unittest
from dotenv import load_dotenv, find_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_networking_services.dns_records_v1 import (
    DnsRecordsV1,
    BatchDnsRecordsRequestDeletesItem,
    BatchDnsRecordsRequestPatchesItem,
    BatchDnsRecordsRequestPutsItem,
    DnsrecordInput,
)

configFile = "cis.env"

# load the .env file containing your environment variables
try:
    load_dotenv(find_dotenv(filename="cis.env"))
except:
    print('warning: no cis.env file loaded')


class TestDnsRecordV1(unittest.TestCase):
    """ Test class to call dns record sdk functions """

    @classmethod
    def setUpClass(cls):
        if not os.path.exists(configFile):
            raise unittest.SkipTest(
                'External configuration not available, skipping...')

        api_key = os.getenv("CIS_SERVICES_APIKEY")
        auth_url = os.getenv("CIS_SERVICES_AUTH_URL")
        crn = os.getenv("CRN")
        zone_id = os.getenv("ZONE_ID")
        service_url = os.getenv("API_ENDPOINT")

        if not all([api_key, crn, zone_id]):
            raise unittest.SkipTest("Environment variables not set properly")

        authenticator = IAMAuthenticator(api_key, url=auth_url)
        cls.dns = DnsRecordsV1(
            authenticator=authenticator,
            crn=crn,
            zone_identifier=zone_id,
        )
        if service_url:
            cls.dns.set_service_url(service_url)

        cls.dns.enable_retries(max_retries=4, retry_interval=30)

        try:
            cls.dns.list_all_dns_records()
        except Exception as e:
            raise unittest.SkipTest(f"Authentication failed: {e}")

        cls._clean_dns_records(cls)

    def _clean_dns_records(self):
        response = self.dns.list_all_dns_records()
        assert response is not None
        assert response.status_code == 200
        resp = response.get_result().get("result")
        for record in resp:
            if "example" in record.get("name") or "ibm-example" in record.get("name"):
                self.dns.delete_dns_record(
                    dnsrecord_identifier=record.get("id"))

    def tearDown(self):
        """ tear down """
        print("Clean up complete")

    ################## list_all_dns_records ###################

    def test_01_list_all_dns_records(self):
        """ test list all dns records """
        response = self.dns.list_all_dns_records()
        assert response is not None
        assert response.status_code == 200
        result = response.get_result()
        assert result.get('success') is True

    def test_02_list_all_dns_records_with_filters(self):
        """ test list dns records with filter params """
        response = self.dns.list_all_dns_records(
            type='A',
            per_page=20,
            page=1,
            order='name',
            direction='asc',
            match='all',
        )
        assert response is not None
        assert response.status_code == 200

    ################### A record #################################

    def test_03_dns_record_a(self):
        """ test create/get/update/delete dns A record """
        record_type = 'A'
        name = 'example-ip'
        content = '1.1.1.1'

        # create
        response = self.dns.create_dns_record(
            type=record_type, name=name, content=content, ttl=120)
        assert response is not None
        assert response.status_code == 200
        record_id = response.get_result()["result"]["id"]

        # get
        response = self.dns.get_dns_record(dnsrecord_identifier=record_id)
        assert response.status_code == 200

        # update
        response = self.dns.update_dns_record(
            dnsrecord_identifier=record_id,
            type=record_type, name=name, content='2.2.2.2', ttl=240)
        assert response is not None
        assert response.status_code == 200

        # delete
        response = self.dns.delete_dns_record(dnsrecord_identifier=record_id)
        assert response is not None
        assert response.status_code == 200

    ################### AAAA record ##############################

    def test_04_dns_record_aaaa(self):
        """ test create/get/update/delete dns AAAA record """
        record_type = 'AAAA'
        name = 'example-ipv6'
        content = '2001::9'

        response = self.dns.create_dns_record(
            type=record_type, name=name, content=content, ttl=120)
        assert response is not None
        assert response.status_code == 200
        record_id = response.get_result()["result"]["id"]

        response = self.dns.get_dns_record(dnsrecord_identifier=record_id)
        assert response.status_code == 200

        response = self.dns.update_dns_record(
            dnsrecord_identifier=record_id,
            type=record_type, name=name, content='2002::10', ttl=240)
        assert response is not None
        assert response.status_code == 200

        response = self.dns.delete_dns_record(dnsrecord_identifier=record_id)
        assert response is not None
        assert response.status_code == 200

    ################### CNAME record #############################

    def test_05_dns_record_cname(self):
        """ test create/get/update/delete dns CNAME record """
        record_type = 'CNAME'
        name = 'example-alias'
        content = 'ibm-alias.com'

        response = self.dns.create_dns_record(
            type=record_type, name=name, content=content)
        assert response is not None
        assert response.status_code == 200
        record_id = response.get_result()["result"]["id"]

        response = self.dns.get_dns_record(dnsrecord_identifier=record_id)
        assert response.status_code == 200

        response = self.dns.update_dns_record(
            dnsrecord_identifier=record_id,
            type=record_type, name=name, content='ibm-alias-1.com')
        assert response is not None
        assert response.status_code == 200

        response = self.dns.delete_dns_record(dnsrecord_identifier=record_id)
        assert response is not None
        assert response.status_code == 200

    ################### MX record ################################

    def test_06_dns_record_mx(self):
        """ test create/get/update/delete dns MX record """
        record_type = 'MX'
        name = 'example-mail'
        content = 'mail.dummy.com'

        response = self.dns.create_dns_record(
            type=record_type, name=name, content=content, priority=3)
        assert response is not None
        assert response.status_code == 200
        record_id = response.get_result()["result"]["id"]

        response = self.dns.get_dns_record(dnsrecord_identifier=record_id)
        assert response.status_code == 200

        response = self.dns.update_dns_record(
            dnsrecord_identifier=record_id,
            type=record_type, name=name, content='dummy-mail.ibm.com', priority=6)
        assert response is not None
        assert response.status_code == 200

        response = self.dns.delete_dns_record(dnsrecord_identifier=record_id)
        assert response is not None
        assert response.status_code == 200

    ################### TXT record ################################

    def test_07_dns_record_txt(self):
        """ test create/get/update/delete dns TXT record """
        record_type = 'TXT'
        name = 'ibm-example'
        content = 'sample text'

        response = self.dns.create_dns_record(
            type=record_type, name=name, content=content)
        assert response is not None
        assert response.status_code == 200
        record_id = response.get_result()["result"]["id"]

        response = self.dns.get_dns_record(dnsrecord_identifier=record_id)
        assert response.status_code == 200

        response = self.dns.update_dns_record(
            dnsrecord_identifier=record_id,
            type=record_type, name=name, content='sample text update')
        assert response is not None
        assert response.status_code == 200

        response = self.dns.delete_dns_record(dnsrecord_identifier=record_id)
        assert response is not None
        assert response.status_code == 200

    ################### NS record ################################

    def test_08_dns_record_ns(self):
        """ test create/get/update/delete dns NS record """
        record_type = 'NS'
        name = 'example-beta'
        content = 'ns765.beta.com'

        response = self.dns.create_dns_record(
            type=record_type, name=name, content=content)
        assert response is not None
        assert response.status_code == 200
        record_id = response.get_result()["result"]["id"]

        response = self.dns.get_dns_record(dnsrecord_identifier=record_id)
        assert response.status_code == 200

        response = self.dns.update_dns_record(
            dnsrecord_identifier=record_id,
            type=record_type, name='example-ns', content='ns765.name.com')
        assert response is not None
        assert response.status_code == 200

        response = self.dns.delete_dns_record(dnsrecord_identifier=record_id)
        assert response is not None
        assert response.status_code == 200

    ################### proxied field ############################

    def test_09_dns_record_proxied(self):
        """ test create A record with proxied=True """
        response = self.dns.create_dns_record(
            type='A', name='example-proxied', content='3.3.3.3', proxied=True)
        assert response is not None
        assert response.status_code == 200
        record_id = response.get_result()["result"]["id"]
        assert response.get_result()["result"]["proxied"] is True

        response = self.dns.update_dns_record(
            dnsrecord_identifier=record_id,
            type='A', name='example-proxied', content='3.3.3.3', proxied=False)
        assert response is not None
        assert response.status_code == 200

        response = self.dns.delete_dns_record(dnsrecord_identifier=record_id)
        assert response.status_code == 200

    ################### batch_dns_records ########################

    def test_10_batch_dns_records_posts(self):
        """ test batch dns records with posts (create) """
        posts = [
            DnsrecordInput(type='A', name='example-batch-a', content='10.0.0.1', ttl=120),
            DnsrecordInput(type='AAAA', name='example-batch-aaaa', content='2003::1', ttl=120),
        ]
        response = self.dns.batch_dns_records(posts=posts)
        assert response is not None
        assert response.status_code == 200
        result = response.get_result()
        assert result.get('success') is True
        created = result["result"]["posts"]
        assert len(created) == 2

        # cleanup
        for record in created:
            self.dns.delete_dns_record(dnsrecord_identifier=record["id"])

    def test_11_batch_dns_records_mixed(self):
        """ test batch dns records with deletes, patches, puts, posts in one call """
        # pre-create two records to use in deletes/puts/patches
        r1 = self.dns.create_dns_record(
            type='A', name='example-batch-del', content='10.0.1.1', ttl=120)
        assert r1.status_code == 200
        del_id = r1.get_result()["result"]["id"]

        r2 = self.dns.create_dns_record(
            type='A', name='example-batch-patch', content='10.0.1.2', ttl=120)
        assert r2.status_code == 200
        patch_id = r2.get_result()["result"]["id"]

        r3 = self.dns.create_dns_record(
            type='A', name='example-batch-put', content='10.0.1.3', ttl=120)
        assert r3.status_code == 200
        put_id = r3.get_result()["result"]["id"]

        deletes = [BatchDnsRecordsRequestDeletesItem(id=del_id)]
        patches = [BatchDnsRecordsRequestPatchesItem(id=patch_id, content='10.0.1.22')]
        puts = [BatchDnsRecordsRequestPutsItem(
            id=put_id, name='example-batch-put', type='A', ttl=240, content='10.0.1.33')]
        posts = [DnsrecordInput(type='TXT', name='example-batch-post', content='batchtest')]

        response = self.dns.batch_dns_records(
            deletes=deletes, patches=patches, puts=puts, posts=posts)
        assert response is not None
        assert response.status_code == 200
        result = response.get_result()
        assert result.get('success') is True

        # cleanup records created by puts/posts
        for record in result["result"].get("puts", []):
            self.dns.delete_dns_record(dnsrecord_identifier=record["id"])
        for record in result["result"].get("posts", []):
            self.dns.delete_dns_record(dnsrecord_identifier=record["id"])
        # patch_id still exists, clean it up
        self.dns.delete_dns_record(dnsrecord_identifier=patch_id)


if __name__ == '__main__':
    unittest.main()
