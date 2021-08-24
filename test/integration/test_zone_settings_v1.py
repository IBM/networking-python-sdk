# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.
"""
Integration test code to execute zones settings functions
"""
import os
import unittest
from dotenv import load_dotenv, find_dotenv
from ibm_cloud_networking_services.zones_settings_v1 import ZonesSettingsV1

configFile = "cis.env"

# load the .env file containing your environment variables
try:
    load_dotenv(find_dotenv(filename="cis.env"))
except:
    print('warning: no cis.env file loaded')


class TestZonesSettingsV1(unittest.TestCase):
    """ Sample function to call zones sdk functions """

    # @unittest.skip("skipping")

    def setUp(self):
        """ test case setup """
        if not os.path.exists(configFile):
            raise unittest.SkipTest(
                'External configuration not available, skipping...')

        self.crn = os.getenv("CRN")
        self.endpoint = os.getenv("API_ENDPOINT")
        self.zone_id = os.getenv("ZONE_ID")
        self.url = os.getenv("URL_MATCH")
        # create zones settings record class object
        self.zonesSettings = ZonesSettingsV1.new_instance(
            crn=self.crn, zone_identifier=self.zone_id, service_name="cis_services")
        self.zonesSettings.set_service_url(self.endpoint)

    def tearDown(self):
        """ tear down zone"""
        # Delete the resources
        print("Clean up complete")

    def test_1_zone_settings_dnssec(self):
        """ get zone dnssec """
        response = self.zonesSettings.get_zone_dnssec().get_result()
        assert response is not None and response.get('success') is True
        result = response.get('result')
        if result.get('status') == 'disabled':
            self.status = 'active'
        else:
            self.status = 'disabled'

        """ update zone dnssec """
        response = self.zonesSettings.update_zone_dnssec(
            status=self.status).get_result()

    def test_1_zone_settings_cname_flattening(self):
        """ get zone cname flattening """
        response = self.zonesSettings.get_zone_cname_flattening().get_result()
        assert response is not None and response.get('success') is True
        result = response.get('result')
        if result.get('value') == 'flatten_at_root':
            self.value = 'flatten_all'
        else:
            self.value = 'flatten_at_root'

        """ update zone cname flattening """
        response = self.zonesSettings.update_zone_cname_flattening(
            value=self.value).get_result()
        assert response is not None and response.get('success') is True

    def test_1_zone_settings_opportunistic_encryption(self):
        """ Get opportunistic encryption setting """
        response = self.zonesSettings.get_opportunistic_encryption().get_result()
        assert response is not None and response.get('success') is True
        result = response.get('result')
        if result.get('value') == 'off':
            self.value = 'on'
        else:
            self.value = 'off'

        """ Update opportunistic encryption setting """
        response = self.zonesSettings.update_opportunistic_encryption(
            value=self.value).get_result()
        assert response is not None and response.get('success') is True

    @unittest.skip("skipping")    
    def test_1_automatic_https_rewrites(self):
        """ Get automatic https rewrites setting """
        response = self.zonesSettings.get_automatic_https_rewrites().get_result()
        assert response is not None and response.get('success') is True
        result = response.get('result')
        if result.get('value') == 'off':
            self.value = 'on'
        else:
            self.value = 'off'

        """ Update automatic https rewrites setting """
        response = self.zonesSettings.update_automatic_https_rewrites(
            value=self.value).get_result()
        assert response is not None and response.get('success') is True

    def test_1_true_client_ip_setting(self):
        """ Get true client IP setting """
        response = self.zonesSettings.get_true_client_ip().get_result()
        assert response is not None and response.get('success') is True
        result = response.get('result')
        if result.get('value') == 'off':
            self.value = 'on'
        else:
            self.value = 'off'

        """ Update true client IP setting """
        response = self.zonesSettings.update_true_client_ip(
            value=self.value).get_result()
        assert response is not None and response.get('success') is True

    def test_1_always_use_https(self):
        """ Get true client IP setting """
        response = self.zonesSettings.get_always_use_https().get_result()
        assert response is not None and response.get('success') is True
        result = response.get('result')
        if result.get('value') == 'off':
            self.value = 'on'
        else:
            self.value = 'off'

        """ Update true client IP setting """
        response = self.zonesSettings.update_always_use_https(
            value=self.value).get_result()
        assert response is not None and response.get('success') is True

    def test_1_image_size_optimization(self):
        """ Get image size optimization setting """
        response = self.zonesSettings.get_image_size_optimization().get_result()
        assert response is not None and response.get('success') is True
        result = response.get('result')
        if result.get('value') == 'lossless':
            self.value = 'lossy'
        else:
            self.value = 'lossless'

        """ Update image size optimization setting """
        response = self.zonesSettings.update_image_size_optimization(
            value=self.value).get_result()
        assert response is not None and response.get('success') is True

    def test_1_script_load_optimization_setting(self):
        """ Get script load optimization setting """
        response = self.zonesSettings.get_script_load_optimization().get_result()
        assert response is not None and response.get('success') is True
        result = response.get('result')
        if result.get('value') == 'off':
            self.value = 'on'
        else:
            self.value = 'off'

        """ Update script load optimization setting """
        response = self.zonesSettings.update_script_load_optimization(
            value=self.value).get_result()
        assert response is not None and response.get('success') is True

    def test_1_image_load_optimization_setting(self):
        """ Get image load optimization setting """
        response = self.zonesSettings.get_image_load_optimization().get_result()
        assert response is not None and response.get('success') is True
        result = response.get('result')
        if result.get('value') == 'off':
            self.value = 'on'
        else:
            self.value = 'off'

        """ Update script load optimization setting """
        response = self.zonesSettings.update_image_load_optimization(
            value=self.value).get_result()
        assert response is not None and response.get('success') is True

    def test_1_minify_setting(self):
        """ Get minify setting """
        response = self.zonesSettings.get_minify().get_result()
        assert response is not None and response.get('success') is True
        result = response.get('result').get('value')
        if result.get('css') == 'on':
            self.value = 'off'
        else:
            self.value = 'on'

        """ Update minify css setting """
        self.minfy = {
            'css': self.value,
            'html': self.value,
            'js': self.value
        }
        response = self.zonesSettings.update_minify(
            value=self.minfy).get_result()
        assert response is not None and response.get('success') is True

    @unittest.skip("skipping")    
    def test_1_min_tls_setting(self):
        """ Get min tls setting """
        response = self.zonesSettings.get_min_tls_version().get_result()
        assert response is not None and response.get('success') is True
        result = response.get('result')
        if result.get('value') == '1.0':
            self.value = '1.2'
        else:
            self.value = '1.0'

        """ Update min tls setting """
        response = self.zonesSettings.update_min_tls_version(
            value=self.value).get_result()
        assert response is not None and response.get('success') is True

    def test_1_ip_geolocation_setting(self):
        """ Get IP geolocation setting """
        response = self.zonesSettings.get_ip_geolocation().get_result()
        assert response is not None and response.get('success') is True
        result = response.get('result')
        if result.get('value') == 'off':
            self.value = 'on'
        else:
            self.value = 'off'

        """ Update IP geolocation setting """
        response = self.zonesSettings.update_ip_geolocation(
            value=self.value).get_result()
        assert response is not None and response.get('success') is True

    def test_1_server_side_exclude_setting(self):
        """ Get server side exclude setting """
        response = self.zonesSettings.get_server_side_exclude().get_result()
        assert response is not None and response.get('success') is True
        result = response.get('result')
        if result.get('value') == 'off':
            self.value = 'on'
        else:
            self.value = 'off'

        """ Update server side exclude setting """
        response = self.zonesSettings.update_server_side_exclude(
            value=self.value).get_result()
        assert response is not None and response.get('success') is True

    def test_1_security_header_setting(self):
        """ Get security header setting """
        response = self.zonesSettings.get_security_header().get_result()
        assert response is not None and response.get('success') is True
        result = response.get('result')
        print(result)
        if result.get('value').get('enabled') == True:
            self.value = False
        else:
            self.value = True
        strict_transport_security = {
            "strict_transport_security": {
                "enabled": self.value,
                "max_age": 86400,
                "include_subdomains": self.value,
                "nosniff": self.value
            }}

        """ Update security header setting """
        response = self.zonesSettings.update_security_header(
            value=strict_transport_security).get_result()
        assert response is not None and response.get('success') is True

    
    @unittest.skip("skipping")    
    def test_1_mobile_redirect_setting(self):
        """ Get mobile redirect setting """
        response = self.zonesSettings.get_mobile_redirect().get_result()
        assert response is not None and response.get('success') is True
        result = response.get('result')
        print(result)
        domain = self.url.split('.')[0]
        if result.get('value').get('status') == 'on':
            self.value = {
                "status": "off",
                "mobile_subdomain": domain,
                "strip_uri": False
            }
        else:
            self.value = {
                "status": "on",
                "mobile_subdomain": domain,
                "strip_uri": False
            }

        """ Update mobile redirect setting """
        response = self.zonesSettings.update_mobile_redirect(
            value=self.value).get_result()
        assert response is not None and response.get('success') is True

    def test_1_prefetch_preload_setting(self):
        """ Get prefetch preload setting """
        response = self.zonesSettings.get_prefetch_preload().get_result()
        assert response is not None and response.get('success') is True
        result = response.get('result')
        if result.get('value') == 'off':
            self.value = 'on'
        else:
            self.value = 'off'

        """ Update prefetch preload setting """
        response = self.zonesSettings.update_prefetch_preload(
            value=self.value).get_result()
        assert response is not None and response.get('success') is True

    def test_1_http2_setting(self):
        """ Get http2 setting """
        response = self.zonesSettings.get_http2().get_result()
        assert response is not None and response.get('success') is True
        result = response.get('result')
        if result.get('value') == 'off':
            self.value = 'on'
        else:
            self.value = 'off'

        """ Update http2 setting """
        response = self.zonesSettings.update_http2(
            value=self.value).get_result()
        assert response is not None and response.get('success') is True

    def test_1_http3_setting(self):
        """ Get http3 setting """
        response = self.zonesSettings.get_http3().get_result()
        assert response is not None and response.get('success') is True
        result = response.get('result')
        if result.get('value') == 'off':
            self.value = 'on'
        else:
            self.value = 'off'

        """ Update http3 setting """
        response = self.zonesSettings.update_http3(
            value=self.value).get_result()
        assert response is not None and response.get('success') is True

    def test_1_ipv6_setting(self):
        """ Get ipv6 setting """
        response = self.zonesSettings.get_ipv6().get_result()
        assert response is not None and response.get('success') is True
        result = response.get('result')
        if result.get('value') == 'off':
            self.value = 'on'
        else:
            self.value = 'off'

        """ Update ipv6 setting """
        response = self.zonesSettings.update_ipv6(
            value=self.value).get_result()
        assert response is not None and response.get('success') is True

    def test_1_websockets_setting(self):
        """ Get websockets setting """
        response = self.zonesSettings.get_web_sockets().get_result()
        assert response is not None and response.get('success') is True
        result = response.get('result')
        if result.get('value') == 'off':
            self.value = 'on'
        else:
            self.value = 'off'

        """ Update websockets setting """
        response = self.zonesSettings.update_web_sockets(
            value=self.value).get_result()
        assert response is not None and response.get('success') is True

    def test_1_pseudo_ipv4_setting(self):
        """ Get pseudo ipv4 setting """
        response = self.zonesSettings.get_pseudo_ipv4().get_result()
        assert response is not None and response.get('success') is True
        result = response.get('result')
        if result.get('value') == 'add_header':
            self.value = 'overwrite_header'
        else:
            self.value = 'add_header'

        """ Update pseudo ipv4 setting """
        response = self.zonesSettings.update_pseudo_ipv4(
            value=self.value).get_result()
        assert response is not None and response.get('success') is True

    def test_1_response_buffering_setting(self):
        """ Get response buffer setting """
        response = self.zonesSettings.get_response_buffering().get_result()
        assert response is not None and response.get('success') is True
        result = response.get('result')
        if result.get('value') == 'off':
            self.value = 'on'
        else:
            self.value = 'off'

        """ Update response buffer setting """
        response = self.zonesSettings.update_response_buffering(
            value=self.value).get_result()
        assert response is not None and response.get('success') is True

    def test_1_hotlink_protection_setting(self):
        """ Get hotlink protection setting """
        response = self.zonesSettings.get_hotlink_protection().get_result()
        assert response is not None and response.get('success') is True
        result = response.get('result')
        if result.get('value') == 'off':
            self.value = 'on'
        else:
            self.value = 'off'

        """ Update hotlink protection setting """
        response = self.zonesSettings.update_hotlink_protection(
            value=self.value).get_result()
        assert response is not None and response.get('success') is True

    def test_1_max_upload_setting(self):
        """ Get max upload setting """
        response = self.zonesSettings.get_max_upload().get_result()
        assert response is not None and response.get('success') is True
        result = response.get('result')
        if result.get('value') == 300:
            self.value = 450
        else:
            self.value = 300

        """ Update max upload setting """
        response = self.zonesSettings.update_max_upload(
            value=self.value).get_result()
        assert response is not None and response.get('success') is True

    def test_1_tls_client_auth_setting(self):
        """ Get tls client auth setting """
        response = self.zonesSettings.get_tls_client_auth().get_result()
        assert response is not None and response.get('success') is True
        result = response.get('result')
        if result.get('value') == "on":
            self.value = "off"
        else:
            self.value = "on"

        """ Update tls client auth setting """
        response = self.zonesSettings.update_tls_client_auth(
            value=self.value).get_result()
        assert response is not None and response.get('success') is True

    def test_1_browser_check_setting(self):
        """ Get browser check setting """
        response = self.zonesSettings.get_browser_check().get_result()
        assert response is not None and response.get('success') is True
        result = response.get('result')
        if result.get('value') == "on":
            self.value = "off"
        else:
            self.value = "on"

        """ Update browser check setting """
        response = self.zonesSettings.update_browser_check(
            value=self.value).get_result()
        assert response is not None and response.get('success') is True

    def test_1_origin_error_page_passthru_setting(self):
        """ Get orgin error page pass thru setting """
        response = self.zonesSettings.get_enable_error_pages_on().get_result()
        assert response is not None and response.get('success') is True
        result = response.get('result')
        if result.get('value') == "on":
            self.value = "off"
        else:
            self.value = "on"

        """ Update origin error page pass thru setting """
        response = self.zonesSettings.update_enable_error_pages_on(
            value=self.value).get_result()
        assert response is not None and response.get('success') is True

    def test_1_web_application_firewall_setting(self):
        """ Get waf setting """
        response = self.zonesSettings.get_web_application_firewall().get_result()
        assert response is not None and response.get('success') is True
        result = response.get('result')
        if result.get('value') == "on":
            self.value = "off"
        else:
            self.value = "on"

        """ Update waf setting """
        response = self.zonesSettings.update_web_application_firewall(
            value=self.value).get_result()
        assert response is not None and response.get('success') is True

    def test_1_challenge_ttl_setting(self):
        """ Get challenge ttl setting """
        response = self.zonesSettings.get_challenge_ttl().get_result()
        assert response is not None and response.get('success') is True
        result = response.get('result')
        if result.get('value') == 1800:
            self.value = 7200
        else:
            self.value = 1800

        """ Update challenge ttl setting """
        response = self.zonesSettings.update_challenge_ttl(
            value=self.value).get_result()
        assert response is not None and response.get('success') is True

    def test_1_cipher_setting(self):
        """ Get cipher setting """
        response = self.zonesSettings.get_ciphers().get_result()
        assert response is not None and response.get('success') is True

        """ Update cipher setting """
        response = self.zonesSettings.update_ciphers(
            value=["AES256-GCM-SHA384", "AES256-SHA256"]).get_result()
        print("update", response)
        assert response is not None and response.get('success') is True


if __name__ == '__main__':
    unittest.main()
