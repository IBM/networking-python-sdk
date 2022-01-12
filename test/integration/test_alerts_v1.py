# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2022.

"""
Integration test code to execute Webhooks
"""

import os
import unittest
from dotenv import load_dotenv, find_dotenv
from ibm_cloud_networking_services import AlertsV1
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
        self.service = WebhooksV1.new_instance(
                            service_name="cis_services", crn=self.crn)
        self.service1 = AlertsV1.new_instance(
                            service_name="cis_services", crn=self.crn)
        self.service.set_service_url(self.endpoint)        
        self._clean_webhooks()

    def tearDown(self):
        """ tear down """
        # Delete the resources
        self._clean_webhooks()
        self._clean_alert_policies()
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
    
    def _clean_alert_policies(self):
        response = self.service1.get_alert_policies()
        assert response is not None
        assert response.status_code == 200
        resp = response.get_result()['result']
        if resp is not None:
           for record in resp:
               self.service1.delete_alert_policy(
                   policy_id = record.get("id")
            ) 
    
    def _create_alert_webhook(self, name, url):
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
        webhook_id = response.get_result()['result']['id']
        return webhook_id
    
            
    ################## create Alert-policy ######################
    def test_1_create_alert_policies(self):
        """ test for success """
        # Construct a dict representation of a Webhooks
        webhook_id = self._create_alert_webhook(name ='My Slack Alert Webhook', url ='https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd')
        email_item_model = {}
        email_item_model['id'] = 'mynotifications@email.com'

        webhooks_item_model = {}
        webhooks_item_model['id'] = webhook_id

        mechanisms_model = {}
        mechanisms_model['email'] = [email_item_model]
        mechanisms_model['webhooks'] = [webhooks_item_model]

        # Set up parameter values
        name = 'My Alert Policy'
        enabled = True
        alert_type = 'dos_attack_l7'
        mechanisms = mechanisms_model 
        description = 'A description for my alert policy'
        
        # invoke method
        response = self.service1.create_alert_policy(
            name=name,
            enabled=enabled,
            alert_type=alert_type,
            mechanisms=mechanisms,
            description=description,
        )
        assert response is not None and response.get_status_code() == 201
        alertWebhook_id = response.get_result()['result']['id']
        return alertWebhook_id 
        
    
    ################## list_Alert-policy ###################
    def test_2_list_alert_policies(self):
        """ test for success """
        self.test_1_create_alert_policies()
        
        #List webhooks
        response = self.service1.get_alert_policies() 
        assert response is not None and response.get_status_code() == 200
        assert len(response.get_result()['result']) >= 1
        
    ################## update Alert-policy by id ###################
    def test_3_update_alert_policies(self):
        """ test for success """
        alertsPolicy_id = self.test_1_create_alert_policies()
        
        # Construct a dict representation of a update webhook
        webhook_id = self._create_alert_webhook(name ='My new Slack Alert Webhook', url ='https://hooks.slack.com/services/Ds3fdBFbV/456464Gbd')
        email_item_model = {}
        email_item_model['id'] = 'mynewnotifications@email.com'

        webhooks_item_model = {}
        webhooks_item_model['id'] = webhook_id

        mechanisms_model = {}
        mechanisms_model['email'] = [email_item_model]
        mechanisms_model['webhooks'] = [webhooks_item_model]

        # Set up parameter values
        name = 'My Alert Policy'
        enabled = True
        alert_type = 'dos_attack_l7'
        mechanisms = mechanisms_model 
        description = 'A description for my alert policy'
        conditions = {}
        
        # invoke method
        response = self.service1.update_alert_policy(
            policy_id = alertsPolicy_id,
            name=name,
            enabled=enabled,
            alert_type=alert_type,
            mechanisms=mechanisms,
            description=description,
            conditions=conditions,
        )
        assert response is not None and response.get_status_code() == 200
        updated_policy_id = response.get_result()['result']['id']
        assert updated_policy_id == alertsPolicy_id
        return updated_policy_id
        
    ################# get Alert-policy by id ###################
    def test_4_get_alert_policy(self):
        """ test for success """
        alertsPolicy_id = self.test_3_update_alert_policies()
        
        #Get Alert-policy
        response = self.service1.get_alert_policy(
            policy_id = alertsPolicy_id )
        assert response is not None and response.get_status_code() == 200
        assert len(response.get_result()['result']) >= 1
    
    ################## delete Alert-policy by id ###################        
    def test_5_delete_alert_policy(self):
        """ test for success """
        alertsPolicy_id = self.test_3_update_alert_policies()
        
        #Delete Alert-policy
        response = self.service1.delete_alert_policy(
            policy_id = alertsPolicy_id )
        assert response is not None and response.get_status_code() == 200
        assert len(response.get_result()['result']) >= 1
        delete_policy_id = response.get_result()['result']['id']
        assert delete_policy_id == alertsPolicy_id 
        
if __name__ == '__main__':
    unittest.main()
    
    
    
    
