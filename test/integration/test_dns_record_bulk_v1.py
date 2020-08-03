# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.

"""
Integration test code to execute DNS Import/Export Zone settings
"""

import os
import unittest
from dotenv import load_dotenv, find_dotenv
from ibm_cloud_networking_services.dns_record_bulk_v1 import DnsRecordBulkV1
from ibm_cloud_networking_services.dns_records_v1 import DnsRecordsV1

configFile = "cis.env"

# load the .env file containing your environment variables
try:
    load_dotenv(find_dotenv(filename="cis.env"))
except:
    print('warning: no cis.env file loaded')


class TestDnsRecordBulkV1(unittest.TestCase):
    """ DNS Record Bulk API test class """

    def setUp(self):
        if not os.path.exists(configFile):
            raise unittest.SkipTest(
                'External configuration not available, skipping...')
        self.crn = os.getenv("CRN")
        self.zone_id = os.getenv("ZONE_ID")
        self.endpoint = os.getenv("API_ENDPOINT")
        self.dns = DnsRecordBulkV1.new_instance(
            crn=self.crn, zone_identifier=self.zone_id, service_name="cis_services")
        self.dns.set_service_url(self.endpoint)

        self.record = DnsRecordsV1.new_instance(
            crn=self.crn, zone_identifier=self.zone_id, service_name="cis_services")
        self.record.set_service_url(self.endpoint)
        self._clean_dns_records()
        self._create_dns_record_file()

    def tearDown(self):
        """ tear down """
        # Delete the resources
        self._clean_dns_records()
        print("Clean up complete")

    def _clean_dns_records(self):
        """ clean up dns records """
        response = self.record.list_all_dns_records().get_result()
        for dns in response.get("result"):
            if "example" in dns.get("name"):
                print("\ndeleting: ", dns.get("id"))
                dns_record_id = dns.get("id")
                self.record.delete_dns_record(
                    dnsrecord_identifier=dns_record_id)
        try:
            os.remove("/tmp/records.txt")
        except:
            pass

    def _create_dns_record_file(self):
        self.data = open("/tmp/records.txt", "w+")
        self.data.write("example.sdk.cistest-load.com.   1   IN  A   1.1.1.1")
        self.data.close()

    def test_1_dns_records_bulk(self):
        """ test to export dns records """

        self.data = open("/tmp/records.txt", "rb")
        # export dns records
        resp = self.dns.post_dns_records_bulk(file=self.data)
        self.data.close()
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("result").get("recs_added") > 0

        # import dns records
        resp = self.dns.get_dns_records_bulk()
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().text is not None


if __name__ == '__main__':
    unittest.main()
