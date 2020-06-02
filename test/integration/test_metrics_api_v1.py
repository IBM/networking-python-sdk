# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.

"""
Integration test code to execute metrics api functions
"""

import os
import unittest
import datetime
from ibm_cloud_networking_services.metrics_api_v1 import MetricsApiV1


class TestMetricsApiV1(unittest.TestCase):
    def setUp(self):
        """ test case setup """
        self.endpoint = os.getenv("API_ENDPOINT")
        self.crn = os.getenv("CRN")
        self.zone_id = os.getenv("ZONE_ID")
        today = datetime.date.today()
        self.since = str(today - datetime.timedelta(days=2))+'T12:00:00Z'
        self.until = str(today - datetime.timedelta(days=2))+'T13:00:00Z'
        # create metrics api record class object
        self.metricsApi = MetricsApiV1.new_instance(
            crn=self.crn, zone_id=self.zone_id, service_name="cis_services")
        self.metricsApi.set_service_url(self.endpoint)

    def tearDown(self):
        """ tear down zone"""
        # Delete the resources
        print("Clean up complete")

    ################# Metrics_api integration test cases ###################

    def test_1_metrics_api(self):
        """ test analytics_dashboard without since and until"""
        response = self.metricsApi.analytics_dashboard().get_result()
        assert response is not None and response.get('success') is True

        """ test analytics_dashboard with since and until"""
        continous_values = [True, False]
        for self.continous in continous_values:
            response = self.metricsApi.analytics_dashboard(
                since=self.since,
                until=self.until, continous=self.continous).get_result()
            assert response is not None and response.get('success') is True

        """ test for analytics_by_colos without since, until and continous"""
        response = self.metricsApi.analytics_by_colos().get_result()
        assert response is not None and response.get('success') is True

        """ test for analytics_by_colos with since, until and continous"""
        for self.continous in continous_values:
            response = self.metricsApi.analytics_by_colos(
                since=self.since,
                until=self.until, continous=self.continous).get_result()
            assert response is not None and response.get('success') is True

        """ test for dns_analytics """
        self.dimensions = ["responseCode", "queryName"]
        self.metrics = ["queryCount", "responseTimeAvg"]
        self.sort = []
        self.filters = "responseCode==NOERROR"
        self.limit = 100
        response = self.metricsApi.dns_analytics(
            since=self.since,
            until=self.until, dimensions=self.dimensions, metrics=self.metrics,
            limit=self.limit, filters=self.filters).get_result()
        assert response is not None and response.get('success') is True

        response = self.metricsApi.dns_analytics_by_time().get_result()
        assert response is not None and response.get('success') is True

        """ test dns_analytics_by_time using all params"""
        response = self.metricsApi.dns_analytics_by_time(
            since=self.since,
            until=self.until, dimensions=self.dimensions, metrics=self.metrics,
            sort=self.sort, limit=self.limit, filters=self.filters).get_result()
        assert response is not None and response.get('success') is True

    ################## Negative test cases ###################

    def test_2_metrics_api(self):
        self.dimensions = ["responseCode", "queryName"]
        self.metrics = ["queryCount", "responseTimeAvg"]
        self.sort = ["responseCode", "queryName"]
        self.filters = "responseCode==NOERROR"
        self.limit = 100
        """ test dns_analytics method without since """
        with self.assertRaises(ValueError) as val:
            self.metricsApi.dns_analytics(
                since=None,
                until=self.until, dimensions=self.dimensions, metrics=self.metrics).get_result()
            self.assertEqual(val.exception.msg, 'since must be provided')

        """ test dns_analytics method without until """
        with self.assertRaises(ValueError) as val:
            self.metricsApi.dns_analytics(
                since=self.since,
                until=None, dimensions=self.dimensions, metrics=self.metrics).get_result()
            self.assertEqual(val.exception.msg, 'until must be provided')

        """ test dns_analytics method without dimensions """
        with self.assertRaises(ValueError) as val:
            self.metricsApi.dns_analytics(
                since=self.since,
                until=self.until, dimensions=None, metrics=self.metrics).get_result()
            self.assertEqual(val.exception.msg, 'dimensions must be provided')

        """ test dns_analytics method without metrics """
        with self.assertRaises(ValueError) as val:
            self.metricsApi.dns_analytics(dimensions=self.dimensions,
                since=self.since,
                until=self.until, metrics=None)
            self.assertEqual(val.exception.msg, 'metrics must be provided')


if __name__ == '__main__':
    unittest.main()
