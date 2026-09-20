# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.

"""
Integration test code to execute caching api
"""

from cgitb import enable
from http.client import responses
import os
import unittest
from dotenv import load_dotenv, find_dotenv
from ibm_cloud_networking_services.authenticated_origin_pull_api_v1 import AuthenticatedOriginPullApiV1
from ibm_cloud_networking_services.ssl_certificate_api_v1 import Certificate

configFile = "cis.env"

# load the .env file containing your environment variables
try:
    load_dotenv(find_dotenv(filename="cis.env"))
except:
    print('warning: no cis.env file loaded')

##############################################################################
# ZoneLevelAuthenticatedOriginPull
##############################################################################

class TestZoneAuthenticatedOriginPullApiV1(unittest.TestCase):
    """ Test class for Zone Level Authenticated Origin Pull APIs"""

    def setUp(self):
        if not os.path.exists(configFile):
            raise unittest.SkipTest(
                'External configuration not available, skipping...')
        self.crn = os.getenv("CRN")
        self.zone_id = os.getenv("ZONE_ID")
        self.endpoint = os.getenv("API_ENDPOINT")
        self.auth = AuthenticatedOriginPullApiV1.new_instance(
            crn=self.crn, zone_identifier=self.zone_id, service_name="cis_services")
        self.auth.set_service_url(self.endpoint)
 
        self. certificate_name = "-----BEGIN CERTIFICATE-----\nMIICljCCAX4CCQDXCJC5bOv97DANBgkqhkiG9w0BAQsFADANMQswCQYDVQQGEwJJ\nTjAeFw0yMjA1MTYwNDQxMjFaFw0yMzA1MTYwNDQxMjFaMA0xCzAJBgNVBAYTAklO\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA3ka/M7mE6Exrc2VhHe9z\nCSU6D2Z45+u9IO5TghXM6luZzrPr2CuV/HAKTyG5YZtgIlYFV+CXI1a+hVnJnV6f\nHvkFlXgST7xjqqdff6P72gMJ06HPoR30tvTHzIGF7+ZEoAfSfZZOR/BJRowW9PoA\nvA8BtfNai3Jm+NYQfQxFf4LT25k2AHJW/2o7cGIbfPsEC+mKWBOzXMd38ZSMFq17\nxX81fnMrz0YK1x/tkJwIL5P6HPoLsYNCcpTZ3/f9gJJ+4j8c3xl97j8dh2Zab3rP\noBaDJt4oymanjyLqRZBBx+Xb6dv7L8MUJ9LM80Y9fmAK3Iui5R1s0k21qsA9VbF0\nCQIDAQABMA0GCSqGSIb3DQEBCwUAA4IBAQA6xuG19P4wckXQIRJz4t2me601FuBp\nHsfBXd8oKw4JEVrKtVtPb4bl7qMorC6Mz520QoAVKYe+nRpk63A4LkZ3asjyDs+Z\no2LawLE2goN6/elA6fQd92EtjipKwFK0Z4NrF/ekPheNjPtWUtqXo0JmHb4qDHHf\nsLq/oFym1J0Um8lW8hrpsf7C9Bnh10zvBtl/y7H6mTN7nOafS+puoVTzz+Rj4P6N\nBjFZixpmVgVFL+x9GnsJwSQFybMDfmBgfAEfqxPLTKoV0PlHktTuWSkMoaJBKC1Q\nZa/qK1n5UWhvIVuzbbd5dFQxE/N8P/+4O4YYGEqNmRo3SoId6uCYAEn0\n-----END CERTIFICATE-----\n"
        self.private_key = "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDeRr8zuYToTGtz\nZWEd73MJJToPZnjn670g7lOCFczqW5nOs+vYK5X8cApPIblhm2AiVgVX4JcjVr6F\nWcmdXp8e+QWVeBJPvGOqp19/o/vaAwnToc+hHfS29MfMgYXv5kSgB9J9lk5H8ElG\njBb0+gC8DwG181qLcmb41hB9DEV/gtPbmTYAclb/ajtwYht8+wQL6YpYE7Ncx3fx\nlIwWrXvFfzV+cyvPRgrXH+2QnAgvk/oc+guxg0JylNnf9/2Akn7iPxzfGX3uPx2H\nZlpves+gFoMm3ijKZqePIupFkEHH5dvp2/svwxQn0szzRj1+YArci6LlHWzSTbWq\nwD1VsXQJAgMBAAECggEATaCXlhDsgdRuklaNnE7L9h2yMT6waw7BdobFU2EZt59W\nEAJ2E4DlWMwoTYqRm60P3e3837voDMd2skuxReyN1dtSP+k3O/GnPSpHB+TVSEZX\nYDnasYIsvNiwDpQNmsLopJsWwBWGMUmRzbmPKu9E4mi7SDg9HwZNQApCp+lpPCZl\n527ZM4ikgMbu7zNl5zDaTMXNs4PllPMraimBJSw5/PCgDHGMxn8xzLIPMxvS1lVC\nbgwNQtsbVQ1kqe7MmC/mxNx33F1NGTRy+fGw5HaBgmS+DlWWS29gnO4LXf/sL/KT\n9nSFkggNdWg2LNHVtdJ/G1PZqM8vr3wkhFEkUbmEIQKBgQD4IUDDYD64mX9GDu3/\nnBdOw0hz8TrzNOLdA9NwMzwFX/tvX7wiUj+8H033RW8h3uiru7giGBQ/B9daltdt\n/9/jzMJSjiH7G5WbC8uRapZeW4LWkKcMKZpVvBSHLE8P/v8KbQkIodsHi/PZGoRt\nyoIgwPfnsaAeYTGAXWjYP+dt1wKBgQDlU5H5zV413trx6W+T7jxdh/q3zrbTYmdr\ncfMXQBVl1HCRzrPkQ7aq7XbrDQsCkQDt4mSX6sQg2pTD1ZIgSpoZpMwEHEua6NXv\nIOj1VPuj5y4cOO/skPyA7oqUtuFWeQKxLI5Fm3HDcXvb5kSw7PPIIUVKrHS1+/Bo\neqTgceMxHwKBgDCC59OK5JhYwk5jKtrXnKL0gRzR4/GavGPzlIoSKkDuxAzBTdnz\n9KwF/stCUvjvSNQSjmx0ArlUAiGe7h1+cjpqVO+pBDHA8d3vT2xtx1pJT+o9O7ug\nAqGSdPz8h7Sb6ScTrDl404bFMPaYPZ3tgsV+lLlCvAhUfkYXfSESVV/fAoGACP8V\nS/J1jrF2b2UT/n6rGZQ7DrjqTTKgEgP/YFsgO8VwwReV0Q+i++Oi9aemVexwV+S4\nw4jvNsa8bU5UlDW5A+aGJmchxCr8MYxd9znlQVHRakQFjYdGkJxLDXh7MJRAucig\nsDRf6yXpkP/gk/xHuAMuH7bSQU1n6gFdtHxjSEsCgYAsItXD1hV1aXnYdXeZkMew\nSUWJ6pvLUj+FpuRqJ+zJsv7G1MT9OINwnfXG1hTpxpJ2Igx/cO6ZXvl8AXf5B5rA\nii/573Z7XGUENDfE8LYOKa6eFLyl2fCbSbs/8K+Y6UlsmPmwF1J3eK2oIOKrsyyH\nyN60AdUg197VxTkO6bjBvA==\n-----END PRIVATE KEY-----\n"
        
        self.x_correlation_id = "12345"
        self.url = os.getenv("URL")

    def test_1_zone_origin_pull(self):

        # To check if Authenticated Origin Pull settings is enabled or not
        resp = self.auth.get_zone_origin_pull_settings()
        assert resp is not None
        assert resp.status_code == 202
        assert resp.get_result().get("success") == True

        # To set Authenticated Origin Pull settings enabled -> True or False
        values = [True, False]
        for value in values:
            resp = self.auth.set_zone_origin_pull_settings(enabled=value)
            assert resp is not None
            assert resp.status_code == 202
            assert resp.get_result().get("success") == True
            assert resp.get_result().get("result")["enabled"] == value

        # To fetch list of certificates in the zone
        resp = self.auth.list_zone_origin_pull_certificates()
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("success") == True
        assert isinstance(resp.get_result().get("result"), list)

        # Set Authenticated Origin Pull settings as enabled before uploading
        self.auth.set_zone_origin_pull_settings(enabled=True)
       
        # Upload certificate
        resp = self.auth.upload_zone_origin_pull_certificate(certificate=self.certificate_name, private_key=self.private_key)
        assert resp is not None
        assert resp.status_code == 201
        assert resp.get_result().get("success") == True
        assert resp.get_result().get("result")["certificate"] == self.certificate_name

        cert_identifier = resp.get_result().get("result")["id"]
                
        # Fetch certificate with ID
        resp = self.auth.get_zone_origin_pull_certificate(cert_identifier=cert_identifier, x_correlation_id=self.x_correlation_id)
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("success") == True
        assert resp.get_result().get("result")["id"] == cert_identifier

        # Delete certificate with ID
        resp = self.auth.delete_zone_origin_pull_certificate(cert_identifier=cert_identifier, x_correlation_id=self.x_correlation_id)
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("success") == True
       

##############################################################################
# PerHostnameAuthenticatedOriginPull
##############################################################################


class TestHostnameAuthenticatedOriginPullApiV1(unittest.TestCase):
    """ Test class for Hostname Authenticated Origin Pull APIs"""

    def setUp(self):
        if not os.path.exists(configFile):
            raise unittest.SkipTest(
                'External configuration not available, skipping...')
        self.crn = os.getenv("CRN")
        self.zone_id = os.getenv("ZONE_ID")
        self.endpoint = os.getenv("API_ENDPOINT")
        self.auth = AuthenticatedOriginPullApiV1.new_instance(
            crn=self.crn, zone_identifier=self.zone_id, service_name="cis_services")
        self.auth.set_service_url(self.endpoint)

        self. certificate_name = "-----BEGIN CERTIFICATE-----\nMIICljCCAX4CCQDXCJC5bOv97DANBgkqhkiG9w0BAQsFADANMQswCQYDVQQGEwJJ\nTjAeFw0yMjA1MTYwNDQxMjFaFw0yMzA1MTYwNDQxMjFaMA0xCzAJBgNVBAYTAklO\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA3ka/M7mE6Exrc2VhHe9z\nCSU6D2Z45+u9IO5TghXM6luZzrPr2CuV/HAKTyG5YZtgIlYFV+CXI1a+hVnJnV6f\nHvkFlXgST7xjqqdff6P72gMJ06HPoR30tvTHzIGF7+ZEoAfSfZZOR/BJRowW9PoA\nvA8BtfNai3Jm+NYQfQxFf4LT25k2AHJW/2o7cGIbfPsEC+mKWBOzXMd38ZSMFq17\nxX81fnMrz0YK1x/tkJwIL5P6HPoLsYNCcpTZ3/f9gJJ+4j8c3xl97j8dh2Zab3rP\noBaDJt4oymanjyLqRZBBx+Xb6dv7L8MUJ9LM80Y9fmAK3Iui5R1s0k21qsA9VbF0\nCQIDAQABMA0GCSqGSIb3DQEBCwUAA4IBAQA6xuG19P4wckXQIRJz4t2me601FuBp\nHsfBXd8oKw4JEVrKtVtPb4bl7qMorC6Mz520QoAVKYe+nRpk63A4LkZ3asjyDs+Z\no2LawLE2goN6/elA6fQd92EtjipKwFK0Z4NrF/ekPheNjPtWUtqXo0JmHb4qDHHf\nsLq/oFym1J0Um8lW8hrpsf7C9Bnh10zvBtl/y7H6mTN7nOafS+puoVTzz+Rj4P6N\nBjFZixpmVgVFL+x9GnsJwSQFybMDfmBgfAEfqxPLTKoV0PlHktTuWSkMoaJBKC1Q\nZa/qK1n5UWhvIVuzbbd5dFQxE/N8P/+4O4YYGEqNmRo3SoId6uCYAEn0\n-----END CERTIFICATE-----\n"
        self.private_key = "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDeRr8zuYToTGtz\nZWEd73MJJToPZnjn670g7lOCFczqW5nOs+vYK5X8cApPIblhm2AiVgVX4JcjVr6F\nWcmdXp8e+QWVeBJPvGOqp19/o/vaAwnToc+hHfS29MfMgYXv5kSgB9J9lk5H8ElG\njBb0+gC8DwG181qLcmb41hB9DEV/gtPbmTYAclb/ajtwYht8+wQL6YpYE7Ncx3fx\nlIwWrXvFfzV+cyvPRgrXH+2QnAgvk/oc+guxg0JylNnf9/2Akn7iPxzfGX3uPx2H\nZlpves+gFoMm3ijKZqePIupFkEHH5dvp2/svwxQn0szzRj1+YArci6LlHWzSTbWq\nwD1VsXQJAgMBAAECggEATaCXlhDsgdRuklaNnE7L9h2yMT6waw7BdobFU2EZt59W\nEAJ2E4DlWMwoTYqRm60P3e3837voDMd2skuxReyN1dtSP+k3O/GnPSpHB+TVSEZX\nYDnasYIsvNiwDpQNmsLopJsWwBWGMUmRzbmPKu9E4mi7SDg9HwZNQApCp+lpPCZl\n527ZM4ikgMbu7zNl5zDaTMXNs4PllPMraimBJSw5/PCgDHGMxn8xzLIPMxvS1lVC\nbgwNQtsbVQ1kqe7MmC/mxNx33F1NGTRy+fGw5HaBgmS+DlWWS29gnO4LXf/sL/KT\n9nSFkggNdWg2LNHVtdJ/G1PZqM8vr3wkhFEkUbmEIQKBgQD4IUDDYD64mX9GDu3/\nnBdOw0hz8TrzNOLdA9NwMzwFX/tvX7wiUj+8H033RW8h3uiru7giGBQ/B9daltdt\n/9/jzMJSjiH7G5WbC8uRapZeW4LWkKcMKZpVvBSHLE8P/v8KbQkIodsHi/PZGoRt\nyoIgwPfnsaAeYTGAXWjYP+dt1wKBgQDlU5H5zV413trx6W+T7jxdh/q3zrbTYmdr\ncfMXQBVl1HCRzrPkQ7aq7XbrDQsCkQDt4mSX6sQg2pTD1ZIgSpoZpMwEHEua6NXv\nIOj1VPuj5y4cOO/skPyA7oqUtuFWeQKxLI5Fm3HDcXvb5kSw7PPIIUVKrHS1+/Bo\neqTgceMxHwKBgDCC59OK5JhYwk5jKtrXnKL0gRzR4/GavGPzlIoSKkDuxAzBTdnz\n9KwF/stCUvjvSNQSjmx0ArlUAiGe7h1+cjpqVO+pBDHA8d3vT2xtx1pJT+o9O7ug\nAqGSdPz8h7Sb6ScTrDl404bFMPaYPZ3tgsV+lLlCvAhUfkYXfSESVV/fAoGACP8V\nS/J1jrF2b2UT/n6rGZQ7DrjqTTKgEgP/YFsgO8VwwReV0Q+i++Oi9aemVexwV+S4\nw4jvNsa8bU5UlDW5A+aGJmchxCr8MYxd9znlQVHRakQFjYdGkJxLDXh7MJRAucig\nsDRf6yXpkP/gk/xHuAMuH7bSQU1n6gFdtHxjSEsCgYAsItXD1hV1aXnYdXeZkMew\nSUWJ6pvLUj+FpuRqJ+zJsv7G1MT9OINwnfXG1hTpxpJ2Igx/cO6ZXvl8AXf5B5rA\nii/573Z7XGUENDfE8LYOKa6eFLyl2fCbSbs/8K+Y6UlsmPmwF1J3eK2oIOKrsyyH\nyN60AdUg197VxTkO6bjBvA==\n-----END PRIVATE KEY-----\n"

        self.x_correlation_id = "98765"
        self.url = os.getenv("URL")

    def test_1_hostname_origin_pull(self):
        
        # Get settings for the hostname
        resp = self.auth.get_hostname_origin_pull_settings(hostname=self.url)
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("success") == True


        # Upload certificate
        resp = self.auth.upload_hostname_origin_pull_certificate(certificate=self.certificate_name, private_key=self.private_key, x_correlation_id = self.x_correlation_id)
        assert resp is not None
        assert resp.status_code == 201
        assert resp.get_result().get("success") == True
        assert resp.get_result().get("result")["certificate"] == self.certificate_name

        cert_identifier = resp.get_result().get("result")["id"]

       # Set a hostname to a certificate 
        values = [True, False]
        for value in values:
            config = [
                {
                    "hostname": self.url,
                    "cert_id": cert_identifier,
                    "enabled": value
                }
            ]
            resp = self.auth.set_hostname_origin_pull_settings(config=config)
            assert resp is not None
            assert resp.status_code == 202
            assert resp.get_result().get("success") == True
            assert resp.get_result().get("result")[0]["cert_id"] == cert_identifier
            assert resp.get_result().get("result")[0]["enabled"] == value

        # Get certificate with ID
        resp = self.auth.get_hostname_origin_pull_certificate(cert_identifier=cert_identifier, x_correlation_id=self.x_correlation_id)
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("success") == True

        # Delete certificate with ID
        resp = self.auth.delete_hostname_origin_pull_certificate(cert_identifier=cert_identifier, x_correlation_id=self.x_correlation_id)
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("success") == True


if __name__ == '__main__':
    unittest.main()
