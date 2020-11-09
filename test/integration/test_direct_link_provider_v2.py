# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.

"""
Integration test code to execute DirectLink Provider functions
"""
import datetime
import os
import time
import unittest
from ibm_cloud_sdk_core import ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_networking_services import DirectLinkV1
from ibm_cloud_networking_services import DirectLinkProviderV2
from ibm_cloud_networking_services.direct_link_provider_v2 import ProviderGatewayPortIdentity

from dotenv import load_dotenv, find_dotenv

# load the .env file containing your environment variables
try:
    load_dotenv(find_dotenv(filename=".dl_env"))
except:
    raise unittest.SkipTest('no .dl_env file loaded, skipping...')

class TestDirectLinkProviderV2(unittest.TestCase):
    """ Test class for DirectLink Provider sdk functions """

    def setUp(self):
        """ test case setup """
        self.dl_endpoint = os.getenv("DL_SERVICES_SERVICE_URL")
        self.dl_provider_endpoint = os.getenv("DL_PROVIDER_SERVICES_URL_V2")

        if self.dl_endpoint is None or self.dl_provider_endpoint is None:
            self.skipTest("configuration file unavailable")

        self.version = datetime.date.today()
        authenticator = IAMAuthenticator(apikey=os.getenv("DL_SERVICES_APIKEY"),
                                         url=os.getenv("DL_SERVICES_IAM_URL"))

        authenticatorV2 = IAMAuthenticator(apikey=os.getenv("DL_PROVIDER_SERVICES_APIKEY"),
                                           url=os.getenv("DL_SERVICES_IAM_URL"))

        # create DirectLink class object
        self.dl = DirectLinkV1.new_instance(
            version=self.version, service_name="dl_services")
        self.dl.set_service_url(self.dl_endpoint)
        self.dl.authenticator = authenticator

        #create DirectLink Provider class object
        self.dl_provider = DirectLinkProviderV2.new_instance(
            version=self.version, service_name="dl_provider_services")
        self.dl_provider.set_service_url(self.dl_provider_endpoint)
        self.dl_provider.authenticator = authenticatorV2

        self._clean_dl_records()

    def tearDown(self):
        """ tear down """
        # Delete the resources
        print("Clean up complete")

    def _clean_dl_records(self):
        #clean up accounts in provider account
        response = self.dl_provider.list_provider_gateways()  
        assert response is not None
        assert response.get_status_code() == 200
        resp = response.get_result().get("gateways")
        if resp is not None:
            for record in resp:
                gateway_id = record.get("id")
                if ("SDK-PY-DL-PROVIDER" in record.get("name")) and (
                    ("delet" not in record.get("operational_status")) and ("progress" not in record.get("operational_status"))):
                    self.delete_provider_gateway(gateway_id=gateway_id)
        
        #clean up the above deleted records in client account
        print("Clean dl records")
        response = self.dl.list_gateways()
        assert response is not None
        assert response.get_status_code() == 200
        resp = response.get_result().get("gateways")
        if resp is not None:
            for record in resp:
                gateway_id = record.get("id")
                if ("SDK-PY-DL-PROVIDER" in record.get("name")) and (
                    ("delet" not in record.get("operational_status")) and ("progress" not in record.get("operational_status"))):
                    self.dl.create_gateway_action(id=gateway_id, action="delete_gateway_approve")

    def delete_gateway(self, gateway_id):
        response = self.dl.create_gateway_action(id=gateway_id, action="delete_gateway_approve")
        assert response is not None
        assert response.get_status_code() == 204

        # check gateway until no longer exists
        count = 0
        while count < 24:
            response = None
            try:
                response = self.dl.get_gateway(id=gateway_id)
            except ApiException as e:
                if e.code == 404:
                    break

            if (response is not None) and (response.get_status_code() == 404):
                break
            else:
                time.sleep(10)
                count += 1

    def delete_provider_gateway(self, gateway_id):
        response = self.dl_provider.delete_provider_gateway(
            id=gateway_id)
        assert response is not None


    ################## Direct Link Provider Ports ######################################

    def test_1_list_get_provider_ports(self):
        """ test list/get ports success """
        response = self.dl_provider.list_provider_ports()
        assert response is not None

        port_id = response.get_result().get("ports")[0].get("id")

        # get a port
        response = self.dl_provider.get_provider_port(id=port_id)
        assert response.get_status_code() == 200

    ################## Direct Link Provider Gateways ######################################

    def test_1_provider_gateway_actions(self):
        timestamp = time.time()
        name = os.getenv("DL_PROVIDER_SERVICES_GW_NAME") + "-" + str(int(timestamp))
        print("NAME:")
        print(name)
        bgpAsn = 64999
        customerAccount = os.getenv("DL_PROVIDER_SERVICES_CUSTOMER_ACCT_ID")
        speedMbps = 1000

        """ successfully get a provider port id """
        response = self.dl_provider.list_provider_ports()
        assert response is not None

        port_id = response.get_result().get("ports")[0].get("id")
        port = ProviderGatewayPortIdentity(id=port_id)

        """ test create/get/update/delete provider gateway success """
        #create provider gateway
        response =  self.dl_provider.create_provider_gateway(bgp_asn=bgpAsn,
                                                             customer_account_id=customerAccount,
                                                             name=name,
                                                             port=port,
                                                             speed_mbps=speedMbps)
        assert response is not None
        assert response.get_status_code() == 201
        provider_gateway_id = response.get_result().get("id")

        #get the created gateway
        response = self.dl_provider.get_provider_gateway(id=provider_gateway_id)
        assert response is not None
        assert response.get_status_code() == 200
        assert response.get_result().get("id") == provider_gateway_id
        assert response.get_result().get("name") == name
        assert response.get_result().get("customer_account_id") == customerAccount
        assert response.get_result().get("speed_mbps") == speedMbps
        assert response.get_result().get("provider_api_managed") == True
        assert response.get_result().get("operational_status") == "create_pending"
        assert response.get_result().get("type") == "connect"

        #list the provider created gateways
        response = self.dl_provider.list_provider_gateways()
        assert response is not None
        assert response.get_status_code() == 200
        gateways = response.get_result().get("gateways")
        list_result = False
        for gateway in gateways:
            if gateway["id"] == provider_gateway_id:
                list_result = True
                break
        assert list_result

        #fail update of created gateway due to invalid status
        with self.assertRaises(ApiException) as ex:
            response = self.dl_provider.update_provider_gateway(id=provider_gateway_id, speed_mbps=2000)
        assert ex.exception.code == 400
        
        #delete the gateway
        response = self.dl_provider.delete_provider_gateway(id=provider_gateway_id)
        assert response.get_status_code() == 204

    ################## Direct Link Provider Gateways with Client API ############################

    def test_1_provider_gateway_actions_with_client_api(self):
        timestamp = time.time()
        name = os.getenv("DL_PROVIDER_SERVICES_GW_NAME") + "-" + str(int(timestamp))
        updatedName = os.getenv("DL_PROVIDER_SERVICES_UPDATED_GW_NAME") + "-" + str(int(timestamp))
        bgpAsn = 64999
        customerAccount = os.getenv("DL_PROVIDER_SERVICES_CUSTOMER_ACCT_ID")
        speedMbps = 1000
        updatedSpeedMbps = 2000

        """ successfully get a provider port id """
        response = self.dl_provider.list_provider_ports()
        assert response is not None

        port_id = response.get_result().get("ports")[0].get("id")
        port = ProviderGatewayPortIdentity(id=port_id)

        #created provider gateway
        response =  self.dl_provider.create_provider_gateway(bgp_asn=bgpAsn,
                                                             customer_account_id=customerAccount,
                                                             name=name,
                                                             port=port,
                                                             speed_mbps=speedMbps)
        assert response is not None
        assert response.get_status_code() == 201
        gateway_id = response.get_result().get("id")

        #verfiy client account can see the provider created gateway
        response = self.dl.get_gateway(id=gateway_id)
        assert response is not None
        assert response.get_status_code() == 200
        assert response.get_result().get("id") == gateway_id
        assert response.get_result().get("name") == name
        assert response.get_result().get("speed_mbps") == speedMbps
        assert response.get_result().get("provider_api_managed") == True
        assert response.get_result().get("operational_status") == "create_pending"
        assert response.get_result().get("type") == "connect"
        assert "change_request" in response.get_result()

        #successfully approve the gateway create using client account
        response = self.dl.create_gateway_action(id=gateway_id,
                                                 action="create_gateway_approve",
                                                 metered=False,
                                                 global_=False)
        assert response is not None
        assert response.get_status_code() == 200

        #successfully waits for the gateway to move to provisioned state
        response = self.dl.get_gateway(id=gateway_id)
        assert response is not None
        assert response.get_status_code() == 200

        # wait until gateway moves to provisioned state
        count = 0
        while True:
            response = None
            response = self.dl.get_gateway(id=gateway_id)
            operationalStatus = response.get_result().get("operational_status")
                    
            if (response is not None) and (response.get_result().get("operational_status") == "provisioned"):
                assert response is not None
                assert response.get_status_code() == 200
                assert response.get_result().get("id") == gateway_id
                assert response.get_result().get("name") == name
                assert response.get_result().get("speed_mbps") == speedMbps
                assert response.get_result().get("provider_api_managed") == True
                assert response.get_result().get("operational_status") == "provisioned"
                assert response.get_result().get("type") == "connect"
                break

            if count > 24:
                assert response.get_result().get("operational_status") == "provisioned"
            else:
                time.sleep(10)
                count += 1


        #update the name of the provider gateway
        response = self.dl_provider.update_provider_gateway(id=gateway_id,
                                                            name=updatedName)
        assert response is not None
        assert response.get_status_code() == 200
        assert response.get_result().get("id") == gateway_id
        assert response.get_result().get("name") == updatedName
        assert response.get_result().get("speed_mbps") == speedMbps
        assert "change_request" not in response.get_result()

        #successfully request the speed update of the gateway
        response = self.dl_provider.update_provider_gateway(id=gateway_id,speed_mbps=updatedSpeedMbps)
        assert response is not None
        assert response.get_status_code() == 200
        assert response.get_result().get("id") == gateway_id
        assert response.get_result().get("name") == updatedName
        assert response.get_result().get("speed_mbps") == speedMbps
        assert "change_request" in response.get_result()

        #approve speed update request using client account
        speedMbpsObject = {"speed_mbps": updatedSpeedMbps}
        updateAttributes = [speedMbpsObject]
        response = self.dl.create_gateway_action(id=gateway_id, 
                                                 action="update_attributes_approve",
                                                 updates=updateAttributes)
        assert response is not None
        assert response.get_status_code() == 200
        assert response.get_result().get("id") == gateway_id
        assert response.get_result().get("name") == updatedName
        assert response.get_result().get("speed_mbps") == updatedSpeedMbps

        # wait until gateway moves to provisioned state
        count = 0
        while True:
            response = None
            response = self.dl_provider.get_provider_gateway(id=gateway_id)
            operationalStatus = response.get_result().get("operational_status")
                    
            if (response is not None) and (response.get_result().get("operational_status") == "provisioned"):
                assert response is not None
                assert response.get_status_code() == 200
                assert response.get_result().get("id") == gateway_id
                assert response.get_result().get("name") == updatedName
                assert response.get_result().get("speed_mbps") == updatedSpeedMbps
                assert response.get_result().get("provider_api_managed") == True
                assert response.get_result().get("operational_status") == "provisioned"
                assert response.get_result().get("type") == "connect"
                break

            if count > 24:
                assert response.get_result().get("operational_status") == "provisioned"
            else:
                time.sleep(10)
                count += 1

        #successfully request delete using provider account
        time.sleep(10)
        response = self.dl_provider.delete_provider_gateway(id=gateway_id)
        assert response is not None
        assert response.get_status_code() == 202

        #successfully reject delete gateway using client account
        response = self.dl.create_gateway_action(id=gateway_id, action="delete_gateway_reject")
        assert response is not None
        assert response.get_status_code() == 200

        #successfully verify reject gateway using client account
        response = self.dl.get_gateway(id=gateway_id)
        assert response is not None
        assert response.get_status_code() == 200
        assert "change_request" not in response.get_result()

        # wait until gateway moves to provisioned state
        count = 0
        while True:
            response = None
            response = self.dl_provider.get_provider_gateway(id=gateway_id)
            operationalStatus = response.get_result().get("operational_status")
                    
            if (response is not None) and (response.get_result().get("operational_status") == "provisioned"):
                assert response is not None
                assert response.get_status_code() == 200
                assert response.get_result().get("id") == gateway_id
                assert response.get_result().get("name") == updatedName
                assert response.get_result().get("speed_mbps") == updatedSpeedMbps
                assert response.get_result().get("provider_api_managed") == True
                assert response.get_result().get("operational_status") == "provisioned"
                assert response.get_result().get("type") == "connect"
                break

            if count > 24:
                assert response.get_result().get("operational_status") == "provisioned"
            else:
                time.sleep(10)
                count += 1

        #successfully re-request delete using provider account
        response = self.dl_provider.delete_provider_gateway(id=gateway_id)
        assert response is not None
        assert response.get_status_code() == 202

        #successfully approve delete gateway using client account
        response = self.dl.create_gateway_action(id=gateway_id, action="delete_gateway_approve")
        assert response is not None
        assert response.get_status_code() == 204

if __name__ == '__main__':
    unittest.main()