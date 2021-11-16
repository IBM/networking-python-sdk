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
    load_dotenv(find_dotenv(filename="transit.env"))
except:
    raise unittest.SkipTest('no transit.env file loaded, skipping...')

class TestTransitGatewayApisV1(unittest.TestCase):
    """ Test class for Transit Gateway sdk functions """

    @unittest.skip("tests exceeds Travis 10 min limit")

    def setUp(self):
        """ test case setup """
        self.endpoint = os.getenv("TG_SERVICES_SERVICE_URL")

        if self.endpoint is None:
            self.skipTest("configuration file unavailable")

        self.version = datetime.date.today()
        authenticator = IAMAuthenticator(
            apikey=os.getenv("TG_SERVICES_APIKEY"), 
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
        # Fetch all gateways from testing account.
        response = self.tg.list_transit_gateways()
        assert response is not None
        assert response.get_status_code() == 200

        # Iterate through every Gateway and delete all resources.
        gateways = response.get_result().get("transit_gateways")
        if gateways is not None:
            for gateway in gateways:
                # Fetch all connections from current gateway.
                gateway_id = gateway["id"]
                conn_response = self.tg.list_transit_gateway_connections(
                    transit_gateway_id=gateway_id)

                assert conn_response is not None
                assert conn_response.get_status_code() == 200

                connections = conn_response.get_result().get("connections")
                if connections is not None:
                    # Deletes GRE Connections first.
                    conn_ids = []
                    for connection in connections:
                        if ("SDK-PY" in connection["name"]) and (
                            "delet" not in connection["status"]):
                            if connection["network_type"] == "gre_tunnel":
                                self.delete_resource_test(gateway_id=gateway_id, 
                                    conn_id=connection["id"], rr_id="")
                            else:
                                conn_ids.append(connection["id"])

                    # Deletes Connections from other types.
                    for id in conn_ids:
                        self.delete_resource_test(gateway_id=gateway_id, 
                            conn_id=id, rr_id="")

                # Deletes current gateway
                if ("SDK-PY" in gateway["name"]) and (
                    "delet" not in gateway["status"]):
                    self.delete_resource_test(gateway_id=gateway_id, 
                        conn_id="", rr_id="")

    
###############################################################################
#                         Transit Locations Tests                             #
###############################################################################
           
    def test_01_transit_gateway_location_actions(self):
        
        ############################################# 
        # Success: LIST Transit Locations: 
        ############################################# 
        response = self.tg.list_gateway_locations()
        assert response is not None
        assert response.get_status_code() == 200

        locations = response.get_result().get("locations")
        assert locations != None
        assert len(locations) > 0

        ############################################# 
        # Success: GET Transit Location:
        ############################################# 
        location_name = locations[0].get("name")
        response = self.tg.get_gateway_location(name=location_name)

        assert response is not None
        assert response.get_status_code() == 200
        assert response.get_result().get("type") != ""
        assert response.get_result().get("name") == location_name
        assert response.get_result().get("billing_location") != ""
        assert response.get_result().get("local_connection_locations") != None

        #############################################
        # Failure: GET Location with invalid Name: 
        #############################################
        bad_name = "bad-loc"
        with self.assertRaises(ApiException) as e:
            self.tg.get_gateway_location(name=bad_name)
            self.assertEqual(e.exception.code, 404)
        

###############################################################################
#                           Transit Gateway Tests                             #
###############################################################################

    def test_02_transit_gateway_actions(self):

        ############################################# 
        # Success: POST Transit Gateway:
        ############################################# 
        name = "_" + time.strftime("%H%M%S")
        location = os.getenv("TG_SERVICES_LOCATION")
        name = os.getenv("TG_SERVICES_GW_NAME") + name
        
        response = self.tg.create_transit_gateway(
            name=name, location=location)

        assert response is not None
        assert response.get_status_code() == 201 
        assert response.get_result().get("name") == name
        assert response.get_result().get("location") == location  
        
        # Wait untilt Gateway status = available
        gateway_id = response.get_result().get("id")
        assert self.is_resource_available(
            gateway_id=gateway_id, conn_id="", rr_id="") 

        #############################################
        # Success: GET Transit Gateway:
        #############################################  
        response = self.tg.get_transit_gateway(id=gateway_id)

        assert response is not None
        assert response.get_status_code() == 200
        assert response.get_result().get("name") == name
        assert response.get_result().get("id") == gateway_id
        assert response.get_result().get("location") == location

        #############################################
        # Success: UPDATE Transit Gateway:
        ############################################# 
        updated_name = "UPDATED-" + name
        response = self.tg.update_transit_gateway(
            id=gateway_id, 
            name=updated_name)

        assert response is not None
        assert response.get_status_code() == 200
        assert response.get_result().get("id") == gateway_id
        assert response.get_result().get("name") == updated_name

        #############################################
        # Success: LIST Transit Gateways: 
        ############################################# 
        response = self.tg.list_transit_gateways()

        assert response is not None
        assert response.get_status_code() == 200
        assert len(response.get_result().get("transit_gateways")) > 0
        
        list_result = False
        gateways = response.get_result().get("transit_gateways")
        for gateway in gateways:
            if gateway["id"] == gateway_id:
                assert gateway["name"] == updated_name
                assert gateway["location"] == location
                list_result = True

                break

        assert list_result

        #############################################
        # Failure: POST Gateway with invalid Location: 
        ############################################# 
        location = "bad-" + os.getenv("TG_SERVICES_LOCATION")
        name = os.getenv("TG_SERVICES_GW_NAME")
        with self.assertRaises(ApiException) as e:
            self.tg.create_transit_gateway(name=name, location=location)
            self.assertEqual(e.exception.code, 404)

        #############################################
        # Failure: POST Gateway with invalid Name:
        #############################################  
        location = os.getenv("TG_SERVICES_LOCATION")
        with self.assertRaises(ApiException) as e:
            self.tg.create_transit_gateway(name="", location=location)
            self.assertEqual(e.exception.code, 400)

        #############################################
        # Failure: GET Gateway with invalid ID:
        ############################################# 
        gatewayID = "123abc" 
        with self.assertRaises(ApiException) as e: 
            self.tg.get_transit_gateway(id=gatewayID) 
            self.assertEqual(e.exception.code, 404)

        #############################################
        # Failure: UPDATE Gateway with invalid ID: 
        ############################################# 
        updated_name = "UPDATED_" + os.getenv("TG_SERVICES_GW_NAME")
        with self.assertRaises(ApiException) as e:   
            self.tg.update_transit_gateway(id="abc123", name=updated_name)
            self.assertEqual(e.exception.code, 404)

        #############################################   
        # Failure: DELETE Gateway with invalid ID: 
        ############################################# 
        badID = "123abc" 
        with self.assertRaises(ApiException) as e: 
            self.tg.delete_transit_gateway(id=badID) 
            self.assertEqual(e.exception.code, 404)

        #############################################
        # Success: DELETE Transit Gateway:
        ############################################# 
        assert self.delete_resource_test(
            gateway_id=gateway_id, conn_id="", rr_id="")

            
###############################################################################
#                     Transit Gateway Connections Tests                       #
###############################################################################

    def test_03_transit_gateway_connection_actions(self):
        
        #############################################
        # Success: POST Parent Transit Gateway:
        #############################################
        gw_name = "_" + time.strftime("%H%M%S")
        location = os.getenv("TG_SERVICES_LOCATION")
        gw_name = os.getenv("TG_SERVICES_GW_NAME") + gw_name
        
        response = self.tg.create_transit_gateway(
            name=gw_name, location=location)

        assert response is not None
        assert response.get_status_code() == 201 
        assert response.get_result().get("id") != ""
        assert response.get_result().get("name") == gw_name
        assert response.get_result().get("location") == location  
        
        # Wait untilt Gateway status = available
        gateway_id = response.get_result().get("id")
        assert self.is_resource_available(
            gateway_id=gateway_id, conn_id="", rr_id="") 

        #############################################
        # Success: POST Transit CLASSIC Connection:
        #############################################
        classic_name = "-Classic_" + time.strftime("%H%M%S")
        classic_name = os.getenv("TG_SERVICES_CONN_NAME") + classic_name
        
        response = self.tg.create_transit_gateway_connection(
            name=classic_name,
            network_type="classic", 
            transit_gateway_id=gateway_id)

        assert response is not None
        assert response.get_status_code() == 201 
        assert response.get_result().get("id") != ""
        assert response.get_result().get("name") == classic_name
        assert response.get_result().get("network_type") == "classic"
        
        # wait until the Connection status = attached
        classic_conn_id = response.get_result().get("id")
        assert self.is_resource_available(gateway_id=gateway_id, 
            conn_id=classic_conn_id, rr_id="")
        
        #############################################     
        # Success: POST Transit VPC Connection:
        #############################################
        vpc_crn = os.getenv("TG_SERVICES_VPC_CRN")
        vpc_name = "-VPC_" + time.strftime("%H%M%S")
        vpc_name = os.getenv("TG_SERVICES_CONN_NAME") + vpc_name
        
        response = self.tg.create_transit_gateway_connection(
            name=vpc_name,
            network_type="vpc", 
            network_id=vpc_crn,
            transit_gateway_id=gateway_id)

        assert response is not None
        assert response.get_status_code() == 201 
        assert response.get_result().get("id") != ""
        assert response.get_result().get("name") == vpc_name
        assert response.get_result().get("network_id") == vpc_crn
        assert response.get_result().get("network_type") == "vpc"
        
        # wait until the Connection status = attached
        vpc_conn_id = response.get_result().get("id")
        assert self.is_resource_available(gateway_id=gateway_id, 
            conn_id=vpc_conn_id, rr_id="")   
        
        #############################################
        # Success: POST Transit DL Connection:
        #############################################
        dl_crn = os.getenv("TG_SERVICES_DL_CRN")
        dl_name = "-DL_" + time.strftime("%H%M%S")
        dl_name =  os.getenv("TG_SERVICES_CONN_NAME") + dl_name 

        response = self.tg.create_transit_gateway_connection(
            name=dl_name,
            network_id=dl_crn,
            network_type="directlink", 
            transit_gateway_id=gateway_id)
            
        assert response is not None
        assert response.get_status_code() == 201 
        assert response.get_result().get("id") != ""
        assert response.get_result().get("name") == dl_name
        assert response.get_result().get("network_id") == dl_crn
        assert response.get_result().get("network_type") == "directlink"
        
        # wait until the Connection status = attached
        dl_conn_id = response.get_result().get("id")
        assert self.is_resource_available(gateway_id=gateway_id, 
            conn_id=dl_conn_id, rr_id="")   
        
        #############################################
        # Success: POST Transit GRE Connection:
        #############################################
        zone = {}; zone['name'] = 'us-south-1'
        gre_name = "-GRE_" + time.strftime("%H%M%S")
        gre_name = os.getenv("TG_SERVICES_CONN_NAME") + gre_name
        
        response = self.tg.create_transit_gateway_connection(
            zone=zone,
            name=gre_name,
            network_type="gre_tunnel", 
            transit_gateway_id=gateway_id,
            local_gateway_ip="192.168.100.1", 
            local_tunnel_ip="192.168.101.1",
            remote_gateway_ip="10.242.63.12",
            remote_tunnel_ip="192.168.101.2",
            base_connection_id=classic_conn_id)

        assert response is not None
        assert response.get_status_code() == 201 
        assert response.get_result().get("id") != ""
        assert response.get_result().get("zone") == zone
        assert response.get_result().get("name") == gre_name
        assert response.get_result().get("network_type") == "gre_tunnel"
        assert response.get_result().get("base_connection_id") == classic_conn_id
        
        # wait until the Connection status = attached
        gre_conn_id = response.get_result().get("id")
        assert self.is_resource_available(gateway_id=gateway_id, 
            conn_id=gre_conn_id, rr_id="")

        #############################################   
        # Success: GET Transit CLASSIC Connection:
        #############################################
        response = self.tg.get_transit_gateway_connection(
            transit_gateway_id=gateway_id, id=classic_conn_id)

        assert response is not None
        assert response.get_status_code() == 200
        assert response.get_result().get("name") == classic_name
        assert response.get_result().get("id") == classic_conn_id 
        assert response.get_result().get("network_type") == "classic"

        #############################################
        # Success: GET Transit VPC Connection:
        #############################################
        response = self.tg.get_transit_gateway_connection(
            transit_gateway_id=gateway_id, id=vpc_conn_id)

        assert response is not None
        assert response.get_status_code() == 200
        assert response.get_result().get("name") == vpc_name
        assert response.get_result().get("id") == vpc_conn_id
        assert response.get_result().get("network_id") == vpc_crn
        assert response.get_result().get("network_type") == "vpc"

        #############################################
        # Success: GET Transit DL Connection:
        #############################################        
        response = self.tg.get_transit_gateway_connection(
            transit_gateway_id=gateway_id, id=dl_conn_id)

        assert response is not None
        assert response.get_status_code() == 200
        assert response.get_result().get("name") == dl_name
        assert response.get_result().get("id") == dl_conn_id
        assert response.get_result().get("network_id") == dl_crn
        assert response.get_result().get("network_type") == "directlink"

        #############################################  
        # Success: GET Transit GRE Connection:
        #############################################
        response = self.tg.get_transit_gateway_connection(
            transit_gateway_id=gateway_id, id=gre_conn_id)

        assert response is not None
        assert response.get_status_code() == 200
        assert response.get_result().get("zone") == zone
        assert response.get_result().get("name") == gre_name
        assert response.get_result().get("id") == gre_conn_id    
        assert response.get_result().get("network_type") == "gre_tunnel"
        assert response.get_result().get("base_connection_id") == classic_conn_id

        #############################################    
        # Success: UPDATE Transit CLASSIC Connection:
        #############################################
        classic_name = "UPDATED_" + classic_name
        response = self.tg.update_transit_gateway_connection(
            transit_gateway_id=gateway_id, 
            name=classic_name,
            id=classic_conn_id)

        assert response is not None
        assert response.get_status_code() == 200
        assert response.get_result().get("name") == classic_name
        assert response.get_result().get("id") == classic_conn_id

        #############################################
        # Success: UPDATE Transit VPC Connection:
        #############################################
        vpc_name = "UPDATED_" + vpc_name
        response = self.tg.update_transit_gateway_connection(
            transit_gateway_id=gateway_id,
            name=vpc_name, 
            id=vpc_conn_id)

        assert response is not None
        assert response.get_status_code() == 200
        assert response.get_result().get("id") == vpc_conn_id
        assert response.get_result().get("name") == vpc_name

        #############################################
        # Success: UPDATE Transit DL Connection:
        #############################################
        dl_name = "UPDATED_" + dl_name
        response = self.tg.update_transit_gateway_connection(
            transit_gateway_id=gateway_id, 
            name=dl_name,
            id=dl_conn_id)

        assert response is not None
        assert response.get_status_code() == 200
        assert response.get_result().get("id") == dl_conn_id
        assert response.get_result().get("name") == dl_name  

        #############################################  
        # Success: UPDATE Transit GRE Connection:
        #############################################
        gre_name = "UPDATED_" + gre_name
        response = self.tg.update_transit_gateway_connection(
            transit_gateway_id=gateway_id, 
            name=gre_name,
            id=gre_conn_id)

        assert response is not None
        assert response.get_status_code() == 200
        assert response.get_result().get("id") == gre_conn_id
        assert response.get_result().get("name") == gre_name

        #############################################
        # Success: LIST Transit Connections:
        #############################################
        response = self.tg.list_transit_gateway_connections(
            transit_gateway_id=gateway_id)

        assert response is not None
        assert response.get_status_code() == 200
        assert len(response.get_result().get("connections")) > 0
        
        gre_found = dl_found = vpc_found = classic_found = False
        conns = response.get_result().get("connections")          
        for conn in conns:
            if conn["network_type"] == "directlink":
                assert conn["name"] == dl_name
                assert conn["id"] == dl_conn_id
                dl_found = True

            elif conn["network_type"] == "gre_tunnel":
                assert conn["name"] == gre_name
                assert conn["id"] == gre_conn_id
                gre_found = True
            
            elif conn["network_type"] == "vpc":
                assert conn["name"] == vpc_name
                assert conn["id"] == vpc_conn_id
                vpc_found = True

            elif conn["network_type"] == "classic":
                assert conn["name"] == classic_name
                assert conn["id"] == classic_conn_id
                classic_found = True          

        assert dl_found
        assert gre_found
        assert vpc_found  
        assert classic_found 
        
        #############################################
        # Failure: POST Connection with invalid ID:
        #############################################
        crn = os.getenv("TG_SERVICES_VPC_CRN")
        name = os.getenv("TG_SERVICES_CONN_NAME")
        with self.assertRaises(ApiException) as e:
            self.tg.create_transit_gateway_connection(
                transit_gateway_id="bad-id", 
                network_type="vpc", 
                name=name,
                network_id=crn)
            self.assertEqual(e.exception.code, 404)

        #############################################    
        # Failure: POST Connection with invalid CRN: 
        #############################################
        bad_crn = "bad_crn"
        name = os.getenv("TG_SERVICES_CONN_NAME")
        with self.assertRaises(ApiException) as e:
            self.tg.create_transit_gateway_connection(
                transit_gateway_id=gateway_id, 
                network_type="vpc", 
                name=name,
                network_id=bad_crn) 
            self.assertEqual(e.exception.code, 400)

        #############################################    
        # Failure: GET Connection with invalid ID:
        #############################################
        bad_conn_id = "123abc" 
        with self.assertRaises(ApiException) as e: 
            self.tg.get_transit_gateway_connection(
                transit_gateway_id=gateway_id, id=bad_conn_id) 
            self.assertEqual(e.exception.code, 404)
            
        #############################################      
        # Failure: UPDATE Connection with invalid ID:
        ############################################# 
        updated_name = "UPDATED_" + os.getenv("TG_SERVICES_CONN_NAME")
        with self.assertRaises(ApiException) as e:   
            self.tg.update_transit_gateway_connection(
                transit_gateway_id=gateway_id, id=bad_conn_id, name=updated_name)
            self.assertEqual(e.exception.code, 404)

        #############################################
        # Failure: DELETE Connection with invalid ID:
        ############################################# 
        with self.assertRaises(ApiException) as e: 
            self.tg.delete_transit_gateway_connection(
                transit_gateway_id=gateway_id, id=bad_conn_id)
            self.assertEqual(e.exception.code, 404)

        #############################################
        # Success: POST Gateway Route Report:
        #############################################
        response = self.tg.create_transit_gateway_route_report(
            transit_gateway_id=gateway_id)

        assert response is not None
        assert response.get_status_code() == 202 
        assert response.get_result().get("id") != ""
        assert response.get_result().get("status") != ""
        assert response.get_result().get("created_at") != ""  
        assert response.get_result().get("connections") != None 
        
        # Wait untilt Gateway status = complete
        route_report_id = response.get_result().get("id")
        assert self.is_resource_available(gateway_id=gateway_id, 
            conn_id="", rr_id=route_report_id) 
            
        #############################################
        # Success: GET Gateway Route Report:
        #############################################
        response = self.tg.get_transit_gateway_route_report(
            transit_gateway_id=gateway_id, id=route_report_id)

        assert response is not None
        assert response.get_status_code() == 200
        assert response.get_result().get("created_at") != ""  
        assert response.get_result().get("updated_at") != "" 
        assert response.get_result().get("connections") != None
        assert len(response.get_result().get("connections")) > 0
        assert response.get_result().get("id") == route_report_id

        conns = response.get_result().get("connections")
        gre_found = dl_found = vpc_found = classic_found = False
        for conn in conns:
            if conn["type"] == "vpc":
                assert conn["id"] == vpc_conn_id
                assert conn["name"] == vpc_name
                vpc_found = True

            elif conn["type"] == "directlink":
                assert conn["id"] == dl_conn_id
                assert conn["name"] == dl_name
                dl_found = True

            elif conn["type"] == "gre_tunnel":
                assert conn["id"] == gre_conn_id
                assert conn["name"] == gre_name
                gre_found = True

            elif conn["type"] == "classic":
                assert conn["id"] == classic_conn_id
                assert conn["name"] == classic_name
                classic_found = True  

        assert dl_found
        assert gre_found
        assert vpc_found  
        assert classic_found

        #############################################
        # Success: LIST Gateway Route Report: 
        ############################################# 
        response = self.tg.list_transit_gateway_route_reports(
            transit_gateway_id=gateway_id)

        assert response is not None
        assert response.get_status_code() == 200
        
        found = False
        route_reports = response.get_result().get("route_reports")
        for route_report in route_reports:
            if route_report["id"] == route_report_id: 
                assert route_report["created_at"] != "" 
                assert route_report["updated_at"] != "" 
                assert route_report["status"] == "complete"
                assert len(route_report["connections"]) > 0
                found = True
                
                break

        assert found

        #############################################
        # Failure: POST Route Report with invalid Gateway ID:
        #############################################
        invalid_id = "123abc"
        with self.assertRaises(ApiException) as e:
            self.tg.create_transit_gateway_route_report(
                transit_gateway_id=invalid_id)
            self.assertEqual(e.exception.code, 404)

        #############################################
        # Failure: GET Route Report with invalid ID:
        #############################################
        with self.assertRaises(ApiException) as e:
            self.tg.get_transit_gateway_route_report(
                transit_gateway_id=gateway_id, id=invalid_id)
            self.assertEqual(e.exception.code, 404)

        #############################################
        # Failure: DELETE Route Report with invalid ID:
        #############################################
        with self.assertRaises(ApiException) as e:
            self.tg.delete_transit_gateway_route_report(
                transit_gateway_id=invalid_id, id=invalid_id) 
            self.assertEqual(e.exception.code, 404)

        #############################################
        # Success: DELETE Gateway Route Report:
        #############################################
        assert self.delete_resource_test(gateway_id=gateway_id, 
            conn_id="", rr_id=route_report_id)
            
        #############################################
        # Success: DELETE Gateway Connections:
        #############################################
        # Delete GRE Connection
        assert self.delete_resource_test(gateway_id=gateway_id, 
            conn_id=gre_conn_id, rr_id="")

        # Delete DL Connection
        assert self.delete_resource_test(gateway_id=gateway_id, 
            conn_id=dl_conn_id, rr_id="")

        # Delete VPC Connection
        assert self.delete_resource_test(gateway_id=gateway_id, 
            conn_id=vpc_conn_id, rr_id="")

        # Delete CLASSIC Connection
        assert self.delete_resource_test(gateway_id=gateway_id, 
            conn_id=classic_conn_id, rr_id="")
        
        #############################################
        # Success: DELETE Transit Gateway:
        #############################################
        assert self.delete_resource_test( 
            gateway_id=gateway_id, conn_id="", rr_id="")


###############################################################################
#                           Test Helper Methods                               #
###############################################################################

    # delete_resource_test deletes a Transit Gateway or Connection 
    def delete_resource_test(self, gateway_id, conn_id, rr_id):        
        # Deletes resource depending on input:
        response = None
        if conn_id != "" and rr_id == "":
            response = self.tg.delete_transit_gateway_connection(
                transit_gateway_id=gateway_id, id=conn_id)

        elif conn_id == "" and rr_id != "":
            response = self.tg.delete_transit_gateway_route_report(
                transit_gateway_id=gateway_id, id=rr_id)  
        else:
            response = self.tg.delete_transit_gateway(id=gateway_id)
        
        # Success: Transit Resource deleted:
        assert response is not None
        assert response.get_status_code() == 204

        # Guarantees the deleted resource no longer exists:
        count = 0 
        while count < 24:
            # Retrieves resource depending on input:
            response = None
            try:
                if conn_id != "" and rr_id == "":
                    response = self.tg.get_transit_gateway_connection(
                        transit_gateway_id=gateway_id, id=conn_id) 

                elif conn_id == "" and rr_id != "":
                    response = self.tg.get_transit_gateway_route_report(
                    transit_gateway_id=gateway_id, id=rr_id) 
                else:
                    response = self.tg.get_transit_gateway(id=gateway_id)

            except ApiException as e:
                if e.code == 404:
                    break

            # Checks the resource has been actually deleted:           
            if (response is not None) and (response.get_status_code() == 404):
                break
            else:
                time.sleep(10)
                count += 1

        return True

    # is_resource_available checks until the resource status is available/attached.
    def is_resource_available(self, gateway_id, conn_id, rr_id):
        count = delay = 0
        input_id = gateway_id

        while count < 24:
            # Retrieves resource depending on input:
            response = None
            if conn_id != "" and rr_id == "":
                delay = 10
                input_id = conn_id
                response = self.tg.get_transit_gateway_connection(
                    transit_gateway_id=gateway_id, id=conn_id)

            elif conn_id == "" and rr_id != "":
                delay = 7
                input_id = rr_id
                response = self.tg.get_transit_gateway_route_report(
                    transit_gateway_id=gateway_id, id=rr_id) 

            else:
                delay = 5
                response = self.tg.get_transit_gateway(id=gateway_id)
            
            status = response.get_result().get("status")
            resource_id = response.get_result().get("id")

            # Success: Transit Resource retrieved:
            assert resource_id == input_id
            assert response.get_status_code() == 200

            # Checks the resource is ready to be used:  
            if status == "available" or status == "attached" or status == "complete": 
                break
            else:
                time.sleep(delay)
                count += 1

        return True        

if __name__ == '__main__':
    unittest.main()
