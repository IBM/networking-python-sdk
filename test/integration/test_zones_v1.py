# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.

"""
Integration test code to execute zones functions
"""

import os
import unittest
import uuid
from dotenv import load_dotenv, find_dotenv
from ibm_cloud_sdk_core.api_exception import ApiException
from ibm_cloud_networking_services.zones_v1 import ZonesV1

configFile = "cis.env"

# load the .env file containing your environment variables
try:
    load_dotenv(find_dotenv(filename=configFile))
except:
    print('warning: no cis.env file loaded')


class TestZonesV1(unittest.TestCase):
    """ Sample function to call zones sdk functions """
        
    @unittest.skip("Authentication failing")

    def setUp(self):
        """ test case setup """
        if not os.path.exists(configFile):
            raise unittest.SkipTest(
                'External configuration not available, skipping...')

        self.crn = os.getenv("CRN")
        self.endpoint = os.getenv("API_ENDPOINT")
        # create zones record class object
        self.zones = ZonesV1.new_instance(
            crn=self.crn, service_name="cis_services")
        self.zones.set_service_url(self.endpoint)
        self._cleanup_zones()

    def tearDown(self):
        """ tear down """
        # Delete the resources
        self._cleanup_zones()
        print("Clean up complete")

    def _cleanup_zones(self):
        response = self.zones.list_zones()
        assert response is not None
        assert response.status_code == 200
        zone = {}
        zones = response.get_result().get("result")
        for zone in zones:
            if "uuid" in zone.get("name"):
                self.zones.delete_zone(
                    zone_identifier=zone.get("id"))

    ################## zones integration test ###################
    def test_1_zones(self):
        """ create a zone """
        self.zone_name = "uuid-" + \
            str(uuid.uuid1())[1:6] + ".sdk.cistest-load.com"
        response = self.zones.create_zone(
            name=self.zone_name).get_result()
        assert response is not None and response.get('success') is True
        result = response.get('result')
        self.zone_id = result.get('id')
        self.paused = result.get('paused')

        """ list all zones """
        response = self.zones.list_zones().get_result()
        assert response is not None and response.get('success') is True

        """ get a zone """
        response = self.zones.get_zone(
            zone_identifier=self.zone_id).get_result()
        assert response is not None and response.get('success') is True

        """ zone activation check """
        try:
            response = self.zones.zone_activation_check(
                zone_identifier=self.zone_id).get_result()
            assert response is not None and response.get('success') is True
        except ApiException as e:
            print("Exception:", e)

        """ update a zone """
        self.paused = not self.paused
        response = self.zones.update_zone(
            zone_identifier=self.zone_id, paused=self.paused).get_result()
        assert response is not None and response.get('success') is True

        self.paused = not self.paused
        response = self.zones.update_zone(
            zone_identifier=self.zone_id, paused=self.paused).get_result()
        assert response is not None and response.get('success') is True

        """ delete a zone """
        response = self.zones.delete_zone(
            zone_identifier=self.zone_id).get_result()
        assert response is not None and response.get('success') is True

    ################## Negative test cases ###################
    def test_2_zones(self):
        """ get zone method without zone identifier """
        with self.assertRaises(ValueError) as val:
            self.zones.get_zone(
                zone_identifier=None).get_result()
            self.assertEqual(val.exception.msg,
                             'zone_identifier must be provided')

        """ update zone method without zone identifier """
        with self.assertRaises(ValueError) as val:
            self.zones.update_zone(
                zone_identifier=None, paused=False).get_result()
            self.assertEqual(val.exception.msg,
                             'zone_identifier must be provided')

        """ zone activation check method without zone identifier """
        with self.assertRaises(ValueError) as val:
            self.zones.zone_activation_check(
                zone_identifier=None).get_result()
            self.assertEqual(val.exception.msg,
                             'zone_identifier must be provided')

        """ delete zone method without zone identifier """
        with self.assertRaises(ValueError) as val:
            self.zones.delete_zone(
                zone_identifier=None).get_result()
            self.assertEqual(val.exception.msg,
                             'zone_identifier must be provided')
            
    ################## partial zone integration test ###################
    def test_3_zones(self):
        """ create a partial zone """
        self.zone_name = "uuid-" + \
            str(uuid.uuid1())[1:6] + ".ibm.com"
        response = self.zones.create_zone(
            name=self.zone_name, type="partial").get_result()
        assert response is not None and response.get('success') is True
        result = response.get('result')
        self.zone_id = result.get('id')
        self.paused = result.get('paused')

        """ list all zones """
        response = self.zones.list_zones().get_result()
        assert response is not None and response.get('success') is True

        """ zone activation check """
        try:
            response = self.zones.zone_activation_check(
                zone_identifier=self.zone_id).get_result()
            assert response is not None and response.get('success') is True
        except ApiException as e:
            print("Exception:", e)

        """ update a zone """
        self.paused = not self.paused
        response = self.zones.update_zone(
            zone_identifier=self.zone_id, paused=self.paused).get_result()
        assert response is not None and response.get('success') is True
    
        self.paused = not self.paused
        response = self.zones.update_zone(
            zone_identifier=self.zone_id, paused=self.paused).get_result()
        assert response is not None and response.get('success') is True

        """ delete a zone """
        response = self.zones.delete_zone(
            zone_identifier=self.zone_id).get_result()
        assert response is not None and response.get('success') is True




if __name__ == '__main__':
    unittest.main()
