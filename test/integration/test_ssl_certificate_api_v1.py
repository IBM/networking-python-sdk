# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.

"""
Integration test code to execute ssl certificate client functions
"""

import os
import unittest
from ibm_cloud_networking_services import SslCertificateApiV1


class TestSSLCertV1(unittest.TestCase):
    """ Test class to call SSL sdk functions """

    def setUp(self):
        """ test case setup """
        self.crn = os.getenv("CRN")
        self.zone_id = os.getenv("ZONE_ID")
        self.endpoint = os.getenv("API_ENDPOINT")
        self.ssl = SslCertificateApiV1.new_instance(
            crn=self.crn, zone_identifier=self.zone_id, service_name="cis_services")
        self.ssl.set_service_url(self.endpoint)
        self.certificate = os.getenv("CERTIFICATE")
        self.private_key = os.getenv("PRIVATE_KEY")
        self.update_certificate = os.getenv("UPDATE_CERTIFICATE")
        self.update_private_key = os.getenv("UPDATE_PRIVATE_KEY")

    def tearDown(self):
        """ tear down """
        # Delete the resources
        self._clean_ssl_certificates()
        print("Clean up complete")

    def _clean_ssl_certificates(self):
        resp = self.ssl.list_certificates()
        certs = resp.get_result().get("result")
        for cert in certs:
            print("ssl certificate id", cert.get("id"))
            self.ssl.delete_certificate(cert.get("id"))

    def test_1_list_certificates(self):
        """ test method list all ssl certificate packs """
        resp = self.ssl.list_certificates()
        assert resp is not None
        assert resp.status_code == 200

    def test_1_certificate_actions(self):
        """ test method for order/view/delete ssl certificate packs """
        # order certificate
        resp = self.ssl.order_certificate(
            x_correlation_id="1234", type="dedicated", hosts=["sdk.cistest-load.com"])
        assert resp is not None
        assert resp.status_code == 200
        cert_id = resp.get_result().get("result")["id"]

        # delete certificate
        resp = self.ssl.delete_certificate(
            cert_identifier=cert_id)
        assert resp is not None
        assert resp.status_code == 200

    def test_1_change_ssl_setting(self):
        """ test method change ssl certificate settings """
        resp = self.ssl.change_ssl_setting(value="strict")
        assert resp is not None
        assert resp.status_code == 200

        resp = self.ssl.get_ssl_setting()
        assert resp is not None
        assert resp.status_code == 200

    def test_1_list_custom_certificates(self):
        """ test method list custom ssl certificate settings """
        resp = self.ssl.list_custom_certificates()
        assert resp is not None
        assert resp.status_code == 200

    def test_1_custom_certificate_actions(self):
        """ test method upload/delete/update/get given customized ssl certificate """

        # Construct a dict representation of a CustomCertReqGeoRestrictions model
        custom_cert_req_geo_restrictions_model = {
            'label': 'us'
        }

        # upload custom certificate
        resp = self.ssl.upload_custom_certificate(certificate=self.certificate, private_key=self.private_key,
                                                  bundle_method="optimal", geo_restrictions=custom_cert_req_geo_restrictions_model)
        assert resp is not None
        assert resp.status_code == 200
        custom_cert_id = resp.get_result().get("result")["id"]

        # get custom certificate
        resp = self.ssl.get_custom_certificate(
            custom_cert_id=custom_cert_id)
        assert resp is not None
        assert resp.status_code == 200

        # get update custom certificate
        resp = self.ssl.update_custom_certificate(custom_cert_id=custom_cert_id, certificate=self.update_certificate, private_key=self.update_private_key,
                                                  bundle_method="ubiquitous", geo_restrictions=custom_cert_req_geo_restrictions_model)
        assert resp is not None
        assert resp.status_code == 200

        # list custom certificate
        resp = self.ssl.list_custom_certificates()
        assert resp is not None
        assert resp.status_code == 200

        # set priority of custom certificate

        cust_cert_priority = {
            "id": custom_cert_id,
            "priority": 4}
        resp = self.ssl.change_certificate_priority(
            custom_cert_id=custom_cert_id, certificates=[cust_cert_priority])
        assert resp is not None
        assert resp.status_code == 200

        cust_cert_priority = {
            "id": custom_cert_id,
            "priority": 20}
        resp = self.ssl.change_certificate_priority(
            custom_cert_id=custom_cert_id, certificates=[cust_cert_priority])
        assert resp is not None
        assert resp.status_code == 200

        # delete custom certificate
        resp = self.ssl.delete_custom_certificate(
            custom_cert_id=custom_cert_id)
        assert resp is not None
        assert resp.status_code == 200

    def test_1_universal_certificate_setting_actions(self):
        """ test method get/set custom ssl certificate settings """

        # Construct a dict representation of a CustomCertReqGeoRestrictions model
        custom_cert_req_geo_restrictions_model = {
            'label': 'us'
        }

        # upload custom certificate
        resp = self.ssl.upload_custom_certificate(certificate=self.certificate, private_key=self.private_key,
                                                  bundle_method="optimal",
                                                  geo_restrictions=custom_cert_req_geo_restrictions_model)
        assert resp is not None
        assert resp.status_code == 200
        cert_id = resp.get_result().get("result")["id"]

        # set universal certificate setting
        resp = self.ssl.change_universal_certificate_setting(
            custom_cert_id=cert_id, enabled=False)

        # get uiversal certificate setting
        resp = self.ssl.get_universal_certificate_setting(
            custom_cert_id=cert_id)
        assert resp is not None
        assert resp.status_code == 200

        # delete custom certificate
        resp = self.ssl.delete_custom_certificate(custom_cert_id=cert_id)
        assert resp is not None
        assert resp.status_code == 200

    def test_1_change_tls_verion_12_setting(self):
        """ test method to set tls 1.2 version setting """

        # get tls 1.2 only setting
        resp = self.ssl.get_tls12_setting()
        assert resp is not None
        assert resp.status_code == 200

        # change tls 1.2 only setting "off"
        resp = self.ssl.change_tls12_setting(
            value="off")
        assert resp is not None
        assert resp.status_code == 200

    def test_1_change_tls_verion_13_setting(self):
        """ test method to set tls 1.3 version setting """
        # get tls 1.2 only setting
        resp = self.ssl.get_tls13_setting()
        assert resp is not None
        assert resp.status_code == 200

        # change tls 1.2 only setting
        resp = self.ssl.change_tls13_setting(
            value="on")
        assert resp is not None
        assert resp.status_code == 200


if __name__ == '__main__':
    unittest.main()
