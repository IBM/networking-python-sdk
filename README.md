[![Build Status](https://travis-ci.com/IBM/networking-python-sdk.svg?branch=master)](https://travis-ci.com/IBM/networking-python-sdk)
[![Release](https://img.shields.io/github/v/release/IBM/networking-python-sdk)](https://github.com/IBM/networking-python-sdk/releases/latest)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ibm-cloud-networking-services)](https://pypi.org/project/ibm-cloud-networking-services/)
[![PyPI](https://img.shields.io/pypi/v/ibm-cloud-networking-services)](https://pypi.org/project/ibm-cloud-networking-services/)
![PyPI - Downloads](https://img.shields.io/pypi/dm/ibm-cloud-networking-services)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![codecov](https://codecov.io/gh/IBM/networking-python-sdk/branch/master/graph/badge.svg)](https://codecov.io/gh/IBM/networking-python-sdk)
[![semantic-release](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg)](https://github.com/semantic-release/semantic-release)

# IBM Cloud Networking Services Python SDK Version 0.2.0

Python client library to interact with various [IBM Cloud Networking Service APIs](https://cloud.ibm.com/apidocs?category=network).

## Table of Contents

<!--
  The TOC below is generated using the `markdown-toc` node package.

      https://github.com/jonschlinkert/markdown-toc

  You should regenerate the TOC after making changes to this file.

      npx markdown-toc -i README.md
  -->

<!-- toc -->

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Using the SDK](#using-the-sdk)
- [Questions](#questions)
- [Issues](#issues)
- [Open source @ IBM](#open-source--ibm)
- [Contributing](#contributing)
- [License](#license)

<!-- tocstop -->

## Overview

The IBM Cloud Networking Services Python SDK allows developers to programmatically interact with the following
IBM Cloud services:

| CIS Service Name                                                                               | Imported Class Name         |
| ---------------------------------------------------------------------------------------------- | --------------------------- |
| [CIS: Cache](https://cloud.ibm.com/apidocs/cis/cache)                                          | CachingApiV1                |
| [CIS: IP](https://cloud.ibm.com/apidocs/cis/ip)                                                | CisIpApiV1                  |
| [CIS: Custom Pages](https://cloud.ibm.com/apidocs/cis)                                         | CustomPagesV1               |
| [CIS: DNS Records Bulk](https://cloud.ibm.com/apidocs/cis/dnsrecords)                          | DnsRecordBulkV1             |
| [CIS: DNS Records](https://cloud.ibm.com/apidocs/cis/dnsrecords)                               | DnsRecordsV1                |
| [CIS: Firewall Access Rules](https://cloud.ibm.com/apidocs/cis/firewall-access-rule)           | FirewallAccessRulesV1       |
| [CIS: Security Level Settings](https://cloud.ibm.com/apidocs/cis/security-level-settings)      | FirewallApiV1               |
| [CIS: GLB Events](https://cloud.ibm.com/apidocs/cis/glb-events)                                | GlobalLoadBalancerEventsV1  |
| [CIS: GLB Monitor](https://cloud.ibm.com/apidocs/cis/glb-monitor)                              | GlobalLoadBalancerMonitorV1 |
| [CIS: GLB Pools](https://cloud.ibm.com/apidocs/cis/glb-pool)                                   | GlobalLoadBalancerPoolsV0   |
| [CIS: GLB Service](https://cloud.ibm.com/apidocs/cis/glb)                                      | GlobalLoadBalancerV1        |
| [CIS: Page Rules](https://cloud.ibm.com/apidocs/cis/page-rules)                                | PageRuleApiV1               |
| [CIS: Range Application](https://cloud.ibm.com/apidocs/cis/range)                              | RangeApplicationsV1         |
| [CIS: Routing](https://cloud.ibm.com/apidocs/cis/routing)                                      | RoutingV1                   |
| [CIS: Security Events](https://cloud.ibm.com/apidocs/cis)                                      | SecurityEventsApiV1         |
| [CIS: SSL/TLS](https://cloud.ibm.com/apidocs/cis/tls)                                          | SslCertificateApiV1         |
| [CIS: User Agent Blocking Rules](https://cloud.ibm.com/apidocs/cis/user-agent-rules)           | UserAgentBlockingRulesV1    |
| [CIS: WAF Settings](https://cloud.ibm.com/apidocs/cis/waf)                                     | WafApiV1                    |
| [CIS: WAF Rule Groups](https://cloud.ibm.com/apidocs/cis/waf-groups)                           | WafRuleGroupsApiV1          |
| [CIS: WAF Rule Packages](https://cloud.ibm.com/apidocs/cis/waf-packages)                       | WafRulePackagesApiV1        |
| [CIS: WAF Rules](https://cloud.ibm.com/apidocs/cis/waf-rules)                                  | WafRulesApiV1               |
| [CIS: Zone Firewall Access Rules](https://cloud.ibm.com/apidocs/cis/zone-firewall-access-rule) | ZoneFirewallAccessRulesV1   |
| [CIS: Zone Lockdown](https://cloud.ibm.com/apidocs/cis/zone-lockdown)                          | ZoneLockdownV1              |
| [CIS: Zone Rate Limits](https://cloud.ibm.com/apidocs/cis)                                     | ZoneRateLimitsV1            |
| [CIS: Zone Settings](https://cloud.ibm.com/apidocs/cis/zonesettings)                           | ZonesSettingsV1             |
| [CIS: Zones](https://cloud.ibm.com/apidocs/cis/zones)                                          | ZonesV1                     |

| PDNS Service Name                                                                | Imported Class Name            |
| -------------------------------------------------------------------------------- | ------------------------------ |
| [PDNS: Zones API](https://cloud.ibm.com/apidocs/dns-svcs)                        | DnsZonesV1                     |
| [PDNS: Resource Records API](https://cloud.ibm.com/apidocs/dns-svcs)             | ResourceRecordsV1              |
| [PDNS: Permitted Networks for Zones API](https://cloud.ibm.com/apidocs/dns-svcs) | PermittedNetworksForDnsZonesV1 |

| Direct Link Service                                      | Imported Class Name |
| -------------------------------------------------------- | ------------------- |
| [Direct Link](https://cloud.ibm.com/apidocs/direct_link?code=python) | DirectLinkV1    |
| [Direct Link Provider](https://cloud.ibm.com/apidocs/direct_link_provider_api?code=python) | DirectLinkProviderV2    |

| Transit Service                                                  | Imported Class Name  |
| ---------------------------------------------------------------- | -------------------- |
| [Transit Gateway](https://cloud.ibm.com/apidocs/transit-gateway) | TransitGatewayApisV1 |

## Prerequisites

[ibm-cloud-onboarding]: https://cloud.ibm.com/registration

- An [IBM Cloud][ibm-cloud-onboarding] account.
- An IAM API key to allow the SDK to access your account. Create one [here](https://cloud.ibm.com/iam/apikeys).
- Python 3.5.3 or above.

## Installation

To install, use `pip` or `easy_install`:

```bash
pip install --upgrade "ibm-cloud-networking-services==0.2.0"
```

or

```bash
easy_install --upgrade "ibm-cloud-networking-servies==0.2.0"
```

## Using the SDK

For general SDK usage information, please see [this link](https://github.com/IBM/ibm-cloud-sdk-common/blob/master/README.md)

## Questions

If you are having difficulties using this SDK or have a question about the IBM Cloud services,
please ask a question
[Stack Overflow](http://stackoverflow.com/questions/ask?tags=ibm-cloud).

## Issues

If you encounter an issue with the project, you are welcome to submit a
[bug report](<github-repo-url>/issues).
Before that, please search for similar issues. It's possible that someone has already reported the problem.

## Open source @ IBM

Find more open source projects on the [IBM Github Page](http://ibm.github.io/)

## Contributing

See [CONTRIBUTING](CONTRIBUTING.md).

## License

This SDK is released under the Apache 2.0 license.
The license's full text can be found in [LICENSE](LICENSE).
