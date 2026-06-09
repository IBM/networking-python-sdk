# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2026.

"""
Integration test code to execute logpush jobs functions
"""

import os
import unittest
from dotenv import load_dotenv, find_dotenv
from ibm_cloud_sdk_core.api_exception import ApiException
from ibm_cloud_networking_services.logpush_jobs_api_v1 import (
    LogpushJobsApiV1,
    CreateLogpushJobV2RequestLogpushJobLogdnaReq,
    CreateLogpushJobV2RequestLogpushJobGenericReq,
    CreateLogpushJobV2RequestLogpushJobCosReq,
    CreateLogpushJobV2RequestLogpushJobIbmclReq,
    UpdateLogpushJobV2RequestLogpushJobsUpdateLogdnaReq,
    UpdateLogpushJobV2RequestLogpushJobsUpdateGenericReq,
    UpdateLogpushJobV2RequestLogpushJobsUpdateCosReq,
    LogpushJobIbmclReqIbmcl,
)

configFile = "cis.env"

# load the .env file containing your environment variables
try:
    load_dotenv(find_dotenv(filename=configFile))
except:
    print('warning: no cis.env file loaded')


class TestLogpushJobsApiV1(unittest.TestCase):
    """ Integration tests for Logpush Jobs API """

    @unittest.skip("Skipping...")

    def setUp(self):
        """ test case setup """
        if not os.path.exists(configFile):
            raise unittest.SkipTest(
                'External configuration not available, skipping...')

        self.crn = os.getenv("CRN")
        self.zone_id = os.getenv("ZONE_ID")
        self.endpoint = os.getenv("API_ENDPOINT")
        self.ingress_key = os.getenv("INGRESS_KEY")
        self.logdna_region = os.getenv("LOGDNA_REGION")
        self.logdna_domain = os.getenv("DOMAIN_NAME")
        self.cos_bucket = os.getenv("COS_BUCKET")
        self.cos_region = os.getenv("COS_REGION")
        self.cos_instance = os.getenv("COS_INSTANCE")
        self.ownership_token = os.getenv("OWNERSHIP_TOKEN")
        self.dataset = "http_requests"

        # create logpush jobs service instance
        self.service = LogpushJobsApiV1.new_instance(
            crn=self.crn,
            zone_id=self.zone_id,
            dataset=self.dataset,
            service_name="cis_services"
        )
        self.service.set_service_url(self.endpoint)
        self._cleanup_jobs()

    def tearDown(self):
        """ tear down """
        # Delete the resources
        self._cleanup_jobs()
        print("Clean up complete")

    def _cleanup_jobs(self):
        """ Delete all existing logpush jobs """
        try:
            response = self.service.get_logpush_jobs_v2()
            assert response is not None
            result = response.get_result()
            if result and result.get("result"):
                for job in result.get("result"):
                    job_id = str(job.get("id"))
                    self.service.delete_logpush_job_v2(job_id=job_id)
        except ApiException as e:
            print(f"Cleanup error: {e}")

    def test_1_logpush_jobs_logdna(self):
        """ create/update/delete/get logpush jobs for logdna """
        # Skip this test - requires LogDNA setup
        self.skipTest("Skipping LogDNA test")

        # Create logpush job for LogDNA
        create_request = CreateLogpushJobV2RequestLogpushJobLogdnaReq(
            name="Test123",
            enabled=False,
            logpull_options="timestamps=rfc3339&timestamps=rfc3339",
            logdna={
                "ingress_key": self.ingress_key,
                "region": self.logdna_region,
                "hostname": self.logdna_domain
            },
            dataset="http_requests",
            frequency="high"
        )

        response = self.service.create_logpush_job_v2(
            create_logpush_job_v2_request=create_request
        )
        assert response is not None
        result = response.get_result()
        assert result.get("success") is True
        job = result.get("result")
        job_id = str(job.get("id"))

        # List all logpush jobs
        response = self.service.get_logpush_jobs_v2()
        assert response is not None
        result = response.get_result()
        assert result.get("success") is True
        all_jobs = result.get("result")

        # Get specific logpush job
        get_job = all_jobs[0]
        get_job_id = str(get_job.get("id"))
        response = self.service.get_logpush_job_v2(job_id=get_job_id)
        assert response is not None
        result = response.get_result()
        assert result.get("success") is True

        # Update logpush job
        update_request = UpdateLogpushJobV2RequestLogpushJobsUpdateLogdnaReq(
            enabled=False,
            logpull_options="timestamps=rfc3339&timestamps=rfc3339",
            logdna={
                "ingress_key": self.ingress_key,
                "region": self.logdna_region,
                "hostname": self.logdna_domain
            },
            frequency="high"
        )

        response = self.service.update_logpush_job_v2(
            job_id=job_id,
            update_logpush_job_v2_request=update_request
        )
        assert response is not None
        result = response.get_result()
        assert result.get("success") is True

        # Delete all logpush jobs
        for this_job in all_jobs:
            this_job_id = str(this_job.get("id"))
            response = self.service.delete_logpush_job_v2(job_id=this_job_id)
            assert response is not None
            result = response.get_result()
            assert result.get("success") is True

    def test_2_logpush_jobs_generic(self):
        """ create/update/delete/get logpush jobs for generic destination """
        # Skip this test - requires S3 setup
        self.skipTest("Skipping generic destination test")

        # Create logpush job with generic destination
        create_request = CreateLogpushJobV2RequestLogpushJobGenericReq(
            name="Test123",
            enabled=False,
            logpull_options="timestamps=rfc3339&timestamps=rfc3339",
            destination_conf="s3://mybucket/logs?region=us-west-2",
            dataset="http_requests",
            frequency="high"
        )

        response = self.service.create_logpush_job_v2(
            create_logpush_job_v2_request=create_request
        )
        assert response is not None
        result = response.get_result()
        assert result.get("success") is True
        job = result.get("result")
        job_id = str(job.get("id"))

        # List all logpush jobs
        response = self.service.get_logpush_jobs_v2()
        assert response is not None
        result = response.get_result()
        assert result.get("success") is True

        # Get specific logpush job
        response = self.service.get_logpush_job_v2(job_id=job_id)
        assert response is not None
        result = response.get_result()
        assert result.get("success") is True

        # Update logpush job
        update_request = UpdateLogpushJobV2RequestLogpushJobsUpdateGenericReq(
            enabled=False,
            logpull_options="timestamps=rfc3339&timestamps=rfc3339",
            destination_conf="s3://mybucket/logs?region=us-west-1",
            frequency="high"
        )

        response = self.service.update_logpush_job_v2(
            job_id=job_id,
            update_logpush_job_v2_request=update_request
        )
        assert response is not None
        result = response.get_result()
        assert result.get("success") is True

        # Delete logpush job
        response = self.service.delete_logpush_job_v2(job_id=job_id)
        assert response is not None
        result = response.get_result()
        assert result.get("success") is True

    def test_3_logpush_jobs_http_destination(self):
        """ create/update/delete/get logpush jobs with custom HTTP destination """

        # Create logpush job with custom HTTP destination
        create_request = CreateLogpushJobV2RequestLogpushJobGenericReq(
            name="Test123",
            enabled=False,
            logpull_options="fields=ClientIP,ClientRequestHost,ClientRequestMethod",
            destination_conf="https://httpbin.org/post",
            dataset="http_requests",
            frequency="high"
        )

        response = self.service.create_logpush_job_v2(
            create_logpush_job_v2_request=create_request
        )
        assert response is not None
        result = response.get_result()
        assert result.get("success") is True
        job = result.get("result")
        job_id = str(job.get("id"))

        # List all logpush jobs
        response = self.service.get_logpush_jobs_v2()
        assert response is not None
        result = response.get_result()
        assert result.get("success") is True
        all_jobs = result.get("result")

        # Get specific logpush job
        get_job = all_jobs[0]
        get_job_id = str(get_job.get("id"))
        response = self.service.get_logpush_job_v2(job_id=get_job_id)
        assert response is not None
        result = response.get_result()
        assert result.get("success") is True

        # Update logpush job
        update_request = UpdateLogpushJobV2RequestLogpushJobsUpdateGenericReq(
            enabled=False,
            logpull_options="fields=ClientIP,ClientRequestHost",
            destination_conf="https://httpbin.org/post",
            frequency="high"
        )

        response = self.service.update_logpush_job_v2(
            job_id=job_id,
            update_logpush_job_v2_request=update_request
        )
        assert response is not None
        result = response.get_result()
        assert result.get("success") is True

        # Delete all logpush jobs
        for this_job in all_jobs:
            this_job_id = str(this_job.get("id"))
            response = self.service.delete_logpush_job_v2(job_id=this_job_id)
            assert response is not None
            result = response.get_result()
            assert result.get("success") is True

    def test_4_logpush_jobs_cos(self):
        """ create/update/delete/get logpush jobs for COS """
        # Skip this test - requires COS setup
        self.skipTest("Skipping COS test")

        # Create logpush job for COS
        create_request = CreateLogpushJobV2RequestLogpushJobCosReq(
            name="Test123",
            enabled=False,
            logpull_options="timestamps=rfc3339&timestamps=rfc3339",
            cos={
                "bucket_name": "cos-bucket001",
                "region": "us-south",
                "id": "231f5467-3072-4cb9-9e39-a906fa3032ea"
            },
            dataset="http_requests",
            frequency="high",
            ownership_challenge="xxxxx"
        )

        response = self.service.create_logpush_job_v2(
            create_logpush_job_v2_request=create_request
        )
        assert response is not None
        result = response.get_result()
        assert result.get("success") is True
        job = result.get("result")
        job_id = str(job.get("id"))

        # List all logpush jobs
        response = self.service.get_logpush_jobs_v2()
        assert response is not None
        result = response.get_result()
        assert result.get("success") is True
        all_jobs = result.get("result")

        # Get specific logpush job
        get_job = all_jobs[0]
        get_job_id = str(get_job.get("id"))
        response = self.service.get_logpush_job_v2(job_id=get_job_id)
        assert response is not None
        result = response.get_result()
        assert result.get("success") is True

        # Update logpush job
        update_request = UpdateLogpushJobV2RequestLogpushJobsUpdateCosReq(
            enabled=False,
            logpull_options="timestamps=rfc3339&timestamps=rfc3339",
            frequency="low"
        )

        response = self.service.update_logpush_job_v2(
            job_id=job_id,
            update_logpush_job_v2_request=update_request
        )
        assert response is not None
        result = response.get_result()
        assert result.get("success") is True

        # Delete all logpush jobs
        for this_job in all_jobs:
            this_job_id = str(this_job.get("id"))
            response = self.service.delete_logpush_job_v2(job_id=this_job_id)
            assert response is not None
            result = response.get_result()
            assert result.get("success") is True

    def test_5_logpush_jobs_ibmcl(self):
        """ create/update/delete/get logpush jobs for IBM Cloud Logs """

        # Create logpush job for IBM Cloud Logs
        ibmcl_config = LogpushJobIbmclReqIbmcl(
            instance_id=os.getenv("CIS_IBMCL_INSTANCE_ID"),
            region="us-south",
            api_key=os.getenv("CIS_SERVICES_APIKEY")
        )

        create_request = CreateLogpushJobV2RequestLogpushJobIbmclReq(
            name="Test123",
            enabled=False,
            logpull_options="timestamps=rfc3339&timestamps=rfc3339",
            ibmcl=ibmcl_config,
            dataset="http_requests",
            frequency="high"
        )

        response = self.service.create_logpush_job_v2(
            create_logpush_job_v2_request=create_request
        )
        assert response is not None
        result = response.get_result()
        assert result.get("success") is True
        job = result.get("result")
        job_id = str(job.get("id"))

        # List all logpush jobs
        response = self.service.get_logpush_jobs_v2()
        assert response is not None
        result = response.get_result()
        assert result.get("success") is True
        all_jobs = result.get("result")

        # Get specific logpush job
        get_job = all_jobs[0]
        get_job_id = str(get_job.get("id"))
        response = self.service.get_logpush_job_v2(job_id=get_job_id)
        assert response is not None
        result = response.get_result()
        assert result.get("success") is True

        # Update logpush job
        update_request = UpdateLogpushJobV2RequestLogpushJobsUpdateCosReq(
            enabled=False,
            logpull_options="timestamps=rfc3339&timestamps=rfc3339",
            frequency="low"
        )

        response = self.service.update_logpush_job_v2(
            job_id=job_id,
            update_logpush_job_v2_request=update_request
        )
        assert response is not None
        result = response.get_result()
        assert result.get("success") is True

        # Delete all logpush jobs
        for this_job in all_jobs:
            this_job_id = str(this_job.get("id"))
            response = self.service.delete_logpush_job_v2(job_id=this_job_id)
            assert response is not None
            result = response.get_result()
            assert result.get("success") is True

    def test_6_ownership_challenge(self):
        """ Post/Validate Logpush Ownership challenge """

        # Send ownership to destination
        response = self.service.get_logpush_ownership_v2(
            cos={
                "bucket_name": self.cos_bucket,
                "region": self.cos_region,
                "id": self.cos_instance
            }
        )
        assert response is not None
        result = response.get_result()
        assert result.get("success") is True

        # Validate Logpush Ownership Challenge
        response = self.service.validate_logpush_ownership_challenge_v2(
            cos={
                "bucket_name": self.cos_bucket,
                "region": self.cos_region,
                "id": self.cos_instance
            },
            ownership_challenge=self.ownership_token
        )
        assert response is not None
        result = response.get_result()
        assert result.get("success") is True

    def test_7_list_fields_and_jobs(self):
        """ List available fields and jobs """

        # List available fields
        response = self.service.list_fields_for_dataset_v2()
        assert response is not None
        result = response.get_result()
        assert result.get("success") is True

        # List logpush jobs for dataset
        response = self.service.list_logpush_jobs_for_dataset_v2()
        assert response is not None


if __name__ == '__main__':
    unittest.main()
