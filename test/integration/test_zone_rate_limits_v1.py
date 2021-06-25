# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.

"""
Integration test code for Rate Limit Service
"""

import os
import unittest
from dotenv import load_dotenv, find_dotenv
from ibm_cloud_networking_services.zone_rate_limits_v1 import ZoneRateLimitsV1

configFile = "cis.env"

# load the .env file containing your environment variables
try:
    load_dotenv(find_dotenv(filename="cis.env"))
except:
    print('warning: no cis.env file loaded')


class TestRateLimitsApiV1(unittest.TestCase):
    """ Rate Limits API test class """

    @unittest.skip("skipping")

    def setUp(self):
        if not os.path.exists(configFile):
            raise unittest.SkipTest(
                'External configuration not available, skipping...')

        self.crn = os.getenv("CRN")
        self.zone_id = os.getenv("ZONE_ID")
        self.endpoint = os.getenv("API_ENDPOINT")
        self.rate_limit = ZoneRateLimitsV1.new_instance(
            crn=self.crn, zone_identifier=self.zone_id, service_name="cis_services")
        self.rate_limit.set_service_url(self.endpoint)
        self._clean_up_page_rules()

    def tearDown(self):
        """ tear down """
        # Delete the resources
        print("Clean up complete")

    def _clean_up_page_rules(self):
        resp = self.rate_limit.list_all_zone_rate_limits()
        assert resp is not None
        assert resp.status_code == 200
        if resp.get_result().get('result') is not None:
            ids = resp.get_result().get('result')
            for id in ids:
                self.rate_limit.delete_zone_rate_limit(
                    rate_limit_identifier=id.get("id"))

    def test_1_rate_limit_mode_simulate_ban(self):
        modes = ["simulate", "ban"]
        i = 0
        for mode in modes:
            print("Test with mode: ", mode)
            threshold = 40
            period = 2
            url = "*.example.org/path*"
            action = {
                "mode": mode,
                "timeout": 60,
                "response": {
                    "content_type": "text/plain",
                    "body": "This request has been rate-limited."
                }
            }
            correlate = {
                "by": "nat"
            }
            match = {
                "request": {
                    "methods": [
                        "_ALL_"
                    ],
                    "schemes": [
                        "_ALL_"
                    ],
                    "url": url
                }
            }

            bypass = [
                {
                    "name": "url",
                    "value": "api.example.com/*"
                }
            ]

            # create rate limits
            resp = self.rate_limit.create_zone_rate_limits(
                threshold=threshold, period=period, action=action, match=match, bypass=bypass, correlate=correlate)
            assert resp is not None
            assert resp.status_code == 200
            print("rate limit id : ", resp.get_result().get("result")["id"])
            id = resp.get_result().get("result")["id"]
            url = "ibm.example.com/*"
            match = {
                "request": {
                    "methods": [
                        "_ALL_"
                    ],
                    "schemes": [
                        "_ALL_"
                    ],
                    "url": url
                }
            }
            i = i + 1
            mode_update = modes[i % len(modes)]
            action = {
                "mode": mode_update,
                "timeout": 60,
                "response": {
                    "content_type": "text/plain",
                    "body": "This request has been rate-limited."
                }
            }

            print("updating mode to", mode_update)
            # update rate limits
            resp = self.rate_limit.update_rate_limit(
                rate_limit_identifier=id, threshold=threshold, period=period, action=action, match=match, bypass=bypass, correlate=correlate)
            assert resp is not None
            assert resp.status_code == 200
            assert resp.get_result().get("result").get(
                "match").get("request").get("url") == url
            assert resp.get_result().get("result").get("action").get("mode") == mode_update

            # get rate limits
            resp = self.rate_limit.get_rate_limit(
                rate_limit_identifier=id)
            assert resp is not None
            assert resp.status_code == 200

            # delete rate limits
            resp = self.rate_limit.delete_zone_rate_limit(
                rate_limit_identifier=id)
            assert resp is not None
            assert resp.status_code == 200

    def test_1_rate_limit_mode_challenge(self):
        modes = ["challenge", "js_challenge"]
        i = 0
        for mode in modes:
            print("Test with mode: ", mode)
            threshold = 40
            period = 2
            url = "*.example.org/path*"
            action = {
                "mode": mode,
            }
            correlate = {
                "by": "nat"
            }
            match = {
                "request": {
                    "methods": [
                        "_ALL_"
                    ],
                    "schemes": [
                        "_ALL_"
                    ],
                    "url": url
                }
            }

            bypass = [
                {
                    "name": "url",
                    "value": "api.example.com/*"
                }
            ]

            # create rate limits
            resp = self.rate_limit.create_zone_rate_limits(
                threshold=threshold, period=period, action=action, match=match, bypass=bypass, correlate=correlate)
            assert resp is not None
            assert resp.status_code == 200
            print("rate limit id : ", resp.get_result().get("result")["id"])
            id = resp.get_result().get("result")["id"]
            url = "ibm.example.com/*"
            match = {
                "request": {
                    "methods": [
                        "_ALL_"
                    ],
                    "schemes": [
                        "_ALL_"
                    ],
                    "url": url
                }
            }
            i = i + 1
            mode_update = modes[i % len(modes)]
            action = {
                "mode": mode_update,
            }

            print("updating mode to", mode_update)
            # update rate limits
            resp = self.rate_limit.update_rate_limit(
                rate_limit_identifier=id, threshold=threshold, period=period, action=action, match=match, bypass=bypass, correlate=correlate)
            assert resp is not None
            assert resp.status_code == 200
            assert resp.get_result().get("result").get(
                "match").get("request").get("url") == url
            assert resp.get_result().get("result").get("action").get("mode") == mode_update

            # get rate limits
            resp = self.rate_limit.get_rate_limit(rate_limit_identifier=id)
            assert resp is not None
            assert resp.status_code == 200
            assert resp.get_result().get("result").get("action").get("mode") == mode_update

            # delete rate limits
            resp = self.rate_limit.delete_zone_rate_limit(
                rate_limit_identifier=id)
            assert resp is not None
            assert resp.status_code == 200

    def test_1_rate_limit_mode_simulate_ban_with_action_response_content(self):
        modes = ["simulate", "ban"]
        contents = {
            "text/plain": "This request has been rate-limited.",
            "application/json": '{ "name": "rate_limit", "msg": "This request has been rate-limited."}'
        }
        content_list = list(contents.keys())
        i = 0
        for mode in modes:
            for content in contents.keys():
                print("Test with mode: ", mode, " content :", content)
                threshold = 40
                period = 2
                url = "*.example.org/path*"
                action = {
                    "mode": mode,
                    "timeout": 60,
                    "response": {
                        "content_type": content,
                        "body": contents[content]
                    }
                }
                correlate = {
                    "by": "nat"
                }
                match = {
                    "request": {
                        "methods": [
                            "_ALL_"
                        ],
                        "schemes": [
                            "_ALL_"
                        ],
                        "url": url
                    }
                }

                bypass = [
                    {
                        "name": "url",
                        "value": "api.example.com/*"
                    }
                ]

                # create rate limits
                resp = self.rate_limit.create_zone_rate_limits(
                    threshold=threshold, period=period, action=action, match=match, bypass=bypass, correlate=correlate)
                assert resp is not None
                assert resp.status_code == 200
                print("rate limit id : ",
                      resp.get_result().get("result")["id"])
                id = resp.get_result().get("result")["id"]

                i = i + 1
                update_content = content_list[i % len(content_list)]
                action = {
                    "mode": mode,
                    "timeout": 60,
                    "response": {
                        "content_type": update_content,
                        "body": contents[update_content]
                    }
                }

                # update rate limit
                resp = self.rate_limit.update_rate_limit(
                    rate_limit_identifier=id, threshold=threshold, period=period, action=action, match=match, bypass=bypass, correlate=correlate)
                assert resp is not None
                assert resp.status_code == 200
                assert resp.get_result().get("result").get("action").get(
                    "response").get("content_type") == update_content
                assert resp.get_result().get("result").get("action").get(
                    "response").get("body") == contents[update_content]

                # get rate limit
                resp = self.rate_limit.get_rate_limit(rate_limit_identifier=id)
                assert resp is not None
                assert resp.status_code == 200

                # delete rate limit
                resp = self.rate_limit.delete_zone_rate_limit(
                    rate_limit_identifier=id)
                assert resp is not None
                assert resp.status_code == 200

    def test_1_rate_limit_mode_simulate_ban_with_request_content(self):
        mode = "simulate"
        methods = ["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "_ALL_"]
        schemas = ["HTTP", "HTTPS", "_ALL_"]
        url = "*.example.org/path*"
        threshold = 40
        period = 2
        i = 0

        for method in methods:
            for schema in schemas:
                print("Test with mode: ", method, " content :", schema)
                action = {
                    "mode": mode,
                    "timeout": 60,
                    "response": {
                        "content_type": "text/plain",
                        "body": "This request has been rate-limited."
                    }
                }
                correlate = {
                    "by": "nat"
                }
                match = {
                    "request": {
                        "methods": [
                            method,
                        ],
                        "schemes": [
                            schema
                        ],
                        "url": url
                    }
                }

                bypass = [
                    {
                        "name": "url",
                        "value": "api.example.com/*"
                    }
                ]
                resp = self.rate_limit.create_zone_rate_limits(
                    threshold=threshold, period=period, action=action, match=match, bypass=bypass, correlate=correlate)
                assert resp is not None
                assert resp.status_code == 200
                print("rate limit id : ",
                      resp.get_result().get("result")["id"])
                id = resp.get_result().get("result")["id"]

                i = i + 1
                method_update = methods[i % len(methods)]
                schema_update = schemas[i % len(schemas)]
                match = {
                    "request": {
                        "methods": [
                            method_update,
                        ],
                        "schemes": [
                            schema_update,
                        ],
                        "url": url
                    }
                }
                print("updating method to ", method_update,
                      ", schemas to ", schema_update)
                # update rate limit
                resp = self.rate_limit.update_rate_limit(
                    rate_limit_identifier=id, threshold=threshold, period=period, action=action, match=match, bypass=bypass, correlate=correlate)
                assert resp is not None
                assert resp.status_code == 200
                assert resp.get_result().get("result").get("match").get(
                    "request").get("methods")[0] == method_update
                assert resp.get_result().get("result").get("match").get(
                    "request").get("schemes")[0] == schema_update

                resp = self.rate_limit.get_rate_limit(
                    rate_limit_identifier=id)
                assert resp is not None
                assert resp.status_code == 200

                resp = self.rate_limit.delete_zone_rate_limit(
                    rate_limit_identifier=id)
                assert resp is not None
                assert resp.status_code == 200

    def test_1_rate_limit_mode_simulate_ban_with_response_content(self):
        url = "*.example.org/path*"
        threshold = 40
        period = 2

        action = {
            "mode": "simulate",
            "timeout": 60,
            "response": {
                    "content_type": "text/plain",
                    "body": "This request has been rate-limited."
            }
        }
        correlate = {
            "by": "nat"
        }
        match = {
            "request": {
                "methods": [
                    "_ALL_",
                ],
                "schemes": [
                    "_ALL_"
                ],
                "url": url
            },
            "response": {
                "name": "Cf-Cache-Status",
                        "op": "eq",
                        "value": "HIT"
            }
        }
        bypass = [
            {
                "name": "url",
                "value": "api.example.com/*"
            }
        ]

        # create rate limit
        resp = self.rate_limit.create_zone_rate_limits(
            threshold=threshold, period=period, action=action, match=match, bypass=bypass, correlate=correlate)
        assert resp is not None
        assert resp.status_code == 200
        print("rate limit id : ", resp.get_result().get("result")["id"])
        id = resp.get_result().get("result")["id"]

        # get rate limit
        resp = self.rate_limit.get_rate_limit(
            rate_limit_identifier=id)
        assert resp is not None
        assert resp.status_code == 200

        # delete rate limit
        resp = self.rate_limit.delete_zone_rate_limit(
            rate_limit_identifier=id)
        assert resp is not None
        assert resp.status_code == 200

    def test_1_list_all_rate_limits(self):
        mode = "simulate"
        threshold = 40
        period = 2
        url = "*.example.org/path*"
        action = {
            "mode": mode,
            "timeout": 60,
            "response": {
                "content_type": "text/plain",
                "body": "This request has been rate-limited."
            }
        }
        correlate = {
            "by": "nat"
        }
        match = {
            "request": {
                "methods": [
                    "_ALL_"
                ],
                "schemes": [
                    "_ALL_"
                ],
                "url": url
            }
        }
        bypass = [
            {
                "name": "url",
                "value": "api.example.com/*"
            }
        ]
        # create rate limits
        resp = self.rate_limit.create_zone_rate_limits(
            threshold=threshold, period=period, action=action, match=match, bypass=bypass, correlate=correlate)
        assert resp is not None
        assert resp.status_code == 200

        url = "*.example1.org/path*"
        match = {
            "request": {
                "methods": [
                    "_ALL_"
                ],
                "schemes": [
                    "_ALL_"
                ],
                "url": url
            }
        }
        # create rate limits
        resp = self.rate_limit.create_zone_rate_limits(
            threshold=threshold, period=period, action=action, match=match, bypass=bypass, correlate=correlate)
        assert resp is not None
        assert resp.status_code == 200

        # list all zone rate limits
        resp = self.rate_limit.list_all_zone_rate_limits()
        assert resp is not None
        assert resp.status_code == 200

        if resp.get_result().get('result') is not None:
            ids = resp.get_result().get('result')
            for id in ids:
                # delete zone rate limit
                self.rate_limit.delete_zone_rate_limit(
                    rate_limit_identifier=id.get("id"))


if __name__ == '__main__':
    unittest.main()
