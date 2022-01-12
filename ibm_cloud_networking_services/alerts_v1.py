# coding: utf-8

# (C) Copyright IBM Corp. 2022.
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

# IBM OpenAPI SDK Code Generator Version: 3.43.0-49eab5c7-20211117-152138
 
"""
CIS Alert Policies

API Version: 1.0.0
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

class AlertsV1(BaseService):
    """The Alerts V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.cis.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'alerts'

    @classmethod
    def new_instance(cls,
                     crn: str,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'AlertsV1':
        """
        Return a new client for the Alerts service using the specified parameters
               and external configuration.

        :param str crn: Full url-encoded CRN of the service instance.
        """
        if crn is None:
            raise ValueError('crn must be provided')

        authenticator = get_authenticator_from_environment(service_name)
        service = cls(
            crn,
            authenticator
            )
        service.configure_service(service_name)
        return service

    def __init__(self,
                 crn: str,
                 authenticator: Authenticator = None,
                ) -> None:
        """
        Construct a new client for the Alerts service.

        :param str crn: Full url-encoded CRN of the service instance.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/main/README.md
               about initializing the authenticator of your choice.
        """
        if crn is None:
            raise ValueError('crn must be provided')

        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)
        self.crn = crn


    #########################
    # Alert Policies
    #########################


    def get_alert_policies(self,
        **kwargs
    ) -> DetailedResponse:
        """
        List alert policies.

        List configured alert policies for the CIS instance.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListAlertPoliciesResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_alert_policies')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn']
        path_param_values = self.encode_path_vars(self.crn)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/alerting/policies'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def create_alert_policy(self,
        *,
        name: str = None,
        enabled: bool = None,
        alert_type: str = None,
        mechanisms: 'CreateAlertPolicyInputMechanisms' = None,
        description: str = None,
        filters: object = None,
        conditions: object = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create an alert policy.

        Create a new alert policy for the CIS instance.

        :param str name: (optional) Policy name.
        :param bool enabled: (optional) Is the alert policy active.
        :param str alert_type: (optional) Condition for the alert.
        :param CreateAlertPolicyInputMechanisms mechanisms: (optional) Delivery
               mechanisms for the alert.
        :param str description: (optional) Policy description.
        :param object filters: (optional) Optional filters depending for the alert
               type.
        :param object conditions: (optional) Conditions depending on the alert
               type. HTTP DDOS Attack Alerter does not have any conditions. The Load
               Balancing Pool Enablement Alerter takes conditions that describe for all
               pools whether the pool is being enabled, disabled, or both. This field is
               not required when creating a new alert.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AlertSuccessResp` object
        """

        if mechanisms is not None:
            mechanisms = convert_model(mechanisms)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_alert_policy')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'enabled': enabled,
            'alert_type': alert_type,
            'mechanisms': mechanisms,
            'description': description,
            'filters': filters,
            'conditions': conditions
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn']
        path_param_values = self.encode_path_vars(self.crn)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/alerting/policies'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def get_alert_policy(self,
        policy_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get an alert policy.

        Get an alert policy for the CIS instance.

        :param str policy_id: Alert policy identifier.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `GetAlertPolicyResp` object
        """

        if policy_id is None:
            raise ValueError('policy_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_alert_policy')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'policy_id']
        path_param_values = self.encode_path_vars(self.crn, policy_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/alerting/policies/{policy_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def update_alert_policy(self,
        policy_id: str,
        *,
        name: str = None,
        enabled: bool = None,
        alert_type: str = None,
        mechanisms: 'UpdateAlertPolicyInputMechanisms' = None,
        conditions: object = None,
        description: str = None,
        filters: object = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update an alert policy.

        Update an existing alert policy for the CIS instance.

        :param str policy_id: Alert policy identifier.
        :param str name: (optional) Policy name.
        :param bool enabled: (optional) Is the alert policy active.
        :param str alert_type: (optional) Condition for the alert. Use
               'dos_attack_l7' to set up an HTTP DDOS Attack Alerter, use
               'g6_pool_toggle_alert' to set up Load Balancing Pool Enablement Alerter,
               use 'clickhouse_alert_fw_anomaly' to set up WAF Alerter and
               'clickhouse_alert_fw_ent_anomaly' to set up Advanced Security Alerter.
        :param UpdateAlertPolicyInputMechanisms mechanisms: (optional) Delivery
               mechanisms for the alert, can include an email, a webhook, or both.
        :param object conditions: (optional) Conditions depending on the alert
               type. HTTP DDOS Attack Alerter does not have any conditions. The Load
               Balancing Pool Enablement Alerter takes conditions that describe for all
               pools whether the pool is being enabled, disabled, or both.
        :param str description: (optional) Policy description.
        :param object filters: (optional) Optional filters depending for the alert
               type. HTTP DDOS Attack Alerter does not require any filters. The Load
               Balancing Pool Enablement Alerter requires a list of IDs for the pools and
               their corresponding alert trigger (set whether alerts are recieved on
               disablement, enablement, or both). The basic WAF Alerter requires a list of
               zones to be monitored. The Advanced Security Alerter requires a list of
               zones to be monitored as well as a list of services to monitor.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AlertSuccessResp` object
        """

        if policy_id is None:
            raise ValueError('policy_id must be provided')
        if mechanisms is not None:
            mechanisms = convert_model(mechanisms)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_alert_policy')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'enabled': enabled,
            'alert_type': alert_type,
            'mechanisms': mechanisms,
            'conditions': conditions,
            'description': description,
            'filters': filters
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'policy_id']
        path_param_values = self.encode_path_vars(self.crn, policy_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/alerting/policies/{policy_id}'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def delete_alert_policy(self,
        policy_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete an alert policy.

        Delete an alert policy for the CIS instance.

        :param str policy_id: Alert policy identifier.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AlertSuccessResp` object
        """

        if policy_id is None:
            raise ValueError('policy_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_alert_policy')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'policy_id']
        path_param_values = self.encode_path_vars(self.crn, policy_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/alerting/policies/{policy_id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


##############################################################################
# Models
##############################################################################


class AlertSuccessRespErrorsItem():
    """
    AlertSuccessRespErrorsItem.

    :attr str id: (optional)
    """

    def __init__(self,
                 *,
                 id: str = None) -> None:
        """
        Initialize a AlertSuccessRespErrorsItem object.

        :param str id: (optional)
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AlertSuccessRespErrorsItem':
        """Initialize a AlertSuccessRespErrorsItem object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AlertSuccessRespErrorsItem object from a json dictionary."""
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
        """Return a `str` version of this AlertSuccessRespErrorsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AlertSuccessRespErrorsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AlertSuccessRespErrorsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class AlertSuccessRespMessagesItem():
    """
    AlertSuccessRespMessagesItem.

    :attr str id: (optional)
    """

    def __init__(self,
                 *,
                 id: str = None) -> None:
        """
        Initialize a AlertSuccessRespMessagesItem object.

        :param str id: (optional)
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AlertSuccessRespMessagesItem':
        """Initialize a AlertSuccessRespMessagesItem object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AlertSuccessRespMessagesItem object from a json dictionary."""
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
        """Return a `str` version of this AlertSuccessRespMessagesItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AlertSuccessRespMessagesItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AlertSuccessRespMessagesItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class AlertSuccessRespResult():
    """
    Container for response information.

    :attr str id: Policy ID.
    """

    def __init__(self,
                 id: str) -> None:
        """
        Initialize a AlertSuccessRespResult object.

        :param str id: Policy ID.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AlertSuccessRespResult':
        """Initialize a AlertSuccessRespResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in AlertSuccessRespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AlertSuccessRespResult object from a json dictionary."""
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
        """Return a `str` version of this AlertSuccessRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AlertSuccessRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AlertSuccessRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class CreateAlertPolicyInputMechanisms():
    """
    Delivery mechanisms for the alert.

    :attr List[CreateAlertPolicyInputMechanismsEmailItem] email: (optional)
    :attr List[CreateAlertPolicyInputMechanismsWebhooksItem] webhooks: (optional)
    """

    def __init__(self,
                 *,
                 email: List['CreateAlertPolicyInputMechanismsEmailItem'] = None,
                 webhooks: List['CreateAlertPolicyInputMechanismsWebhooksItem'] = None) -> None:
        """
        Initialize a CreateAlertPolicyInputMechanisms object.

        :param List[CreateAlertPolicyInputMechanismsEmailItem] email: (optional)
        :param List[CreateAlertPolicyInputMechanismsWebhooksItem] webhooks:
               (optional)
        """
        self.email = email
        self.webhooks = webhooks

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CreateAlertPolicyInputMechanisms':
        """Initialize a CreateAlertPolicyInputMechanisms object from a json dictionary."""
        args = {}
        if 'email' in _dict:
            args['email'] = [CreateAlertPolicyInputMechanismsEmailItem.from_dict(x) for x in _dict.get('email')]
        if 'webhooks' in _dict:
            args['webhooks'] = [CreateAlertPolicyInputMechanismsWebhooksItem.from_dict(x) for x in _dict.get('webhooks')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CreateAlertPolicyInputMechanisms object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'email') and self.email is not None:
            _dict['email'] = [x.to_dict() for x in self.email]
        if hasattr(self, 'webhooks') and self.webhooks is not None:
            _dict['webhooks'] = [x.to_dict() for x in self.webhooks]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CreateAlertPolicyInputMechanisms object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CreateAlertPolicyInputMechanisms') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CreateAlertPolicyInputMechanisms') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class CreateAlertPolicyInputMechanismsEmailItem():
    """
    CreateAlertPolicyInputMechanismsEmailItem.

    :attr str id: (optional)
    """

    def __init__(self,
                 *,
                 id: str = None) -> None:
        """
        Initialize a CreateAlertPolicyInputMechanismsEmailItem object.

        :param str id: (optional)
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CreateAlertPolicyInputMechanismsEmailItem':
        """Initialize a CreateAlertPolicyInputMechanismsEmailItem object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CreateAlertPolicyInputMechanismsEmailItem object from a json dictionary."""
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
        """Return a `str` version of this CreateAlertPolicyInputMechanismsEmailItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CreateAlertPolicyInputMechanismsEmailItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CreateAlertPolicyInputMechanismsEmailItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class CreateAlertPolicyInputMechanismsWebhooksItem():
    """
    CreateAlertPolicyInputMechanismsWebhooksItem.

    :attr str id: (optional)
    """

    def __init__(self,
                 *,
                 id: str = None) -> None:
        """
        Initialize a CreateAlertPolicyInputMechanismsWebhooksItem object.

        :param str id: (optional)
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CreateAlertPolicyInputMechanismsWebhooksItem':
        """Initialize a CreateAlertPolicyInputMechanismsWebhooksItem object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CreateAlertPolicyInputMechanismsWebhooksItem object from a json dictionary."""
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
        """Return a `str` version of this CreateAlertPolicyInputMechanismsWebhooksItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CreateAlertPolicyInputMechanismsWebhooksItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CreateAlertPolicyInputMechanismsWebhooksItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class GetAlertPolicyRespErrorsItem():
    """
    GetAlertPolicyRespErrorsItem.

    :attr str id: (optional)
    """

    def __init__(self,
                 *,
                 id: str = None) -> None:
        """
        Initialize a GetAlertPolicyRespErrorsItem object.

        :param str id: (optional)
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'GetAlertPolicyRespErrorsItem':
        """Initialize a GetAlertPolicyRespErrorsItem object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a GetAlertPolicyRespErrorsItem object from a json dictionary."""
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
        """Return a `str` version of this GetAlertPolicyRespErrorsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'GetAlertPolicyRespErrorsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'GetAlertPolicyRespErrorsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class GetAlertPolicyRespMessagesItem():
    """
    GetAlertPolicyRespMessagesItem.

    :attr str id: (optional)
    """

    def __init__(self,
                 *,
                 id: str = None) -> None:
        """
        Initialize a GetAlertPolicyRespMessagesItem object.

        :param str id: (optional)
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'GetAlertPolicyRespMessagesItem':
        """Initialize a GetAlertPolicyRespMessagesItem object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a GetAlertPolicyRespMessagesItem object from a json dictionary."""
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
        """Return a `str` version of this GetAlertPolicyRespMessagesItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'GetAlertPolicyRespMessagesItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'GetAlertPolicyRespMessagesItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class GetAlertPolicyRespResult():
    """
    Container for response information.

    :attr str id: Policy ID.
    :attr str name: Policy Name.
    :attr str description: Alert Policy description.
    :attr bool enabled: Is the alert enabled.
    :attr str alert_type: Condition for the alert.
    :attr GetAlertPolicyRespResultMechanisms mechanisms: Delivery mechanisms for the
          alert, can include an email, a webhook, or both.
    :attr str created: When was the policy first created.
    :attr str modified: When was the policy last modified.
    :attr object conditions: Optional conditions depending for the alert type.
    :attr object filters: Optional filters depending for the alert type.
    """

    def __init__(self,
                 id: str,
                 name: str,
                 description: str,
                 enabled: bool,
                 alert_type: str,
                 mechanisms: 'GetAlertPolicyRespResultMechanisms',
                 created: str,
                 modified: str,
                 conditions: object,
                 filters: object) -> None:
        """
        Initialize a GetAlertPolicyRespResult object.

        :param str id: Policy ID.
        :param str name: Policy Name.
        :param str description: Alert Policy description.
        :param bool enabled: Is the alert enabled.
        :param str alert_type: Condition for the alert.
        :param GetAlertPolicyRespResultMechanisms mechanisms: Delivery mechanisms
               for the alert, can include an email, a webhook, or both.
        :param str created: When was the policy first created.
        :param str modified: When was the policy last modified.
        :param object conditions: Optional conditions depending for the alert type.
        :param object filters: Optional filters depending for the alert type.
        """
        self.id = id
        self.name = name
        self.description = description
        self.enabled = enabled
        self.alert_type = alert_type
        self.mechanisms = mechanisms
        self.created = created
        self.modified = modified
        self.conditions = conditions
        self.filters = filters

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'GetAlertPolicyRespResult':
        """Initialize a GetAlertPolicyRespResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in GetAlertPolicyRespResult JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in GetAlertPolicyRespResult JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        else:
            raise ValueError('Required property \'description\' not present in GetAlertPolicyRespResult JSON')
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        else:
            raise ValueError('Required property \'enabled\' not present in GetAlertPolicyRespResult JSON')
        if 'alert_type' in _dict:
            args['alert_type'] = _dict.get('alert_type')
        else:
            raise ValueError('Required property \'alert_type\' not present in GetAlertPolicyRespResult JSON')
        if 'mechanisms' in _dict:
            args['mechanisms'] = GetAlertPolicyRespResultMechanisms.from_dict(_dict.get('mechanisms'))
        else:
            raise ValueError('Required property \'mechanisms\' not present in GetAlertPolicyRespResult JSON')
        if 'created' in _dict:
            args['created'] = _dict.get('created')
        else:
            raise ValueError('Required property \'created\' not present in GetAlertPolicyRespResult JSON')
        if 'modified' in _dict:
            args['modified'] = _dict.get('modified')
        else:
            raise ValueError('Required property \'modified\' not present in GetAlertPolicyRespResult JSON')
        if 'conditions' in _dict:
            args['conditions'] = _dict.get('conditions')
        else:
            raise ValueError('Required property \'conditions\' not present in GetAlertPolicyRespResult JSON')
        if 'filters' in _dict:
            args['filters'] = _dict.get('filters')
        else:
            raise ValueError('Required property \'filters\' not present in GetAlertPolicyRespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a GetAlertPolicyRespResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'alert_type') and self.alert_type is not None:
            _dict['alert_type'] = self.alert_type
        if hasattr(self, 'mechanisms') and self.mechanisms is not None:
            _dict['mechanisms'] = self.mechanisms.to_dict()
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = self.created
        if hasattr(self, 'modified') and self.modified is not None:
            _dict['modified'] = self.modified
        if hasattr(self, 'conditions') and self.conditions is not None:
            _dict['conditions'] = self.conditions
        if hasattr(self, 'filters') and self.filters is not None:
            _dict['filters'] = self.filters
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this GetAlertPolicyRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'GetAlertPolicyRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'GetAlertPolicyRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class AlertTypeEnum(str, Enum):
        """
        Condition for the alert.
        """
        DOS_ATTACK_L7 = 'dos_attack_l7'
        G6_POOL_TOGGLE_ALERT = 'g6_pool_toggle_alert'
        CLICKHOUSE_ALERT_FW_ANOMALY = 'clickhouse_alert_fw_anomaly'
        CLICKHOUSE_ALERT_FW_ENT_ANOMALY = 'clickhouse_alert_fw_ent_anomaly'


class GetAlertPolicyRespResultMechanisms():
    """
    Delivery mechanisms for the alert, can include an email, a webhook, or both.

    :attr List[GetAlertPolicyRespResultMechanismsEmailItem] email: (optional)
    :attr List[GetAlertPolicyRespResultMechanismsWebhooksItem] webhooks: (optional)
    """

    def __init__(self,
                 *,
                 email: List['GetAlertPolicyRespResultMechanismsEmailItem'] = None,
                 webhooks: List['GetAlertPolicyRespResultMechanismsWebhooksItem'] = None) -> None:
        """
        Initialize a GetAlertPolicyRespResultMechanisms object.

        :param List[GetAlertPolicyRespResultMechanismsEmailItem] email: (optional)
        :param List[GetAlertPolicyRespResultMechanismsWebhooksItem] webhooks:
               (optional)
        """
        self.email = email
        self.webhooks = webhooks

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'GetAlertPolicyRespResultMechanisms':
        """Initialize a GetAlertPolicyRespResultMechanisms object from a json dictionary."""
        args = {}
        if 'email' in _dict:
            args['email'] = [GetAlertPolicyRespResultMechanismsEmailItem.from_dict(x) for x in _dict.get('email')]
        if 'webhooks' in _dict:
            args['webhooks'] = [GetAlertPolicyRespResultMechanismsWebhooksItem.from_dict(x) for x in _dict.get('webhooks')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a GetAlertPolicyRespResultMechanisms object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'email') and self.email is not None:
            _dict['email'] = [x.to_dict() for x in self.email]
        if hasattr(self, 'webhooks') and self.webhooks is not None:
            _dict['webhooks'] = [x.to_dict() for x in self.webhooks]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this GetAlertPolicyRespResultMechanisms object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'GetAlertPolicyRespResultMechanisms') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'GetAlertPolicyRespResultMechanisms') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class GetAlertPolicyRespResultMechanismsEmailItem():
    """
    GetAlertPolicyRespResultMechanismsEmailItem.

    :attr str id: (optional)
    """

    def __init__(self,
                 *,
                 id: str = None) -> None:
        """
        Initialize a GetAlertPolicyRespResultMechanismsEmailItem object.

        :param str id: (optional)
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'GetAlertPolicyRespResultMechanismsEmailItem':
        """Initialize a GetAlertPolicyRespResultMechanismsEmailItem object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a GetAlertPolicyRespResultMechanismsEmailItem object from a json dictionary."""
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
        """Return a `str` version of this GetAlertPolicyRespResultMechanismsEmailItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'GetAlertPolicyRespResultMechanismsEmailItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'GetAlertPolicyRespResultMechanismsEmailItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class GetAlertPolicyRespResultMechanismsWebhooksItem():
    """
    GetAlertPolicyRespResultMechanismsWebhooksItem.

    :attr str id: (optional)
    """

    def __init__(self,
                 *,
                 id: str = None) -> None:
        """
        Initialize a GetAlertPolicyRespResultMechanismsWebhooksItem object.

        :param str id: (optional)
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'GetAlertPolicyRespResultMechanismsWebhooksItem':
        """Initialize a GetAlertPolicyRespResultMechanismsWebhooksItem object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a GetAlertPolicyRespResultMechanismsWebhooksItem object from a json dictionary."""
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
        """Return a `str` version of this GetAlertPolicyRespResultMechanismsWebhooksItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'GetAlertPolicyRespResultMechanismsWebhooksItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'GetAlertPolicyRespResultMechanismsWebhooksItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ListAlertPoliciesRespErrorsItem():
    """
    ListAlertPoliciesRespErrorsItem.

    :attr str id: (optional)
    """

    def __init__(self,
                 *,
                 id: str = None) -> None:
        """
        Initialize a ListAlertPoliciesRespErrorsItem object.

        :param str id: (optional)
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListAlertPoliciesRespErrorsItem':
        """Initialize a ListAlertPoliciesRespErrorsItem object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListAlertPoliciesRespErrorsItem object from a json dictionary."""
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
        """Return a `str` version of this ListAlertPoliciesRespErrorsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListAlertPoliciesRespErrorsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListAlertPoliciesRespErrorsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ListAlertPoliciesRespMessagesItem():
    """
    ListAlertPoliciesRespMessagesItem.

    :attr str id: (optional)
    """

    def __init__(self,
                 *,
                 id: str = None) -> None:
        """
        Initialize a ListAlertPoliciesRespMessagesItem object.

        :param str id: (optional)
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListAlertPoliciesRespMessagesItem':
        """Initialize a ListAlertPoliciesRespMessagesItem object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListAlertPoliciesRespMessagesItem object from a json dictionary."""
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
        """Return a `str` version of this ListAlertPoliciesRespMessagesItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListAlertPoliciesRespMessagesItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListAlertPoliciesRespMessagesItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ListAlertPoliciesRespResultItem():
    """
    ListAlertPoliciesRespResultItem.

    :attr str id: Policy ID.
    :attr str name: Policy Name.
    :attr str description: Alert Policy description.
    :attr bool enabled: Is the alert enabled.
    :attr str alert_type: Condition for the alert.
    :attr ListAlertPoliciesRespResultItemMechanisms mechanisms: Delivery mechanisms
          for the alert, can include an email, a webhook, or both.
    :attr str created: When was the policy first created.
    :attr str modified: When was the policy last modified.
    :attr object conditions: Optional conditions depending for the alert type.
    :attr object filters: Optional filters depending for the alert type.
    """

    def __init__(self,
                 id: str,
                 name: str,
                 description: str,
                 enabled: bool,
                 alert_type: str,
                 mechanisms: 'ListAlertPoliciesRespResultItemMechanisms',
                 created: str,
                 modified: str,
                 conditions: object,
                 filters: object) -> None:
        """
        Initialize a ListAlertPoliciesRespResultItem object.

        :param str id: Policy ID.
        :param str name: Policy Name.
        :param str description: Alert Policy description.
        :param bool enabled: Is the alert enabled.
        :param str alert_type: Condition for the alert.
        :param ListAlertPoliciesRespResultItemMechanisms mechanisms: Delivery
               mechanisms for the alert, can include an email, a webhook, or both.
        :param str created: When was the policy first created.
        :param str modified: When was the policy last modified.
        :param object conditions: Optional conditions depending for the alert type.
        :param object filters: Optional filters depending for the alert type.
        """
        self.id = id
        self.name = name
        self.description = description
        self.enabled = enabled
        self.alert_type = alert_type
        self.mechanisms = mechanisms
        self.created = created
        self.modified = modified
        self.conditions = conditions
        self.filters = filters

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListAlertPoliciesRespResultItem':
        """Initialize a ListAlertPoliciesRespResultItem object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in ListAlertPoliciesRespResultItem JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in ListAlertPoliciesRespResultItem JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        else:
            raise ValueError('Required property \'description\' not present in ListAlertPoliciesRespResultItem JSON')
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        else:
            raise ValueError('Required property \'enabled\' not present in ListAlertPoliciesRespResultItem JSON')
        if 'alert_type' in _dict:
            args['alert_type'] = _dict.get('alert_type')
        else:
            raise ValueError('Required property \'alert_type\' not present in ListAlertPoliciesRespResultItem JSON')
        if 'mechanisms' in _dict:
            args['mechanisms'] = ListAlertPoliciesRespResultItemMechanisms.from_dict(_dict.get('mechanisms'))
        else:
            raise ValueError('Required property \'mechanisms\' not present in ListAlertPoliciesRespResultItem JSON')
        if 'created' in _dict:
            args['created'] = _dict.get('created')
        else:
            raise ValueError('Required property \'created\' not present in ListAlertPoliciesRespResultItem JSON')
        if 'modified' in _dict:
            args['modified'] = _dict.get('modified')
        else:
            raise ValueError('Required property \'modified\' not present in ListAlertPoliciesRespResultItem JSON')
        if 'conditions' in _dict:
            args['conditions'] = _dict.get('conditions')
        else:
            raise ValueError('Required property \'conditions\' not present in ListAlertPoliciesRespResultItem JSON')
        if 'filters' in _dict:
            args['filters'] = _dict.get('filters')
        else:
            raise ValueError('Required property \'filters\' not present in ListAlertPoliciesRespResultItem JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListAlertPoliciesRespResultItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'alert_type') and self.alert_type is not None:
            _dict['alert_type'] = self.alert_type
        if hasattr(self, 'mechanisms') and self.mechanisms is not None:
            _dict['mechanisms'] = self.mechanisms.to_dict()
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = self.created
        if hasattr(self, 'modified') and self.modified is not None:
            _dict['modified'] = self.modified
        if hasattr(self, 'conditions') and self.conditions is not None:
            _dict['conditions'] = self.conditions
        if hasattr(self, 'filters') and self.filters is not None:
            _dict['filters'] = self.filters
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListAlertPoliciesRespResultItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListAlertPoliciesRespResultItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListAlertPoliciesRespResultItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class AlertTypeEnum(str, Enum):
        """
        Condition for the alert.
        """
        DOS_ATTACK_L7 = 'dos_attack_l7'
        G6_POOL_TOGGLE_ALERT = 'g6_pool_toggle_alert'
        CLICKHOUSE_ALERT_FW_ANOMALY = 'clickhouse_alert_fw_anomaly'
        CLICKHOUSE_ALERT_FW_ENT_ANOMALY = 'clickhouse_alert_fw_ent_anomaly'


class ListAlertPoliciesRespResultItemMechanisms():
    """
    Delivery mechanisms for the alert, can include an email, a webhook, or both.

    :attr List[ListAlertPoliciesRespResultItemMechanismsEmailItem] email: (optional)
    :attr List[ListAlertPoliciesRespResultItemMechanismsWebhooksItem] webhooks:
          (optional)
    """

    def __init__(self,
                 *,
                 email: List['ListAlertPoliciesRespResultItemMechanismsEmailItem'] = None,
                 webhooks: List['ListAlertPoliciesRespResultItemMechanismsWebhooksItem'] = None) -> None:
        """
        Initialize a ListAlertPoliciesRespResultItemMechanisms object.

        :param List[ListAlertPoliciesRespResultItemMechanismsEmailItem] email:
               (optional)
        :param List[ListAlertPoliciesRespResultItemMechanismsWebhooksItem]
               webhooks: (optional)
        """
        self.email = email
        self.webhooks = webhooks

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListAlertPoliciesRespResultItemMechanisms':
        """Initialize a ListAlertPoliciesRespResultItemMechanisms object from a json dictionary."""
        args = {}
        if 'email' in _dict:
            args['email'] = [ListAlertPoliciesRespResultItemMechanismsEmailItem.from_dict(x) for x in _dict.get('email')]
        if 'webhooks' in _dict:
            args['webhooks'] = [ListAlertPoliciesRespResultItemMechanismsWebhooksItem.from_dict(x) for x in _dict.get('webhooks')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListAlertPoliciesRespResultItemMechanisms object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'email') and self.email is not None:
            _dict['email'] = [x.to_dict() for x in self.email]
        if hasattr(self, 'webhooks') and self.webhooks is not None:
            _dict['webhooks'] = [x.to_dict() for x in self.webhooks]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListAlertPoliciesRespResultItemMechanisms object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListAlertPoliciesRespResultItemMechanisms') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListAlertPoliciesRespResultItemMechanisms') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ListAlertPoliciesRespResultItemMechanismsEmailItem():
    """
    ListAlertPoliciesRespResultItemMechanismsEmailItem.

    :attr str id: (optional)
    """

    def __init__(self,
                 *,
                 id: str = None) -> None:
        """
        Initialize a ListAlertPoliciesRespResultItemMechanismsEmailItem object.

        :param str id: (optional)
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListAlertPoliciesRespResultItemMechanismsEmailItem':
        """Initialize a ListAlertPoliciesRespResultItemMechanismsEmailItem object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListAlertPoliciesRespResultItemMechanismsEmailItem object from a json dictionary."""
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
        """Return a `str` version of this ListAlertPoliciesRespResultItemMechanismsEmailItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListAlertPoliciesRespResultItemMechanismsEmailItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListAlertPoliciesRespResultItemMechanismsEmailItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ListAlertPoliciesRespResultItemMechanismsWebhooksItem():
    """
    ListAlertPoliciesRespResultItemMechanismsWebhooksItem.

    :attr str id: (optional)
    """

    def __init__(self,
                 *,
                 id: str = None) -> None:
        """
        Initialize a ListAlertPoliciesRespResultItemMechanismsWebhooksItem object.

        :param str id: (optional)
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListAlertPoliciesRespResultItemMechanismsWebhooksItem':
        """Initialize a ListAlertPoliciesRespResultItemMechanismsWebhooksItem object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListAlertPoliciesRespResultItemMechanismsWebhooksItem object from a json dictionary."""
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
        """Return a `str` version of this ListAlertPoliciesRespResultItemMechanismsWebhooksItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListAlertPoliciesRespResultItemMechanismsWebhooksItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListAlertPoliciesRespResultItemMechanismsWebhooksItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class UpdateAlertPolicyInputMechanisms():
    """
    Delivery mechanisms for the alert, can include an email, a webhook, or both.

    :attr List[UpdateAlertPolicyInputMechanismsEmailItem] email: (optional)
    :attr List[UpdateAlertPolicyInputMechanismsWebhooksItem] webhooks: (optional)
    """

    def __init__(self,
                 *,
                 email: List['UpdateAlertPolicyInputMechanismsEmailItem'] = None,
                 webhooks: List['UpdateAlertPolicyInputMechanismsWebhooksItem'] = None) -> None:
        """
        Initialize a UpdateAlertPolicyInputMechanisms object.

        :param List[UpdateAlertPolicyInputMechanismsEmailItem] email: (optional)
        :param List[UpdateAlertPolicyInputMechanismsWebhooksItem] webhooks:
               (optional)
        """
        self.email = email
        self.webhooks = webhooks

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'UpdateAlertPolicyInputMechanisms':
        """Initialize a UpdateAlertPolicyInputMechanisms object from a json dictionary."""
        args = {}
        if 'email' in _dict:
            args['email'] = [UpdateAlertPolicyInputMechanismsEmailItem.from_dict(x) for x in _dict.get('email')]
        if 'webhooks' in _dict:
            args['webhooks'] = [UpdateAlertPolicyInputMechanismsWebhooksItem.from_dict(x) for x in _dict.get('webhooks')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a UpdateAlertPolicyInputMechanisms object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'email') and self.email is not None:
            _dict['email'] = [x.to_dict() for x in self.email]
        if hasattr(self, 'webhooks') and self.webhooks is not None:
            _dict['webhooks'] = [x.to_dict() for x in self.webhooks]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this UpdateAlertPolicyInputMechanisms object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'UpdateAlertPolicyInputMechanisms') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'UpdateAlertPolicyInputMechanisms') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class UpdateAlertPolicyInputMechanismsEmailItem():
    """
    UpdateAlertPolicyInputMechanismsEmailItem.

    :attr str id: (optional)
    """

    def __init__(self,
                 *,
                 id: str = None) -> None:
        """
        Initialize a UpdateAlertPolicyInputMechanismsEmailItem object.

        :param str id: (optional)
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'UpdateAlertPolicyInputMechanismsEmailItem':
        """Initialize a UpdateAlertPolicyInputMechanismsEmailItem object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a UpdateAlertPolicyInputMechanismsEmailItem object from a json dictionary."""
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
        """Return a `str` version of this UpdateAlertPolicyInputMechanismsEmailItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'UpdateAlertPolicyInputMechanismsEmailItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'UpdateAlertPolicyInputMechanismsEmailItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class UpdateAlertPolicyInputMechanismsWebhooksItem():
    """
    UpdateAlertPolicyInputMechanismsWebhooksItem.

    :attr str id: (optional)
    """

    def __init__(self,
                 *,
                 id: str = None) -> None:
        """
        Initialize a UpdateAlertPolicyInputMechanismsWebhooksItem object.

        :param str id: (optional)
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'UpdateAlertPolicyInputMechanismsWebhooksItem':
        """Initialize a UpdateAlertPolicyInputMechanismsWebhooksItem object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a UpdateAlertPolicyInputMechanismsWebhooksItem object from a json dictionary."""
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
        """Return a `str` version of this UpdateAlertPolicyInputMechanismsWebhooksItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'UpdateAlertPolicyInputMechanismsWebhooksItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'UpdateAlertPolicyInputMechanismsWebhooksItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class AlertSuccessResp():
    """
    Alert Policies Response.

    :attr bool success: Was operation successful.
    :attr List[AlertSuccessRespErrorsItem] errors: Array of errors encountered.
    :attr List[AlertSuccessRespMessagesItem] messages: Array of messages returned.
    :attr AlertSuccessRespResult result: Container for response information.
    """

    def __init__(self,
                 success: bool,
                 errors: List['AlertSuccessRespErrorsItem'],
                 messages: List['AlertSuccessRespMessagesItem'],
                 result: 'AlertSuccessRespResult') -> None:
        """
        Initialize a AlertSuccessResp object.

        :param bool success: Was operation successful.
        :param List[AlertSuccessRespErrorsItem] errors: Array of errors
               encountered.
        :param List[AlertSuccessRespMessagesItem] messages: Array of messages
               returned.
        :param AlertSuccessRespResult result: Container for response information.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AlertSuccessResp':
        """Initialize a AlertSuccessResp object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in AlertSuccessResp JSON')
        if 'errors' in _dict:
            args['errors'] = [AlertSuccessRespErrorsItem.from_dict(x) for x in _dict.get('errors')]
        else:
            raise ValueError('Required property \'errors\' not present in AlertSuccessResp JSON')
        if 'messages' in _dict:
            args['messages'] = [AlertSuccessRespMessagesItem.from_dict(x) for x in _dict.get('messages')]
        else:
            raise ValueError('Required property \'messages\' not present in AlertSuccessResp JSON')
        if 'result' in _dict:
            args['result'] = AlertSuccessRespResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in AlertSuccessResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AlertSuccessResp object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'success') and self.success is not None:
            _dict['success'] = self.success
        if hasattr(self, 'errors') and self.errors is not None:
            _dict['errors'] = [x.to_dict() for x in self.errors]
        if hasattr(self, 'messages') and self.messages is not None:
            _dict['messages'] = [x.to_dict() for x in self.messages]
        if hasattr(self, 'result') and self.result is not None:
            _dict['result'] = self.result.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AlertSuccessResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AlertSuccessResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AlertSuccessResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class GetAlertPolicyResp():
    """
    Get Alert Policies Response.

    :attr bool success: Was operation successful.
    :attr List[GetAlertPolicyRespErrorsItem] errors: Array of errors encountered.
    :attr List[GetAlertPolicyRespMessagesItem] messages: Array of messages returned.
    :attr GetAlertPolicyRespResult result: Container for response information.
    """

    def __init__(self,
                 success: bool,
                 errors: List['GetAlertPolicyRespErrorsItem'],
                 messages: List['GetAlertPolicyRespMessagesItem'],
                 result: 'GetAlertPolicyRespResult') -> None:
        """
        Initialize a GetAlertPolicyResp object.

        :param bool success: Was operation successful.
        :param List[GetAlertPolicyRespErrorsItem] errors: Array of errors
               encountered.
        :param List[GetAlertPolicyRespMessagesItem] messages: Array of messages
               returned.
        :param GetAlertPolicyRespResult result: Container for response information.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'GetAlertPolicyResp':
        """Initialize a GetAlertPolicyResp object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in GetAlertPolicyResp JSON')
        if 'errors' in _dict:
            args['errors'] = [GetAlertPolicyRespErrorsItem.from_dict(x) for x in _dict.get('errors')]
        else:
            raise ValueError('Required property \'errors\' not present in GetAlertPolicyResp JSON')
        if 'messages' in _dict:
            args['messages'] = [GetAlertPolicyRespMessagesItem.from_dict(x) for x in _dict.get('messages')]
        else:
            raise ValueError('Required property \'messages\' not present in GetAlertPolicyResp JSON')
        if 'result' in _dict:
            args['result'] = GetAlertPolicyRespResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in GetAlertPolicyResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a GetAlertPolicyResp object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'success') and self.success is not None:
            _dict['success'] = self.success
        if hasattr(self, 'errors') and self.errors is not None:
            _dict['errors'] = [x.to_dict() for x in self.errors]
        if hasattr(self, 'messages') and self.messages is not None:
            _dict['messages'] = [x.to_dict() for x in self.messages]
        if hasattr(self, 'result') and self.result is not None:
            _dict['result'] = self.result.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this GetAlertPolicyResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'GetAlertPolicyResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'GetAlertPolicyResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ListAlertPoliciesResp():
    """
    List Alert Policies Response.

    :attr bool success: Was operation successful.
    :attr List[ListAlertPoliciesRespErrorsItem] errors: Array of errors encountered.
    :attr List[ListAlertPoliciesRespMessagesItem] messages: Array of messages
          returned.
    :attr List[ListAlertPoliciesRespResultItem] result: Container for response
          information.
    """

    def __init__(self,
                 success: bool,
                 errors: List['ListAlertPoliciesRespErrorsItem'],
                 messages: List['ListAlertPoliciesRespMessagesItem'],
                 result: List['ListAlertPoliciesRespResultItem']) -> None:
        """
        Initialize a ListAlertPoliciesResp object.

        :param bool success: Was operation successful.
        :param List[ListAlertPoliciesRespErrorsItem] errors: Array of errors
               encountered.
        :param List[ListAlertPoliciesRespMessagesItem] messages: Array of messages
               returned.
        :param List[ListAlertPoliciesRespResultItem] result: Container for response
               information.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListAlertPoliciesResp':
        """Initialize a ListAlertPoliciesResp object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in ListAlertPoliciesResp JSON')
        if 'errors' in _dict:
            args['errors'] = [ListAlertPoliciesRespErrorsItem.from_dict(x) for x in _dict.get('errors')]
        else:
            raise ValueError('Required property \'errors\' not present in ListAlertPoliciesResp JSON')
        if 'messages' in _dict:
            args['messages'] = [ListAlertPoliciesRespMessagesItem.from_dict(x) for x in _dict.get('messages')]
        else:
            raise ValueError('Required property \'messages\' not present in ListAlertPoliciesResp JSON')
        if 'result' in _dict:
            args['result'] = [ListAlertPoliciesRespResultItem.from_dict(x) for x in _dict.get('result')]
        else:
            raise ValueError('Required property \'result\' not present in ListAlertPoliciesResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListAlertPoliciesResp object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'success') and self.success is not None:
            _dict['success'] = self.success
        if hasattr(self, 'errors') and self.errors is not None:
            _dict['errors'] = [x.to_dict() for x in self.errors]
        if hasattr(self, 'messages') and self.messages is not None:
            _dict['messages'] = [x.to_dict() for x in self.messages]
        if hasattr(self, 'result') and self.result is not None:
            _dict['result'] = [x.to_dict() for x in self.result]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListAlertPoliciesResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListAlertPoliciesResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListAlertPoliciesResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
