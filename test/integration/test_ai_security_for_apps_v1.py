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
    ApiGatewayOperation,
    ApiGatewayOperationsLabelsInputManaged,
    ApiGatewayOperationsLabelsInputSelector,
    ApiGatewayOperationsLabelsInputSelectorInclude,
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
            service_name='cis_services',
        )

    def test_01_get_ai_security_settings(self):
        """ Get AI Security Settings """
        response = self.service.get_ai_security_settings()
        assert response is not None
        assert response.status_code == 200
        result = response.result
        assert result.get('success') is True
        assert 'result' in result

    def test_02_replace_zone_ai_security_settings(self):
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

    def test_03_get_api_gateway_discovery(self):
        """ Get API Gateway Discovery """
        response = self.service.get_api_gateway_discovery()
        assert response is not None
        assert response.status_code == 200
        assert response.result.get('success') is True

    def test_04_list_api_gateway_discovery_operations(self):
        """ List API Gateway Discovery Operations """
        response = self.service.list_api_gateway_discovery_operations()
        assert response is not None
        assert response.status_code == 200
        assert response.result.get('success') is True

    def test_05_get_api_gateway_schemas(self):
        """ Get API Gateway Schemas """
        response = self.service.get_api_gateway_schemas()
        assert response is not None
        assert response.status_code == 200
        assert response.result.get('success') is True

    # ------------------------------------------------------------------
    # Block 1 — Single operation lifecycle
    # ------------------------------------------------------------------

    def test_06_create_single_api_gateway_operation(self):
        """ Create a single API Gateway operation and retrieve it by operation ID """
        create_response = self.service.create_api_gateway_operation_item(
            method='POST',
            host='api.example.com',
            endpoint='/v1/messages',
        )
        assert create_response is not None
        assert create_response.status_code == 200
        assert create_response.result.get('success') is True

        operation_id = create_response.result['result']['operation_id']
        assert operation_id is not None

        # Store on the class so subsequent single-lifecycle tests can use it
        TestAiSecurityForAppsV1.single_operation_id = operation_id

        # Retrieve by operation ID and confirm it matches
        get_response = self.service.get_zone_api_gateway_operation(
            operation_id=operation_id,
        )
        assert get_response is not None
        assert get_response.status_code == 200
        assert get_response.result.get('success') is True
        assert get_response.result['result']['operation_id'] == operation_id

    def test_07_delete_single_api_gateway_operation(self):
        """ Delete the single API Gateway operation created in test_6 """
        operation_id = getattr(TestAiSecurityForAppsV1, 'single_operation_id', None)
        if not operation_id:
            self.skipTest('single_operation_id not set — test_06 may have failed')

        delete_response = self.service.delete_zone_api_gateway_operation(
            operation_id=operation_id,
        )
        assert delete_response is not None
        assert delete_response.status_code in (200, 204)

    def test_08_verify_deleted_single_operation_returns_404(self):
        """ Verify that the deleted single operation returns HTTP 404 """
        operation_id = getattr(TestAiSecurityForAppsV1, 'single_operation_id', None)
        if not operation_id:
            self.skipTest('single_operation_id not set — test_06 may have failed')

        try:
            self.service.get_zone_api_gateway_operation(
                operation_id=operation_id,
            )
            self.fail('Expected an exception for a deleted operation but none was raised')
        except Exception as exc:
            # The IBM SDK raises ApiException (a subclass of Exception) whose
            # http_response.status_code carries the HTTP status.
            status_code = getattr(getattr(exc, 'http_response', None), 'status_code', None)
            assert status_code == 404, (
                f'Expected HTTP 404 for deleted operation but got {status_code}: {exc}'
            )

    # ------------------------------------------------------------------
    # Block 2 — Bulk lifecycle
    # ------------------------------------------------------------------

    # Shared state for all three bulk scenarios; populated by test_9.
    bulk_operation_ids = []

    def test_09_bulk_create_api_gateway_operations_and_retrieve_second(self):
        """ Create 3 operations in bulk and retrieve the second one """
        operations = [
            ApiGatewayOperation(method='GET',    host='api.example.com', endpoint='/v2/users'),
            ApiGatewayOperation(method='POST',   host='api.example.com', endpoint='/v2/orders'),
            ApiGatewayOperation(method='DELETE', host='api.example.com', endpoint='/v2/sessions'),
        ]

        create_response = self.service.create_zone_api_gateway_operation(
            api_gateway_operation=operations,
        )
        assert create_response is not None
        assert create_response.status_code == 200
        assert create_response.result.get('success') is True

        result_items = create_response.result['result']
        assert len(result_items) == 3

        # Collect IDs into the class-level shared list
        TestAiSecurityForAppsV1.bulk_operation_ids = [
            item['operation_id'] for item in result_items
        ]
        assert len(TestAiSecurityForAppsV1.bulk_operation_ids) == 3

        # Retrieve the second operation
        second_id = TestAiSecurityForAppsV1.bulk_operation_ids[1]
        get_response = self.service.get_zone_api_gateway_operation(
            operation_id=second_id,
        )
        assert get_response is not None
        assert get_response.status_code == 200
        assert get_response.result.get('success') is True
        assert get_response.result['result']['operation_id'] == second_id

    def test_10_update_labels_for_bulk_operations(self):
        """ Add a managed label (cf-llm) to all bulk operations, then narrow selector """
        bulk_ids = TestAiSecurityForAppsV1.bulk_operation_ids
        if not bulk_ids:
            self.skipTest('bulk_operation_ids not populated — test_09 may have failed')

        managed_label = 'cf-llm'

        # --- Step 1: add managed label to all 3 operations ---
        selector_all = ApiGatewayOperationsLabelsInputSelector(
            include=ApiGatewayOperationsLabelsInputSelectorInclude(
                operation_ids=bulk_ids,
            ),
        )
        managed_labels = ApiGatewayOperationsLabelsInputManaged(labels=[managed_label])

        label_response_all = self.service.update_api_gateway_operation_labels(
            selector=selector_all,
            managed=managed_labels,
        )
        assert label_response_all is not None
        assert label_response_all.status_code == 200
        assert label_response_all.result.get('success') is True

        labeled_items_all = label_response_all.result['result']
        assert len(labeled_items_all) == 3
        for item in labeled_items_all:
            label_names = [lbl['name'] for lbl in item['labels']]
            assert managed_label in label_names, (
                f'Expected label "{managed_label}" in {label_names} for operation {item["operation_id"]}'
            )

        # --- Step 2: narrow selector to only 2nd and 3rd IDs ---
        narrowed_ids = bulk_ids[1:]
        selector_narrow = ApiGatewayOperationsLabelsInputSelector(
            include=ApiGatewayOperationsLabelsInputSelectorInclude(
                operation_ids=narrowed_ids,
            ),
        )

        label_response_narrow = self.service.update_api_gateway_operation_labels(
            selector=selector_narrow,
            managed=managed_labels,
        )
        assert label_response_narrow is not None
        assert label_response_narrow.status_code == 200
        assert label_response_narrow.result.get('success') is True

        labeled_items_narrow = label_response_narrow.result['result']
        for item in labeled_items_narrow:
            label_names = [lbl['name'] for lbl in item['labels']]
            assert managed_label in label_names, (
                f'Expected label "{managed_label}" still present in {label_names} '
                f'for operation {item["operation_id"]}'
            )

    def test_11_delete_all_bulk_api_gateway_operations(self):
        """ Delete all bulk-created API Gateway operations """
        bulk_ids = TestAiSecurityForAppsV1.bulk_operation_ids
        if not bulk_ids:
            self.skipTest('bulk_operation_ids not populated — test_09 may have failed')

        for operation_id in bulk_ids:
            delete_response = self.service.delete_zone_api_gateway_operation(
                operation_id=operation_id,
            )
            assert delete_response is not None
            assert delete_response.status_code in (200, 204)


if __name__ == '__main__':
    unittest.main()
