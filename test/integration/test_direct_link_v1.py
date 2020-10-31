# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.

"""
Integration test code to execute DirectLink client functions
"""
import datetime
import os
import time
import unittest
from ibm_cloud_sdk_core import ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_networking_services import DirectLinkV1
from ibm_cloud_networking_services.direct_link_v1 import (
    GatewayTemplateGatewayTypeDedicatedTemplate)
# from ibm_cloud_networking_services.direct_link_v1 import (
#     GatewayMacsecConfigTemplate)
# from ibm_cloud_networking_services.direct_link_v1 import (
#     GatewayMacsecConfigTemplatePrimaryCak)
# from ibm_cloud_networking_services.direct_link_v1 import (
#     GatewayMacsecConfigPatchTemplate)
# from ibm_cloud_networking_services.direct_link_v1 import (
#     GatewayMacsecConfigPatchTemplateFallbackCak)
from dotenv import load_dotenv, find_dotenv

# load the .env file containing your environment variables
try:
    load_dotenv(find_dotenv(filename=".dl_env"))
except:
    raise unittest.SkipTest('no .dl_env file loaded, skipping...')

class TestDirectLinkV1(unittest.TestCase):
    """ Test class for DirectLink sdk functions """

    def setUp(self):
        """ test case setup """
        self.endpoint = os.getenv("DL_SERVICES_SERVICE_URL")

        if self.endpoint is None:
            self.skipTest("configuration file unavailable")

        self.version = datetime.date.today()
        authenticator = IAMAuthenticator(apikey=os.getenv("DL_SERVICES_APIKEY"),
                                         url=os.getenv("DL_SERVICES_IAM_URL"))
        # create DirectLink class object
        self.dl = DirectLinkV1.new_instance(
            version=self.version, service_name="dl_services")
        self.dl.set_service_url(self.endpoint)
        self.dl.authenticator = authenticator
        self._clean_dl_records()

    def tearDown(self):
        """ tear down """
        # Delete the resources
        print("Clean up complete")

    def _clean_dl_records(self):
        response = self.dl.list_gateways()
        assert response is not None
        assert response.get_status_code() == 200
        resp = response.get_result().get("gateways")
        if resp is not None:
            for record in resp:
                gateway_id = record.get("id")
                conn_response = self.dl.list_gateway_virtual_connections(
                    gateway_id=gateway_id)
                assert conn_response is not None
                assert conn_response.get_status_code() == 200
                conn_resp = conn_response.get_result().get("virtual_connections")
                if conn_resp is not None:
                    for conn_record in conn_resp:
                        if ("SDK-PY" in conn_record.get("name")) and (
                            "delet" not in conn_record.get("status")):
                            self.delete_connection(gateway_id=gateway_id,
                                conn_id=conn_record.get("id"))

                if ("SDK-PY" in record.get("name")) and (
                    "delet" not in record.get("operational_status")):
                    self.delete_gateway(gateway_id=gateway_id)

    def delete_gateway(self, gateway_id):
        response = self.dl.delete_gateway(
            id=gateway_id)
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

    def delete_connection(self, gateway_id, conn_id):
        # delete gateway connection
        response = self.dl.delete_gateway_virtual_connection(
            gateway_id=gateway_id, id=conn_id)
        assert response is not None
        assert response.get_status_code() == 204

        # check connection until no longer exists
        count = 0
        while count < 24:
            response = None
            try:
                response = self.dl.get_gateway_virtual_connection(
                    gateway_id=gateway_id, id=conn_id)
            except ApiException as e:
                if e.code == 404:
                    break

            if (response is not None) and (response.get_status_code() == 404):
                break
            else:
                time.sleep(10)
                count += 1

    ################## DirectLink Gateways ######################################

    def test_1_gateway_actions(self):
        bgpAsn = 64999
        bgpBaseCidr = "169.254.0.0/16"
        crossConnectRouter = "LAB-xcr01.dal09"
        global_bool = True
        locationName = os.getenv("DL_SERVICES_LOCATION_NAME")
        speedMbps = 1000
        metered = False
        carrierName = "carrier1"
        customerName = "customer1"
        gatewayType = "dedicated"

        """ test create/get/update/delete gateway success """
        # create gateway
        name = os.getenv("DL_SERVICES_GW_NAME")
        gtw_template = GatewayTemplateGatewayTypeDedicatedTemplate(name=name,
            type=gatewayType, speed_mbps=speedMbps, global_=global_bool,
            bgp_asn=bgpAsn, bgp_base_cidr=bgpBaseCidr, metered=metered, 
            carrier_name=carrierName, cross_connect_router=crossConnectRouter,
            customer_name=customerName, location_name=locationName)
        response = self.dl.create_gateway(gateway_template=gtw_template)
        assert response is not None
        assert response.get_status_code() == 201
        gateway_id = response.get_result().get("id")

        # list gateways
        response = self.dl.list_gateways()
        assert response is not None
        assert response.get_status_code() == 200
        gateways = response.get_result().get("gateways")
        list_result = False
        for gateway in gateways:
            if gateway["id"] == gateway_id:
                list_result = True
                break
        assert list_result

        # update gateway name
        update_name = os.getenv("DL_SERVICES_GW_NAME")+"-PATCH"
        response = self.dl.update_gateway(id=gateway_id,
            name=update_name, metered=True)
        assert response is not None
        assert response.get_status_code() == 200
        assert response.get_result()["name"] == update_name

        # delete gateway
        self.delete_gateway(gateway_id)
    
    # def test_2_macsec_gateway_actions(self):
        # bgpAsn = 64999
        # bgpBaseCidr = "169.254.0.0/16"
        # crossConnectRouter = "LAB-xcr01.lab0907"
        # global_bool = True
        # locationName = os.getenv("DL_SERVICES_LOCATION_NAME")
        # speedMbps = 10000
        # metered = False
        # carrierName = "carrier1"
        # customerName = "customer1"
        # gatewayType = "dedicated"
        # macsec_active_bool = True
        # macsecActiveCak = os.getenv("DL_SERVICES_PRIMARY_CAK")
        # macsecFallbackCak = os.getenv("DL_SERVICES_FALLBACK_CAK")

        # """ test create/get/update/delete gateway success """
        # # create gateway
        # name = os.getenv("DL_SERVICES_GW_NAME")
        # primary_cak_template = GatewayMacsecConfigTemplatePrimaryCak(crn=macsecActiveCak)
        # macsec_template = GatewayMacsecConfigTemplate(active=macsec_active_bool, primary_cak=primary_cak_template)
        # gtw_template = GatewayTemplateGatewayTypeDedicatedTemplate(name=name,
        #     type=gatewayType, speed_mbps=speedMbps, global_=global_bool,
        #     bgp_asn=bgpAsn, bgp_base_cidr=bgpBaseCidr, metered=metered, 
        #     carrier_name=carrierName, cross_connect_router=crossConnectRouter,
        #     customer_name=customerName, location_name=locationName, macsec_config=macsec_template)
        # response = self.dl.create_gateway(gateway_template=gtw_template)
        # assert response is not None
        # assert response.get_status_code() == 201
        # assert response.get_result().get("macsec_config") is not None
        # gateway_id = response.get_result().get("id")

        # # update gateway name
        # update_name = os.getenv("DL_SERVICES_GW_NAME")+"-PATCH"
        # fallback_cak_template = GatewayMacsecConfigPatchTemplateFallbackCak(crn=macsecFallbackCak)
        # macsec_patch_template = GatewayMacsecConfigPatchTemplate(fallback_cak=fallback_cak_template)
        # response = self.dl.update_gateway(id=gateway_id,macsec_config=macsec_patch_template )
        # assert response is not None
        # assert response.get_status_code() == 200
        # assert response.get_result().get("macsec_config") is not None
        # assert response.get_result()["name"] == update_name

        # # delete gateway
        # self.delete_gateway(gateway_id)
        
################### Ports ############################
    def test_1_list_get_ports(self):
        response = self.dl.list_ports()
        assert response is not None

        port_id = response.get_result().get("ports")[0].get("id")

        # get a port
        response = self.dl.get_port(id=port_id)
        assert response.get_status_code() == 200


################## Offering Types ###########################################
    def test1_offering_type_locations(self):
        """ test getting all locations by offering type """
        response = self.dl.list_offering_type_locations(
            offering_type="dedicated")
        assert response is not None
        assert response.get_status_code() == 200
        assert response.get_result() is not None

    def test1_offering_type_locations_cross_connect_router(self):
        """ test getting location info by short name """
        locationName = os.getenv("DL_SERVICES_LOCATION_NAME")
        response = self.dl.list_offering_type_location_cross_connect_routers(
            offering_type="dedicated", location_name=locationName)
        assert response is not None
        assert response.get_status_code() == 200
        assert response.get_result() is not None

    def test2_offering_type_locations_cross_connect_router(self):
        """ test getting location info by long name """
        locationLongName = os.getenv("DL_SERVICES_LOCATION_LONG_NAME")
        response = self.dl.list_offering_type_location_cross_connect_routers(
            offering_type="dedicated", location_name=locationLongName)
        assert response is not None
        assert response.get_status_code() == 200
        assert response.get_result() is not None

    def test1_offering_type_speeds(self):
        """ test getting all sppeds by offering type """
        response = self.dl.list_offering_type_speeds(
            offering_type="dedicated")
        assert response is not None
        assert response.get_status_code() == 200
        assert response.get_result() is not None



################## Virtual Connections ######################################
    def test_1_gateway_vc_actions(self):
        """ test create/get/update/delete gateway connections success """
        bgpAsn = 64999
        bgpBaseCidr = "169.254.0.0/16"
        crossConnectRouter = "LAB-xcr01.dal09"
        global_bool = True
        locationName = os.getenv("DL_SERVICES_LOCATION_NAME")
        speedMbps = 1000
        metered = False
        carrierName = "carrier1"
        customerName = "customer1"
        gatewayType = "dedicated"

        """ test create/get/update/delete gateway success """
        # create gateway
        name = os.getenv("DL_SERVICES_GW_NAME")
        gtw_template = GatewayTemplateGatewayTypeDedicatedTemplate(name=name,
            type=gatewayType, speed_mbps=speedMbps, global_=global_bool,
            bgp_asn=bgpAsn, bgp_base_cidr=bgpBaseCidr, metered=metered, 
            carrier_name=carrierName, cross_connect_router=crossConnectRouter,
            customer_name=customerName, location_name=locationName)
        response = self.dl.create_gateway(gateway_template=gtw_template)
        assert response is not None
        assert response.get_status_code() == 201
        gateway_id = response.get_result().get("id")

        # create virtual connection
        name = os.getenv("DL_SERVICES_CONN_NAME")
        crn = os.getenv("DL_SERVICES_VPC_CRN")
        response = self.dl.create_gateway_virtual_connection(
            gateway_id=gateway_id, type="vpc", name=name,
            network_id=crn)
        assert response is not None
        assert response.get_status_code() == 201
        conn_id = response.get_result()["id"]

        # list gateway connections
        response = self.dl.list_gateway_virtual_connections(
            gateway_id=gateway_id)
        assert response is not None
        assert response.get_status_code() == 200
        conns = response.get_result().get("virtual_connections")
        list_result = False
        for conn in conns:
            if conn["id"] == conn_id:
                list_result = True
                break
        assert list_result

        # update gateway connection
        name = "update"+os.getenv("DL_SERVICES_CONN_NAME")
        response = self.dl.update_gateway_virtual_connection(
            gateway_id=gateway_id, id=conn_id, name=name)
        assert response is not None
        assert response.get_status_code() == 200
        assert response.get_result()["name"] == name

        # delete gateway connection
        self.delete_connection(gateway_id, conn_id)
        
        # delete gateway
        self.delete_gateway(gateway_id)

################### LOA and Completion Notice #######################
# notes about LOA and CN testing.  When a GW is created, a github issue is also created by dl-rest.  The issue is used for managing the LOA and CN.  In normal operation,
# an LOA is added to the issue via manual GH interaction.  After that occurs and the GH label changed, then CN upload is allowed.  Since we do not have the ability to
# do the manual steps for integration testing, the test will only do the following
#  - Issue GET LOA for a gateway.  It will expect a 404 error since no one has added the LOA to the GH issue
#  - PUT a completion notice to the gw.  It will fail with a 412 error because the GH issue and GW status are in the wrong state due to no manual interaction
#  - GET CN for a gw.  It will expect a 404 since the CN could not be uploaded

    def test_1_loa_and_completion(self):
        bgpAsn = 64999
        bgpBaseCidr = "169.254.0.0/16"
        crossConnectRouter = "LAB-xcr01.dal09"
        global_bool = True
        locationName = os.getenv("DL_SERVICES_LOCATION_NAME")
        speedMbps = 1000
        metered = False
        carrierName = "carrier1"
        customerName = "customer1"
        gatewayType = "dedicated"

        """ test create/get/update/delete gateway success """
        # create gateway
        name = os.getenv("DL_SERVICES_GW_NAME")
        gtw_template = GatewayTemplateGatewayTypeDedicatedTemplate(name=name,
            type=gatewayType, speed_mbps=speedMbps, global_=global_bool,
            bgp_asn=bgpAsn, bgp_base_cidr=bgpBaseCidr, metered=metered, 
            carrier_name=carrierName, cross_connect_router=crossConnectRouter,
            customer_name=customerName, location_name=locationName)
        response = self.dl.create_gateway(gateway_template=gtw_template)
        assert response is not None
        assert response.get_status_code() == 201
        gateway_id = response.get_result().get("id")

        """ get LOA """

        with self.assertRaises(ApiException) as ex:
            response = self.dl.list_gateway_letter_of_authorization(id=gateway_id)
        assert ex.exception.code == 404
        
        """ create completion notice """
        cn = None
        try:
            cn = open("test/integration/completion_notice.pdf", 'rb')
            with self.assertRaises(ApiException) as ex:
                response = self.dl.create_gateway_completion_notice(
                    id=gateway_id, upload=cn)
            assert ex.exception.code == 412
        finally:
            if cn is not None:
                cn.close()
        
        """ get completion notice """
        with self.assertRaises(ApiException) as ex:
            response = self.dl.list_gateway_completion_notice(id=gateway_id)
        assert ex.exception.code == 404

        # delete gateway
        self.delete_gateway(gateway_id)


if __name__ == '__main__':
    unittest.main()
