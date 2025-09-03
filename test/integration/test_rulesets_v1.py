# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2025.

"""
Integration test code for RulesetsV1
"""

import os
import unittest
from dotenv import load_dotenv, find_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_networking_services.rulesets_v1 import (
    RulesetsV1,
    RulesOverride,
    CategoriesOverride,
    Overrides,
    ActionParameters,
    Position,
    RuleCreate,
    Ratelimit
)

configFile = "cis.env"

# load the .env file containing your environment variables
try:
    load_dotenv(find_dotenv(filename="cis.env"))
except:
    print('warning: no cis.env file loaded')


class TestInstanceRulesetsIntegration(unittest.TestCase):
    """Instance Rulesets API integration test"""

    @classmethod
    def setUpClass(cls):
        if not os.path.exists(configFile):
            raise unittest.SkipTest("External configuration not available, skipping...")

        api_key = os.getenv("CIS_SERVICES_APIKEY")
        auth_url = os.getenv("CIS_SERVICES_AUTH_URL")
        crn = os.getenv("CRN")
        zone_id = os.getenv("ZONE_ID")
        service_url = os.getenv("API_ENDPOINT")

        if not all([api_key, crn, zone_id]):
            raise unittest.SkipTest("Environment variables not set properly")

        authenticator = IAMAuthenticator(api_key, url=auth_url)
        cls.rulesets_service = RulesetsV1(
            authenticator=authenticator,
            crn=crn,
            zone_identifier=zone_id
        )
        if service_url:
            cls.rulesets_service.set_service_url(service_url)

        cls.ruleset_to_deploy_id = None
        cls.rule1_id = None
        cls.rule2_id = None
        cls.ruleset_for_testing_id = None

        cls.rulesets_service.enable_retries(max_retries=4, retry_interval=30)

        try:
            cls.rulesets_service.get_instance_rulesets()
        except Exception as e:
            raise unittest.SkipTest(f"Authentication failed: {e}")

    def test_01_list_and_get_instance_ruleset(self):
        list_resp = self.rulesets_service.get_instance_rulesets().get_result()
        self.assertIn("result", list_resp)
        self.assertGreater(len(list_resp["result"]), 0)

        self.__class__.ruleset_to_deploy_id = list_resp["result"][0]["id"]

        get_resp = self.rulesets_service.get_instance_ruleset(
            ruleset_id=self.ruleset_to_deploy_id
        ).get_result()
        self.assertIn("result", get_resp)
        self.assertIn("rules", get_resp["result"])
        self.assertGreaterEqual(len(get_resp["result"]["rules"]), 2)

        self.__class__.rule1_id = get_resp["result"]["rules"][0]["id"]
        self.__class__.rule2_id = get_resp["result"]["rules"][1]["id"]

    def test_02_update_instance_entrypoint_ruleset(self):
        rule_override = RulesOverride(
            id=self.rule1_id,
            enabled=True,
            action="block",
            score_threshold=60
        )

        category_override = CategoriesOverride(
            category="wordpress",
            enabled=True,
            action="log"
        )

        overrides = Overrides(
            action="log",
            enabled=True,
            rules=[rule_override],
            categories=[category_override]
        )

        action_params = ActionParameters(
            id=self.ruleset_to_deploy_id,
            overrides=overrides
        )

        position = Position(index=1)

        rule_create = RuleCreate(
            action="execute",
            action_parameters=action_params,
            description="Overriding rule",
            enabled=True,
            expression='(ip.src ne 1.1.1.1) and cf.zone.plan eq "ENT"',
            ref=self.ruleset_to_deploy_id,
            position=position
        )

        update_resp = self.rulesets_service.update_instance_entrypoint_ruleset(
            ruleset_phase="http_request_firewall_managed",
            description="creating/updating entrypoint ruleset",
            rules=[rule_create]
        ).get_result()

        self.assertIn("result", update_resp)
        rules = update_resp["result"].get("rules", [])
        self.assertGreater(len(rules), 0)
        self.assertEqual(
            rules[0]["action_parameters"]["overrides"]["rules"][0]["score_threshold"], 60
        )

        self.__class__.ruleset_for_testing_id = update_resp["result"]["id"]

    def test_03_update_instance_ruleset(self):
        resp = self.rulesets_service.get_instance_entrypoint_ruleset(
            ruleset_phase="http_request_firewall_managed"
        ).get_result()
        ruleset2update_id = resp["result"]["id"]

        rule_override = RulesOverride(
            id=self.rule1_id,
            enabled=True,
            action="block"
        )

        category_override = CategoriesOverride(
            category="wordpress",
            enabled=True,
            action="block"
        )

        overrides = Overrides(
            action="block",
            enabled=True,
            rules=[rule_override],
            categories=[category_override]
        )

        action_params = ActionParameters(
            id=self.ruleset_to_deploy_id,
            overrides=overrides
        )

        position = Position(index=1)

        rule_create = RuleCreate(
            action="execute",
            action_parameters=action_params,
            description="update rules",
            enabled=True,
            expression='(ip.src ne 1.1.1.2) and cf.zone.plan eq "ENT"',
            ref=self.ruleset_to_deploy_id,
            position=position
        )

        update_resp = self.rulesets_service.update_instance_ruleset(
            ruleset_id=ruleset2update_id,
            description="updating Instance ruleset",
            rules=[rule_create]
        ).get_result()

        self.assertIn("result", update_resp)
        self.assertEqual(update_resp["result"]["id"], ruleset2update_id)
        self.assertGreater(len(update_resp["result"]["rules"]), 0)

    def test_04_get_instance_entrypoint_ruleset(self):
        resp = self.rulesets_service.get_instance_entrypoint_ruleset(
            ruleset_phase="http_request_firewall_managed"
        )
        self.assertEqual(resp.get_status_code(), 200)
        result = resp.get_result()
        self.assertIsNotNone(result)
        self.assertIn("result", result)

    def test_05_list_and_get_instance_entrypoint_ruleset_version(self):
        list_resp = self.rulesets_service.get_instance_entry_point_ruleset_versions(
            ruleset_phase="http_request_firewall_managed"
        )
        self.assertEqual(list_resp.get_status_code(), 200)
        list_result = list_resp.get_result()
        self.assertIsNotNone(list_result)
        self.assertIn("result", list_result)
        self.assertGreater(len(list_result["result"]), 1, "Need at least two versions for test")

        version = list_result["result"][1]["version"]

        get_version_resp = self.rulesets_service.get_instance_entry_point_ruleset_version(
            ruleset_phase="http_request_firewall_managed",
            ruleset_version=version
        )
        self.assertEqual(get_version_resp.get_status_code(), 200)
        version_result = get_version_resp.get_result()
        self.assertIsNotNone(version_result)
        self.assertIn("result", version_result)

    def test_06_list_get_delete_instance_ruleset_version(self):
        ruleset_id = self.ruleset_for_testing_id
        self.assertIsNotNone(ruleset_id, "ruleset_for_testing_id is None, cannot test versions")

        list_resp = self.rulesets_service.get_instance_ruleset_versions(
            ruleset_id=ruleset_id
        ).get_result()

        self.assertIsNotNone(list_resp)
        self.assertIn("result", list_resp)
        self.assertGreater(len(list_resp["result"]), 1, "Need at least two versions to test deletion")

        versions_sorted = sorted(list_resp["result"], key=lambda v: v["version"])
        latest_version = versions_sorted[-1]["version"]
        version_to_delete = None
        for v in reversed(versions_sorted[:-1]):
            if v["version"] != latest_version:
                version_to_delete = v["version"]
                break

        self.assertIsNotNone(version_to_delete, "No deletable version found")

        get_resp = self.rulesets_service.get_instance_ruleset_version(
            ruleset_id=ruleset_id,
            ruleset_version=version_to_delete
        ).get_result()
        self.assertIsNotNone(get_resp)

        delete_resp = self.rulesets_service.delete_instance_ruleset_version(
            ruleset_id=ruleset_id,
            ruleset_version=version_to_delete
        )
        self.assertEqual(delete_resp.get_status_code(), 204)

    def test_07_create_instance_ruleset_rule(self):

        resp = self.rulesets_service.get_instance_entrypoint_ruleset(
            ruleset_phase="http_request_firewall_managed"
        ).get_result()
        ruleset2update_id = resp["result"]["id"]

        rule_override = RulesOverride(
            id=self.rule2_id,
            enabled=True,
            action="log"
        )

        category_override = CategoriesOverride(
            category="wordpress",
            enabled=True,
            action="log"
        )

        overrides = Overrides(
            enabled=False,
            rules=[rule_override],
            categories=[category_override]
        )

        action_params = ActionParameters(
            id=self.ruleset_to_deploy_id,
            overrides=overrides
        )

        position = Position(index=1)

        create_resp = self.rulesets_service.create_instance_ruleset_rule(
            ruleset_id=ruleset2update_id,
            action="execute",
            action_parameters=action_params,
            description="adding a rule to execute managed rules",
            enabled=True,
            expression='(ip.src ne 1.1.1.1) and cf.zone.plan eq "ENT"',
            ref=ruleset2update_id,
            position=position
        ).get_result()

        self.assertIsNotNone(create_resp)
        self.assertIn("id", create_resp["result"])

    def test_08_create_instance_ruleset_rule_new(self):
        from ibm_cloud_networking_services.rulesets_v1 import (
            RulesOverride, CategoriesOverride, Overrides,
            ActionParameters, Position
        )

        resp = self.rulesets_service.get_instance_entrypoint_ruleset(
            ruleset_phase="http_request_firewall_managed"
        ).get_result()
        ruleset2update_id = resp["result"]["id"]

        rule_override = RulesOverride(
            id=self.rule2_id,
            enabled=True,
            action="log"
        )

        category_override = CategoriesOverride(
            category="wordpress",
            enabled=True,
            action="log"
        )

        overrides = Overrides(
            enabled=False,
            rules=[rule_override],
            categories=[category_override]
        )

        action_params = ActionParameters(
            id=self.ruleset_to_deploy_id,
            overrides=overrides
        )

        position = Position(index=1)

        create_resp = self.rulesets_service.create_instance_ruleset_rule(
            ruleset_id=ruleset2update_id,
            action="execute",
            action_parameters=action_params,
            description="adding a rule to execute managed rules",
            enabled=True,
            expression='(ip.src ne 1.1.1.1) and cf.zone.plan eq "ENT"',
            position=position
        )

        self.assertIsNotNone(create_resp)
        self.assertIn("id", create_resp.get_result()["result"])

    def test_09_update_delete_instance_ruleset_rule(self):
        from ibm_cloud_networking_services.rulesets_v1 import (
            RulesOverride, CategoriesOverride, Overrides,
            ActionParameters
        )

        resp = self.rulesets_service.get_instance_entrypoint_ruleset(
            ruleset_phase="http_request_firewall_managed"
        ).get_result()
        ruleset2update_id = resp["result"]["id"]
        rule2update_id = resp["result"]["rules"][0]["id"]

        rule_override = RulesOverride(
            id=self.rule2_id,
            enabled=True,
            action="block"
        )

        category_override = CategoriesOverride(
            category="wordpress",
            enabled=True,
            action="block"
        )

        overrides = Overrides(
            action="block",
            enabled=True,
            rules=[rule_override],
            categories=[category_override]
        )

        action_params = ActionParameters(
            id=self.ruleset_to_deploy_id,
            overrides=overrides
        )

        update_resp = self.rulesets_service.update_instance_ruleset_rule(
            ruleset_id=ruleset2update_id,
            rule_id=rule2update_id,
            action="execute",
            action_parameters=action_params,
            description="editting rule",
            enabled=True,
            expression='(ip.src ne 1.1.1.3) and cf.zone.plan eq "ENT"'
        )

        self.assertEqual(update_resp.get_status_code(), 200)
        update_result = update_resp.get_result()
        self.assertIsNotNone(update_result)

        delete_resp = self.rulesets_service.delete_instance_ruleset_rule(
            ruleset_id=ruleset2update_id,
            rule_id=rule2update_id
        )
        self.assertEqual(delete_resp.get_status_code(), 200)
        delete_result = delete_resp.get_result()
        self.assertIsNotNone(delete_result)

    def test_10_delete_instance_ruleset(self):
        ruleset_id = self.ruleset_for_testing_id
        self.assertIsNotNone(ruleset_id, "ruleset_for_testing_id is None, cannot delete")

        response = self.rulesets_service.delete_instance_ruleset(
            ruleset_id=ruleset_id
        )

        self.assertEqual(response.get_status_code(), 204)

    def test_11_get_instance_ruleset_version_by_tag(self):
        ruleset_id = self.ruleset_to_deploy_id
        self.assertIsNotNone(ruleset_id, "ruleset_to_deploy_id is None, cannot get version by tag")

        rule_tag = "wordpress"

        versions_resp = self.rulesets_service.get_instance_ruleset_versions(
            ruleset_id=ruleset_id
        ).get_result()

        versions = [v["version"] for v in versions_resp["result"]]
        self.assertTrue(len(versions) > 0, "No versions found for ruleset")

        ruleset_version = str(max(versions))

        resp = self.rulesets_service.get_instance_ruleset_version_by_tag(
            ruleset_id=ruleset_id,
            ruleset_version=ruleset_version,
            rule_tag=rule_tag
        )

        self.assertEqual(resp.get_status_code(), 200)
        result = resp.get_result()
        self.assertIsNotNone(result)

    @classmethod
    def tearDownClass(cls):
        if getattr(cls, "instance_ruleset_for_testing_id", None):
            try:
                resp = cls.rulesets_service.delete_instance_ruleset(cls.instance_ruleset_for_testing_id)
                logger.info(f"Deleted instance ruleset {cls.instance_ruleset_for_testing_id}, status: {resp.get_status_code()}")
            except Exception as e:
                logger.warning(f"Failed to delete instance ruleset: {e}")
            cls.instance_ruleset_for_testing_id = None

        if getattr(cls, "zone_ruleset_for_testing_id", None):
            try:
                resp = cls.rulesets_service.delete_zone_ruleset(cls.zone_ruleset_for_testing_id)
                logger.info(f"Deleted zone ruleset {cls.zone_ruleset_for_testing_id}, status: {resp.get_status_code()}")
            except Exception as e:
                logger.warning(f"Failed to delete zone ruleset: {e}")
            cls.zone_ruleset_for_testing_id = None


class TestZoneRulesets(unittest.TestCase):
    """Zone Rulesets API integration test"""

    @classmethod
    def setUpClass(cls):
        cls.zone_ruleset_to_deploy = None
        cls.zone_ruleset_to_deploy2 = None
        cls.rule1_id = None
        cls.rule2_id = None
        cls.ruleset_for_testing_id = None
        cls.ruleset_ep_ratelimit_testing_id = None

        api_key = os.getenv("CIS_SERVICES_APIKEY")
        auth_url = os.getenv("CIS_SERVICES_AUTH_URL")
        crn = os.getenv("CRN")
        zone_id = os.getenv("ZONE_ID")
        service_url = os.getenv("API_ENDPOINT")

        if not all([api_key, crn, zone_id]):
            raise unittest.SkipTest("Environment variables not set properly")

        authenticator = IAMAuthenticator(api_key, url=auth_url)
        cls.rulesets_service = RulesetsV1(
            authenticator=authenticator,
            crn=crn,
            zone_identifier=zone_id
        )
        if service_url:
            cls.rulesets_service.set_service_url(service_url)

        cls.rulesets_service.enable_retries(max_retries=4, retry_interval=30)

        
        response = cls.rulesets_service.get_zone_rulesets()
        rulesets = response.get_result()['result']

        for ruleset in rulesets:
            if "CIS Managed Ruleset" in ruleset['name']:
                cls.zone_ruleset_to_deploy = ruleset['id']
            if "CIS Managed Free Ruleset" in ruleset['name']:
                cls.zone_ruleset_to_deploy2 = ruleset['id']

        
        response = cls.rulesets_service.get_zone_ruleset(cls.zone_ruleset_to_deploy)
        rules = response.get_result().get('result', {}).get('rules', [])
        cls.rule1_id = rules[0]['id']
        cls.rule2_id = rules[2]['id']

        
        response = cls.rulesets_service.update_zone_entrypoint_ruleset(
            ruleset_phase="http_request_firewall_managed",
            description="temporary entrypoint ruleset for test"
        )
        cls.ruleset_for_testing_id = response.get_result()['result']['id']

    def test_list_get_zone_rulesets(self):
        response = self.rulesets_service.get_zone_rulesets()
        self.assertEqual(response.get_status_code(), 200)
        rulesets = response.get_result()['result']

        for ruleset in rulesets:
            if "CIS Managed Ruleset" in ruleset['name']:
                self.__class__.zone_ruleset_to_deploy = ruleset['id']
            if "CIS Managed Free Ruleset" in ruleset['name']:
                self.__class__.zone_ruleset_to_deploy2 = ruleset['id']

        
        response = self.rulesets_service.get_zone_ruleset(self.zone_ruleset_to_deploy)
        self.assertEqual(response.get_status_code(), 200)
        rules = response.get_result().get('result', {}).get('rules', [])
        self.__class__.rule1_id = rules[0]['id']
        self.__class__.rule2_id = rules[2]['id']

    def test_update_zone_entrypoint_ruleset(self):
        overrides = {
            "action": "log",
            "enabled": True,
            "rules": [{
                "id": self.rule1_id,
                "enabled": True,
                "action": "log",
                "score_threshold": 60
            }],
            "categories": [{
                "category": "wordpress",
                "enabled": True,
                "action": "log"
            }]
        }

        action_params = {"id": self.zone_ruleset_to_deploy, "overrides": overrides}

        rule_create = {
            "action": "execute",
            "action_parameters": action_params,
            "description": "overriding entrypoint ruleset rule",
            "enabled": True,
            "expression": "ip.src ne 1.1.1.1",
            "position": {"index": 1}
        }

        response = self.rulesets_service.update_zone_entrypoint_ruleset(
            ruleset_phase="http_request_firewall_managed",
            description="updating entrypoint ruleset",
            rules=[rule_create]
        )
        self.assertEqual(response.get_status_code(), 200)
        self.__class__.ruleset_for_testing_id = response.get_result()['result']['id']

    def test_update_zone_entrypoint_ruleset_ratelimit(self):
        
        response = self.rulesets_service.update_zone_entrypoint_ruleset(
            ruleset_phase="http_ratelimit",
            description="updating entrypoint ruleset for ratelimit"
        )

        self.assertEqual(response.get_status_code(), 200)
        self.__class__.ruleset_ep_ratelimit_testing_id = response.get_result()['result']['id']

    def test_update_zone_ruleset(self):
        rules_override = [{
            "id": self.rule1_id,
            "enabled": True,
            "action": "block"
        }]
    
        categories_override = [{
            "category": "wordpress",
            "enabled": True,
            "action": "block"
        }]
    
        overrides = {
            "action": "block",
            "enabled": True,
            "rules": rules_override,
            "categories": categories_override
        }
    
        action_params = {
            "id": self.zone_ruleset_to_deploy,
            "overrides": overrides
        }
    
        rule_create = {
            "action": "execute",
            "action_parameters": action_params,
            "description": "deploying a managed rule",
            "enabled": True,
            "expression": "ip.src ne 1.1.1.2",
            "ref": self.ruleset_for_testing_id,
            "position": {"index": 1}
        }
    
        response = self.rulesets_service.update_zone_ruleset(
            ruleset_id=self.ruleset_for_testing_id,
            description="Updating a zone ruleset",
            rules=[rule_create]
        )
    
        self.assertEqual(response.get_status_code(), 200)

    def test_get_zone_entrypoint_ruleset(self):
        from ibm_cloud_sdk_core import ApiException

        try:
            response = self.rulesets_service.get_zone_entrypoint_ruleset(
                ruleset_phase="http_request_firewall_managed"
            )
        except ApiException as e:
            if e.status_code == 404:
                
                resp = self.rulesets_service.update_zone_entrypoint_ruleset(
                    ruleset_phase="http_request_firewall_managed",
                    description="temporary entrypoint ruleset for test"
                )
                self.__class__.ruleset_for_testing_id = resp.get_result()['result']['id']
                
                response = self.rulesets_service.get_zone_entrypoint_ruleset(
                    ruleset_phase="http_request_firewall_managed"
                )
            else:
                raise
        self.assertEqual(response.get_status_code(), 200)
        self.assertIsNotNone(response.get_result())

    def test_list_get_zone_entrypoint_ruleset_versions(self):
        list_resp = self.rulesets_service.get_zone_entry_point_ruleset_versions(
            ruleset_phase="http_request_firewall_managed"
        )
        self.assertEqual(list_resp.get_status_code(), 200)
        results = list_resp.get_result().get('result', [])
        self.assertGreater(len(results), 0)

        
        if len(results) > 1:
            version = results[1]['version']
        else:
            version = results[0]['version']

        get_version_resp = self.rulesets_service.get_zone_entry_point_ruleset_version(
            ruleset_phase="http_request_firewall_managed",
            ruleset_version=version
        )
        self.assertEqual(get_version_resp.get_status_code(), 200)
        self.assertIsNotNone(get_version_resp.get_result())

    def test_list_get_delete_zone_ruleset_version(self):
        
        list_resp = self.rulesets_service.get_zone_ruleset_versions(
            ruleset_id=self.ruleset_for_testing_id
        )
        self.assertEqual(list_resp.get_status_code(), 200)
        versions = list_resp.get_result().get('result', [])
        self.assertGreater(len(versions), 0)

        
        if len(versions) > 1:
            version_to_delete = versions[0]['version'] 
        else:
            version_to_delete = None  

        if version_to_delete:
            
            get_resp = self.rulesets_service.get_zone_ruleset_version(
                ruleset_id=self.ruleset_for_testing_id,
                ruleset_version=version_to_delete
            )
            self.assertEqual(get_resp.get_status_code(), 200)
            self.assertIsNotNone(get_resp.get_result())

            
            delete_resp = self.rulesets_service.delete_zone_ruleset_version(
                ruleset_id=self.ruleset_for_testing_id,
                ruleset_version=version_to_delete
            )
            self.assertEqual(delete_resp.get_status_code(), 204)
        else:
            print("No older ruleset version to delete; skipping deletion.")

    def test_create_zone_ruleset_rule_execute(self):
        
        self.assertIsNotNone(self.ruleset_for_testing_id, "ruleset_for_testing_id is not set")
        self.assertIsNotNone(self.zone_ruleset_to_deploy2, "zone_ruleset_to_deploy2 is not set")

        
        response = self.rulesets_service.get_zone_ruleset(self.ruleset_for_testing_id)
        rules = response.get_result().get('result', {}).get('rules', [])
        
        rule_id_to_use = rules[0]['id'] if rules else None

        
        rules_override = RulesOverride(
            id=rule_id_to_use,
            enabled=True,
            action="log"
        )

        categories_override = CategoriesOverride(
            category="wordpress",
            enabled=True,
            action="log"
        )

        overrides = Overrides(
            action="log",
            enabled=True,
            rules=[rules_override] if rule_id_to_use else [],
            categories=[categories_override]
        )

        action_params = ActionParameters(
            id=self.zone_ruleset_to_deploy2,
            overrides=overrides
        )

        position = Position(index=1)

        
        response = self.rulesets_service.create_zone_ruleset_rule(
            ruleset_id=self.ruleset_for_testing_id,
            action="execute",
            action_parameters=action_params,
            description="deploying managed rule",
            enabled=True,
            expression="ip.src ne 1.1.1.3",
            ref=self.ruleset_for_testing_id,
            position=position
        )

        self.assertIsNotNone(response.get_result())

    def test_create_zone_ruleset_rule_skip(self):
        
        response = self.rulesets_service.get_zone_entrypoint_ruleset(
            ruleset_phase="http_request_firewall_custom"
        )
        self.assertEqual(response.get_status_code(), 200)
        custom_ruleset_id = response.get_result()['result']['id']
        self.assertIsNotNone(custom_ruleset_id, "Custom ruleset ID is None")

        
        action_parameters = ActionParameters(
            phases=["http_ratelimit", "http_request_firewall_managed"],
            products=["waf"]
        )

        
        rule_response = self.rulesets_service.create_zone_ruleset_rule(
            ruleset_id=custom_ruleset_id,
            action="skip",
            action_parameters=action_parameters,
            description="deploying custom rule",
            enabled=True,
            expression="ip.src ne 1.1.1.3",
            ref=self.ruleset_for_testing_id  
        )

        self.assertEqual(rule_response.get_status_code(), 200)
        self.assertIsNotNone(rule_response.get_result())

    def test_update_delete_zone_ruleset_rule_skip(self):
        
        response = self.rulesets_service.get_zone_entrypoint_ruleset(
            ruleset_phase="http_request_firewall_custom"
        )
        self.assertEqual(response.get_status_code(), 200)
        ruleset_result = response.get_result()['result']
        self.assertIsNotNone(ruleset_result, "Ruleset result is None")

        
        rules = ruleset_result.get('rules', [])
        self.assertGreater(len(rules), 0, "No rules found in the ruleset")
        last_rule = rules[-1]
        custom_rule_id = last_rule['id']
        custom_ruleset_id = ruleset_result['id']

        
        action_parameters = ActionParameters(
            phases=["http_ratelimit", "http_request_firewall_managed"],
            products=["waf"]
        )

        
        update_response = self.rulesets_service.update_zone_ruleset_rule(
            ruleset_id=custom_ruleset_id,
            rule_id=custom_rule_id,
            action="skip",
            action_parameters=action_parameters,
            description="Updating the rule with correct IDs",
            enabled=True,
            expression="ip.src ne 1.1.1.4"
        )
        self.assertEqual(update_response.get_status_code(), 200)

        
        delete_response = self.rulesets_service.delete_zone_ruleset_rule(
            ruleset_id=custom_ruleset_id,
            rule_id=custom_rule_id
        )
        self.assertEqual(delete_response.get_status_code(), 200)


    def test_create_zone_ruleset_rule_http_ratelimit(self):
        
        response = self.rulesets_service.get_zone_entrypoint_ruleset(
            ruleset_phase="http_ratelimit"
        )
        self.assertEqual(response.get_status_code(), 200)

        
        rulesetEPRatelimitTestingId = response.get_result()['result']['id']
        self.assertIsNotNone(rulesetEPRatelimitTestingId, "Ratelimit ruleset ID not found")

        
        ratelimit = Ratelimit(
            characteristics=["cf.colo.id", "ip.src"],
            counting_expression='(http.host eq "www.example.com") and (http.response.code eq 404)',
            mitigation_timeout=600,
            period=60,
            requests_per_period=100
        )

        
        create_rule_options = {
            "ruleset_id": rulesetEPRatelimitTestingId,
            "action": "block",
            "description": "deploying managed rule",
            "enabled": True,
            "expression": "ip.src ne 1.1.1.3",
            "ref": rulesetEPRatelimitTestingId,
            "ratelimit": ratelimit
        }

        detailed_response = self.rulesets_service.create_zone_ruleset_rule(**create_rule_options)

        
        self.assertEqual(detailed_response.get_status_code(), 200)
        self.assertIsNotNone(detailed_response.get_result())

    def test_update_delete_zone_ruleset_rule_http_ratelimit(self):
        
        detailed_response = self.rulesets_service.get_zone_entrypoint_ruleset(
        ruleset_phase="http_ratelimit"
        )
        self.assertEqual(detailed_response.get_status_code(), 200)

        ruleset_result = detailed_response.get_result()['result']
        self.assertIsNotNone(ruleset_result, "Ruleset result is None")

       
        rules = ruleset_result.get('rules', [])
        self.assertGreater(len(rules), 0, "No rules found in the ruleset")
        rule_id = rules[0]['id']
        ruleset_id = ruleset_result['id']

        
        ratelimit = Ratelimit(
            characteristics=["cf.colo.id", "ip.src"],
            counting_expression='(http.host eq "www.example.com") and (http.response.code eq 404)',
            mitigation_timeout=30,
            period=10,
            requests_per_period=5
        )

        
        update_options = {
            "ruleset_id": ruleset_id,
            "rule_id": rule_id,
            "action": "block",
            "description": "updating the rule",
            "enabled": True,
            "expression": "ip.src ne 1.1.1.4",
            "ref": ruleset_id,
            "ratelimit": ratelimit
        }

        update_response = self.rulesets_service.update_zone_ruleset_rule(**update_options)
        self.assertEqual(update_response.get_status_code(), 200)
        self.assertIsNotNone(update_response.get_result())

        
        delete_options = {
            "ruleset_id": ruleset_id,
            "rule_id": rule_id
        }

        delete_response = self.rulesets_service.delete_zone_ruleset_rule(**delete_options)
        self.assertEqual(delete_response.get_status_code(), 200)
        self.assertIsNotNone(delete_response.get_result())


    def test_delete_zone_ruleset(self):
        if not self.ruleset_for_testing_id:
        
            resp = self.rulesets_service.update_zone_entrypoint_ruleset(
                ruleset_phase="http_request_firewall_managed",
                description="temporary ruleset for delete test"
            )
            self.__class__.ruleset_for_testing_id = resp.get_result()['result']['id']

        response = self.rulesets_service.delete_zone_ruleset(self.ruleset_for_testing_id)
        self.assertEqual(response.get_status_code(), 204)
        self.__class__.ruleset_for_testing_id = None