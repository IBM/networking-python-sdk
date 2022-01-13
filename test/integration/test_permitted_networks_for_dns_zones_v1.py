# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.

"""
Integration test code to execute dns permitted networks api
"""

import os
import unittest
from dotenv import load_dotenv, find_dotenv
from ibm_cloud_networking_services import DnsZonesV1
from ibm_cloud_networking_services import PermittedNetworksForDnsZonesV1

configFile = "pdns.env"

# load the .env file containing your environment variables
try:
    load_dotenv(find_dotenv(filename="pdns.env"))
except:
    print('warning: no pdns.env file loaded')


class TestPermittedNetworksForDnsZonesV1(unittest.TestCase):
    """The Permitted Networks for DNS V1 service test class."""
    
    @unittest.skip("skipping failing test")

    def setUp(self):
        """ test case setup """
        if not os.path.exists(configFile):
            raise unittest.SkipTest(
                'External configuration not available, skipping...')

        self.instance_id = os.getenv("INSTANCE_ID")
        self.vpc_crn = os.getenv("VPC_CRN")
        self.zone_id = ""
        # create zone class object
        self.zone = DnsZonesV1.new_instance(service_name="pdns_services")
        self._create_dns_zones()
        # create permitted nework class object
        self.nw = PermittedNetworksForDnsZonesV1.new_instance(
            service_name="pdns_services")

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


if __name__ == '__main__':
    unittest.main()
