# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.

"""
Integration test code to execute dns zones
"""

import os
import unittest
from ibm_cloud_networking_services import DnsZonesV1


class TestZonesV1(unittest.TestCase):
    """The DNS Zones V1 service test class."""

    def setUp(self):
        """ test case setup """
        self.instance_id = os.getenv("INSTANCE_ID")
        # create zone class object
        self.zone = DnsZonesV1.new_instance(service_name="pdns_services")
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
                print(zone.get("id"))
                self.zone.delete_dnszone(instance_id=self.instance_id, dnszone_id=zone.get("id"))

    def test_1_pdns_zone_action(self):
        """ test private dns zone create/delete/update/get functionality """
        name = "test.example36.com"
        label = "us-south"
        resp = self.zone.list_dnszones(instance_id=self.instance_id)
        assert resp is not None
        assert resp.status_code == 200

        # create dns zone
        resp = self.zone.create_dnszone(instance_id=self.instance_id, name=name, label=label)
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("instance_id") == self.instance_id
        assert resp.get_result().get("name") == name
        assert resp.get_result().get("label") == label
        zone_id = resp.get_result().get("id")

        # get dns zone
        resp = self.zone.get_dnszone(instance_id=self.instance_id, dnszone_id=zone_id)
        assert resp.status_code == 200
        assert resp.get_result().get("instance_id") == self.instance_id
        assert resp.get_result().get("name") == name
        assert resp.get_result().get("label") == label


        # update dns zone
        label = "us-south-1"
        desc = "test instance"
        resp = self.zone.update_dnszone(instance_id=self.instance_id, dnszone_id=zone_id, description=desc, label=label)
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("instance_id") == self.instance_id
        assert resp.get_result().get("name") == name
        assert resp.get_result().get("label") == label
        assert resp.get_result().get("description") == desc


        # delete dns zone
        resp = self.zone.delete_dnszone(instance_id=self.instance_id, dnszone_id=zone_id)
        assert resp is not None
        assert resp.status_code == 204

    def test_1_pdns_zone_list(self):
        """ test private dns zone list functionality """

        name = "test.example34.com"
        label = "us-south"
        # create dns zone
        resp = self.zone.create_dnszone(instance_id=self.instance_id, name=name, label=label)
        assert resp is not None
        assert resp.status_code == 200

        name = "test.example35.com"
        # create dns zone
        resp = self.zone.create_dnszone(instance_id=self.instance_id, name=name, label=label)
        assert resp is not None
        assert resp.status_code == 200

        name = "test.example36.com"
        # create dns zone
        resp = self.zone.create_dnszone(instance_id=self.instance_id, name=name, label=label)
        assert resp is not None
        assert resp.status_code == 200

        name = "test.example37.com"
        # create dns zone
        resp = self.zone.create_dnszone(instance_id=self.instance_id, name=name, label=label)
        assert resp is not None
        assert resp.status_code == 200


        resp = self.zone.list_dnszones(instance_id=self.instance_id, offset=1, limit=2)
        assert resp is not None
        assert resp.status_code == 200


if __name__ == '__main__':
    unittest.main()