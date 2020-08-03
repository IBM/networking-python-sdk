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


    def security_events(self,
        *,
        ip_class: str = None,
        method: str = None,
        scheme: str = None,
        ip: str = None,
        host: str = None,
        proto: str = None,
        uri: str = None,
        ua: str = None,
        colo: str = None,
        ray_id: str = None,
        kind: str = None,
        action: str = None,
        cursor: str = None,
        country: str = None,
        since: datetime = None,
        source: str = None,
        limit: int = None,
        rule_id: str = None,
        until: datetime = None,
        **kwargs
    ) -> DetailedResponse:
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='security_events')
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

        url = '/v1/{0}/zones/{1}/security/events'.format(
            *self.encode_path_vars(self.crn, self.zone_id))
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

    class IpClass(str, Enum):
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
    class Method(str, Enum):
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
    class Scheme(str, Enum):
        """
        The scheme of the uri.
        """
        UNKNOWN = 'unknown'
        HTTP = 'http'
        HTTPS = 'https'
    class Proto(str, Enum):
        """
        The protocol of the request.
        """
        UNK = 'UNK'
        HTTP_1_0 = 'HTTP/1.0'
        HTTP_1_1 = 'HTTP/1.1'
        HTTP_1_2 = 'HTTP/1.2'
        HTTP_2 = 'HTTP/2'
        SPDY_3_1 = 'SPDY/3.1'
    class Kind(str, Enum):
        """
        Kind of events. Now it is only firewall.
        """
        FIREWALL = 'firewall'
    class Action(str, Enum):
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
    class Source(str, Enum):
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


##############################################################################
# Models
##############################################################################


class ResultInfoCursors():
    """
    Cursor positions of the security events.

    :attr str after: The events in the response is after this cursor position.
    :attr str before: The events in the response is before this cursor position.
    """

    def __init__(self,
                 after: str,
                 before: str) -> None:
        """
        Initialize a ResultInfoCursors object.

        :param str after: The events in the response is after this cursor position.
        :param str before: The events in the response is before this cursor
               position.
        """
        self.after = after
        self.before = before

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResultInfoCursors':
        """Initialize a ResultInfoCursors object from a json dictionary."""
        args = {}
        if 'after' in _dict:
            args['after'] = _dict.get('after')
        else:
            raise ValueError('Required property \'after\' not present in ResultInfoCursors JSON')
        if 'before' in _dict:
            args['before'] = _dict.get('before')
        else:
            raise ValueError('Required property \'before\' not present in ResultInfoCursors JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResultInfoCursors object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'after') and self.after is not None:
            _dict['after'] = self.after
        if hasattr(self, 'before') and self.before is not None:
            _dict['before'] = self.before
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResultInfoCursors object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResultInfoCursors') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResultInfoCursors') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ResultInfoScannedRange():
    """
    The time window of the events.

    :attr str since: Start date and time of the events.
    :attr str until: End date and time of the events.
    """

    def __init__(self,
                 since: str,
                 until: str) -> None:
        """
        Initialize a ResultInfoScannedRange object.

        :param str since: Start date and time of the events.
        :param str until: End date and time of the events.
        """
        self.since = since
        self.until = until

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResultInfoScannedRange':
        """Initialize a ResultInfoScannedRange object from a json dictionary."""
        args = {}
        if 'since' in _dict:
            args['since'] = _dict.get('since')
        else:
            raise ValueError('Required property \'since\' not present in ResultInfoScannedRange JSON')
        if 'until' in _dict:
            args['until'] = _dict.get('until')
        else:
            raise ValueError('Required property \'until\' not present in ResultInfoScannedRange JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResultInfoScannedRange object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'since') and self.since is not None:
            _dict['since'] = self.since
        if hasattr(self, 'until') and self.until is not None:
            _dict['until'] = self.until
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResultInfoScannedRange object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResultInfoScannedRange') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResultInfoScannedRange') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SecurityEventObjectMatchesItem():
    """
    SecurityEventObjectMatchesItem.

    :attr str rule_id: The ID of the rule that triggered the event, should be
          considered in the context of source.
    :attr str source: Source of the event.
    :attr str action: What type of action was taken.
    :attr object metadata: metadata.
    """

    def __init__(self,
                 rule_id: str,
                 source: str,
                 action: str,
                 metadata: object) -> None:
        """
        Initialize a SecurityEventObjectMatchesItem object.

        :param str rule_id: The ID of the rule that triggered the event, should be
               considered in the context of source.
        :param str source: Source of the event.
        :param str action: What type of action was taken.
        :param object metadata: metadata.
        """
        self.rule_id = rule_id
        self.source = source
        self.action = action
        self.metadata = metadata

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SecurityEventObjectMatchesItem':
        """Initialize a SecurityEventObjectMatchesItem object from a json dictionary."""
        args = {}
        if 'rule_id' in _dict:
            args['rule_id'] = _dict.get('rule_id')
        else:
            raise ValueError('Required property \'rule_id\' not present in SecurityEventObjectMatchesItem JSON')
        if 'source' in _dict:
            args['source'] = _dict.get('source')
        else:
            raise ValueError('Required property \'source\' not present in SecurityEventObjectMatchesItem JSON')
        if 'action' in _dict:
            args['action'] = _dict.get('action')
        else:
            raise ValueError('Required property \'action\' not present in SecurityEventObjectMatchesItem JSON')
        if 'metadata' in _dict:
            args['metadata'] = _dict.get('metadata')
        else:
            raise ValueError('Required property \'metadata\' not present in SecurityEventObjectMatchesItem JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SecurityEventObjectMatchesItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'rule_id') and self.rule_id is not None:
            _dict['rule_id'] = self.rule_id
        if hasattr(self, 'source') and self.source is not None:
            _dict['source'] = self.source
        if hasattr(self, 'action') and self.action is not None:
            _dict['action'] = self.action
        if hasattr(self, 'metadata') and self.metadata is not None:
            _dict['metadata'] = self.metadata
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SecurityEventObjectMatchesItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SecurityEventObjectMatchesItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SecurityEventObjectMatchesItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ResultInfo():
    """
    Statistics of results.

    :attr ResultInfoCursors cursors: Cursor positions of the security events.
    :attr ResultInfoScannedRange scanned_range: The time window of the events.
    """

    def __init__(self,
                 cursors: 'ResultInfoCursors',
                 scanned_range: 'ResultInfoScannedRange') -> None:
        """
        Initialize a ResultInfo object.

        :param ResultInfoCursors cursors: Cursor positions of the security events.
        :param ResultInfoScannedRange scanned_range: The time window of the events.
        """
        self.cursors = cursors
        self.scanned_range = scanned_range

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResultInfo':
        """Initialize a ResultInfo object from a json dictionary."""
        args = {}
        if 'cursors' in _dict:
            args['cursors'] = ResultInfoCursors.from_dict(_dict.get('cursors'))
        else:
            raise ValueError('Required property \'cursors\' not present in ResultInfo JSON')
        if 'scanned_range' in _dict:
            args['scanned_range'] = ResultInfoScannedRange.from_dict(_dict.get('scanned_range'))
        else:
            raise ValueError('Required property \'scanned_range\' not present in ResultInfo JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResultInfo object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'cursors') and self.cursors is not None:
            _dict['cursors'] = self.cursors.to_dict()
        if hasattr(self, 'scanned_range') and self.scanned_range is not None:
            _dict['scanned_range'] = self.scanned_range.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResultInfo object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResultInfo') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResultInfo') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SecurityEventObject():
    """
    Security event object.

    :attr str ray_id: Ray ID of the request.
    :attr str kind: Kind of events. Now it is only firewall.
    :attr str source: Source of the event.
    :attr str action: What type of action was taken.
    :attr str rule_id: The ID of the rule that triggered the event, should be
          considered in the context of source.
    :attr str ip: The IPv4 or IPv6 address from which the request originated.
    :attr str ip_class: IP class is a map of client IP to visitor classification.
    :attr str country: The 2-digit country code in which the request originated.
    :attr str colo: The 3-letter CF PoP code.
    :attr str host: The hostname the request attempted to access.
    :attr str method: The HTTP method of the request.
    :attr str proto: The protocol of the request.
    :attr str scheme: The scheme of the uri.
    :attr str ua: The client user agent that initiated the request.
    :attr str uri: The URI requested from the hostname.
    :attr datetime occurred_at: The time that the event occurred.
    :attr List[SecurityEventObjectMatchesItem] matches: The firewall rules those the
          event matches.
    """

    def __init__(self,
                 ray_id: str,
                 kind: str,
                 source: str,
                 action: str,
                 rule_id: str,
                 ip: str,
                 ip_class: str,
                 country: str,
                 colo: str,
                 host: str,
                 method: str,
                 proto: str,
                 scheme: str,
                 ua: str,
                 uri: str,
                 occurred_at: datetime,
                 matches: List['SecurityEventObjectMatchesItem']) -> None:
        """
        Initialize a SecurityEventObject object.

        :param str ray_id: Ray ID of the request.
        :param str kind: Kind of events. Now it is only firewall.
        :param str source: Source of the event.
        :param str action: What type of action was taken.
        :param str rule_id: The ID of the rule that triggered the event, should be
               considered in the context of source.
        :param str ip: The IPv4 or IPv6 address from which the request originated.
        :param str ip_class: IP class is a map of client IP to visitor
               classification.
        :param str country: The 2-digit country code in which the request
               originated.
        :param str colo: The 3-letter CF PoP code.
        :param str host: The hostname the request attempted to access.
        :param str method: The HTTP method of the request.
        :param str proto: The protocol of the request.
        :param str scheme: The scheme of the uri.
        :param str ua: The client user agent that initiated the request.
        :param str uri: The URI requested from the hostname.
        :param datetime occurred_at: The time that the event occurred.
        :param List[SecurityEventObjectMatchesItem] matches: The firewall rules
               those the event matches.
        """
        self.ray_id = ray_id
        self.kind = kind
        self.source = source
        self.action = action
        self.rule_id = rule_id
        self.ip = ip
        self.ip_class = ip_class
        self.country = country
        self.colo = colo
        self.host = host
        self.method = method
        self.proto = proto
        self.scheme = scheme
        self.ua = ua
        self.uri = uri
        self.occurred_at = occurred_at
        self.matches = matches

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SecurityEventObject':
        """Initialize a SecurityEventObject object from a json dictionary."""
        args = {}
        if 'ray_id' in _dict:
            args['ray_id'] = _dict.get('ray_id')
        else:
            raise ValueError('Required property \'ray_id\' not present in SecurityEventObject JSON')
        if 'kind' in _dict:
            args['kind'] = _dict.get('kind')
        else:
            raise ValueError('Required property \'kind\' not present in SecurityEventObject JSON')
        if 'source' in _dict:
            args['source'] = _dict.get('source')
        else:
            raise ValueError('Required property \'source\' not present in SecurityEventObject JSON')
        if 'action' in _dict:
            args['action'] = _dict.get('action')
        else:
            raise ValueError('Required property \'action\' not present in SecurityEventObject JSON')
        if 'rule_id' in _dict:
            args['rule_id'] = _dict.get('rule_id')
        else:
            raise ValueError('Required property \'rule_id\' not present in SecurityEventObject JSON')
        if 'ip' in _dict:
            args['ip'] = _dict.get('ip')
        else:
            raise ValueError('Required property \'ip\' not present in SecurityEventObject JSON')
        if 'ip_class' in _dict:
            args['ip_class'] = _dict.get('ip_class')
        else:
            raise ValueError('Required property \'ip_class\' not present in SecurityEventObject JSON')
        if 'country' in _dict:
            args['country'] = _dict.get('country')
        else:
            raise ValueError('Required property \'country\' not present in SecurityEventObject JSON')
        if 'colo' in _dict:
            args['colo'] = _dict.get('colo')
        else:
            raise ValueError('Required property \'colo\' not present in SecurityEventObject JSON')
        if 'host' in _dict:
            args['host'] = _dict.get('host')
        else:
            raise ValueError('Required property \'host\' not present in SecurityEventObject JSON')
        if 'method' in _dict:
            args['method'] = _dict.get('method')
        else:
            raise ValueError('Required property \'method\' not present in SecurityEventObject JSON')
        if 'proto' in _dict:
            args['proto'] = _dict.get('proto')
        else:
            raise ValueError('Required property \'proto\' not present in SecurityEventObject JSON')
        if 'scheme' in _dict:
            args['scheme'] = _dict.get('scheme')
        else:
            raise ValueError('Required property \'scheme\' not present in SecurityEventObject JSON')
        if 'ua' in _dict:
            args['ua'] = _dict.get('ua')
        else:
            raise ValueError('Required property \'ua\' not present in SecurityEventObject JSON')
        if 'uri' in _dict:
            args['uri'] = _dict.get('uri')
        else:
            raise ValueError('Required property \'uri\' not present in SecurityEventObject JSON')
        if 'occurred_at' in _dict:
            args['occurred_at'] = string_to_datetime(_dict.get('occurred_at'))
        else:
            raise ValueError('Required property \'occurred_at\' not present in SecurityEventObject JSON')
        if 'matches' in _dict:
            args['matches'] = [SecurityEventObjectMatchesItem.from_dict(x) for x in _dict.get('matches')]
        else:
            raise ValueError('Required property \'matches\' not present in SecurityEventObject JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SecurityEventObject object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'ray_id') and self.ray_id is not None:
            _dict['ray_id'] = self.ray_id
        if hasattr(self, 'kind') and self.kind is not None:
            _dict['kind'] = self.kind
        if hasattr(self, 'source') and self.source is not None:
            _dict['source'] = self.source
        if hasattr(self, 'action') and self.action is not None:
            _dict['action'] = self.action
        if hasattr(self, 'rule_id') and self.rule_id is not None:
            _dict['rule_id'] = self.rule_id
        if hasattr(self, 'ip') and self.ip is not None:
            _dict['ip'] = self.ip
        if hasattr(self, 'ip_class') and self.ip_class is not None:
            _dict['ip_class'] = self.ip_class
        if hasattr(self, 'country') and self.country is not None:
            _dict['country'] = self.country
        if hasattr(self, 'colo') and self.colo is not None:
            _dict['colo'] = self.colo
        if hasattr(self, 'host') and self.host is not None:
            _dict['host'] = self.host
        if hasattr(self, 'method') and self.method is not None:
            _dict['method'] = self.method
        if hasattr(self, 'proto') and self.proto is not None:
            _dict['proto'] = self.proto
        if hasattr(self, 'scheme') and self.scheme is not None:
            _dict['scheme'] = self.scheme
        if hasattr(self, 'ua') and self.ua is not None:
            _dict['ua'] = self.ua
        if hasattr(self, 'uri') and self.uri is not None:
            _dict['uri'] = self.uri
        if hasattr(self, 'occurred_at') and self.occurred_at is not None:
            _dict['occurred_at'] = datetime_to_string(self.occurred_at)
        if hasattr(self, 'matches') and self.matches is not None:
            _dict['matches'] = [x.to_dict() for x in self.matches]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SecurityEventObject object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SecurityEventObject') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SecurityEventObject') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class KindEnum(str, Enum):
        """
        Kind of events. Now it is only firewall.
        """
        FIREWALL = 'firewall'


    class SourceEnum(str, Enum):
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


    class ActionEnum(str, Enum):
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


    class IpClassEnum(str, Enum):
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


    class MethodEnum(str, Enum):
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


    class ProtoEnum(str, Enum):
        """
        The protocol of the request.
        """
        UNK = 'UNK'
        HTTP_1_0 = 'HTTP/1.0'
        HTTP_1_1 = 'HTTP/1.1'
        HTTP_1_2 = 'HTTP/1.2'
        HTTP_2 = 'HTTP/2'
        SPDY_3_1 = 'SPDY/3.1'


    class SchemeEnum(str, Enum):
        """
        The scheme of the uri.
        """
        UNKNOWN = 'unknown'
        HTTP = 'http'
        HTTPS = 'https'


class SecurityEvents():
    """
    security events objects.

    :attr List[SecurityEventObject] result: Container for response information.
    :attr ResultInfo result_info: Statistics of results.
    :attr bool success: Was the get successful.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    """

    def __init__(self,
                 result: List['SecurityEventObject'],
                 result_info: 'ResultInfo',
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]]) -> None:
        """
        Initialize a SecurityEvents object.

        :param List[SecurityEventObject] result: Container for response
               information.
        :param ResultInfo result_info: Statistics of results.
        :param bool success: Was the get successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        """
        self.result = result
        self.result_info = result_info
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SecurityEvents':
        """Initialize a SecurityEvents object from a json dictionary."""
        args = {}
        if 'result' in _dict:
            args['result'] = [SecurityEventObject.from_dict(x) for x in _dict.get('result')]
        else:
            raise ValueError('Required property \'result\' not present in SecurityEvents JSON')
        if 'result_info' in _dict:
            args['result_info'] = ResultInfo.from_dict(_dict.get('result_info'))
        else:
            raise ValueError('Required property \'result_info\' not present in SecurityEvents JSON')
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in SecurityEvents JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in SecurityEvents JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in SecurityEvents JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SecurityEvents object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'result') and self.result is not None:
            _dict['result'] = [x.to_dict() for x in self.result]
        if hasattr(self, 'result_info') and self.result_info is not None:
            _dict['result_info'] = self.result_info.to_dict()
        if hasattr(self, 'success') and self.success is not None:
            _dict['success'] = self.success
        if hasattr(self, 'errors') and self.errors is not None:
            _dict['errors'] = self.errors
        if hasattr(self, 'messages') and self.messages is not None:
            _dict['messages'] = self.messages
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SecurityEvents object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SecurityEvents') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SecurityEvents') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
