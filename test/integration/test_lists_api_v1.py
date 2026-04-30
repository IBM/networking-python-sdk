# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2026.

"""
Integration test code to execute Lists API
"""

import os
import unittest
from dotenv import load_dotenv, find_dotenv
from ibm_cloud_networking_services import ListsApiV1

configFile = "cis.env"

# load the .env file containing your environment variables
try:
    load_dotenv(find_dotenv(filename="cis.env"))
except:
    print('warning: no cis.env file loaded')

class TestListsApiV1(unittest.TestCase):
    """ Test class to call Lists API sdk functions """

    @unittest.skip("Authentication failing")
    
    def setUp(self):
        """ test case setup """
        if not os.path.exists(configFile):
            raise unittest.SkipTest(
                'External configuration not available, skipping...')
        self.crn = os.getenv("CRN")
        self.endpoint = os.getenv("API_ENDPOINT")
        # Initialize with placeholder values for required path parameters
        self.service = ListsApiV1.new_instance(
            service_name="cis_services",
            crn=self.crn,
            item_id="placeholder_item_id",
            list_id="placeholder_list_id",
            operation_id="placeholder_operation_id"
        )
        self.service.set_service_url(self.endpoint)
        self._clean_custom_lists()

    def tearDown(self):
        """ tear down """
        # Delete the resources
        self._clean_custom_lists()
        print("Clean up complete")
        
    def _clean_custom_lists(self):
        response = self.service.get_custom_lists()
        assert response is not None
        assert response.status_code == 200
        resp = response.get_result()['result']
        if resp is not None:
            for record in resp:
                # Update list_id for deletion
                self.service.list_id = record.get("id")
                self.service.delete_custom_list()
    
    def _create_custom_list(self, name, kind, description):
        """ create a custom list """
        response = self.service.create_custom_lists(
            name=name,
            kind=kind,
            description=description
        )
        assert response is not None and response.get_status_code() == 201
        list_id = response.get_result()['result']['id']
        return list_id
    
    ################## get managed lists ######################
    def test_1_get_managed_lists(self):
        """ test for success """
        response = self.service.get_managed_lists()
        assert response is not None and response.get_status_code() == 200
        
    ################## create custom list ######################
    def test_2_create_custom_lists(self):
        """ test for success """
        name = 'Test IP List'
        kind = 'ip'
        description = 'A test list for IP addresses'
        
        response = self.service.create_custom_lists(
            name=name,
            kind=kind,
            description=description
        )
        assert response is not None and response.get_status_code() == 201
        list_id = response.get_result()['result']['id']
        return list_id
    
    ################## list custom lists ###################
    def test_3_get_custom_lists(self):
        """ test for success """
        self.test_2_create_custom_lists()
        
        response = self.service.get_custom_lists()
        assert response is not None and response.get_status_code() == 200
        assert len(response.get_result()['result']) >= 1
        
    ################## get custom list by id ###################
    def test_4_get_custom_list(self):
        """ test for success """
        list_id = self.test_2_create_custom_lists()
        
        # Update list_id in service instance
        self.service.list_id = list_id
        
        response = self.service.get_custom_list()
        assert response is not None and response.get_status_code() == 200
        assert response.get_result()['result']['id'] == list_id
        
    ################## update custom list by id ###################
    def test_5_update_custom_list(self):
        """ test for success """
        list_id = self.test_2_create_custom_lists()
        
        # Update list_id in service instance
        self.service.list_id = list_id
        
        description = 'Updated description for test list'
        
        response = self.service.update_custom_list(
            description=description
        )
        assert response is not None and response.get_status_code() == 200
        updated_list_id = response.get_result()['result']['id']
        assert updated_list_id == list_id
        return updated_list_id
        
    ################## create list items ###################
    def test_6_create_list_items(self):
        """ test for success """
        list_id = self.test_2_create_custom_lists()
        
        # Update list_id in service instance
        self.service.list_id = list_id
        
        # Create list items
        from ibm_cloud_networking_services.lists_api_v1 import CreateListItemsReqItem
        
        item1 = CreateListItemsReqItem(
            ip='192.0.2.1',
            comment='Test IP address'
        )
        
        response = self.service.create_list_items(
            create_list_items_req_item=[item1]
        )
        assert response is not None and response.get_status_code() == 200
        operation_id = response.get_result()['result']['operation_id']
        return list_id, operation_id
        
    ################## get list items ###################
    def test_7_get_list_items(self):
        """ test for success """
        list_id, operation_id = self.test_6_create_list_items()
        
        # Update list_id in service instance
        self.service.list_id = list_id
        
        response = self.service.get_list_items()
        assert response is not None and response.get_status_code() == 200
        
    ################## get list item by id ###################
    def test_8_get_list_item(self):
        """ test for success """
        list_id, operation_id = self.test_6_create_list_items()
        
        # Update list_id in service instance
        self.service.list_id = list_id
        
        # Get list items to find an item_id
        response = self.service.get_list_items()
        assert response is not None
        items = response.get_result()['result']
        
        if items and len(items) > 0:
            item_id = items[0]['id']
            self.service.item_id = item_id
            
            response = self.service.get_list_item()
            assert response is not None and response.get_status_code() == 200
            assert response.get_result()['result']['id'] == item_id
        
    ################## update list items ###################
    def test_9_update_list_items(self):
        """ test for success """
        list_id, operation_id = self.test_6_create_list_items()
        
        # Update list_id in service instance
        self.service.list_id = list_id
        
        from ibm_cloud_networking_services.lists_api_v1 import CreateListItemsReqItem
        
        item1 = CreateListItemsReqItem(
            ip='192.0.2.2',
            comment='Updated IP address'
        )
        
        response = self.service.update_list_items(
            create_list_items_req_item=[item1]
        )
        assert response is not None and response.get_status_code() == 200
        
    ################## delete list items ###################
    def test_10_delete_list_items(self):
        """ test for success """
        list_id, operation_id = self.test_6_create_list_items()
        
        # Update list_id in service instance
        self.service.list_id = list_id
        
        # Get list items to find item IDs to delete
        response = self.service.get_list_items()
        assert response is not None
        items = response.get_result()['result']
        
        if items and len(items) > 0:
            from ibm_cloud_networking_services.lists_api_v1 import DeleteListItemsReqItemsItem
            
            items_to_delete = [DeleteListItemsReqItemsItem(id=item['id']) for item in items]
            
            response = self.service.delete_list_items(
                items=items_to_delete
            )
            assert response is not None and response.get_status_code() == 200
        
    ################## get operation status ###################
    def test_11_get_operation_status(self):
        """ test for success """
        list_id, operation_id = self.test_6_create_list_items()
        
        # Update operation_id in service instance
        self.service.operation_id = operation_id
        
        response = self.service.get_operation_status()
        assert response is not None and response.get_status_code() == 200
        assert response.get_result()['result']['id'] == operation_id
        
    ################## delete custom list by id ###################        
    def test_12_delete_custom_list(self):
        """ test for success """
        list_id = self.test_5_update_custom_list()
        
        # Update list_id in service instance
        self.service.list_id = list_id
        
        response = self.service.delete_custom_list()
        assert response is not None and response.get_status_code() == 200
        delete_list_id = response.get_result()['result']['id']
        assert delete_list_id == list_id
        
if __name__ == '__main__':
    unittest.main()
