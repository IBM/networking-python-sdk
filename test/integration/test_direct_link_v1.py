# coding: utf-8

# (C) Copyright IBM Corp. 2023.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Integration test code to execute DirectLink client functions
"""
import datetime
import os
import time
import unittest
import pytest
from ibm_cloud_sdk_core import ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_networking_services import DirectLinkV1
from ibm_cloud_networking_services.direct_link_v1 import (
    GatewayTemplateGatewayTypeDedicatedTemplate,
    AuthenticationKeyIdentity,
    GatewayTemplateGatewayTypeConnectTemplate,
    GatewayPatchTemplate,
    GatewayPortIdentity,
    Gateway,
    AsPrependTemplate,
    GatewayBfdConfigTemplate,
    GatewayBfdPatchTemplate,
    GatewayTemplateRouteFilter,
    UpdateRouteFilterTemplate
)
from dotenv import load_dotenv, find_dotenv

# load the .env file containing your environment variables
try:
    load_dotenv(find_dotenv(filename="dl.env"))
except:
    raise unittest.SkipTest('no dl.env file loaded, skipping...')


class TestDirectLinkV1(unittest.TestCase):
    """ Test class for DirectLink sdk functions """

    @unittest.skip("skipping due to travis timeout error")
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

                if ("SDK-PY" in record.get("name") and "PROVIDER" not in record.get("name")) and (
                        ("delet" not in record.get("operational_status")) and ("progress" not in record.get("operational_status"))):
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

    def get_port_id(self):
        # Fetch the list of ports and use a port to create a connect gateway
        response = self.dl.list_ports()
        assert response is not None

        ports = response.get_result().get("ports")
        port_id = ""
        provider_to_be_used = "DL2-TEST"
        for port in ports:
            if provider_to_be_used in port.get("provider_name"):
                port_id = port.get("id")
                break

        return port_id

    ################## DirectLink Gateways ######################################

    def test_gateway_crud_actions(self):
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
        vlan = 10

        """ test create/get/update/delete gateway success """
        # create gateway
        name = os.getenv("DL_SERVICES_GW_NAME")
        gtw_template = GatewayTemplateGatewayTypeDedicatedTemplate(name=name,
                                                                   type=gatewayType, speed_mbps=speedMbps, global_=global_bool,
                                                                   bgp_asn=bgpAsn, bgp_base_cidr=bgpBaseCidr, metered=metered,
                                                                   carrier_name=carrierName, cross_connect_router=crossConnectRouter,
                                                                   customer_name=customerName, location_name=locationName, vlan=vlan)
        response = self.dl.create_gateway(gateway_template=gtw_template)
        assert response is not None
        assert response.get_status_code() == 201
        gateway_id = response.get_result().get("id")

        # vlan check after create
        assert response.get_result()["vlan"] == vlan

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

        # update gateway name and vlan
        update_name = os.getenv("DL_SERVICES_GW_NAME")+"-PATCH"
        updated_vlan = 99
        gtw_patch_template = GatewayPatchTemplate(
            name=update_name, metered=True, vlan=updated_vlan)
        response = self.dl.update_gateway(
            id=gateway_id, gateway_patch_template=gtw_patch_template)
        assert response is not None
        assert response.get_status_code() == 200
        assert response.get_result()["name"] == update_name

        # vlan check after update
        assert response.get_result()["vlan"] == updated_vlan

        # update for vlan reset
        # gtw_vlan_patch_template = GatewayPatchTemplate(metered=True, vlan=None)
        # to reset vlan, we need pass this as JSON object
        reset_response = self.dl.update_gateway(id=gateway_id, gateway_patch_template={
                                                "metered": True, "vlan": None})
        assert reset_response is not None
        assert reset_response.get_status_code() == 200

        # vlan is unset after update
        assert reset_response.get_result().get("vlan") is None

        # delete gateway
        self.delete_gateway(gateway_id)

    ################### Ports ############################
    def test_list_get_ports(self):
        response = self.dl.list_ports()
        assert response is not None

        port_id = response.get_result().get("ports")[0].get("id")

        # get a port
        response = self.dl.get_port(id=port_id)
        assert response.get_status_code() == 200

    ################## Offering Types ###########################################

    def test_offering_type_locations(self):
        """ test getting all locations by offering type """
        response = self.dl.list_offering_type_locations(
            offering_type="dedicated")
        assert response is not None
        assert response.get_status_code() == 200
        assert response.get_result() is not None

    def test_offering_type_locations_cross_connect_router_short_name(self):
        """ test getting location info by short name """
        locationName = os.getenv("DL_SERVICES_LOCATION_NAME")
        response = self.dl.list_offering_type_location_cross_connect_routers(
            offering_type="dedicated", location_name=locationName)
        assert response is not None
        assert response.get_status_code() == 200
        assert response.get_result() is not None

    def test_offering_type_locations_cross_connect_router_long_name(self):
        """ test getting location info by long name """
        locationLongName = os.getenv("DL_SERVICES_LOCATION_LONG_NAME")
        response = self.dl.list_offering_type_location_cross_connect_routers(
            offering_type="dedicated", location_name=locationLongName)
        assert response is not None
        assert response.get_status_code() == 200
        assert response.get_result() is not None

    def test_offering_type_speeds(self):
        """ test getting all sppeds by offering type """
        response = self.dl.list_offering_type_speeds(
            offering_type="dedicated")
        assert response is not None
        assert response.get_status_code() == 200
        assert response.get_result() is not None
        # Check if we are recieving capabilities as part of 100G changes
        assert response.get_result().get(
            "speeds")[0].get("capabilities") is not None

    ################## Virtual Connections ######################################
    def test_gateway_vc_actions(self):
        pytest.skip("skipping failing test case")
        bgpAsn = 64999
        global_bool = True
        speedMbps = 1000
        metered = False
        gatewayType = "connect"

        """ test create/update/delete gateway with connection_mode success """
        # Get the port id to create a connect gateway
        port_id = self.get_port_id()

        # create connect gateway
        gwPort = GatewayPortIdentity(id=port_id)
        name = os.getenv("DL_SERVICES_GW_NAME") + \
            str("-CONNECT-DLAAS-") + str(int(time.time()))
        gtw_template = GatewayTemplateGatewayTypeConnectTemplate(name=name,
                                                                 type=gatewayType, speed_mbps=speedMbps, global_=global_bool,
                                                                 bgp_asn=bgpAsn, metered=metered, port=gwPort)
        response = self.dl.create_gateway(gateway_template=gtw_template)
        assert response is not None
        assert response.get_status_code() == 201
        gateway_id = response.get_result().get("id")

        # check gateway status until provisioned
        count = 0
        while count < 24:
            response = self.dl.get_gateway(id=gateway_id)
            status = response.get_result()["operational_status"]
            ret_id = response.get_result()["id"]
            assert ret_id == gateway_id
            assert response.get_status_code() == 200
            if status == "provisioned":
                break
            else:
                time.sleep(5)
                count += 1

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

        # create gateway route report
        response = self.dl.create_gateway_route_report(
            gateway_id=gateway_id)

        assert response is not None
        assert response.get_status_code() == 202
        assert response.get_result().get("id") != ""
        assert response.get_result().get("status") != ""
        assert response.get_result().get("created_at") != ""
        assert response.get_result().get("virtual_connections") != None

        # Wait until route report status = complete
        route_report_id = response.get_result().get("id")
        count = 0
        while count < 24:
            response = self.dl.get_gateway_route_report(
                gateway_id=gateway_id, id=route_report_id)
            status = response.get_result()["status"]
            ret_id = response.get_result()["id"]
            assert ret_id == route_report_id
            assert response.get_status_code() == 200
            if status == "complete":
                break
            else:
                time.sleep(5)
                count += 1

        # list route reports
        response = self.dl.list_gateway_route_reports(
            gateway_id=gateway_id)
        assert response is not None
        assert response.get_status_code() == 200

        # successfully delete route report
        response = self.dl.delete_gateway_route_report(
            gateway_id=gateway_id,
            id=route_report_id
        )
        assert response is not None
        assert response.get_status_code() == 204

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

    def test_loa_and_completion(self):
        pytest.skip("skipping failing test case")
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
            response = self.dl.list_gateway_letter_of_authorization(
                id=gateway_id)
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

    ################## Direct Link Gateways with Customer API MD5 Auth ############################

    def test_gateway_with_md5(self):
        pytest.skip("skipping failing test case")
        bgpAsn = 64999
        crossConnectRouter = "LAB-xcr01.dal09"
        global_bool = True
        locationName = os.getenv("DL_SERVICES_LOCATION_NAME")
        speedMbps = 1000
        metered = False
        carrierName = "carrier1"
        customerName = "customer1"
        gatewayType = "dedicated"
        authKeyCrn = os.getenv("DL_SERVICES_AUTHENTICATION_KEY")
        authKey = AuthenticationKeyIdentity(crn=authKeyCrn)

        """ test create/update/delete gateway with authentication ket success """
        # create gateway with authentication key
        name = os.getenv("DL_SERVICES_GW_NAME") + str(int(time.time()))
        gtw_template = GatewayTemplateGatewayTypeDedicatedTemplate(name=name,
                                                                   type=gatewayType, speed_mbps=speedMbps, global_=global_bool,
                                                                   bgp_asn=bgpAsn, metered=metered,
                                                                   carrier_name=carrierName, cross_connect_router=crossConnectRouter,
                                                                   customer_name=customerName, location_name=locationName,
                                                                   authentication_key=authKey)
        response = self.dl.create_gateway(gateway_template=gtw_template)
        assert response is not None
        assert response.get_status_code() == 201
        gateway_id = response.get_result().get("id")

        res = response.get_result()
        assert res["name"] == name
        assert res["authentication_key"]["crn"] == authKeyCrn
        assert response.get_result().get("authentication_key") is not None

        # clear the authentication for the created gateway\
        updAuthKey = AuthenticationKeyIdentity(crn="")
        response = self.dl.update_gateway(id=gateway_id,
                                          authentication_key=updAuthKey)
        assert response is not None
        assert response.get_status_code() == 200
        assert response.get_result()["name"] == name
        assert response.get_result()["id"] == gateway_id
        assert response.get_result().get("authentication_key") is None

        # delete gateway
        self.delete_gateway(gateway_id)

    ################## Direct Link Dedicated Gateways with Connection Mode ############################

    def test_dedicated_gateway_with_connection_mode(self):
        bgpAsn = 64999
        crossConnectRouter = "LAB-xcr01.dal09"
        global_bool = True
        locationName = os.getenv("DL_SERVICES_LOCATION_NAME")
        speedMbps = 1000
        metered = False
        carrierName = "carrier1"
        customerName = "customer1"
        gatewayType = "dedicated"
        connectionMode = "transit"

        """ test create/update/delete gateway with connection_mode success """
        # create gateway with connection_mode as transit
        name = os.getenv("DL_SERVICES_GW_NAME") + \
            str("-DEDICATED-DLAAS-") + str(int(time.time()))
        gtw_template = GatewayTemplateGatewayTypeDedicatedTemplate(name=name,
                                                                   type=gatewayType, speed_mbps=speedMbps, global_=global_bool,
                                                                   bgp_asn=bgpAsn, metered=metered,
                                                                   carrier_name=carrierName, cross_connect_router=crossConnectRouter,
                                                                   customer_name=customerName, location_name=locationName,
                                                                   connection_mode=connectionMode)
        response = self.dl.create_gateway(gateway_template=gtw_template)
        assert response is not None
        assert response.get_status_code() == 201
        gateway_id = response.get_result().get("id")

        res = response.get_result()
        assert res["name"] == name
        assert res["connection_mode"] == connectionMode

        # update the connection_mode to direct
        response = self.dl.update_gateway(id=gateway_id,
                                          connection_mode="direct")
        assert response is not None
        assert response.get_status_code() == 200
        assert response.get_result()["name"] == name
        assert response.get_result()["id"] == gateway_id
        assert response.get_result()["connection_mode"] == "direct"

        # delete gateway
        self.delete_gateway(gateway_id)

    ################## Direct Link Connect Gateways with Connection Mode ############################

    def test_connect_gateway_with_connection_mode(self):
        pytest.skip("skipping failing test case")
        bgpAsn = 64999
        global_bool = True
        speedMbps = 1000
        metered = False
        gatewayType = "connect"
        connectionMode = "direct"

        """ test create/update/delete gateway with connection_mode success """
        # Get the port id to create a connect gateway
        port_id = self.get_port_id()

        # create gateway with connection_mode as transit
        gwPort = GatewayPortIdentity(id=port_id)
        name = os.getenv("DL_SERVICES_GW_NAME") + \
            str("-CONNECT-DLAAS-") + str(int(time.time()))
        gtw_template = GatewayTemplateGatewayTypeConnectTemplate(name=name,
                                                                 type=gatewayType, speed_mbps=speedMbps, global_=global_bool,
                                                                 bgp_asn=bgpAsn, metered=metered, connection_mode=connectionMode, port=gwPort)
        response = self.dl.create_gateway(gateway_template=gtw_template)
        assert response is not None
        assert response.get_status_code() == 201
        gateway_id = response.get_result().get("id")

        res = response.get_result()
        assert res["name"] == name
        assert res["connection_mode"] == connectionMode

        # check gateway status until provisioned
        count = 0
        while count < 24:
            response = self.dl.get_gateway(id=gateway_id)
            status = response.get_result()["operational_status"]
            ret_id = response.get_result()["id"]
            assert ret_id == gateway_id
            assert response.get_status_code() == 200
            if status == "provisioned":
                break
            else:
                time.sleep(5)
                count += 1

        # update the connection_mode to direct
        response = self.dl.update_gateway(id=gateway_id,
                                          connection_mode="transit")
        assert response is not None
        assert response.get_status_code() == 200
        assert response.get_result()["name"] == name
        assert response.get_result()["id"] == gateway_id
        assert response.get_result()["connection_mode"] == "transit"

        # check gateway status until provisioned
        count = 0
        while count < 24:
            response = self.dl.get_gateway(id=gateway_id)
            status = response.get_result()["operational_status"]
            ret_id = response.get_result()["id"]
            assert ret_id == gateway_id
            assert response.get_status_code() == 200
            if status == "provisioned":
                break
            else:
                time.sleep(5)
                count += 1

        # delete gateway
        self.delete_gateway(gateway_id)

    ################## Direct Link Dedicated Gateways with BGP IP Update ############################

    def test_dedicated_gateway_with_bgp_ip_update(self):
        pytest.skip("skipping failing test case")
        bgpAsn = 64999
        crossConnectRouter = "LAB-xcr01.dal09"
        global_bool = True
        locationName = os.getenv("DL_SERVICES_LOCATION_NAME")
        speedMbps = 1000
        metered = False
        carrierName = "carrier1"
        customerName = "customer1"
        gatewayType = "dedicated"

        """ test create/update/delete gateway with bgp_asn bgp_cer_cidr bgp_ibm_cidr success """
        # create a dedicated gateway
        name = os.getenv("DL_SERVICES_GW_NAME") + \
            str("-DEDICATED-BGP-IP-UPDATE-") + str(int(time.time()))
        gtw_template = GatewayTemplateGatewayTypeDedicatedTemplate(name=name,
                                                                   type=gatewayType, speed_mbps=speedMbps, global_=global_bool,
                                                                   bgp_asn=bgpAsn, metered=metered,
                                                                   carrier_name=carrierName, cross_connect_router=crossConnectRouter,
                                                                   customer_name=customerName, location_name=locationName)
        response = self.dl.create_gateway(gateway_template=gtw_template)
        assert response is not None
        assert response.get_status_code() == 201
        gateway_id = response.get_result().get("id")

        res = response.get_result()
        assert res["name"] == name

        # update the bgp_asn
        response = self.dl.update_gateway(id=gateway_id,
                                          bgp_asn=63999)
        assert response is not None
        assert response.get_status_code() == 200
        assert response.get_result()["name"] == name
        assert response.get_result()["id"] == gateway_id
        assert response.get_result()["bgp_asn"] == 63999

        # update the bgp ip cer and ibm cidr
        try:
            response = self.dl.update_gateway(id=gateway_id,
                                              bgp_cer_cidr="172.17.252.2/29", bgp_ibm_cidr="172.17.252.1/29")
            assert response.get_status_code() == 200
            assert response.get_result()["name"] == name
            assert response.get_result()["id"] == gateway_id
            assert response.get_result()["bgp_asn"] == 63999
        except ApiException as e:
            assert e.code == 400
            assert e.detail == "Please make sure localIP and remoteIP are not in use"

        # delete gateway
        self.delete_gateway(gateway_id)

    ################## Direct Link Connect Gateways with Connection Mode ############################

    def test_connect_gateway_with_bgp_ip_update(self):
        pytest.skip("skipping failing test case")
        bgpAsn = 64999
        global_bool = True
        speedMbps = 1000
        metered = False
        gatewayType = "connect"

        """ test create/update/delete gateway with bgp_asn bgp_cer_cidr bgp_ibm_cidr success """
        # Get the port id to create a connect gateway
        port_id = self.get_port_id()

        # create a connect gateway
        gwPort = GatewayPortIdentity(id=port_id)
        name = os.getenv("DL_SERVICES_GW_NAME") + \
            str("-DEDICATED-BGP-IP-UPDATE-") + str(int(time.time()))
        gtw_template = GatewayTemplateGatewayTypeConnectTemplate(name=name,
                                                                 type=gatewayType, speed_mbps=speedMbps, global_=global_bool,
                                                                 bgp_asn=bgpAsn, metered=metered, port=gwPort)
        response = self.dl.create_gateway(gateway_template=gtw_template)
        assert response is not None
        assert response.get_status_code() == 201
        gateway_id = response.get_result().get("id")

        res = response.get_result()
        assert res["name"] == name

        # check gateway status until provisioned
        count = 0
        while count < 24:
            response = self.dl.get_gateway(id=gateway_id)
            status = response.get_result()["operational_status"]
            ret_id = response.get_result()["id"]
            assert ret_id == gateway_id
            assert response.get_status_code() == 200
            if status == "provisioned":
                break
            else:
                time.sleep(5)
                count += 1

        # update the bgp_asn
        response = self.dl.update_gateway(id=gateway_id,
                                          bgp_asn=63999)
        assert response is not None
        assert response.get_status_code() == 200
        assert response.get_result()["name"] == name
        assert response.get_result()["id"] == gateway_id
        assert response.get_result()["bgp_asn"] == 63999

        # check gateway status until provisioned
        count = 0
        while count < 24:
            response = self.dl.get_gateway(id=gateway_id)
            status = response.get_result()["operational_status"]
            ret_id = response.get_result()["id"]
            assert ret_id == gateway_id
            assert response.get_status_code() == 200
            if status == "provisioned":
                break
            else:
                time.sleep(5)
                count += 1

        # update the bgp ip cer and ibm cidr
        try:
            response = self.dl.update_gateway(id=gateway_id,
                                              bgp_cer_cidr="172.17.252.2/29", bgp_ibm_cidr="172.17.252.1/29")
            assert response.get_status_code() == 200
            assert response.get_result()["name"] == name
            assert response.get_result()["id"] == gateway_id
            assert response.get_result()["bgp_cer_cidr"] == "172.17.252.2/29"
            assert response.get_result()["bgp_ibm_cidr"] == "172.17.252.1/29"
        except ApiException as e:
            assert e.code == 400
            assert e.detail == "Please make sure localIP and remoteIP are not in use"

        # check gateway status until provisioned
        count = 0
        while count < 24:
            response = self.dl.get_gateway(id=gateway_id)
            status = response.get_result()["operational_status"]
            ret_id = response.get_result()["id"]
            assert ret_id == gateway_id
            assert response.get_status_code() == 200
            if status == "provisioned":
                break
            else:
                time.sleep(5)
                count += 1

        # delete gateway
        self.delete_gateway(gateway_id)

    ################## Direct Link Dedicated Gateways with BFD Config ############################

    def test_dedicated_gateway_with_bfd_config(self):
        bgpAsn = 64999
        crossConnectRouter = "LAB-xcr01.dal09"
        global_bool = True
        locationName = os.getenv("DL_SERVICES_LOCATION_NAME")
        speedMbps = 1000
        metered = False
        carrierName = "carrier1"
        customerName = "customer1"
        gatewayType = "dedicated"

        bfdInterval = 1000
        bfdMultiplier = 2
        bfdConfig = GatewayBfdConfigTemplate(
            interval=bfdInterval, multiplier=bfdMultiplier)

        """ test create/update/delete gateway with bfd_config """
        # create a dedicated gateway
        name = os.getenv("DL_SERVICES_GW_NAME") + \
            str("-DEDICATED-BFD-") + str(int(time.time()))
        gtw_template = GatewayTemplateGatewayTypeDedicatedTemplate(name=name,
                                                                   type=gatewayType, speed_mbps=speedMbps, global_=global_bool,
                                                                   bgp_asn=bgpAsn, metered=metered,
                                                                   carrier_name=carrierName, cross_connect_router=crossConnectRouter,
                                                                   customer_name=customerName, location_name=locationName, bfd_config=bfdConfig)
        response = self.dl.create_gateway(gateway_template=gtw_template)
        assert response is not None
        assert response.get_status_code() == 201
        assert response.get_result()["bfd_config"]["interval"] == bfdInterval
        assert response.get_result(
        )["bfd_config"]["multiplier"] == bfdMultiplier
        gateway_id = response.get_result().get("id")

        res = response.get_result()
        assert res["name"] == name

        # update the bfd_config
        updatedBfdInterval = 700
        updatedBfdMultiplier = 10
        updatedBfdConfig = GatewayBfdPatchTemplate(
            interval=updatedBfdInterval, multiplier=updatedBfdMultiplier)
        response = self.dl.update_gateway(id=gateway_id,
                                          bfd_config=updatedBfdConfig)
        assert response is not None
        assert response.get_status_code() == 200
        assert response.get_result()["name"] == name
        assert response.get_result()["id"] == gateway_id
        assert response.get_result(
        )["bfd_config"]["interval"] == updatedBfdInterval
        assert response.get_result(
        )["bfd_config"]["multiplier"] == updatedBfdMultiplier

        # delete gateway
        self.delete_gateway(gateway_id)

    ################## Direct Link Connect Gateways BFD Config ############################

    def test_connect_gateway_with_bfd_config(self):
        pytest.skip("skipping failing test case")
        bgpAsn = 64999
        global_bool = True
        speedMbps = 1000
        metered = False
        gatewayType = "connect"

        """ test create/update/delete gateway with bfd_config """
        # Get the port id to create a connect gateway
        port_id = self.get_port_id()

        # create a connect gateway
        gwPort = GatewayPortIdentity(id=port_id)
        name = os.getenv("DL_SERVICES_GW_NAME") + \
            str("-DEDICATED-BFD-CONFIG-") + str(int(time.time()))

        bfdInterval = 1000
        bfdMultiplier = 2
        bfdConfig = GatewayBfdConfigTemplate(
            interval=bfdInterval, multiplier=bfdMultiplier)

        gtw_template = GatewayTemplateGatewayTypeConnectTemplate(name=name,
                                                                 type=gatewayType, speed_mbps=speedMbps, global_=global_bool,
                                                                 bgp_asn=bgpAsn, metered=metered, port=gwPort, bfd_config=bfdConfig)
        response = self.dl.create_gateway(gateway_template=gtw_template)
        assert response is not None
        assert response.get_status_code() == 201
        gateway_id = response.get_result().get("id")

        res = response.get_result()
        assert res["name"] == name

        # check gateway status until provisioned
        count = 0
        while count < 24:
            response = self.dl.get_gateway(id=gateway_id)
            status = response.get_result()["operational_status"]
            ret_id = response.get_result()["id"]
            assert ret_id == gateway_id
            assert response.get_status_code() == 200
            if status == "provisioned":
                break
            else:
                time.sleep(5)
                count += 1

        # update the bfd_config
        updatedBfdInterval = 700
        updatedBfdMultiplier = 10
        updatedBfdConfig = GatewayBfdPatchTemplate(
            interval=updatedBfdInterval, multiplier=updatedBfdMultiplier)
        response = self.dl.update_gateway(id=gateway_id,
                                          bfd_config=updatedBfdConfig)
        assert response is not None
        assert response.get_status_code() == 200
        assert response.get_result()["name"] == name
        assert response.get_result()["id"] == gateway_id
        assert response.get_result(
        )["bfd_config"]["interval"] == updatedBfdInterval
        assert response.get_result(
        )["bfd_config"]["multiplier"] == updatedBfdMultiplier

        # check gateway status until provisioned
        count = 0
        while count < 24:
            response = self.dl.get_gateway(id=gateway_id)
            status = response.get_result()["operational_status"]
            ret_id = response.get_result()["id"]
            assert ret_id == gateway_id
            assert response.get_status_code() == 200
            if status == "provisioned":
                break
            else:
                time.sleep(5)
                count += 1

        # delete gateway
        self.delete_gateway(gateway_id)

    ################## Direct Link Dedicated Gateways Status ############################

    def test_dedicated_gateway_with_status(self):
        bgpAsn = 64999
        crossConnectRouter = "LAB-xcr01.dal09"
        global_bool = True
        locationName = os.getenv("DL_SERVICES_LOCATION_NAME")
        speedMbps = 1000
        metered = False
        carrierName = "carrier1"
        customerName = "customer1"
        gatewayType = "dedicated"

        bfdInterval = 1000
        bfdMultiplier = 2
        bfdConfig = GatewayBfdConfigTemplate(
            interval=bfdInterval, multiplier=bfdMultiplier)

        """ test create/update/delete gateway with get gateway status """
        # create a dedicated gateway
        name = os.getenv("DL_SERVICES_GW_NAME") + \
            str("-DEDICATED-GW-STATUS") + str(int(time.time()))
        gtw_template = GatewayTemplateGatewayTypeDedicatedTemplate(name=name,
                                                                   type=gatewayType, speed_mbps=speedMbps, global_=global_bool,
                                                                   bgp_asn=bgpAsn, metered=metered,
                                                                   carrier_name=carrierName, cross_connect_router=crossConnectRouter,
                                                                   customer_name=customerName, location_name=locationName, bfd_config=bfdConfig)
        response = self.dl.create_gateway(gateway_template=gtw_template)
        assert response is not None
        assert response.get_status_code() == 201
        assert response.get_result()["bfd_config"]["interval"] == bfdInterval
        assert response.get_result(
        )["bfd_config"]["multiplier"] == bfdMultiplier
        gateway_id = response.get_result().get("id")

        res = response.get_result()
        assert res["name"] == name

        # get the gateway status
        response = self.dl.get_gateway_status(id=gateway_id, type="link")
        assert response is not None
        assert response.get_status_code() == 200
        assert response.get_result()["status"] is not None

        # delete gateway
        self.delete_gateway(gateway_id)

    ################## Direct Link AS Prepends ############################
    def test_gateway_as_prepends(self):

        # Construct a dict representation of a AsPrependTemplate model
        as_prepend_template_model = AsPrependTemplate(
            length=4, policy='import', specific_prefixes=['172.17.0.0/16'])

        """ test create gateway with as_prepends """
        bgpAsn = 64999
        crossConnectRouter = "LAB-xcr01.dal09"
        global_bool = True
        locationName = os.getenv("DL_SERVICES_LOCATION_NAME")
        speedMbps = 1000
        metered = False
        carrierName = "carrier1"
        customerName = "customer1"
        gatewayType = "dedicated"

        # create a dedicated gateway
        name = os.getenv("DL_SERVICES_GW_NAME") + \
            str("-DEDICATED-BFD-") + str(int(time.time()))
        gtw_template = GatewayTemplateGatewayTypeDedicatedTemplate(name=name,
                                                                   type=gatewayType, speed_mbps=speedMbps, global_=global_bool,
                                                                   bgp_asn=bgpAsn, metered=metered,
                                                                   carrier_name=carrierName, cross_connect_router=crossConnectRouter,
                                                                   customer_name=customerName, location_name=locationName, as_prepends=[as_prepend_template_model])
        response = self.dl.create_gateway(gateway_template=gtw_template)
        print(response)
        assert response is not None
        assert response.get_status_code() == 201
        gateway_id = response.get_result().get("id")
        gateway_as_prepends = response.get_result().get("as_prepends")
        assert gateway_as_prepends[0]['specific_prefixes'][0] == '172.17.0.0/16'

        """ Test list gateway as_prepends"""
        asp_list_response = self.dl.list_gateway_as_prepends(gateway_id)
        assert asp_list_response.status_code == 200
        asp_list_result = asp_list_response.get_result()
        assert asp_list_result['as_prepends'][0]['specific_prefixes'][0] == '172.17.0.0/16'

        """Test put gateway as_prepends"""
        etag = asp_list_response.get_headers()['etag']

        as_prepend_prefix_array_template_model = AsPrependTemplate(
            length=4, policy='import', specific_prefixes=['192.168.3.0/24'])

        asp_put_response = self.dl.replace_gateway_as_prepends(
            gateway_id, as_prepends=[as_prepend_prefix_array_template_model], if_match=etag)
        assert asp_put_response.get_status_code() == 201

        # delete gateway
        self.delete_gateway(gateway_id)

    ################## Direct Link Export/Import Route Filters ############################
    def test_gateway_export_import_route_filter(self):

        # Construct a dict representation of a AsPrependTemplate
        as_prepend_template_model = AsPrependTemplate(
            length=4, policy='import', specific_prefixes=['172.17.0.0/16'])
        # Construct a dict representation of a RouteFilterTemplate
        route_filter_template_model = GatewayTemplateRouteFilter(action='permit',
                                                                 prefix='192.168.100.0/24',
                                                                 ge=25,
                                                                 le=30)

        """ test create gateway with export/import route filters """
        bgpAsn = 64999
        crossConnectRouter = "LAB-xcr01.dal09"
        global_bool = True
        locationName = os.getenv("DL_SERVICES_LOCATION_NAME")
        speedMbps = 1000
        metered = False
        carrierName = "carrier1"
        customerName = "customer1"
        gatewayType = "dedicated"

        # create a dedicated gateway
        name = os.getenv("DL_SERVICES_GW_NAME") + \
            str("-DEDICATED-BGPRF-") + str(int(time.time()))
        gtw_template = GatewayTemplateGatewayTypeDedicatedTemplate(name=name,
                                                                   type=gatewayType, speed_mbps=speedMbps, global_=global_bool,
                                                                   bgp_asn=bgpAsn, metered=metered, carrier_name=carrierName,
                                                                   cross_connect_router=crossConnectRouter, customer_name=customerName,
                                                                   location_name=locationName, as_prepends=[
                                                                       as_prepend_template_model],
                                                                   default_export_route_filter='permit', default_import_route_filter='permit',
                                                                   export_route_filters=[route_filter_template_model], import_route_filters=[route_filter_template_model])
        response = self.dl.create_gateway(gateway_template=gtw_template)
        print(response)
        assert response is not None
        assert response.get_status_code() == 201
        gateway_id = response.get_result().get("id")
        gateway_route_filter_action = response.get_result().get(
            "default_export_route_filter")
        assert gateway_route_filter_action == 'permit'
        time.sleep(15)

        # erf - export_route_filter

        """ Test create gateway export route filters"""
        erf_create_response = self.dl.create_gateway_export_route_filter(
            gateway_id, action='permit', prefix='172.168.100.0/24', ge=25, le=30)
        assert erf_create_response.status_code == 201
        time.sleep(15)

        """ Test list gateway export route filters"""
        erf_list_response = self.dl.list_gateway_export_route_filters(
            gateway_id)
        assert erf_list_response.status_code == 200
        erf_list_result = erf_list_response.get_result()
        assert erf_list_result['export_route_filters'][0]['prefix'] == '192.168.100.0/24'
        print(erf_list_response.headers)
        etag = erf_list_response.headers['etag']

        """ Test put gateway export route filters"""
        erf_collection_template = [GatewayTemplateRouteFilter(
            action='permit', prefix='100.100.101.0/24', ge=25, le=30)]
        erf_put_response = self.dl.replace_gateway_export_route_filters(
            if_match=etag,
            gateway_id=gateway_id,
            export_route_filters=erf_collection_template)
        erf_put_result = erf_put_response.get_result()
        erf_id = erf_put_result['export_route_filters'][0]['id']

        assert erf_put_response.status_code == 201
        assert len(erf_put_result['export_route_filters']) == 1
        time.sleep(15)

        """ Test get gateway export route filter"""
        erf_get_response = self.dl.get_gateway_export_route_filter(
            gateway_id, erf_id)
        erf_get_result = erf_get_response.get_result()

        assert erf_get_response.status_code == 200
        assert erf_get_result['prefix'] == '100.100.101.0/24'

        """ Test update gateway export route filter"""
        update_erf_template = UpdateRouteFilterTemplate(
            prefix='101.100.100.0/24')
        erf_update_response = self.dl.update_gateway_export_route_filter(
            gateway_id, erf_id, update_erf_template)

        assert erf_update_response.status_code == 200
        time.sleep(15)

        """ Test delete gateway export route filter"""
        erf_delete_response = self.dl.delete_gateway_export_route_filter(
            gateway_id, erf_id)
        assert erf_delete_response.status_code == 204

        # irf - import_route_filter

        """ Test create gateway import route filters"""
        irf_create_response = self.dl.create_gateway_import_route_filter(
            gateway_id, action='permit', prefix='172.168.100.0/24', ge=25, le=30)
        assert irf_create_response.status_code == 201
        time.sleep(15)

        """ Test list gateway import route filters"""
        irf_list_response = self.dl.list_gateway_import_route_filters(
            gateway_id)
        assert irf_list_response.status_code == 200
        irf_list_result = irf_list_response.get_result()
        assert irf_list_result['import_route_filters'][0]['prefix'] == '192.168.100.0/24'
        print(irf_list_response.headers)
        etag = irf_list_response.headers['etag']

        """ Test put gateway import route filters"""
        irf_collection_template = [GatewayTemplateRouteFilter(
            action='permit', prefix='100.100.101.0/24', ge=25, le=30)]
        irf_put_response = self.dl.replace_gateway_import_route_filters(
            if_match=etag,
            gateway_id=gateway_id,
            import_route_filters=irf_collection_template)
        irf_put_result = irf_put_response.get_result()
        irf_id = irf_put_result['import_route_filters'][0]['id']

        assert irf_put_response.status_code == 201
        assert len(irf_put_result['import_route_filters']) == 1
        time.sleep(15)

        """ Test get gateway import route filter"""
        irf_get_response = self.dl.get_gateway_import_route_filter(
            gateway_id, irf_id)
        irf_get_result = irf_get_response.get_result()

        assert irf_get_response.status_code == 200
        assert irf_get_result['prefix'] == '100.100.101.0/24'

        """ Test update gateway import route filter"""
        update_irf_template = UpdateRouteFilterTemplate(
            prefix='101.100.100.0/24')
        irf_update_response = self.dl.update_gateway_import_route_filter(
            gateway_id, irf_id, update_irf_template)

        assert irf_update_response.status_code == 200
        time.sleep(15)

        """ Test delete gateway import route filter"""
        irf_delete_response = self.dl.delete_gateway_import_route_filter(
            gateway_id, irf_id)
        assert irf_delete_response.status_code == 204

        # delete gateway
        self.delete_gateway(gateway_id)

    ################## Direct Link Route Reports ############################
    def test_gateway_route_reports(self):
        pytest.skip("skipping it due to travis timeout")

        as_prepend_template_model = AsPrependTemplate(
            length=4, policy='import', specific_prefixes=['172.17.0.0/16'])

        """ test create gateway """
        bgpAsn = 64999
        crossConnectRouter = "LAB-xcr01.dal09"
        global_bool = True
        locationName = os.getenv("DL_SERVICES_LOCATION_NAME")
        speedMbps = 1000
        metered = False
        carrierName = "carrier1"
        customerName = "customer1"
        gatewayType = "dedicated"

        # create a dedicated gateway
        name = os.getenv("DL_SERVICES_GW_NAME") + \
            str("-DEDICATED-RR-") + str(int(time.time()))
        gtw_template = GatewayTemplateGatewayTypeDedicatedTemplate(name=name,
                                                                   type=gatewayType, speed_mbps=speedMbps, global_=global_bool,
                                                                   bgp_asn=bgpAsn, metered=metered, carrier_name=carrierName,
                                                                   cross_connect_router=crossConnectRouter, customer_name=customerName,
                                                                   location_name=locationName, as_prepends=[as_prepend_template_model])
        response = self.dl.create_gateway(gateway_template=gtw_template)
        print(response)
        assert response is not None
        assert response.get_status_code() == 201
        gateway_id = response.get_result().get("id")
        time.sleep(15)

        # route_reports

        """ Test create gateway route reports"""
        rr_create_response = self.dl.create_gateway_route_report(gateway_id)
        assert rr_create_response.status_code == 202
        rr_create_result = rr_create_response.get_result()
        assert rr_create_result['id'] is not None
        assert rr_create_result['gateway_routes'] is not None
        assert rr_create_result['virtual_connection_routes'] is not None

        """ Test list gateway route reports"""
        rr_list_response = self.dl.list_gateway_route_reports(gateway_id)
        assert rr_list_response.status_code == 200
        rr_list_result = rr_list_response.get_result()
        assert len(rr_list_result['route_reports']) == 1
        rr_id = rr_list_result['route_reports'][0]['id']
        print(rr_id)

        """ Test get gateway route reports"""
        rr_get_response = self.dl.get_gateway_route_report(
            gateway_id, id=rr_id)
        assert rr_get_response.get_status_code() == 200
        rr_get_result = rr_get_response.get_result()
        assert rr_get_result['id'] is not None
        assert rr_get_result['gateway_routes'] is not None
        assert rr_get_result['virtual_connection_routes'] is not None

        """ Test delete gateway route reports"""
        rr_delete_response = self.dl.delete_gateway_route_report(
            gateway_id, id=rr_id)
        assert rr_delete_response.status_code == 204

        # delete gateway
        self.delete_gateway(gateway_id)

    ################## Direct Link Gateway MACsec ############################
    def test_gateway_macsec(self):

        """ test create gateway """
        bgpAsn = 64999
        crossConnectRouter = "LAB-xcr02.dal09"
        global_bool = True
        locationName = os.getenv("DL_SERVICES_LOCATION_NAME")
        speedMbps = 10000
        metered = True
        carrierName = "PYSDK_TEST_CARRIER"
        customerName = "PYSDK_TEST_CUSTOMER"
        gatewayType = "dedicated"

        # create a dedicated gateway
        name = os.getenv("DL_SERVICES_GW_NAME") + \
            str("-DEDICATED-MACsec-") + str(int(time.time()))
        gtw_template = GatewayTemplateGatewayTypeDedicatedTemplate(name=name,
                                                                   type=gatewayType, speed_mbps=speedMbps, global_=global_bool,
                                                                   bgp_asn=bgpAsn, metered=metered, carrier_name=carrierName,
                                                                   cross_connect_router=crossConnectRouter, customer_name=customerName,
                                                                   location_name=locationName)
        response = self.dl.create_gateway(gateway_template=gtw_template)
        print(response)
        assert response is not None
        assert response.get_status_code() == 201
        gateway_id = response.get_result().get("id")
        time.sleep(15)

        # macsec

        # Construct of HpcsKeyIdentity
        hpcs_key_identity = {}
        hpcs_key_identity['crn'] = 'crn:v1:staging:public:hs-crypto:us-south:a/3f455c4c574447adbc14bda52f80e62f:b2044455-b89e-4c57-96ae-3f17c092dd31:key:ebc0fbe6-fd7c-4971-b127-71a385c8f602'

        # Construct of GatewayMacsecCakPrototype
        gateway_macsec_cak_prototype = {}
        gateway_macsec_cak_prototype['key'] = hpcs_key_identity
        gateway_macsec_cak_prototype['name'] = 'AA01'
        gateway_macsec_cak_prototype['session'] = 'primary'

        # Construct of SakRekeyPrototypeSakRekeyTimerModePrototype
        sak_rekey_prototype = {}
        sak_rekey_prototype['interval'] = 76
        sak_rekey_prototype['mode'] = 'timer'

        # Parameter values
        active = True
        caks = [gateway_macsec_cak_prototype]
        sak_rekey = sak_rekey_prototype
        security_policy = 'must_secure'
        window_size = 522

        """ Test set gateway macsec"""
        macsec_set_response = self.dl.set_gateway_macsec(
            gateway_id,
            active,
            caks,
            sak_rekey,
            security_policy,
            window_size=window_size
        )
        assert macsec_set_response.status_code == 200
        macsec_set_result = macsec_set_response.get_result()
        assert macsec_set_result['active'] == True
        assert macsec_set_result['sak_rekey'] == sak_rekey
        assert macsec_set_result['security_policy'] == 'must_secure'
        assert macsec_set_result['window_size'] == 522

        """ Test get gateway macsec"""
        macsec_get_response = self.dl.get_gateway_macsec(gateway_id)
        assert macsec_get_response.status_code == 200
        macsec_get_result = macsec_get_response.get_result()
        assert macsec_get_result['active'] == True
        assert macsec_get_result['security_policy'] == 'must_secure'
        assert macsec_get_result['window_size'] == 522

        """ Test list gateway macsec caks"""
        macsec_list_caks_response = self.dl.list_gateway_macsec_caks(gateway_id)
        assert macsec_list_caks_response.status_code == 200
        macsec_list_caks_result = macsec_list_caks_response.get_result()
        assert len(macsec_list_caks_result['caks']) == 1
        get_macsec_caks_id = macsec_list_caks_result['caks'][0]['id']

        """ Test get gateway macsec cak"""
        macsec_get_cak_response = self.dl.get_gateway_macsec_cak(gateway_id, get_macsec_caks_id)
        assert macsec_get_cak_response.status_code == 200
        macsec_get_cak_result = macsec_get_cak_response.get_result()
        assert macsec_get_cak_result['id'] == get_macsec_caks_id

        # Construct of HpcsKeyIdentity for create cak
        create_cak_hpcs_key_identity = {}
        create_cak_hpcs_key_identity['crn'] = 'crn:v1:staging:public:hs-crypto:us-south:a/3f455c4c574447adbc14bda52f80e62f:b2044455-b89e-4c57-96ae-3f17c092dd31:key:6f79b964-229c-45ab-b1d9-47e111cd03f6'

        create_cak_key = create_cak_hpcs_key_identity
        create_cak_name = 'BB02'
        create_cak_session = 'fallback'

        """ Test create gateway macsec cak"""
        macsec_create_cak_response = self.dl.create_gateway_macsec_cak(
            gateway_id,
            create_cak_key,
            create_cak_name,
            create_cak_session,
        )
        assert macsec_create_cak_response.status_code == 201
        macsec_create_cak_result = macsec_create_cak_response.get_result()
        assert macsec_create_cak_result['key'] == create_cak_key
        assert macsec_create_cak_result['name'] == create_cak_name
        assert macsec_create_cak_result['session'] == create_cak_session
        macsec_new_cak_id = macsec_create_cak_result['id']

        # Construct of HpcsKeyIdentity for update cak
        update_cak_hpcs_key_identity = {}
        update_cak_hpcs_key_identity['crn'] = 'crn:v1:staging:public:hs-crypto:us-south:a/3f455c4c574447adbc14bda52f80e62f:b2044455-b89e-4c57-96ae-3f17c092dd31:key:6f79b964-229c-45ab-b1d9-47e111cd03f6'

        # Construct of GatewayMacsecCakPatch for update cak
        gateway_macsec_cak_patch = {}
        gateway_macsec_cak_patch['key'] = update_cak_hpcs_key_identity
        gateway_macsec_cak_patch['name'] = 'AA02'

        """ Test update gateway macsec cak"""
        macsec_update_cak_response = self.dl.update_gateway_macsec_cak(
            gateway_id,
            macsec_new_cak_id,
            gateway_macsec_cak_patch,
        )
        assert macsec_update_cak_response.status_code == 201
        macsec_update_cak_result = macsec_update_cak_response.get_result()
        assert macsec_update_cak_result['name'] == 'AA02'

        """ Test delete gateway macsec cak"""
        macsec_delete_cak_response = self.dl.delete_gateway_macsec_cak(gateway_id, macsec_new_cak_id)
        assert macsec_delete_cak_response.status_code == 204

        gateway_macsec_patch = {}
        gateway_macsec_patch['active'] = True
        gateway_macsec_patch['sak_rekey'] = sak_rekey_prototype
        gateway_macsec_patch['security_policy'] = 'must_secure'
        gateway_macsec_patch['window_size'] = 74

        """ Test update gateway macsec"""
        macsec_update_response = self.dl.update_gateway_macsec(
            gateway_id,
            gateway_macsec_patch
        )
        assert macsec_update_response.get_status_code() == 200
        macsec_update_result = macsec_update_response.get_result()
        assert macsec_update_result['window_size'] == gateway_macsec_patch['window_size']

        """ Test unset gateway macsec"""
        macsec_unset_response = self.dl.unset_gateway_macsec(gateway_id)
        assert macsec_unset_response.status_code == 204

        # delete gateway
        self.delete_gateway(gateway_id)


if __name__ == '__main__':
    unittest.main()