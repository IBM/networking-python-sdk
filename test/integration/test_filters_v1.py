# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2021.

"""
Integration test code to execute Filters of a Zone
"""

import os
import unittest
from dotenv import load_dotenv, find_dotenv
from ibm_cloud_networking_services import FiltersV1

configFile = "cis.env"

# load the .env file containing your environment variables
try:
    load_dotenv(find_dotenv(filename="cis.env"))
except:
    print('warning: no cis.env file loaded')

class TestFiltersV1(unittest.TestCase):
    """ Test class to call dns record sdk functions """
    
    def setUp(self):
        """ test case setup """
        if not os.path.exists(configFile):
            raise unittest.SkipTest(
                'External configuration not available, skipping...')
        self.crn = os.getenv("CRN")
        self.zone_id = os.getenv("ZONE_ID")
        self.endpoint = os.getenv("API_ENDPOINT")
        self.x_auth_user_token = os.getenv("CIS_SERVICES_APIKEY")
        # create dns record class object
        self.service = FiltersV1.new_instance(
                            service_name="cis_services")
        self.service.set_service_url(self.endpoint)        
        self._clean_filters()

    def tearDown(self):
        """ tear down """
        # Delete the resources
        self._clean_filters()
        print("Clean up complete")

    def _clean_filters(self):
        response = self.service.list_all_filters(
            x_auth_user_token = self.x_auth_user_token,
            crn = self.crn,
            zone_identifier = self.zone_id
            )
        assert response is not None
        assert response.status_code == 200
        resp = response.get_result().get("result")
        for record in resp:
            self.service.delete_filter(
                x_auth_user_token = self.x_auth_user_token,
                crn = self.crn,
                zone_identifier = self.zone_id,
                filter_identifier = record.get("id")
            )

    def _create_filter(self, expression, description, paused=False):
        filter_input_model = {}
        filter_input_model['expression'] = expression
        filter_input_model['paused'] = False
        filter_input_model['description'] = description
        filter_input = [filter_input_model]

        response = self.service.create_filter(
            x_auth_user_token = self.x_auth_user_token,
            crn = self.crn,
            zone_identifier = self.zone_id,
            filter_input = filter_input
            )
        assert response is not None and response.get_status_code() == 200
        filter_id = response.get_result()['result'][0]['id']
        return filter_id
    
    ################## create Filter ######################
    def test_1_create_filter(self):
        """ test for success """
        # Construct a dict representation of a FilterInput model
        filter_input_model = {}
        filter_input_model['expression'] = 'not http.request.uri.path matches "^/test/.*$"'
        filter_input_model['paused'] = False
        filter_input_model['description'] = 'not /test'
        filter_input = [filter_input_model]

        response = self.service.create_filter(
            x_auth_user_token = self.x_auth_user_token,
            crn = self.crn,
            zone_identifier = self.zone_id,
            filter_input = filter_input
            )
        assert response is not None and response.get_status_code() == 200
        self.filter_id = response.get_result()['result'][0]['id']
       
    ################## list_all_filters ###################

    def test_2_list_all_filters(self):
        """ test for success """
        filter_input_model = {}
        filter_input_model['expression'] = 'http.request.uri.path matches "^/list-all/.*$"'
        filter_input_model['paused'] = False
        filter_input_model['description'] = 'list test'
        filter_input = [filter_input_model]

        response = self.service.create_filter(
            x_auth_user_token = self.x_auth_user_token,
            crn = self.crn,
            zone_identifier = self.zone_id,
            filter_input = filter_input
            )
        assert response is not None and response.get_status_code() == 200

        response = self.service.list_all_filters(
            x_auth_user_token = self.x_auth_user_token,
            crn = self.crn,
            zone_identifier = self.zone_id
            )
        assert response is not None and response.get_status_code() == 200
        assert len(response.get_result()['result']) >= 1

    ################## update filters ###################
    def test_3_update_filters(self):
        filter_input_model = {}
        filter_input_model['expression'] = 'http.request.uri.path matches "^/update-one/.*$"'
        filter_input_model['paused'] = False
        filter_input_model['description'] = 'Update test'
        filter_input = [filter_input_model]

        response = self.service.create_filter(
            x_auth_user_token = self.x_auth_user_token,
            crn = self.crn,
            zone_identifier = self.zone_id,
            filter_input = filter_input
            )
        assert response is not None and response.get_status_code() == 200
        filter_id = response.get_result()['result'][0]['id']
        # Construct a dict representation of a FilterUpdateInput model
        filter_update_input_model = {}
        filter_update_input_model['id'] = filter_id
        filter_update_input_model['expression'] = '(ip.src eq 13.15.12.24)'
        filter_update_input_model['description'] = 'sdk python update lists'
        filter_update_input_model['paused'] = False
        filter_update_input = [filter_update_input_model]

        response = self.service.update_filters(
            x_auth_user_token = self.x_auth_user_token,
            crn = self.crn,
            zone_identifier = self.zone_id,
            filter_update_input = filter_update_input            
        )
        assert response is not None and response.get_status_code() == 200
        update_filter_id = response.get_result()['result'][0]['id']
        assert update_filter_id == filter_id
        assert response.get_result()['result'][0]['expression'] == filter_update_input_model['expression']


    ################## get filter by id ###################
    def test_4_get_filter_by_id(self):
        expression = 'http.request.uri.path matches "^/get-filter/.*$"'
        filter_id = self._create_filter(
            expression = expression,
            description = 'Update Filter'
        )
        response = self.service.get_filter(
            x_auth_user_token = self.x_auth_user_token,
            crn = self.crn,
            zone_identifier = self.zone_id,
            filter_identifier = filter_id
        )
        assert response is not None and response.get_status_code() == 200
        get_filter_id = response.get_result()['result']['id']
        assert get_filter_id == filter_id
        assert response.get_result()['result']['expression'] == expression

    ################## update filter by id ###################
    def test_5_update_filter_by_id(self):
        filter_id = self._create_filter(
            expression = 'http.request.uri.path matches "^/get-filter/.*$"',
            description = 'Update Filter'
        )

        response = self.service.update_filter(
            x_auth_user_token = self.x_auth_user_token,
            crn = self.crn,
            zone_identifier = self.zone_id,
            filter_identifier = filter_id,
            id = filter_id,
            expression = '(ip.src eq 213.115.12.24)',
            description = 'update a single filter test'
        )
        assert response is not None and response.get_status_code() == 200
        get_filter_id = response.get_result()['result']['id']
        assert get_filter_id == filter_id

    ################## delete a filter by id ###################
    def test_6_delete_filter_by_id(self):
        filter_id = self._create_filter(
            expression = 'http.request.uri.path matches "^/delete-filter/.*$"',
            description = 'Delete Filter'
        )
        response = self.service.delete_filter(
            x_auth_user_token = self.x_auth_user_token,
            crn = self.crn,
            zone_identifier = self.zone_id,
            filter_identifier = filter_id
        )
        assert response is not None and response.get_status_code() == 200
        get_filter_id = response.get_result()['result']['id']
        assert get_filter_id == filter_id
    
    ################## delete filters ###################
    def test_7_delete_filters(self):
        # Create a filter
        # Construct a dict representation of a FilterInput model
        filter_input_model = {}
        filter_input_model['expression'] = 'ip.src eq 193.184.216.0'
        filter_input_model['paused'] = False
        filter_input_model['description'] = 'not from ip'
        filter_input = [filter_input_model]

        response = self.service.create_filter(
            x_auth_user_token = self.x_auth_user_token,
            crn = self.crn,
            zone_identifier = self.zone_id,
            filter_input = filter_input
        )
        assert response is not None and response.get_status_code() == 200
        filter_id_to_del = response.get_result()['result'][0]['id']

        response = self.service.delete_filters(
            x_auth_user_token = self.x_auth_user_token,
            crn = self.crn,
            zone_identifier = self.zone_id,
            id = filter_id_to_del
        )
        assert response is not None and response.get_status_code() == 200
        print(response.get_result())
        get_filter_id = response.get_result()['result'][0]['id']
        assert get_filter_id == filter_id_to_del

if __name__ == '__main__':
    unittest.main()





