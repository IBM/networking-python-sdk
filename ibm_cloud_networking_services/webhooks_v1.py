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
CIS Alert Webhooks

API Version: 1.0.0
"""

from typing import Dict, List
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################

class WebhooksV1(BaseService):
    """The Webhooks V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.cis.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'webhooks'

    @classmethod
    def new_instance(cls,
                     crn: str,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'WebhooksV1':
        """
        Return a new client for the Webhooks service using the specified parameters
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
        Construct a new client for the Webhooks service.

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
    # Alert Webhooks
    #########################


    def get_alert_webhooks(self,
        **kwargs
    ) -> DetailedResponse:
        """
        List alert webhooks.

        List configured alert webhooks for the CIS instance.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListAlertWebhooksResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_alert_webhooks')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn']
        path_param_values = self.encode_path_vars(self.crn)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/alerting/destinations/webhooks'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def create_alert_webhook(self,
        *,
        name: str = None,
        url: str = None,
        secret: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create an alert webhook.

        Create a new alert webhook for the CIS instance.

        :param str name: (optional) Webhook Name.
        :param str url: (optional) Webhook url.
        :param str secret: (optional) The optional secret or API key needed to use
               the webhook.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `WebhookSuccessResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_alert_webhook')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'url': url,
            'secret': secret
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
        url = '/v1/{crn}/alerting/destinations/webhooks'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def get_alert_webhook(self,
        webhook_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get an alert webhook.

        Get an alert webhook for the CIS instance.

        :param str webhook_id: Alert webhook identifier.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `GetAlertWebhookResp` object
        """

        if webhook_id is None:
            raise ValueError('webhook_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_alert_webhook')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'webhook_id']
        path_param_values = self.encode_path_vars(self.crn, webhook_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/alerting/destinations/webhooks/{webhook_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def update_alert_webhook(self,
        webhook_id: str,
        *,
        name: str = None,
        url: str = None,
        secret: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update an alert webhook.

        Update an existing alert webhook for the CIS instance.

        :param str webhook_id: Alert webhook identifier.
        :param str name: (optional) Webhook Name.
        :param str url: (optional) Webhook url.
        :param str secret: (optional) The optional secret or API key needed to use
               the webhook.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `WebhookSuccessResp` object
        """

        if webhook_id is None:
            raise ValueError('webhook_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_alert_webhook')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'url': url,
            'secret': secret
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'webhook_id']
        path_param_values = self.encode_path_vars(self.crn, webhook_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/alerting/destinations/webhooks/{webhook_id}'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def delete_alert_webhook(self,
        webhook_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete an alert webhook.

        Delete an alert webhook for the CIS instance.

        :param str webhook_id: Alert webhook identifier.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `WebhookSuccessResp` object
        """

        if webhook_id is None:
            raise ValueError('webhook_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_alert_webhook')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'webhook_id']
        path_param_values = self.encode_path_vars(self.crn, webhook_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/alerting/destinations/webhooks/{webhook_id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


##############################################################################
# Models
##############################################################################


class GetAlertWebhookRespResult():
    """
    Container for response information.

    :attr str id: Webhook ID.
    :attr str name: Webhook Name.
    :attr str url: Webhook url.
    :attr str type: Webhook type.
    :attr str created_at: When was the webhook created.
    :attr str last_success: When was the webhook last used successfully.
    :attr str last_failure: When was the webhook last used and failed.
    """

    def __init__(self,
                 id: str,
                 name: str,
                 url: str,
                 type: str,
                 created_at: str,
                 last_success: str,
                 last_failure: str) -> None:
        """
        Initialize a GetAlertWebhookRespResult object.

        :param str id: Webhook ID.
        :param str name: Webhook Name.
        :param str url: Webhook url.
        :param str type: Webhook type.
        :param str created_at: When was the webhook created.
        :param str last_success: When was the webhook last used successfully.
        :param str last_failure: When was the webhook last used and failed.
        """
        self.id = id
        self.name = name
        self.url = url
        self.type = type
        self.created_at = created_at
        self.last_success = last_success
        self.last_failure = last_failure

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'GetAlertWebhookRespResult':
        """Initialize a GetAlertWebhookRespResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in GetAlertWebhookRespResult JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in GetAlertWebhookRespResult JSON')
        if 'url' in _dict:
            args['url'] = _dict.get('url')
        else:
            raise ValueError('Required property \'url\' not present in GetAlertWebhookRespResult JSON')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in GetAlertWebhookRespResult JSON')
        if 'created_at' in _dict:
            args['created_at'] = _dict.get('created_at')
        else:
            raise ValueError('Required property \'created_at\' not present in GetAlertWebhookRespResult JSON')
        if 'last_success' in _dict:
            args['last_success'] = _dict.get('last_success')
        else:
            raise ValueError('Required property \'last_success\' not present in GetAlertWebhookRespResult JSON')
        if 'last_failure' in _dict:
            args['last_failure'] = _dict.get('last_failure')
        else:
            raise ValueError('Required property \'last_failure\' not present in GetAlertWebhookRespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a GetAlertWebhookRespResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = self.created_at
        if hasattr(self, 'last_success') and self.last_success is not None:
            _dict['last_success'] = self.last_success
        if hasattr(self, 'last_failure') and self.last_failure is not None:
            _dict['last_failure'] = self.last_failure
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this GetAlertWebhookRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'GetAlertWebhookRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'GetAlertWebhookRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ListAlertWebhooksRespResultItem():
    """
    ListAlertWebhooksRespResultItem.

    :attr str id: Webhook ID.
    :attr str name: Webhook Name.
    :attr str url: Webhook url.
    :attr str type: Webhook type.
    :attr str created_at: When was the webhook created.
    :attr str last_success: When was the webhook last used successfully.
    :attr str last_failure: When was the webhook last used and failed.
    """

    def __init__(self,
                 id: str,
                 name: str,
                 url: str,
                 type: str,
                 created_at: str,
                 last_success: str,
                 last_failure: str) -> None:
        """
        Initialize a ListAlertWebhooksRespResultItem object.

        :param str id: Webhook ID.
        :param str name: Webhook Name.
        :param str url: Webhook url.
        :param str type: Webhook type.
        :param str created_at: When was the webhook created.
        :param str last_success: When was the webhook last used successfully.
        :param str last_failure: When was the webhook last used and failed.
        """
        self.id = id
        self.name = name
        self.url = url
        self.type = type
        self.created_at = created_at
        self.last_success = last_success
        self.last_failure = last_failure

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListAlertWebhooksRespResultItem':
        """Initialize a ListAlertWebhooksRespResultItem object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in ListAlertWebhooksRespResultItem JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in ListAlertWebhooksRespResultItem JSON')
        if 'url' in _dict:
            args['url'] = _dict.get('url')
        else:
            raise ValueError('Required property \'url\' not present in ListAlertWebhooksRespResultItem JSON')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in ListAlertWebhooksRespResultItem JSON')
        if 'created_at' in _dict:
            args['created_at'] = _dict.get('created_at')
        else:
            raise ValueError('Required property \'created_at\' not present in ListAlertWebhooksRespResultItem JSON')
        if 'last_success' in _dict:
            args['last_success'] = _dict.get('last_success')
        else:
            raise ValueError('Required property \'last_success\' not present in ListAlertWebhooksRespResultItem JSON')
        if 'last_failure' in _dict:
            args['last_failure'] = _dict.get('last_failure')
        else:
            raise ValueError('Required property \'last_failure\' not present in ListAlertWebhooksRespResultItem JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListAlertWebhooksRespResultItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = self.created_at
        if hasattr(self, 'last_success') and self.last_success is not None:
            _dict['last_success'] = self.last_success
        if hasattr(self, 'last_failure') and self.last_failure is not None:
            _dict['last_failure'] = self.last_failure
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListAlertWebhooksRespResultItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListAlertWebhooksRespResultItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListAlertWebhooksRespResultItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class WebhookSuccessRespResult():
    """
    Container for response information.

    :attr str id: Webhook ID.
    """

    def __init__(self,
                 id: str) -> None:
        """
        Initialize a WebhookSuccessRespResult object.

        :param str id: Webhook ID.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'WebhookSuccessRespResult':
        """Initialize a WebhookSuccessRespResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in WebhookSuccessRespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WebhookSuccessRespResult object from a json dictionary."""
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
        """Return a `str` version of this WebhookSuccessRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'WebhookSuccessRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'WebhookSuccessRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class GetAlertWebhookResp():
    """
    Get Alert Webhooks Response.

    :attr bool success: Was operation successful.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    :attr GetAlertWebhookRespResult result: Container for response information.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: 'GetAlertWebhookRespResult') -> None:
        """
        Initialize a GetAlertWebhookResp object.

        :param bool success: Was operation successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        :param GetAlertWebhookRespResult result: Container for response
               information.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'GetAlertWebhookResp':
        """Initialize a GetAlertWebhookResp object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in GetAlertWebhookResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in GetAlertWebhookResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in GetAlertWebhookResp JSON')
        if 'result' in _dict:
            args['result'] = GetAlertWebhookRespResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in GetAlertWebhookResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a GetAlertWebhookResp object from a json dictionary."""
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
        """Return a `str` version of this GetAlertWebhookResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'GetAlertWebhookResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'GetAlertWebhookResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ListAlertWebhooksResp():
    """
    List Alert Webhooks Response.

    :attr bool success: Was operation successful.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    :attr List[ListAlertWebhooksRespResultItem] result: Container for response
          information.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: List['ListAlertWebhooksRespResultItem']) -> None:
        """
        Initialize a ListAlertWebhooksResp object.

        :param bool success: Was operation successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        :param List[ListAlertWebhooksRespResultItem] result: Container for response
               information.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListAlertWebhooksResp':
        """Initialize a ListAlertWebhooksResp object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in ListAlertWebhooksResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in ListAlertWebhooksResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in ListAlertWebhooksResp JSON')
        if 'result' in _dict:
            args['result'] = [ListAlertWebhooksRespResultItem.from_dict(x) for x in _dict.get('result')]
        else:
            raise ValueError('Required property \'result\' not present in ListAlertWebhooksResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListAlertWebhooksResp object from a json dictionary."""
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
        """Return a `str` version of this ListAlertWebhooksResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListAlertWebhooksResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListAlertWebhooksResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class WebhookSuccessResp():
    """
    Alert Webhooks Response.

    :attr bool success: Was operation successful.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    :attr WebhookSuccessRespResult result: Container for response information.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: 'WebhookSuccessRespResult') -> None:
        """
        Initialize a WebhookSuccessResp object.

        :param bool success: Was operation successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        :param WebhookSuccessRespResult result: Container for response information.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'WebhookSuccessResp':
        """Initialize a WebhookSuccessResp object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in WebhookSuccessResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in WebhookSuccessResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in WebhookSuccessResp JSON')
        if 'result' in _dict:
            args['result'] = WebhookSuccessRespResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in WebhookSuccessResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WebhookSuccessResp object from a json dictionary."""
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
        """Return a `str` version of this WebhookSuccessResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'WebhookSuccessResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'WebhookSuccessResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
