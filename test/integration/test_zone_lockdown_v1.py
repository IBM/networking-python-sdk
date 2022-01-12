# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.

"""
Integration test code for zone firewall lockdown service
"""

import os
import unittest
from dotenv import load_dotenv, find_dotenv
from ibm_cloud_networking_services.zone_lockdown_v1 import ZoneLockdownV1

configFile = "cis.env"

# load the .env file containing your environment variables
try:
    load_dotenv(find_dotenv(filename="cis.env"))
except:
    print('warning: no cis.env file loaded')


class TestZoneLockdownV1(unittest.TestCase):
    """ Zone Lockdown test class """

    def setUp(self):
        if not os.path.exists(configFile):
            raise unittest.SkipTest(
                'External configuration not available, skipping...')

        self.crn = os.getenv("CRN")
        self.zone_id = os.getenv("ZONE_ID")
        self.endpoint = os.getenv("API_ENDPOINT")
        self.lockdown = ZoneLockdownV1.new_instance(
            crn=self.crn, zone_identifier=self.zone_id, service_name="cis_services")
        self.lockdown.set_service_url(self.endpoint)
        self._clean_lockdown_rules()

    def tearDown(self):
        """ tear down """
        # Delete the resources
        print("Clean up complete")

    def _clean_lockdown_rules(self):
        # list all zone firewall lockdown
        resp = self.lockdown.list_all_zone_lockown_rules()
        assert resp is not None
        assert resp.status_code == 200

        for rule_id in resp.get_result().get("result"):
            print("rule id :", rule_id.get("id"))
            # delete zone firewall lockdown rule
            resp = self.lockdown.delete_zone_lockdown_rule(
                lockdown_rule_identifier=rule_id.get("id"))

    def test_zone_lockdown_rule_url_action(self):
        url = ["api.mysite.com/some/endpoint*"]
        config = [{
            "target": "ip",
            "value": "198.51.100.4"
        }]
        pause = True

        # create zone lockdown rule
        resp = self.lockdown.create_zone_lockdown_rule(
            urls=url, configurations=config, paused=pause)
        assert resp is not None
        assert resp.status_code == 200
        assert url[0] in resp.get_result().get("result").get("urls")
        id = resp.get_result().get("result")["id"]

        # get zone firewall lockdown rule
        resp = self.lockdown.get_lockdown(lockdown_rule_identifier=id)
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("result")["id"] == id

        # update zone lockdown rule
        url = ["api.oursite.com/some/endpoint*",
               "api.mysite.com/some/endpoint*"]
        resp = self.lockdown.update_lockdown_rule(
            lockdown_rule_identifier=id, urls=url, configurations=config)
        assert resp is not None
        assert resp.status_code == 200
        assert url[0] in resp.get_result().get("result").get("urls")

        # delete zone firewall lockdown rule
        resp = self.lockdown.delete_zone_lockdown_rule(
            lockdown_rule_identifier=id)
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("result")["id"] == id

    def test_zone_lockdown_rule_pause_action(self):
        url = ["api.mysite.com/some/endpoint*"]
        config = [{
            "target": "ip",
            "value": "198.51.100.4"
        }]
        pause = True

        # create zone lockdown rule
        resp = self.lockdown.create_zone_lockdown_rule(
            urls=url, configurations=config, paused=pause)
        assert resp is not None
        assert resp.status_code == 200
        assert url[0] in resp.get_result().get("result").get("urls")
        assert resp.get_result().get("result").get("paused") == pause

        id = resp.get_result().get("result")["id"]

        # get zone firewall lockdown rule
        resp = self.lockdown.get_lockdown(lockdown_rule_identifier=id)
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("result")["id"] == id

        # update zone lockdown rule
        pause = False
        resp = self.lockdown.update_lockdown_rule(
            lockdown_rule_identifier=id, urls=url, paused=pause, configurations=config)
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("result").get("paused") == pause

        # delete zone firewall lockdown rule
        resp = self.lockdown.delete_zone_lockdown_rule(
            lockdown_rule_identifier=id)
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("result")["id"] == id

    def test_zone_lockdown_rule_ip_action(self):
        url = ["api.mysite.com/some/endpoint*"]
        config = [{
            "target": "ip",
            "value": "198.51.100.4"
        }]
        pause = True

        # create zone lockdown rule
        resp = self.lockdown.create_zone_lockdown_rule(
            urls=url, configurations=config, paused=pause)
        assert resp is not None
        assert resp.status_code == 200
        assert url[0] in resp.get_result().get("result").get("urls")
        assert config[0] in resp.get_result().get(
            "result").get("configurations")

        id = resp.get_result().get("result")["id"]

        # get zone firewall lockdown rule
        resp = self.lockdown.get_lockdown(lockdown_rule_identifier=id)
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("result")["id"] == id

        # update zone lockdown rule
        config = [
            {
                "target": "ip",
                "value": "198.51.100.4"
            },
            {
                "target": "ip",
                "value": "198.51.10.4"
            }
        ]

        resp = self.lockdown.update_lockdown_rule(
            lockdown_rule_identifier=id, urls=url, paused=pause, configurations=config)
        assert resp is not None
        assert resp.status_code == 200
        assert config[1] in resp.get_result().get(
            "result").get("configurations")

        # delete zone firewall lockdown rule
        resp = self.lockdown.delete_zone_lockdown_rule(
            lockdown_rule_identifier=id)
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("result")["id"] == id

    def test_zone_lockdown_rule_ip_range_action(self):
        url = ["api.mysite.com/some/endpoint*"]
        config = [{
            "target": "ip_range",
            "value": "198.51.100.0/24"
        }]
        pause = True

        # create zone lockdown rule
        resp = self.lockdown.create_zone_lockdown_rule(
            urls=url, configurations=config, paused=pause)
        assert resp is not None
        assert resp.status_code == 200
        assert url[0] in resp.get_result().get("result").get("urls")
        assert config[0] in resp.get_result().get(
            "result").get("configurations")

        id = resp.get_result().get("result")["id"]

        # get zone firewall lockdown rule
        resp = self.lockdown.get_lockdown(lockdown_rule_identifier=id)
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("result")["id"] == id

        # update zone lockdown rule
        config = [
            {
                "target": "ip_range",
                "value": "198.51.100.4/24"
            },
            {
                "target": "ip_range",
                "value": "198.51.10.4/24"
            }
        ]

        resp = self.lockdown.update_lockdown_rule(
            lockdown_rule_identifier=id, urls=url, paused=pause, configurations=config)
        assert resp is not None
        assert resp.status_code == 200
        assert config[1] in resp.get_result().get(
            "result").get("configurations")

        # delete zone firewall lockdown rule
        resp = self.lockdown.delete_zone_lockdown_rule(
            lockdown_rule_identifier=id)
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("result")["id"] == id

    def test_zone_lockdown_rule_list(self):
        url = ["api.mysite.com/some/endpoint*"]
        config = [{
            "target": "ip",
            "value": "198.51.100.4"
        }]
        pause = True

        # create zone lockdown rule
        resp = self.lockdown.create_zone_lockdown_rule(
            urls=url, configurations=config, paused=pause)
        assert resp is not None
        assert resp.status_code == 200
        assert url[0] in resp.get_result().get("result").get("urls")

        url = ["api.oursite.com/some/endpoint*"]
        config = [{
            "target": "ip",
            "value": "198.51.10.4"
        }]

        # create zone lockdown rule
        resp = self.lockdown.create_zone_lockdown_rule(
            urls=url, configurations=config, paused=pause)
        assert resp is not None
        assert resp.status_code == 200
        assert url[0] in resp.get_result().get("result").get("urls")

        # list all zone firewall lockdown
        resp = self.lockdown.list_all_zone_lockown_rules()
        assert resp is not None
        assert resp.status_code == 200

        for rule_id in resp.get_result().get("result"):
            print("rule id :", rule_id.get("id"))
            # delete zone firewall lockdown rule
            resp = self.lockdown.delete_zone_lockdown_rule(
                lockdown_rule_identifier=rule_id.get("id"))
            assert resp is not None
            assert resp.status_code == 200
            assert resp.get_result().get("result")["id"] == rule_id.get("id")


if __name__ == '__main__':
    unittest.main()
