# coding: utf-8
# Copyright 2020 IBM All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Python client library for the IBM Cloud Networking Services"""

from ibm_cloud_sdk_core import IAMTokenManager, DetailedResponse, BaseService, ApiException

from .common import get_sdk_headers
from .version import __version__

# CIS Service packages
from .caching_api_v1 import CachingApiV1
from .cis_ip_api_v1 import CisIpApiV1
from .custom_pages_v1 import CustomPagesV1
from .dns_record_bulk_v1 import DnsRecordBulkV1
from .dns_records_v1 import DnsRecordsV1
from .filters_v1 import FiltersV1
from .firewall_access_rules_v1 import FirewallAccessRulesV1
from .filters_v1 import FiltersV1
from .firewall_api_v1 import FirewallApiV1
from .firewall_rules_v1 import FirewallRulesV1
from .global_load_balancer_events_v1 import GlobalLoadBalancerEventsV1
from .global_load_balancer_monitor_v1 import GlobalLoadBalancerMonitorV1
from .global_load_balancer_pools_v0 import GlobalLoadBalancerPoolsV0
from .global_load_balancer_v1 import GlobalLoadBalancerV1
from .page_rule_api_v1 import PageRuleApiV1
from .range_applications_v1 import RangeApplicationsV1
from .routing_v1 import RoutingV1
from .security_events_api_v1 import SecurityEventsApiV1
from .ssl_certificate_api_v1 import SslCertificateApiV1
from .user_agent_blocking_rules_v1 import UserAgentBlockingRulesV1
from .waf_api_v1 import WafApiV1
from .waf_rule_groups_api_v1 import WafRuleGroupsApiV1
from .waf_rule_packages_api_v1 import WafRulePackagesApiV1
from .waf_rules_api_v1 import WafRulesApiV1
from .zone_firewall_access_rules_v1 import ZoneFirewallAccessRulesV1
from .zone_lockdown_v1 import ZoneLockdownV1
from .zone_rate_limits_v1 import ZoneRateLimitsV1
from .zones_settings_v1 import ZonesSettingsV1
from .zones_v1 import ZonesV1
from .webhooks_v1 import WebhooksV1
from .alerts_v1 import AlertsV1

# Private DNS Service Packages
from .dns_zones_v1 import DnsZonesV1
from .resource_records_v1 import ResourceRecordsV1
from .permitted_networks_for_dns_zones_v1 import PermittedNetworksForDnsZonesV1
from .global_load_balancers_v1 import GlobalLoadBalancersV1
from .dns_svcs_v1 import DnsSvcsV1

# Directlink Service Packages
from .direct_link_v1 import DirectLinkV1
from .direct_link_provider_v2 import DirectLinkProviderV2

# Transit Service Packages
from .transit_gateway_apis_v1 import TransitGatewayApisV1
