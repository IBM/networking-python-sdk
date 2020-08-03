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
This document describes CIS Pagerule API.
"""

from enum import Enum
from typing import Dict, List
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_model

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################

class PageRuleApiV1(BaseService):
    """The Page Rule API V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.cis.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'page_rule_api'

    @classmethod
    def new_instance(cls,
                     crn: str,
                     zone_id: str,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'PageRuleApiV1':
        """
        Return a new client for the Page Rule API service using the specified
               parameters and external configuration.

        :param str crn: instance id.

        :param str zone_id: zone id.
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
        Construct a new client for the Page Rule API service.

        :param str crn: instance id.

        :param str zone_id: zone id.

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
    # Page Rules
    #########################


    def get_page_rule(self,
        rule_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get page rule.

        Get a page rule details.

        :param str rule_id: rule id.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PageRulesResponseWithoutResultInfo` object
        """

        if rule_id is None:
            raise ValueError('rule_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_page_rule')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/pagerules/{2}'.format(
            *self.encode_path_vars(self.crn, self.zone_id, rule_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def change_page_rule(self,
        rule_id: str,
        *,
        targets: List['TargetsItem'] = None,
        actions: List['PageRulesBodyActionsItem'] = None,
        priority: int = None,
        status: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Change page rule.

        Change a page rule.

        :param str rule_id: rule id.
        :param List[TargetsItem] targets: (optional) targets.
        :param List[PageRulesBodyActionsItem] actions: (optional) actions.
        :param int priority: (optional) priority.
        :param str status: (optional) status.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PageRulesResponseWithoutResultInfo` object
        """

        if rule_id is None:
            raise ValueError('rule_id must be provided')
        if targets is not None:
            targets = [convert_model(x) for x in targets]
        if actions is not None:
            actions = [convert_model(x) for x in actions]
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='change_page_rule')
        headers.update(sdk_headers)

        data = {
            'targets': targets,
            'actions': actions,
            'priority': priority,
            'status': status
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/pagerules/{2}'.format(
            *self.encode_path_vars(self.crn, self.zone_id, rule_id))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def update_page_rule(self,
        rule_id: str,
        *,
        targets: List['TargetsItem'] = None,
        actions: List['PageRulesBodyActionsItem'] = None,
        priority: int = None,
        status: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update page rule.

        Replace a page rule. The final rule will exactly match the data passed with this
        request.

        :param str rule_id: rule id.
        :param List[TargetsItem] targets: (optional) targets.
        :param List[PageRulesBodyActionsItem] actions: (optional) actions.
        :param int priority: (optional) priority.
        :param str status: (optional) status.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PageRulesResponseWithoutResultInfo` object
        """

        if rule_id is None:
            raise ValueError('rule_id must be provided')
        if targets is not None:
            targets = [convert_model(x) for x in targets]
        if actions is not None:
            actions = [convert_model(x) for x in actions]
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_page_rule')
        headers.update(sdk_headers)

        data = {
            'targets': targets,
            'actions': actions,
            'priority': priority,
            'status': status
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/pagerules/{2}'.format(
            *self.encode_path_vars(self.crn, self.zone_id, rule_id))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def delete_page_rule(self,
        rule_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete page rule.

        Delete a page rule.

        :param str rule_id: rule id.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PageRulesDeleteResponse` object
        """

        if rule_id is None:
            raise ValueError('rule_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_page_rule')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/pagerules/{2}'.format(
            *self.encode_path_vars(self.crn, self.zone_id, rule_id))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def list_page_rules(self,
        *,
        status: str = None,
        order: str = None,
        direction: str = None,
        match: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List page rules.

        List page rules.

        :param str status: (optional) default value: disabled. valid values:
               active, disabled.
        :param str order: (optional) default value: priority. valid values: status,
               priority.
        :param str direction: (optional) default value: desc. valid values: asc,
               desc.
        :param str match: (optional) default value: all. valid values: any, all.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PageRulesResponseListAll` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_page_rules')
        headers.update(sdk_headers)

        params = {
            'status': status,
            'order': order,
            'direction': direction,
            'match': match
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/pagerules'.format(
            *self.encode_path_vars(self.crn, self.zone_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def create_page_rule(self,
        *,
        targets: List['TargetsItem'] = None,
        actions: List['PageRulesBodyActionsItem'] = None,
        priority: int = None,
        status: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create page rule.

        Create a page rule.

        :param List[TargetsItem] targets: (optional) targets.
        :param List[PageRulesBodyActionsItem] actions: (optional) actions.
        :param int priority: (optional) priority.
        :param str status: (optional) status.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PageRulesResponseWithoutResultInfo` object
        """

        if targets is not None:
            targets = [convert_model(x) for x in targets]
        if actions is not None:
            actions = [convert_model(x) for x in actions]
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_page_rule')
        headers.update(sdk_headers)

        data = {
            'targets': targets,
            'actions': actions,
            'priority': priority,
            'status': status
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/pagerules'.format(
            *self.encode_path_vars(self.crn, self.zone_id))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


##############################################################################
# Models
##############################################################################


class PageRulesBodyActionsItem():
    """
    PageRulesBodyActionsItem.

    :attr str id: " Page rule action field map from UI to API
              CF-UI                    map             API,
          'Disable Security'           to        'disable_security',
          'Browser Integrity Check'    to        'browser_check',
          'Server Side Excludes'       to        'server_side_exclude',
          'SSL'                        to        'ssl',
          'Browser Cache TTL'          to        'browser_cache_ttl',
          'Security Level'             to        'security_level',
          'Cache Level'                to        'cache_level',
          'Edge Cache TTL'             to        'edge_cache_ttl'
          'IP Geolocation Header'      to        'ip_geolocation,
          'Email Obfuscation'          to        'email_obfuscation',
          'Automatic HTTPS Rewrites'   to        'automatic_https_rewrites',
          'Opportunistic Encryption'   to        'opportunistic_encryption',
          'Forwarding URL'             to        'forwarding_url',
          'Always Use HTTPS'           to        'always_use_https',
          'Origin Cache Control'       to        'explicit_cache_control',
          'Bypass Cache on Cookie'     to        'bypass_cache_on_cookie',
          'Cache Deception Armor'      to        'cache_deception_armor',
          'WAF'                        to        'waf'
                            Page rule conflict list
          "forwarding_url"             with     all other settings for the rules
          "always_use_https"           with     all other settings for the rules
          "disable_security"           with     "email_obfuscation",
          "server_side_exclude", "waf"
          ".
    :attr object value: (optional) value.
    """

    def __init__(self,
                 id: str,
                 *,
                 value: object = None) -> None:
        """
        Initialize a PageRulesBodyActionsItem object.

        :param str id: " Page rule action field map from UI to API
                   CF-UI                    map             API,
               'Disable Security'           to        'disable_security',
               'Browser Integrity Check'    to        'browser_check',
               'Server Side Excludes'       to        'server_side_exclude',
               'SSL'                        to        'ssl',
               'Browser Cache TTL'          to        'browser_cache_ttl',
               'Security Level'             to        'security_level',
               'Cache Level'                to        'cache_level',
               'Edge Cache TTL'             to        'edge_cache_ttl'
               'IP Geolocation Header'      to        'ip_geolocation,
               'Email Obfuscation'          to        'email_obfuscation',
               'Automatic HTTPS Rewrites'   to        'automatic_https_rewrites',
               'Opportunistic Encryption'   to        'opportunistic_encryption',
               'Forwarding URL'             to        'forwarding_url',
               'Always Use HTTPS'           to        'always_use_https',
               'Origin Cache Control'       to        'explicit_cache_control',
               'Bypass Cache on Cookie'     to        'bypass_cache_on_cookie',
               'Cache Deception Armor'      to        'cache_deception_armor',
               'WAF'                        to        'waf'
                                 Page rule conflict list
               "forwarding_url"             with     all other settings for the rules
               "always_use_https"           with     all other settings for the rules
               "disable_security"           with     "email_obfuscation",
               "server_side_exclude", "waf"
               ".
        :param object value: (optional) value.
        """
        self.id = id
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PageRulesBodyActionsItem':
        """Initialize a PageRulesBodyActionsItem object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in PageRulesBodyActionsItem JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PageRulesBodyActionsItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PageRulesBodyActionsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PageRulesBodyActionsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PageRulesBodyActionsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class IdEnum(str, Enum):
        """
        " Page rule action field map from UI to API
            CF-UI                    map             API,
        'Disable Security'           to        'disable_security',
        'Browser Integrity Check'    to        'browser_check',
        'Server Side Excludes'       to        'server_side_exclude',
        'SSL'                        to        'ssl',
        'Browser Cache TTL'          to        'browser_cache_ttl',
        'Security Level'             to        'security_level',
        'Cache Level'                to        'cache_level',
        'Edge Cache TTL'             to        'edge_cache_ttl'
        'IP Geolocation Header'      to        'ip_geolocation,
        'Email Obfuscation'          to        'email_obfuscation',
        'Automatic HTTPS Rewrites'   to        'automatic_https_rewrites',
        'Opportunistic Encryption'   to        'opportunistic_encryption',
        'Forwarding URL'             to        'forwarding_url',
        'Always Use HTTPS'           to        'always_use_https',
        'Origin Cache Control'       to        'explicit_cache_control',
        'Bypass Cache on Cookie'     to        'bypass_cache_on_cookie',
        'Cache Deception Armor'      to        'cache_deception_armor',
        'WAF'                        to        'waf'
                          Page rule conflict list
        "forwarding_url"             with     all other settings for the rules
        "always_use_https"           with     all other settings for the rules
        "disable_security"           with     "email_obfuscation", "server_side_exclude",
        "waf"
        ".
        """
        DISABLE_SECURITY = 'disable_security'
        BROWSER_CHECK = 'browser_check'
        SERVER_SIDE_EXCLUDE = 'server_side_exclude'
        SSL = 'ssl'
        BROWSER_CACHE_TTL = 'browser_cache_ttl'
        SECURITY_LEVEL = 'security_level'
        CACHE_LEVEL = 'cache_level'
        EDGE_CACHE_TTL = 'edge_cache_ttl'
        IP_GEOLOCATION = 'ip_geolocation'
        EMAIL_OBFUSCATION = 'email_obfuscation'
        AUTOMATIC_HTTPS_REWRITES = 'automatic_https_rewrites'
        OPPORTUNISTIC_ENCRYPTION = 'opportunistic_encryption'
        FORWARDING_URL = 'forwarding_url'
        ALWAYS_USE_HTTPS = 'always_use_https'
        EXPLICIT_CACHE_CONTROL = 'explicit_cache_control'
        BYPASS_CACHE_ON_COOKIE = 'bypass_cache_on_cookie'
        CACHE_DECEPTION_ARMOR = 'cache_deception_armor'
        WAF = 'waf'


class PageRulesDeleteResponseResult():
    """
    result.

    :attr str id: identifier.
    """

    def __init__(self,
                 id: str) -> None:
        """
        Initialize a PageRulesDeleteResponseResult object.

        :param str id: identifier.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PageRulesDeleteResponseResult':
        """Initialize a PageRulesDeleteResponseResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in PageRulesDeleteResponseResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PageRulesDeleteResponseResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PageRulesDeleteResponseResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PageRulesDeleteResponseResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PageRulesDeleteResponseResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class TargetsItem():
    """
    items.

    :attr str target: target.
    :attr TargetsItemConstraint constraint: constraint.
    """

    def __init__(self,
                 target: str,
                 constraint: 'TargetsItemConstraint') -> None:
        """
        Initialize a TargetsItem object.

        :param str target: target.
        :param TargetsItemConstraint constraint: constraint.
        """
        self.target = target
        self.constraint = constraint

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TargetsItem':
        """Initialize a TargetsItem object from a json dictionary."""
        args = {}
        if 'target' in _dict:
            args['target'] = _dict.get('target')
        else:
            raise ValueError('Required property \'target\' not present in TargetsItem JSON')
        if 'constraint' in _dict:
            args['constraint'] = TargetsItemConstraint.from_dict(_dict.get('constraint'))
        else:
            raise ValueError('Required property \'constraint\' not present in TargetsItem JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TargetsItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'target') and self.target is not None:
            _dict['target'] = self.target
        if hasattr(self, 'constraint') and self.constraint is not None:
            _dict['constraint'] = self.constraint.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TargetsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TargetsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TargetsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class TargetsItemConstraint():
    """
    constraint.

    :attr str operator: operator.
    :attr str value: value.
    """

    def __init__(self,
                 operator: str,
                 value: str) -> None:
        """
        Initialize a TargetsItemConstraint object.

        :param str operator: operator.
        :param str value: value.
        """
        self.operator = operator
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TargetsItemConstraint':
        """Initialize a TargetsItemConstraint object from a json dictionary."""
        args = {}
        if 'operator' in _dict:
            args['operator'] = _dict.get('operator')
        else:
            raise ValueError('Required property \'operator\' not present in TargetsItemConstraint JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in TargetsItemConstraint JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TargetsItemConstraint object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'operator') and self.operator is not None:
            _dict['operator'] = self.operator
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TargetsItemConstraint object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TargetsItemConstraint') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TargetsItemConstraint') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PageRulesDeleteResponse():
    """
    page rules delete response.

    :attr bool success: success.
    :attr List[List[str]] errors: errors.
    :attr List[List[str]] messages: messages.
    :attr PageRulesDeleteResponseResult result: result.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: 'PageRulesDeleteResponseResult') -> None:
        """
        Initialize a PageRulesDeleteResponse object.

        :param bool success: success.
        :param List[List[str]] errors: errors.
        :param List[List[str]] messages: messages.
        :param PageRulesDeleteResponseResult result: result.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PageRulesDeleteResponse':
        """Initialize a PageRulesDeleteResponse object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in PageRulesDeleteResponse JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in PageRulesDeleteResponse JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in PageRulesDeleteResponse JSON')
        if 'result' in _dict:
            args['result'] = PageRulesDeleteResponseResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in PageRulesDeleteResponse JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PageRulesDeleteResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'success') and self.success is not None:
            _dict['success'] = self.success
        if hasattr(self, 'errors') and self.errors is not None:
            _dict['errors'] = self.errors
        if hasattr(self, 'messages') and self.messages is not None:
            _dict['messages'] = self.messages
        if hasattr(self, 'result') and self.result is not None:
            _dict['result'] = self.result.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PageRulesDeleteResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PageRulesDeleteResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PageRulesDeleteResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PageRulesResponseListAll():
    """
    page rule response list all.

    :attr bool success: success.
    :attr List[List[str]] errors: errors.
    :attr List[List[str]] messages: messages.
    :attr List[PageRuleResult] result: result.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: List['PageRuleResult']) -> None:
        """
        Initialize a PageRulesResponseListAll object.

        :param bool success: success.
        :param List[List[str]] errors: errors.
        :param List[List[str]] messages: messages.
        :param List[PageRuleResult] result: result.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PageRulesResponseListAll':
        """Initialize a PageRulesResponseListAll object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in PageRulesResponseListAll JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in PageRulesResponseListAll JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in PageRulesResponseListAll JSON')
        if 'result' in _dict:
            args['result'] = [PageRuleResult.from_dict(x) for x in _dict.get('result')]
        else:
            raise ValueError('Required property \'result\' not present in PageRulesResponseListAll JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PageRulesResponseListAll object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'success') and self.success is not None:
            _dict['success'] = self.success
        if hasattr(self, 'errors') and self.errors is not None:
            _dict['errors'] = self.errors
        if hasattr(self, 'messages') and self.messages is not None:
            _dict['messages'] = self.messages
        if hasattr(self, 'result') and self.result is not None:
            _dict['result'] = [x.to_dict() for x in self.result]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PageRulesResponseListAll object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PageRulesResponseListAll') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PageRulesResponseListAll') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PageRulesResponseWithoutResultInfo():
    """
    page rule response without result information.

    :attr bool success: success.
    :attr List[List[str]] errors: errors.
    :attr List[List[str]] messages: messages.
    :attr PageRuleResult result: page rule result.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: 'PageRuleResult') -> None:
        """
        Initialize a PageRulesResponseWithoutResultInfo object.

        :param bool success: success.
        :param List[List[str]] errors: errors.
        :param List[List[str]] messages: messages.
        :param PageRuleResult result: page rule result.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PageRulesResponseWithoutResultInfo':
        """Initialize a PageRulesResponseWithoutResultInfo object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in PageRulesResponseWithoutResultInfo JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in PageRulesResponseWithoutResultInfo JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in PageRulesResponseWithoutResultInfo JSON')
        if 'result' in _dict:
            args['result'] = PageRuleResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in PageRulesResponseWithoutResultInfo JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PageRulesResponseWithoutResultInfo object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'success') and self.success is not None:
            _dict['success'] = self.success
        if hasattr(self, 'errors') and self.errors is not None:
            _dict['errors'] = self.errors
        if hasattr(self, 'messages') and self.messages is not None:
            _dict['messages'] = self.messages
        if hasattr(self, 'result') and self.result is not None:
            _dict['result'] = self.result.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PageRulesResponseWithoutResultInfo object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PageRulesResponseWithoutResultInfo') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PageRulesResponseWithoutResultInfo') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PageRuleResult():
    """
    page rule result.

    :attr str id: identifier.
    :attr List[TargetsItem] targets: targets.
    :attr List[PageRulesBodyActionsItem] actions: actions.
    :attr int priority: priority.
    :attr str status: status.
    :attr str modified_on: modified date.
    :attr str created_on: created date.
    """

    def __init__(self,
                 id: str,
                 targets: List['TargetsItem'],
                 actions: List['PageRulesBodyActionsItem'],
                 priority: int,
                 status: str,
                 modified_on: str,
                 created_on: str) -> None:
        """
        Initialize a PageRuleResult object.

        :param str id: identifier.
        :param List[TargetsItem] targets: targets.
        :param List[PageRulesBodyActionsItem] actions: actions.
        :param int priority: priority.
        :param str status: status.
        :param str modified_on: modified date.
        :param str created_on: created date.
        """
        self.id = id
        self.targets = targets
        self.actions = actions
        self.priority = priority
        self.status = status
        self.modified_on = modified_on
        self.created_on = created_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PageRuleResult':
        """Initialize a PageRuleResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in PageRuleResult JSON')
        if 'targets' in _dict:
            args['targets'] = [TargetsItem.from_dict(x) for x in _dict.get('targets')]
        else:
            raise ValueError('Required property \'targets\' not present in PageRuleResult JSON')
        if 'actions' in _dict:
            args['actions'] = [PageRulesBodyActionsItem.from_dict(x) for x in _dict.get('actions')]
        else:
            raise ValueError('Required property \'actions\' not present in PageRuleResult JSON')
        if 'priority' in _dict:
            args['priority'] = _dict.get('priority')
        else:
            raise ValueError('Required property \'priority\' not present in PageRuleResult JSON')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        else:
            raise ValueError('Required property \'status\' not present in PageRuleResult JSON')
        if 'modified_on' in _dict:
            args['modified_on'] = _dict.get('modified_on')
        else:
            raise ValueError('Required property \'modified_on\' not present in PageRuleResult JSON')
        if 'created_on' in _dict:
            args['created_on'] = _dict.get('created_on')
        else:
            raise ValueError('Required property \'created_on\' not present in PageRuleResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PageRuleResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'targets') and self.targets is not None:
            _dict['targets'] = [x.to_dict() for x in self.targets]
        if hasattr(self, 'actions') and self.actions is not None:
            _dict['actions'] = [x.to_dict() for x in self.actions]
        if hasattr(self, 'priority') and self.priority is not None:
            _dict['priority'] = self.priority
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'modified_on') and self.modified_on is not None:
            _dict['modified_on'] = self.modified_on
        if hasattr(self, 'created_on') and self.created_on is not None:
            _dict['created_on'] = self.created_on
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PageRuleResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PageRuleResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PageRuleResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
