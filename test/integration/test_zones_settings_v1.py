# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2026.

"""
Integration test code to execute Zones Settings
"""

import os
import unittest
from dotenv import load_dotenv, find_dotenv
from ibm_cloud_networking_services import ZonesSettingsV1

configFile = "cis.env"

# load the .env file containing your environment variables
try:
    load_dotenv(find_dotenv(filename="cis.env"))
except:
    print('warning: no cis.env file loaded')


class TestZonesSettingsV1(unittest.TestCase):
    """ Test class to call zones settings sdk functions """

    @unittest.skip("Authentication failing")

    def setUp(self):
        """ test case setup """
        if not os.path.exists(configFile):
            raise unittest.SkipTest(
                'External configuration not available, skipping...')
        self.crn = os.getenv("CRN")
        self.zone_id = os.getenv("ZONE_ID")
        self.endpoint = os.getenv("API_ENDPOINT")
        self.service = ZonesSettingsV1.new_instance(
            service_name="cis_services", crn=self.crn, zone_identifier=self.zone_id)
        self.service.set_service_url(self.endpoint)

    def tearDown(self):
        """ tear down """
        print("Clean up complete")

    ################## Zone DNSSEC ######################
    def test_1_get_zone_dnssec(self):
        """ test get zone dnssec """
        response = self.service.get_zone_dnssec()
        assert response is not None
        assert response.status_code == 200

    def test_2_update_zone_dnssec(self):
        """ test update zone dnssec """
        response = self.service.update_zone_dnssec(
            status='active'
        )
        assert response is not None
        assert response.status_code == 200

    ################## Zone CNAME Flattening ######################
    def test_3_get_zone_cname_flattening(self):
        """ test get zone cname flattening """
        response = self.service.get_zone_cname_flattening()
        assert response is not None
        assert response.status_code == 200

    def test_4_update_zone_cname_flattening(self):
        """ test update zone cname flattening """
        response = self.service.update_zone_cname_flattening(
            value='flatten_at_root'
        )
        assert response is not None
        assert response.status_code == 200

    ################## Opportunistic Encryption ######################
    def test_5_get_opportunistic_encryption(self):
        """ test get opportunistic encryption """
        response = self.service.get_opportunistic_encryption()
        assert response is not None
        assert response.status_code == 200

    def test_6_update_opportunistic_encryption(self):
        """ test update opportunistic encryption """
        response = self.service.update_opportunistic_encryption(
            value='on'
        )
        assert response is not None
        assert response.status_code == 200

    ################## Opportunistic Onion ######################
    def test_7_get_opportunistic_onion(self):
        """ test get opportunistic onion """
        response = self.service.get_opportunistic_onion()
        assert response is not None
        assert response.status_code == 200

    def test_8_update_opportunistic_onion(self):
        """ test update opportunistic onion """
        response = self.service.update_opportunistic_onion(
            value='on'
        )
        assert response is not None
        assert response.status_code == 200

    ################## Challenge TTL ######################
    def test_9_get_challenge_ttl(self):
        """ test get challenge ttl """
        response = self.service.get_challenge_ttl()
        assert response is not None
        assert response.status_code == 200

    def test_10_update_challenge_ttl(self):
        """ test update challenge ttl """
        response = self.service.update_challenge_ttl(
            value=1800
        )
        assert response is not None
        assert response.status_code == 200

    ################## Automatic HTTPS Rewrites ######################
    def test_11_get_automatic_https_rewrites(self):
        """ test get automatic https rewrites """
        response = self.service.get_automatic_https_rewrites()
        assert response is not None
        assert response.status_code == 200

    def test_12_update_automatic_https_rewrites(self):
        """ test update automatic https rewrites """
        response = self.service.update_automatic_https_rewrites(
            value='on'
        )
        assert response is not None
        assert response.status_code == 200

    ################## True Client IP ######################
    def test_13_get_true_client_ip(self):
        """ test get true client ip """
        response = self.service.get_true_client_ip()
        assert response is not None
        assert response.status_code == 200

    def test_14_update_true_client_ip(self):
        """ test update true client ip """
        response = self.service.update_true_client_ip(
            value='on'
        )
        assert response is not None
        assert response.status_code == 200

    ################## Always Use HTTPS ######################
    def test_15_get_always_use_https(self):
        """ test get always use https """
        response = self.service.get_always_use_https()
        assert response is not None
        assert response.status_code == 200

    def test_16_update_always_use_https(self):
        """ test update always use https """
        response = self.service.update_always_use_https(
            value='on'
        )
        assert response is not None
        assert response.status_code == 200

    ################## Image Size Optimization ######################
    def test_17_get_image_size_optimization(self):
        """ test get image size optimization """
        response = self.service.get_image_size_optimization()
        assert response is not None
        assert response.status_code == 200

    def test_18_update_image_size_optimization(self):
        """ test update image size optimization """
        response = self.service.update_image_size_optimization(
            value='lossless'
        )
        assert response is not None
        assert response.status_code == 200

    ################## Script Load Optimization ######################
    def test_19_get_script_load_optimization(self):
        """ test get script load optimization """
        response = self.service.get_script_load_optimization()
        assert response is not None
        assert response.status_code == 200

    def test_20_update_script_load_optimization(self):
        """ test update script load optimization """
        response = self.service.update_script_load_optimization(
            value='on'
        )
        assert response is not None
        assert response.status_code == 200

    ################## Image Load Optimization ######################
    def test_21_get_image_load_optimization(self):
        """ test get image load optimization """
        response = self.service.get_image_load_optimization()
        assert response is not None
        assert response.status_code == 200

    def test_22_update_image_load_optimization(self):
        """ test update image load optimization """
        response = self.service.update_image_load_optimization(
            value='on'
        )
        assert response is not None
        assert response.status_code == 200

    ################## Minify ######################
    def test_23_get_minify(self):
        """ test get minify """
        response = self.service.get_minify()
        assert response is not None
        assert response.status_code == 200

    def test_24_update_minify(self):
        """ test update minify """
        response = self.service.update_minify()
        assert response is not None
        assert response.status_code == 200

    ################## Min TLS Version ######################
    def test_25_get_min_tls_version(self):
        """ test get min tls version """
        response = self.service.get_min_tls_version()
        assert response is not None
        assert response.status_code == 200

    def test_26_update_min_tls_version(self):
        """ test update min tls version """
        response = self.service.update_min_tls_version(
            value='1.2'
        )
        assert response is not None
        assert response.status_code == 200

    ################## IP Geolocation ######################
    def test_27_get_ip_geolocation(self):
        """ test get ip geolocation """
        response = self.service.get_ip_geolocation()
        assert response is not None
        assert response.status_code == 200

    def test_28_update_ip_geolocation(self):
        """ test update ip geolocation """
        response = self.service.update_ip_geolocation(
            value='on'
        )
        assert response is not None
        assert response.status_code == 200

    ################## Server Side Exclude ######################
    def test_29_get_server_side_exclude(self):
        """ test get server side exclude """
        response = self.service.get_server_side_exclude()
        assert response is not None
        assert response.status_code == 200

    def test_30_update_server_side_exclude(self):
        """ test update server side exclude """
        response = self.service.update_server_side_exclude(
            value='on'
        )
        assert response is not None
        assert response.status_code == 200

    ################## Security Header ######################
    def test_31_get_security_header(self):
        """ test get security header """
        response = self.service.get_security_header()
        assert response is not None
        assert response.status_code == 200

    def test_32_update_security_header(self):
        """ test update security header """
        response = self.service.update_security_header()
        assert response is not None
        assert response.status_code == 200

    ################## Mobile Redirect ######################
    def test_33_get_mobile_redirect(self):
        """ test get mobile redirect """
        response = self.service.get_mobile_redirect()
        assert response is not None
        assert response.status_code == 200

    def test_34_update_mobile_redirect(self):
        """ test update mobile redirect """
        response = self.service.update_mobile_redirect()
        assert response is not None
        assert response.status_code == 200

    ################## Prefetch Preload ######################
    def test_35_get_prefetch_preload(self):
        """ test get prefetch preload """
        response = self.service.get_prefetch_preload()
        assert response is not None
        assert response.status_code == 200

    def test_36_update_prefetch_preload(self):
        """ test update prefetch preload """
        response = self.service.update_prefetch_preload(
            value='on'
        )
        assert response is not None
        assert response.status_code == 200

    ################## HTTP2 ######################
    def test_37_get_http2(self):
        """ test get http2 """
        response = self.service.get_http2()
        assert response is not None
        assert response.status_code == 200

    def test_38_update_http2(self):
        """ test update http2 """
        response = self.service.update_http2(
            value='on'
        )
        assert response is not None
        assert response.status_code == 200

    ################## HTTP3 ######################
    def test_39_get_http3(self):
        """ test get http3 """
        response = self.service.get_http3()
        assert response is not None
        assert response.status_code == 200

    def test_40_update_http3(self):
        """ test update http3 """
        response = self.service.update_http3(
            value='on'
        )
        assert response is not None
        assert response.status_code == 200

    ################## IPv6 ######################
    def test_41_get_ipv6(self):
        """ test get ipv6 """
        response = self.service.get_ipv6()
        assert response is not None
        assert response.status_code == 200

    def test_42_update_ipv6(self):
        """ test update ipv6 """
        response = self.service.update_ipv6(
            value='on'
        )
        assert response is not None
        assert response.status_code == 200

    ################## Web Sockets ######################
    def test_43_get_web_sockets(self):
        """ test get web sockets """
        response = self.service.get_web_sockets()
        assert response is not None
        assert response.status_code == 200

    def test_44_update_web_sockets(self):
        """ test update web sockets """
        response = self.service.update_web_sockets(
            value='on'
        )
        assert response is not None
        assert response.status_code == 200

    ################## Pseudo IPv4 ######################
    def test_45_get_pseudo_ipv4(self):
        """ test get pseudo ipv4 """
        response = self.service.get_pseudo_ipv4()
        assert response is not None
        assert response.status_code == 200

    def test_46_update_pseudo_ipv4(self):
        """ test update pseudo ipv4 """
        response = self.service.update_pseudo_ipv4(
            value='off'
        )
        assert response is not None
        assert response.status_code == 200

    ################## Response Buffering ######################
    def test_47_get_response_buffering(self):
        """ test get response buffering """
        response = self.service.get_response_buffering()
        assert response is not None
        assert response.status_code == 200

    def test_48_update_response_buffering(self):
        """ test update response buffering """
        response = self.service.update_response_buffering(
            value='on'
        )
        assert response is not None
        assert response.status_code == 200

    ################## Hotlink Protection ######################
    def test_49_get_hotlink_protection(self):
        """ test get hotlink protection """
        response = self.service.get_hotlink_protection()
        assert response is not None
        assert response.status_code == 200

    def test_50_update_hotlink_protection(self):
        """ test update hotlink protection """
        response = self.service.update_hotlink_protection(
            value='on'
        )
        assert response is not None
        assert response.status_code == 200

    ################## Max Upload ######################
    def test_51_get_max_upload(self):
        """ test get max upload """
        response = self.service.get_max_upload()
        assert response is not None
        assert response.status_code == 200

    def test_52_update_max_upload(self):
        """ test update max upload """
        response = self.service.update_max_upload(
            value=100
        )
        assert response is not None
        assert response.status_code == 200

    ################## TLS Client Auth ######################
    def test_53_get_tls_client_auth(self):
        """ test get tls client auth """
        response = self.service.get_tls_client_auth()
        assert response is not None
        assert response.status_code == 200

    def test_54_update_tls_client_auth(self):
        """ test update tls client auth """
        response = self.service.update_tls_client_auth(
            value='on'
        )
        assert response is not None
        assert response.status_code == 200

    ################## Brotli ######################
    def test_55_get_brotli(self):
        """ test get brotli """
        response = self.service.get_brotli()
        assert response is not None
        assert response.status_code == 200

    def test_56_update_brotli(self):
        """ test update brotli """
        response = self.service.update_brotli(
            value='on'
        )
        assert response is not None
        assert response.status_code == 200

    ################## Proxy Read Timeout ######################
    def test_57_get_proxy_read_timeout(self):
        """ test get proxy read timeout """
        response = self.service.get_proxy_read_timeout()
        assert response is not None
        assert response.status_code == 200

    def test_58_update_proxy_read_timeout(self):
        """ test update proxy read timeout """
        response = self.service.update_proxy_read_timeout(
            value=100
        )
        assert response is not None
        assert response.status_code == 200

    ################## Browser Check ######################
    def test_59_get_browser_check(self):
        """ test get browser check """
        response = self.service.get_browser_check()
        assert response is not None
        assert response.status_code == 200

    def test_60_update_browser_check(self):
        """ test update browser check """
        response = self.service.update_browser_check(
            value='on'
        )
        assert response is not None
        assert response.status_code == 200

    ################## Enable Error Pages On ######################
    def test_61_get_enable_error_pages_on(self):
        """ test get enable error pages on """
        response = self.service.get_enable_error_pages_on()
        assert response is not None
        assert response.status_code == 200

    def test_62_update_enable_error_pages_on(self):
        """ test update enable error pages on """
        response = self.service.update_enable_error_pages_on(
            value='on'
        )
        assert response is not None
        assert response.status_code == 200

    ################## Web Application Firewall ######################
    def test_63_get_web_application_firewall(self):
        """ test get web application firewall """
        response = self.service.get_web_application_firewall()
        assert response is not None
        assert response.status_code == 200

    def test_64_update_web_application_firewall(self):
        """ test update web application firewall """
        response = self.service.update_web_application_firewall(
            value='on'
        )
        assert response is not None
        assert response.status_code == 200

    ################## Ciphers ######################
    def test_65_get_ciphers(self):
        """ test get ciphers """
        response = self.service.get_ciphers()
        assert response is not None
        assert response.status_code == 200

    def test_66_update_ciphers(self):
        """ test update ciphers """
        response = self.service.update_ciphers()
        assert response is not None
        assert response.status_code == 200

    ################## Origin Max HTTP Version ######################
    def test_67_get_origin_max_http_version(self):
        """ test get origin max http version """
        response = self.service.get_origin_max_http_version()
        assert response is not None
        assert response.status_code == 200

    def test_68_update_origin_max_http_version(self):
        """ test update origin max http version """
        response = self.service.update_origin_max_http_version(
            value='2'
        )
        assert response is not None
        assert response.status_code == 200

    ################## Origin Post Quantum Encryption ######################
    def test_69_get_origin_post_quantum_encryption(self):
        """ test get origin post quantum encryption """
        response = self.service.get_origin_post_quantum_encryption()
        assert response is not None
        assert response.status_code == 200

    def test_70_update_origin_post_quantum_encryption(self):
        """ test update origin post quantum encryption """
        response = self.service.update_origin_post_quantum_encryption(
            value='preferred'
        )
        assert response is not None
        assert response.status_code == 200

    ################## Log Retention ######################
    def test_71_get_log_retention(self):
        """ test get log retention """
        response = self.service.get_log_retention(
            crn=self.crn,
            zone_identifier=self.zone_id
        )
        assert response is not None
        assert response.status_code == 200

    def test_72_update_log_retention(self):
        """ test update log retention """
        response = self.service.update_log_retention(
            crn=self.crn,
            zone_identifier=self.zone_id,
            flag=True
        )
        assert response is not None
        assert response.status_code == 200

    ################## Bot Management ######################
    def test_73_get_bot_management(self):
        """ test get bot management """
        response = self.service.get_bot_management()
        assert response is not None
        assert response.status_code == 200

    def test_74_update_bot_management(self):
        """ test update bot management """
        response = self.service.update_bot_management(
            session_score=True,
            enable_js=True,
            use_latest_model=True,
            ai_bots_protection='on'
        )
        assert response is not None
        assert response.status_code == 200

    ################## Replace Insecure JS ######################
    def test_75_get_replace_insecure_js(self):
        """ test get replace insecure js """
        response = self.service.get_replace_insecure_js()
        assert response is not None
        assert response.status_code == 200

    def test_76_update_replace_insecure_js(self):
        """ test update replace insecure js """
        response = self.service.update_replace_insecure_js(
            value='on'
        )
        assert response is not None
        assert response.status_code == 200

    ################## Email Obfuscation ######################
    def test_77_get_email_obfuscation(self):
        """ test get email obfuscation """
        response = self.service.get_email_obfuscation()
        assert response is not None
        assert response.status_code == 200

    def test_78_update_email_obfuscation(self):
        """ test update email obfuscation """
        response = self.service.update_email_obfuscation(
            value='on'
        )
        assert response is not None
        assert response.status_code == 200

    ################## Security Level ######################
    def test_79_get_security_level(self):
        """ test get security level """
        response = self.service.get_security_level()
        assert response is not None
        assert response.status_code == 200

    def test_80_update_security_level(self):
        """ test update security level """
        response = self.service.update_security_level(
            value='medium'
        )
        assert response is not None
        assert response.status_code == 200


if __name__ == '__main__':
    unittest.main()
