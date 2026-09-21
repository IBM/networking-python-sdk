# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2026.

"""
Integration test code to execute AI Security for Apps functions
"""

import os
import unittest
from dotenv import load_dotenv, find_dotenv
from ibm_cloud_networking_services.ai_security_for_apps_v1 import (
    AiSecurityForAppsV1,
)

configFile = "cis.env"

# load the .env file containing your environment variables
try:
    load_dotenv(find_dotenv(filename=configFile))
except Exception:
    print('warning: no cis.env file loaded')


class TestAiSecurityForAppsV1(unittest.TestCase):
    """ Integration tests for AI Security for Apps V1 """

    @classmethod
    def setUpClass(cls):
        """ test class setup """
        if not os.path.exists(configFile):
            cls.skipTest(cls, "External configuration not available, skipping...")

        cls.crn = os.environ.get("CRN")
        cls.zone_identifier = os.environ.get("ZONE_ID")
        cls.service = AiSecurityForAppsV1.new_instance(
            crn=cls.crn,
            zone_identifier=cls.zone_identifier,
        )

    def test_1_get_ai_security_settings(self):
        """ Get AI Security Settings """
        response = self.service.get_ai_security_settings()
        assert response is not None
        assert response.status_code == 200
        result = response.result
        assert result.get('success') is True
        assert 'result' in result

    def test_2_replace_zone_ai_security_settings(self):
        """ Update AI Security Settings """
        # Get current value
        get_response = self.service.get_ai_security_settings()
        assert get_response is not None
        current_enabled = get_response.result['result']['enabled']
        new_enabled = not current_enabled

        response = self.service.replace_zone_ai_security_settings(enabled=new_enabled)
        assert response is not None
        assert response.status_code == 200
        assert response.result.get('success') is True

        # Restore original value
        self.service.replace_zone_ai_security_settings(enabled=current_enabled)

    def test_3_get_api_gateway_discovery(self):
        """ Get API Gateway Discovery """
        response = self.service.get_api_gateway_discovery()
        assert response is not None
        assert response.status_code == 200
        assert response.result.get('success') is True

    def test_4_list_api_gateway_discovery_operations(self):
        """ List API Gateway Discovery Operations """
        response = self.service.list_api_gateway_discovery_operations()
        assert response is not None
        assert response.status_code == 200
        assert response.result.get('success') is True

    def test_5_get_api_gateway_schemas(self):
        """ Get API Gateway Schemas """
        response = self.service.get_api_gateway_schemas()
        assert response is not None
        assert response.status_code == 200
        assert response.result.get('success') is True

    def test_6_create_and_delete_api_gateway_operation_item(self):
        """ Create a single API Gateway operation and delete it """
        create_response = self.service.create_api_gateway_operation_item(
            method='POST',
            host='api.example.com',
            endpoint='/v1/messages',
        )
        assert create_response is not None
        assert create_response.status_code == 200
        assert create_response.result.get('success') is True

        operation_id = create_response.result['result']['operation_id']

        # Delete the created operation
        delete_response = self.service.delete_zone_api_gateway_operation(
            operation_id=operation_id,
        )
        assert delete_response is not None
        assert delete_response.status_code == 204


if __name__ == '__main__':
    unittest.main()
