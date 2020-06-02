# coding: utf-8

# (C) Copyright IBM Corp. 2020.
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

"""
Security Events API
"""

from datetime import datetime
from enum import Enum
from typing import Dict, List
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import datetime_to_string, string_to_datetime

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################

class SecurityEventsApiV1(BaseService):
    """The Security Events API V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.cis.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'security_events_api'

    @classmethod
    def new_instance(cls,
                     crn: str,
                     zone_id: str,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'SecurityEventsApiV1':
        """
        Return a new client for the Security Events API service using the specified
               parameters and external configuration.

        :param str crn: Full url-encoded cloud resource name (CRN) of resource
               instance.

        :param str zone_id: zone identifier.
        """
        if crn is None:
            raise ValueError('crn must be provided')
        if zone_id is None:
            raise ValueError('zone_id must be provided')

        authenticator = get_authenticator_from_environment(service_name)
        service = cls(
            crn,
            zone_id,
            authenticator
            )
        service.configure_service(service_name)
        return service

    def __init__(self,
                 crn: str,
                 zone_id: str,
                 authenticator: Authenticator = None,
                ) -> None:
        """
        Construct a new client for the Security Events API service.

        :param str crn: Full url-encoded cloud resource name (CRN) of resource
               instance.

        :param str zone_id: zone identifier.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/master/README.md
               about initializing the authenticator of your choice.
        """
        if crn is None:
            raise ValueError('crn must be provided')
        if zone_id is None:
            raise ValueError('zone_id must be provided')

        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)
        self.crn = crn
        self.zone_id = zone_id


    #########################
    # Security Events
    #########################


    def security_events(self, *, ip_class: str = None, method: str = None, scheme: str = None, ip: str = None, host: str = None, proto: str = None, uri: str = None, ua: str = None, colo: str = None, ray_id: str = None, kind: str = None, action: str = None, cursor: str = None, country: str = None, since: datetime = None, source: str = None, limit: int = None, rule_id: str = None, until: datetime = None, **kwargs) -> DetailedResponse:
        """
        Logs of the mitigations performed by Firewall features.

        Provides a full log of the mitigations performed by the CIS Firewall features
        including; Firewall Rules, Rate Limiting, Security Level, Access Rules (IP, IP
        Range, ASN, and Country), WAF (Web Application Firewall), User Agent Blocking,
        Zone Lockdown, and Advanced DDoS Protection.

        :param str ip_class: (optional) IP class is a map of client IP to visitor
               classification.
        :param str method: (optional) The HTTP method of the request.
        :param str scheme: (optional) The scheme of the uri.
        :param str ip: (optional) The IPv4 or IPv6 address from which the request
               originated.
        :param str host: (optional) The hostname the request attempted to access.
        :param str proto: (optional) The protocol of the request.
        :param str uri: (optional) The URI requested from the hostname.
        :param str ua: (optional) The client user agent that initiated the request.
        :param str colo: (optional) The 3-letter CF PoP code.
        :param str ray_id: (optional) Ray ID of the request.
        :param str kind: (optional) Kind of events. Now it is only firewall.
        :param str action: (optional) What type of action was taken.
        :param str cursor: (optional) Cursor position and direction for requesting
               next set of records when amount of results was limited by the limit
               parameter. A valid value for the cursor can be obtained from the cursors
               object in the result_info structure.
        :param str country: (optional) The 2-digit country code in which the
               request originated.
        :param datetime since: (optional) Start date and time of requesting data
               period in the ISO8601 format. Can't go back more than a year.
        :param str source: (optional) Source of the event.
        :param int limit: (optional) The number of events to return.
        :param str rule_id: (optional) The ID of the rule that triggered the event,
               should be considered in the context of source.
        :param datetime until: (optional) End date and time of requesting data
               period in the ISO8601 format.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SecurityEvents` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='security_events')
        headers.update(sdk_headers)

        params = {
            'ip_class': ip_class,
            'method': method,
            'scheme': scheme,
            'ip': ip,
            'host': host,
            'proto': proto,
            'uri': uri,
            'ua': ua,
            'colo': colo,
            'ray_id': ray_id,
            'kind': kind,
            'action': action,
            'cursor': cursor,
            'country': country,
            'since': since,
            'source': source,
            'limit': limit,
            'rule_id': rule_id,
            'until': until
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/security/events'.format(*self.encode_path_vars(self.crn, self.zone_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


class SecurityEventsEnums:
    """
    Enums for security_events parameters.
    """

    class IpClass(Enum):
        """
        IP class is a map of client IP to visitor classification.
        """
        UNKNOWN = 'unknown'
        CLEAN = 'clean'
        BADHOST = 'badHost'
        SEARCHENGINE = 'searchEngine'
        WHITELIST = 'whitelist'
        GREYLIST = 'greylist'
        MONITORINGSERVICE = 'monitoringService'
        SECURITYSCANNER = 'securityScanner'
        NORECORD = 'noRecord'
        SCAN = 'scan'
        BACKUPSERVICE = 'backupService'
        MOBILEPLATFORM = 'mobilePlatform'
        TOR = 'tor'
    class Method(Enum):
        """
        The HTTP method of the request.
        """
        GET = 'GET'
        POST = 'POST'
        DELETE = 'DELETE'
        PUT = 'PUT'
        HEAD = 'HEAD'
        PURGE = 'PURGE'
        OPTIONS = 'OPTIONS'
        PROPFIND = 'PROPFIND'
        MKCOL = 'MKCOL'
        PATCH = 'PATCH'
        ACL = 'ACL'
        BCOPY = 'BCOPY'
        BDELETE = 'BDELETE'
        BMOVE = 'BMOVE'
        BPROPFIND = 'BPROPFIND'
        BPROPPATCH = 'BPROPPATCH'
        CHECKIN = 'CHECKIN'
        CHECKOUT = 'CHECKOUT'
        CONNECT = 'CONNECT'
        COPY = 'COPY'
        LABEL = 'LABEL'
        LOCK = 'LOCK'
        MERGE = 'MERGE'
        MKACTIVITY = 'MKACTIVITY'
        MKWORKSPACE = 'MKWORKSPACE'
        MOVE = 'MOVE'
        NOTIFY = 'NOTIFY'
        ORDERPATCH = 'ORDERPATCH'
        POLL = 'POLL'
        PROPPATCH = 'PROPPATCH'
        REPORT = 'REPORT'
        SEARCH = 'SEARCH'
        SUBSCRIBE = 'SUBSCRIBE'
        TRACE = 'TRACE'
        UNCHECKOUT = 'UNCHECKOUT'
        UNLOCK = 'UNLOCK'
        UNSUBSCRIBE = 'UNSUBSCRIBE'
        UPDATE = 'UPDATE'
        VERSION_CONTROL = 'VERSION-CONTROL'
        BASELINE_CONTROL = 'BASELINE-CONTROL'
        X_MS_ENUMATTS = 'X-MS-ENUMATTS'
        RPC_OUT_DATA = 'RPC_OUT_DATA'
        RPC_IN_DATA = 'RPC_IN_DATA'
        JSON = 'JSON'
        COOK = 'COOK'
        TRACK = 'TRACK'
    class Scheme(Enum):
        """
        The scheme of the uri.
        """
        UNKNOWN = 'unknown'
        HTTP = 'http'
        HTTPS = 'https'
    class Proto(Enum):
        """
        The protocol of the request.
        """
        UNK = 'UNK'
        HTTP_1_0 = 'HTTP/1.0'
        HTTP_1_1 = 'HTTP/1.1'
        HTTP_1_2 = 'HTTP/1.2'
        HTTP_2 = 'HTTP/2'
        SPDY_3_1 = 'SPDY/3.1'
    class Kind(Enum):
        """
        Kind of events. Now it is only firewall.
        """
        FIREWALL = 'firewall'
    class Action(Enum):
        """
        What type of action was taken.
        """
        UNKNOWN = 'unknown'
        ALLOW = 'allow'
        DROP = 'drop'
        CHALLENGE = 'challenge'
        JSCHALLENGE = 'jschallenge'
        SIMULATE = 'simulate'
        CONNECTIONCLOSE = 'connectionClose'
        LOG = 'log'
    class Source(Enum):
        """
        Source of the event.
        """
        UNKNOWN = 'unknown'
        ASN = 'asn'
        COUNTRY = 'country'
        IP = 'ip'
        IPRANGE = 'ipRange'
        SECURITYLEVEL = 'securityLevel'
        ZONELOCKDOWN = 'zoneLockdown'
        WAF = 'waf'
        UABLOCK = 'uaBlock'
        RATELIMIT = 'rateLimit'
        FIREWALLRULES = 'firewallRules'
        BIC = 'bic'
        HOT = 'hot'
        L7DDOS = 'l7ddos'

