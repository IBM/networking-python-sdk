# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.

"""

Integration test code to execute Transit Gateway client functions
"""
import datetime
import os
import time
import unittest
from ibm_cloud_sdk_core import ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_networking_services import TransitGatewayApisV1

from dotenv import load_dotenv, find_dotenv

# load the .env file containing your environment variables for the required
try:
    load_dotenv(find_dotenv(filename=".transit_env"))
except:
    raise unittest.SkipTest('no .transit_env file loaded, skipping...')

class TestTransitGatewayApisV1(unittest.TestCase):
    """ Test class for Transit Gateway sdk functions """

    def setUp(self):
        """ test case setup """
        self.endpoint = os.getenv("TG_SERVICES_SERVICE_URL")

        if self.endpoint is None:
            self.skipTest("configuration file unavailable")

        self.version = datetime.date.today()
        authenticator = IAMAuthenticator(apikey=os.getenv("TG_SERVICES_APIKEY"),
                                         url=os.getenv("TG_SERVICES_IAM_URL"))

        # create Transit Gateway class object

        self.tg = TransitGatewayApisV1.new_instance(
            version=self.version, service_name="tg_services")
        self.tg.set_service_url(self.endpoint)
        self.tg.authenticator = authenticator
        self._clean_tg_records()

    def tearDown(self):
        """ tear down """
        # Delete the resources
        print("Clean up complete")

    def _clean_tg_records(self):
        response = self.tg.list_transit_gateways()
        assert response is not None
        assert response.get_status_code() == 200
        resp = response.get_result().get("transit_gateways")
        if resp is not None:
            for record in resp:
                gateway_id = record.get("id")
                conn_response = self.tg.list_transit_gateway_connections(
                    transit_gateway_id=gateway_id)
                assert conn_response is not None
                assert conn_response.get_status_code() == 200
                conn_resp = conn_response.get_result().get("connections")
                if conn_resp is not None:
                    for conn_record in conn_resp:
                        if ("SDK-PY" in conn_record.get("name")) and (
                            "delet" not in conn_record.get("status")):
                            self.delete_connection(gateway_id=gateway_id,
                                conn_id=conn_record.get("id"))

                if ("SDK-PY" in record.get("name")) and (
                    "delet" not in record.get("status")):
                    self.delete_gateway(gateway_id=gateway_id)

    def delete_gateway(self, gateway_id):
        response = self.tg.delete_transit_gateway(
            id=gateway_id)
        assert response is not None
        assert response.get_status_code() == 204

        # check gateway until no longer exists
        count = 0
        while count < 24:
            response = None
            try:
                response = self.tg.get_transit_gateway(id=gateway_id)
            except ApiException as e:
                if e.code == 404:
                    break

            if (response is not None) and (response.get_status_code() == 404):
                break
            else:
                time.sleep(10)
                count += 1

    def delete_connection(self, gateway_id, conn_id):
        # delete gateway connection
        response = self.tg.delete_transit_gateway_connection(
            transit_gateway_id=gateway_id, id=conn_id)
        assert response is not None
        assert response.get_status_code() == 204

        # check connection until no longer exists
        count = 0
        while count < 24:
            response = None
            try:
                response = self.tg.get_transit_gateway_connection(
                    transit_gateway_id=gateway_id, id=conn_id)
            except ApiException as e:
                if e.code == 404:
                    break

            if (response is not None) and (response.get_status_code() == 404):
                break
            else:
                time.sleep(10)
                count += 1

    ################### Transit Gateway Locations ############################
    def test_1_list_get_locations(self):
        response = self.tg.list_gateway_locations()
        assert response is not None

        name = response.get_result().get("locations")[0].get("name")

        # get a location
        response = self.tg.get_gateway_location(name=name)
        assert response.get_status_code() == 200

    ################## Transit Gateways ######################################

    def test_1_gateway_actions(self):
        """ test create/get/update/delete gateway success """
        # create local gateway
        name = os.getenv("TG_SERVICES_GW_NAME")
        location = os.getenv("TG_SERVICES_LOCATION")
        response = self.tg.create_transit_gateway(
            name=name, location=location)
        assert response is not None
        assert response.get_status_code() == 201
        gateway_id = response.get_result().get("id")

        # check gateway status until available using get api
        count = 0
        while count < 24:
            response = self.tg.get_transit_gateway(id=gateway_id)
            status = response.get_result().get("status")
            ret_id = response.get_result().get("id")
            assert ret_id == gateway_id
            assert response.get_status_code() == 200
            if status == "available":
                break
            else:
                time.sleep(5)
                count += 1

        # list gateways
        response = self.tg.list_transit_gateways()
        assert response is not None
        assert response.get_status_code() == 200
        gateways = response.get_result().get("transit_gateways")
        list_result = False
        for gateway in gateways:
            if gateway["id"] == gateway_id:
                list_result = True
                break
        assert list_result

        # update gateway name
        update_name = "update"+os.getenv("TG_SERVICES_GW_NAME")
        response = self.tg.update_transit_gateway(id=gateway_id,
            name=update_name)
        assert response is not None
        assert response.get_status_code() == 200
        assert response.get_result()["name"] == update_name

        # delete gateway
        self.delete_gateway(gateway_id)

################## Transit Connections ######################################
    def test_1_transit_gateway_conn_actions(self):
        """ test create/get/update/delete gateway connections success """
        # create gateway
        name = os.getenv("TG_SERVICES_GW_NAME")
        location = os.getenv("TG_SERVICES_LOCATION")
        response = self.tg.create_transit_gateway(
            name=name, location=location)
        assert response is not None
        assert response.get_status_code() == 201
        gateway_id = response.get_result()["id"]

        # check gateway status until available using get api
        count = 0
        while count < 24:
            response = self.tg.get_transit_gateway(id=gateway_id)
            status = response.get_result()["status"]
            ret_id = response.get_result()["id"]
            assert ret_id == gateway_id
            assert response.get_status_code() == 200
            if status == "available":
                break
            else:
                time.sleep(5)
                count += 1

        # create transit gateway connection
        name = os.getenv("TG_SERVICES_CONN_NAME")
        crn = os.getenv("TG_SERVICES_VPC_CRN")
        response = self.tg.create_transit_gateway_connection(
            transit_gateway_id=gateway_id, network_type="vpc", name=name,
            network_id=crn)
        assert response is not None
        assert response.get_status_code() == 201
        conn_id = response.get_result()["id"]

        # check connection status until attached using get api
        count = 0
        while count < 24:
            response = self.tg.get_transit_gateway_connection(
                transit_gateway_id=gateway_id, id=conn_id)
            status = response.get_result()["status"]
            ret_id = response.get_result()["id"]
            assert ret_id == conn_id
            assert response.get_status_code() == 200
            if status == "attached":
                break
            else:
                time.sleep(10)
                count += 1

        # list gateway connections
        response = self.tg.list_transit_gateway_connections(
            transit_gateway_id=gateway_id)
        assert response is not None
        assert response.get_status_code() == 200
        conns = response.get_result().get("connections")
        list_result = False
        for conn in conns:
            if conn["id"] == conn_id:
                list_result = True
                break
        assert list_result

        # update gateway connection
        name = "update"+os.getenv("TG_SERVICES_CONN_NAME")
        response = self.tg.update_transit_gateway_connection(
            transit_gateway_id=gateway_id, id=conn_id, name=name)
        assert response is not None
        assert response.get_status_code() == 200
        assert response.get_result()["name"] == name

        # delete gateway connection
        self.delete_connection(gateway_id, conn_id)
        
        # delete gateway
        self.delete_gateway(gateway_id)

if __name__ == '__main__':
    unittest.main()
