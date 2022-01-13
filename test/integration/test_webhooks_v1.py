# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2022.

"""
Integration test code to execute Webhooks
"""

import os
import unittest
from dotenv import load_dotenv, find_dotenv
from ibm_cloud_networking_services import WebhooksV1

configFile = "cis.env"

# load the .env file containing your environment variables
try:
    load_dotenv(find_dotenv(filename="cis.env"))
except:
    print('warning: no cis.env file loaded')

class TestWebhooksV1(unittest.TestCase):
    """ Test class to call webhooks sdk functions """
    
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
        self.service = WebhooksV1.new_instance(
                            service_name="cis_services", crn=self.crn)
        self.service.set_service_url(self.endpoint)        
        self._clean_webhooks()

    def tearDown(self):
        """ tear down """
        # Delete the resources
        self._clean_webhooks()
        print("Clean up complete")
        
    def _clean_webhooks(self):
        response = self.service.get_alert_webhooks()
        assert response is not None
        assert response.status_code == 200
        resp = response.get_result()['result']
        if resp is not None:
           for record in resp:
               self.service.delete_alert_webhook(
                   webhook_id = record.get("id")
            )  
            
    ################## create Webhooks ######################
    def test_1_create_webhooks(self):
        """ test for success """
        # Construct a dict representation of a Webhooks
        name = 'My Slack Alert Webhook'
        url = 'https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd'
        secret = self.x_auth_user_token
        response = self.service.create_alert_webhook(
            name=name,
            url=url,
            secret=secret
            )
        assert response is not None and response.get_status_code() == 201
        self.webhook_id = response.get_result()['result']['id']

    
    ################## list_Webhook ###################
    def test_2_list_webhooks(self):
        """ test for success """
        # Construct a dict representation of a Webhooks
        name = 'My Slack Alert Webhook 2'
        url = 'https://hooks.slack.com/services/Ds3fdBFbV/456464B653'
        secret = self.x_auth_user_token
        
        response = self.service.create_alert_webhook(
            name=name,
            url=url,
            secret=secret
            )
        assert response is not None and response.get_status_code() == 201
        #List webhooks
        response = self.service.get_alert_webhooks() 
        assert response is not None and response.get_status_code() == 200
        assert len(response.get_result()['result']) >= 1
        
    ################## update webhooks by id ###################
    def test_3_update_webhooks(self):
        """ test for success """
        # Construct a dict representation of a Webhooks
        name = 'My Slack Alert Webhook 3'
        url = 'https://hooks.slack.com/services/Ds3fdBFbV/456464B653'
        secret = self.x_auth_user_token
        
        response = self.service.create_alert_webhook(
            name=name,
            url=url,
            secret=secret
            )
        assert response is not None and response.get_status_code() == 201
        self.webhook_id = response.get_result()['result']['id']
        
        # Construct a dict representation of a update webhook
        webhook_id= self.webhook_id
        name = 'My Slack Alert Webhook'
        url = 'https://hooks.slack.com/services/Ds3fd89FbV/456464Gdd'
        secret = self.x_auth_user_token

        # Invoke method
        response = self.service.update_alert_webhook(
            webhook_id= webhook_id,
            name=name,
            url=url,
            secret=secret,
        )
        assert response is not None and response.get_status_code() == 200
        updated_webhook_id = response.get_result()['result']['id']
        assert updated_webhook_id == webhook_id
        
    ################## get webhooks by id ###################
    def test_4_get_webhooks(self):
        """ test for success """
        # Construct a dict representation of a Webhooks
        name = 'My Slack Alert Webhook 4'
        url = 'https://hooks.slack.com/services/Ds3fdBFbV/456464B667vr'
        secret = self.x_auth_user_token
        
        response = self.service.create_alert_webhook(
            name=name,
            url=url,
            secret=secret
            )
        assert response is not None and response.get_status_code() == 201
        self.webhook_id = response.get_result()['result']['id']
        #Get webhooks
        response = self.service.get_alert_webhook(
            webhook_id = self.webhook_id )
        assert response is not None and response.get_status_code() == 200
        assert len(response.get_result()['result']) >= 1
    
    ################## delete webhooks by id ###################        
    def test_5_delete_webhooks(self):
        """ test for success """
        # Construct a dict representation of a Webhooks
        name = 'My Slack Alert Webhook 5'
        url = 'https://hooks.slack.com/services/Ds3fdBFBT/456464B667'
        secret = self.x_auth_user_token
        
        response = self.service.create_alert_webhook(
            name=name,
            url=url,
            secret=secret
            )
        assert response is not None and response.get_status_code() == 201
        self.webhook_id = response.get_result()['result']['id']
        
        #Delete webhooks
        response = self.service.delete_alert_webhook(
            webhook_id = self.webhook_id )
        assert response is not None and response.get_status_code() == 200
        assert len(response.get_result()['result']) >= 1
        delete_webhook_id = response.get_result()['result']['id']
        assert delete_webhook_id == self.webhook_id
        
if __name__ == '__main__':
    unittest.main()