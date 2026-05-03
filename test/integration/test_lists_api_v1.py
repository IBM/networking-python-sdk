# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2026.

"""
Integration test code to execute Lists API
"""

import os
import unittest
from dotenv import load_dotenv, find_dotenv
from ibm_cloud_networking_services.lists_api_v1 import ListsApiV1, CreateListItemsReqItem, DeleteListItemsReqItemsItem

configFile = "cis.env"

# load the .env file containing your environment variables
try:
    load_dotenv(find_dotenv(filename="cis.env"))
except:
    print('warning: no cis.env file loaded')

class TestListsApiV1(unittest.TestCase):
    """ Test class to call Lists API sdk functions """

    def setUp(self):
        """ test case setup """
        if not os.path.exists(configFile):
            raise unittest.SkipTest(
                'External configuration not available, skipping...')
        self.crn = os.getenv("CRN")
        self.endpoint = os.getenv("API_ENDPOINT")
        self.service = ListsApiV1.new_instance(
            service_name="cis_services",
            crn=self.crn,
            item_id="00000000000000000000000000000001",
            list_id="00000000000000000000000000000001",
            operation_id="00000000000000000000000000000001",
        )
        self.service.set_service_url(self.endpoint)
        self._clean_custom_lists()

    def tearDown(self):
        """ tear down """
        self._clean_custom_lists()
        print("Clean up complete")

    def _clean_custom_lists(self):
        response = self.service.get_custom_lists()
        assert response is not None
        assert response.status_code == 200
        resp = response.get_result().get('result') or []
        for record in resp:
            if record.get('name', '').startswith('sdk_integration_test'):
                self.service.list_id = record['id']
                self.service.delete_custom_list()

    def _create_custom_list(self):
        response = self.service.create_custom_lists(
            name='sdk_integration_test_list',
            kind='ip',
            description='Integration test custom list',
        )
        assert response is not None
        assert response.get_status_code() in (200, 201)
        list_id = response.get_result()['result']['id']
        self.service.list_id = list_id
        return list_id

    ################## get managed lists ######################
    def test_1_get_managed_lists(self):
        """ test for success """
        response = self.service.get_managed_lists()
        assert response is not None
        assert response.get_status_code() == 200

    ################## list custom lists ###################
    def test_2_get_custom_lists(self):
        """ test for success """
        response = self.service.get_custom_lists()
        assert response is not None
        assert response.get_status_code() == 200

    ################## create custom list ######################
    def test_3_create_custom_lists(self):
        """ test for success """
        list_id = self._create_custom_list()
        assert list_id is not None

    ################## get custom list by id ###################
    def test_4_get_custom_list(self):
        """ test for success """
        self._create_custom_list()
        response = self.service.get_custom_list()
        assert response is not None
        assert response.get_status_code() == 200

    ################## update custom list by id ###################
    def test_5_update_custom_list(self):
        """ test for success """
        self._create_custom_list()
        response = self.service.update_custom_list(
            description='Updated integration test custom list',
        )
        assert response is not None
        assert response.get_status_code() == 200

    ################## create list items ###################
    def test_6_create_list_items(self):
        """ test for success """
        self._create_custom_list()
        item = CreateListItemsReqItem(ip='192.0.2.10', comment='integration test item')
        response = self.service.create_list_items(
            create_list_items_req_item=[item],
        )
        assert response is not None
        assert response.get_status_code() in (200, 202)
        operation_id = response.get_result()['result']['operation_id']
        assert operation_id is not None
        self.service.operation_id = operation_id

    ################## get operation status ###################
    def test_7_get_operation_status(self):
        """ test for success """
        self._create_custom_list()
        item = CreateListItemsReqItem(ip='192.0.2.10', comment='integration test item')
        op_response = self.service.create_list_items(
            create_list_items_req_item=[item],
        )
        assert op_response is not None
        assert op_response.get_status_code() in (200, 202)
        self.service.operation_id = op_response.get_result()['result']['operation_id']

        response = self.service.get_operation_status()
        assert response is not None
        assert response.get_status_code() == 200

    ################## get list items ###################
    def test_8_get_list_items(self):
        """ test for success """
        self._create_custom_list()
        item = CreateListItemsReqItem(ip='192.0.2.10', comment='integration test item')
        self.service.create_list_items(create_list_items_req_item=[item])

        response = self.service.get_list_items(per_page=1, search='192.0.2')
        assert response is not None
        assert response.get_status_code() == 200
        items = response.get_result().get('result') or []
        if items:
            self.service.item_id = items[0]['id']

    ################## get list item by id ###################
    def test_9_get_list_item(self):
        """ test for success """
        self._create_custom_list()
        item = CreateListItemsReqItem(ip='192.0.2.10', comment='integration test item')
        self.service.create_list_items(create_list_items_req_item=[item])

        items_response = self.service.get_list_items()
        assert items_response is not None
        items = items_response.get_result().get('result') or []
        if items:
            self.service.item_id = items[0]['id']
            response = self.service.get_list_item()
            assert response is not None
            assert response.get_status_code() == 200

    ################## update list items ###################
    def test_10_update_list_items(self):
        """ test for success """
        self._create_custom_list()
        item = CreateListItemsReqItem(ip='192.0.2.11', comment='updated integration test item')
        response = self.service.update_list_items(
            create_list_items_req_item=[item],
        )
        assert response is not None
        assert response.get_status_code() in (200, 202)

    ################## delete list items ###################
    def test_11_delete_list_items(self):
        """ test for success """
        self._create_custom_list()
        item = CreateListItemsReqItem(ip='192.0.2.10', comment='integration test item')
        self.service.create_list_items(create_list_items_req_item=[item])

        items_response = self.service.get_list_items()
        assert items_response is not None
        items = items_response.get_result().get('result') or []
        if items:
            items_to_delete = [DeleteListItemsReqItemsItem(id=i['id']) for i in items]
            response = self.service.delete_list_items(items=items_to_delete)
            assert response is not None
            assert response.get_status_code() in (200, 202)

    ################## delete custom list by id ###################
    def test_12_delete_custom_list(self):
        """ test for success """
        self._create_custom_list()
        response = self.service.delete_custom_list()
        assert response is not None
        assert response.get_status_code() == 200


if __name__ == '__main__':
    unittest.main()
