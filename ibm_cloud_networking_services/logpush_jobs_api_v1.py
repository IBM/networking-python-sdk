# coding: utf-8

# (C) Copyright IBM Corp. 2026.
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

# IBM OpenAPI SDK Code Generator Version: 3.114.0-a902401e-20260427-192904

"""
CIS Logpush Jobs

API Version: 1.0.0
"""

from enum import Enum
from typing import Dict, List, Optional
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_model

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################


class LogpushJobsApiV1(BaseService):
    """The Logpush Jobs API V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.cis.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'logpush_jobs_api'

    @classmethod
    def new_instance(
        cls,
        crn: str,
        dataset: str,
        zone_id: str,
        service_name: str = DEFAULT_SERVICE_NAME,
    ) -> 'LogpushJobsApiV1':
        """
        Return a new client for the Logpush Jobs API service using the specified
               parameters and external configuration.

        :param str crn: Full URL-encoded CRN of the service instance.

        :param str dataset: The dataset.

        :param str zone_id: Zone identifier.
        """
        if crn is None:
            raise ValueError('crn must be provided')
        if dataset is None:
            raise ValueError('dataset must be provided')
        if zone_id is None:
            raise ValueError('zone_id must be provided')

        authenticator = get_authenticator_from_environment(service_name)
        service = cls(
            crn,
            dataset,
            zone_id,
            authenticator
            )
        service.configure_service(service_name)
        return service

    def __init__(
        self,
        crn: str,
        dataset: str,
        zone_id: str,
        authenticator: Authenticator = None,
    ) -> None:
        """
        Construct a new client for the Logpush Jobs API service.

        :param str crn: Full URL-encoded CRN of the service instance.

        :param str dataset: The dataset.

        :param str zone_id: Zone identifier.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/main/README.md
               about initializing the authenticator of your choice.
        """
        if crn is None:
            raise ValueError('crn must be provided')
        if dataset is None:
            raise ValueError('dataset must be provided')
        if zone_id is None:
            raise ValueError('zone_id must be provided')

        BaseService.__init__(self, service_url=self.DEFAULT_SERVICE_URL, authenticator=authenticator)
        self.crn = crn
        self.dataset = dataset
        self.zone_id = zone_id

    #########################
    # Logpush Jobs
    #########################

    def get_logpush_jobs_v2(
        self,
        **kwargs,
    ) -> DetailedResponse:
        """
        List logpush jobs.

        List configured logpush jobs for your domain.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListLogpushJobsResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_logpush_jobs_v2',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_id']
        path_param_values = self.encode_path_vars(self.crn, self.zone_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/{crn}/zones/{zone_id}/logpush/jobs'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def create_logpush_job_v2(
        self,
        *,
        create_logpush_job_v2_request: Optional['CreateLogpushJobV2Request'] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a logpush jobs.

        Create a new logpush job for the domain.

        :param CreateLogpushJobV2Request create_logpush_job_v2_request: (optional)
               Create logpush job body.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `LogpushJobsResp` object
        """

        if create_logpush_job_v2_request is not None and isinstance(create_logpush_job_v2_request, CreateLogpushJobV2Request):
            create_logpush_job_v2_request = convert_model(create_logpush_job_v2_request)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_logpush_job_v2',
        )
        headers.update(sdk_headers)

        data = json.dumps(create_logpush_job_v2_request)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_id']
        path_param_values = self.encode_path_vars(self.crn, self.zone_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/{crn}/zones/{zone_id}/logpush/jobs'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_logpush_job_v2(
        self,
        job_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a logpush job.

        Get a logpush job  for a given zone.

        :param str job_id: logpush job identifier.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `LogpushJobsResp` object
        """

        if not job_id:
            raise ValueError('job_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_logpush_job_v2',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_id', 'job_id']
        path_param_values = self.encode_path_vars(self.crn, self.zone_id, job_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/{crn}/zones/{zone_id}/logpush/jobs/{job_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def update_logpush_job_v2(
        self,
        job_id: str,
        *,
        update_logpush_job_v2_request: Optional['UpdateLogpushJobV2Request'] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update a logpush job.

        Update an existing logpush job for a given zone.

        :param str job_id: logpush job identifier.
        :param UpdateLogpushJobV2Request update_logpush_job_v2_request: (optional)
               Update logpush job.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `LogpushJobsResp` object
        """

        if not job_id:
            raise ValueError('job_id must be provided')
        if update_logpush_job_v2_request is not None and isinstance(update_logpush_job_v2_request, UpdateLogpushJobV2Request):
            update_logpush_job_v2_request = convert_model(update_logpush_job_v2_request)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_logpush_job_v2',
        )
        headers.update(sdk_headers)

        data = json.dumps(update_logpush_job_v2_request)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_id', 'job_id']
        path_param_values = self.encode_path_vars(self.crn, self.zone_id, job_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/{crn}/zones/{zone_id}/logpush/jobs/{job_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_logpush_job_v2(
        self,
        job_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete a logpush job.

        Delete a logpush job for a zone.

        :param str job_id: logpush job identifier.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DeleteLogpushJobResp` object
        """

        if not job_id:
            raise ValueError('job_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_logpush_job_v2',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_id', 'job_id']
        path_param_values = self.encode_path_vars(self.crn, self.zone_id, job_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/{crn}/zones/{zone_id}/logpush/jobs/{job_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_logpush_ownership_v2(
        self,
        *,
        cos: Optional[dict] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a new ownership challenge sent to your destination.

        Get a new ownership challenge.

        :param dict cos: (optional) Information to identify the COS bucket where
               the data will be pushed.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `OwnershipChallengeResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_logpush_ownership_v2',
        )
        headers.update(sdk_headers)

        data = {
            'cos': cos,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_id']
        path_param_values = self.encode_path_vars(self.crn, self.zone_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/{crn}/zones/{zone_id}/logpush/ownership'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def validate_logpush_ownership_challenge_v2(
        self,
        *,
        cos: Optional[dict] = None,
        ownership_challenge: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Validate ownership challenge of the destination.

        Validate ownership challenge of the destination.

        :param dict cos: (optional) Information to identify the COS bucket where
               the data will be pushed.
        :param str ownership_challenge: (optional) Ownership challenge token to
               prove destination ownership.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `OwnershipChallengeValidateResult` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='validate_logpush_ownership_challenge_v2',
        )
        headers.update(sdk_headers)

        data = {
            'cos': cos,
            'ownership_challenge': ownership_challenge,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_id']
        path_param_values = self.encode_path_vars(self.crn, self.zone_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/{crn}/zones/{zone_id}/logpush/ownership/validate'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def list_fields_for_dataset_v2(
        self,
        **kwargs,
    ) -> DetailedResponse:
        """
        The list of all fields available for a dataset.

        The list of all fields available for a dataset.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListFieldsResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_fields_for_dataset_v2',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_id', 'dataset']
        path_param_values = self.encode_path_vars(self.crn, self.zone_id, self.dataset)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/{crn}/zones/{zone_id}/logpush/datasets/{dataset}/fields'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def list_logpush_jobs_for_dataset_v2(
        self,
        **kwargs,
    ) -> DetailedResponse:
        """
        List logpush jobs for dataset.

        List configured logpush jobs for a dataset.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `LogpushJobsResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_logpush_jobs_for_dataset_v2',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_id', 'dataset']
        path_param_values = self.encode_path_vars(self.crn, self.zone_id, self.dataset)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/{crn}/zones/{zone_id}/logpush/datasets/{dataset}/jobs'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_logs_retention(
        self,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get log retention.

        Get log retention setting for Logpull/Logpush on your domain.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `LogRetentionResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_logs_retention',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_id']
        path_param_values = self.encode_path_vars(self.crn, self.zone_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_id}/logs/retention'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def create_log_retention(
        self,
        *,
        flag: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update log retention.

        Update log retention flag for Logpull/Logpush.

        :param bool flag: (optional)
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `LogRetentionResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_log_retention',
        )
        headers.update(sdk_headers)

        data = {
            'flag': flag,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_id']
        path_param_values = self.encode_path_vars(self.crn, self.zone_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_id}/logs/retention'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response


##############################################################################
# Models
##############################################################################


class CreateLogpushJobV2Request:
    """
    CreateLogpushJobV2Request.

    """

    def __init__(
        self,
    ) -> None:
        """
        Initialize a CreateLogpushJobV2Request object.

        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
            ", ".join(['CreateLogpushJobV2RequestLogpushJobCosReq', 'CreateLogpushJobV2RequestLogpushJobLogdnaReq', 'CreateLogpushJobV2RequestLogpushJobIbmclReq', 'CreateLogpushJobV2RequestLogpushJobGenericReq'])
        )
        raise Exception(msg)


class LogRetentionRespResult:
    """
    LogRetentionRespResult.

    :param bool flag: (optional)
    """

    def __init__(
        self,
        *,
        flag: Optional[bool] = None,
    ) -> None:
        """
        Initialize a LogRetentionRespResult object.

        :param bool flag: (optional)
        """
        self.flag = flag

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LogRetentionRespResult':
        """Initialize a LogRetentionRespResult object from a json dictionary."""
        args = {}
        if (flag := _dict.get('flag')) is not None:
            args['flag'] = flag
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LogRetentionRespResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'flag') and self.flag is not None:
            _dict['flag'] = self.flag
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this LogRetentionRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LogRetentionRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LogRetentionRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class LogpushJobIbmclReqIbmcl:
    """
    Required information to push logs to your Cloud Logs instance.

    :param str instance_id: GUID of the IBM Cloud Logs instance where you want to
          send logs.
    :param str region: Region where the IBM Cloud Logs instance is located.
    :param str api_key: IBM Cloud API key used to generate a token for pushing to
          your Cloud Logs instance.
    """

    def __init__(
        self,
        instance_id: str,
        region: str,
        api_key: str,
    ) -> None:
        """
        Initialize a LogpushJobIbmclReqIbmcl object.

        :param str instance_id: GUID of the IBM Cloud Logs instance where you want
               to send logs.
        :param str region: Region where the IBM Cloud Logs instance is located.
        :param str api_key: IBM Cloud API key used to generate a token for pushing
               to your Cloud Logs instance.
        """
        self.instance_id = instance_id
        self.region = region
        self.api_key = api_key

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LogpushJobIbmclReqIbmcl':
        """Initialize a LogpushJobIbmclReqIbmcl object from a json dictionary."""
        args = {}
        if (instance_id := _dict.get('instance_id')) is not None:
            args['instance_id'] = instance_id
        else:
            raise ValueError('Required property \'instance_id\' not present in LogpushJobIbmclReqIbmcl JSON')
        if (region := _dict.get('region')) is not None:
            args['region'] = region
        else:
            raise ValueError('Required property \'region\' not present in LogpushJobIbmclReqIbmcl JSON')
        if (api_key := _dict.get('api_key')) is not None:
            args['api_key'] = api_key
        else:
            raise ValueError('Required property \'api_key\' not present in LogpushJobIbmclReqIbmcl JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LogpushJobIbmclReqIbmcl object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'instance_id') and self.instance_id is not None:
            _dict['instance_id'] = self.instance_id
        if hasattr(self, 'region') and self.region is not None:
            _dict['region'] = self.region
        if hasattr(self, 'api_key') and self.api_key is not None:
            _dict['api_key'] = self.api_key
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this LogpushJobIbmclReqIbmcl object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LogpushJobIbmclReqIbmcl') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LogpushJobIbmclReqIbmcl') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class LogpushJobsUpdateIbmclReqIbmcl:
    """
    Required information to push logs to your Cloud Logs instance.

    :param str instance_id: (optional) GUID of the IBM Cloud Logs instance where you
          want to send logs.
    :param str region: (optional) Region where the IBM Cloud Logs instance is
          located.
    :param str api_key: (optional) IBM Cloud API key used to generate a token for
          pushing to your Cloud Logs instance.
    """

    def __init__(
        self,
        *,
        instance_id: Optional[str] = None,
        region: Optional[str] = None,
        api_key: Optional[str] = None,
    ) -> None:
        """
        Initialize a LogpushJobsUpdateIbmclReqIbmcl object.

        :param str instance_id: (optional) GUID of the IBM Cloud Logs instance
               where you want to send logs.
        :param str region: (optional) Region where the IBM Cloud Logs instance is
               located.
        :param str api_key: (optional) IBM Cloud API key used to generate a token
               for pushing to your Cloud Logs instance.
        """
        self.instance_id = instance_id
        self.region = region
        self.api_key = api_key

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LogpushJobsUpdateIbmclReqIbmcl':
        """Initialize a LogpushJobsUpdateIbmclReqIbmcl object from a json dictionary."""
        args = {}
        if (instance_id := _dict.get('instance_id')) is not None:
            args['instance_id'] = instance_id
        if (region := _dict.get('region')) is not None:
            args['region'] = region
        if (api_key := _dict.get('api_key')) is not None:
            args['api_key'] = api_key
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LogpushJobsUpdateIbmclReqIbmcl object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'instance_id') and self.instance_id is not None:
            _dict['instance_id'] = self.instance_id
        if hasattr(self, 'region') and self.region is not None:
            _dict['region'] = self.region
        if hasattr(self, 'api_key') and self.api_key is not None:
            _dict['api_key'] = self.api_key
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this LogpushJobsUpdateIbmclReqIbmcl object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LogpushJobsUpdateIbmclReqIbmcl') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LogpushJobsUpdateIbmclReqIbmcl') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class UpdateLogpushJobV2Request:
    """
    UpdateLogpushJobV2Request.

    """

    def __init__(
        self,
    ) -> None:
        """
        Initialize a UpdateLogpushJobV2Request object.

        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
            ", ".join(['UpdateLogpushJobV2RequestLogpushJobsUpdateCosReq', 'UpdateLogpushJobV2RequestLogpushJobsUpdateLogdnaReq', 'UpdateLogpushJobV2RequestLogpushJobsUpdateIbmclReq', 'UpdateLogpushJobV2RequestLogpushJobsUpdateGenericReq'])
        )
        raise Exception(msg)


class DeleteLogpushJobResp:
    """
    delete logpush job response.

    :param bool success: success response.
    :param List[List[str]] errors: errors.
    :param List[List[str]] messages: messages.
    :param dict result: result.
    """

    def __init__(
        self,
        success: bool,
        errors: List[List[str]],
        messages: List[List[str]],
        result: dict,
    ) -> None:
        """
        Initialize a DeleteLogpushJobResp object.

        :param bool success: success response.
        :param List[List[str]] errors: errors.
        :param List[List[str]] messages: messages.
        :param dict result: result.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteLogpushJobResp':
        """Initialize a DeleteLogpushJobResp object from a json dictionary."""
        args = {}
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        else:
            raise ValueError('Required property \'success\' not present in DeleteLogpushJobResp JSON')
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        else:
            raise ValueError('Required property \'errors\' not present in DeleteLogpushJobResp JSON')
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        else:
            raise ValueError('Required property \'messages\' not present in DeleteLogpushJobResp JSON')
        if (result := _dict.get('result')) is not None:
            args['result'] = result
        else:
            raise ValueError('Required property \'result\' not present in DeleteLogpushJobResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteLogpushJobResp object from a json dictionary."""
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
            _dict['result'] = self.result
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DeleteLogpushJobResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteLogpushJobResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteLogpushJobResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ListFieldsResp:
    """
    list fields response.

    :param bool success: success response.
    :param List[List[str]] errors: errors.
    :param List[List[str]] messages: messages.
    :param dict result: (optional) result.
    """

    def __init__(
        self,
        success: bool,
        errors: List[List[str]],
        messages: List[List[str]],
        *,
        result: Optional[dict] = None,
    ) -> None:
        """
        Initialize a ListFieldsResp object.

        :param bool success: success response.
        :param List[List[str]] errors: errors.
        :param List[List[str]] messages: messages.
        :param dict result: (optional) result.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListFieldsResp':
        """Initialize a ListFieldsResp object from a json dictionary."""
        args = {}
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        else:
            raise ValueError('Required property \'success\' not present in ListFieldsResp JSON')
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        else:
            raise ValueError('Required property \'errors\' not present in ListFieldsResp JSON')
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        else:
            raise ValueError('Required property \'messages\' not present in ListFieldsResp JSON')
        if (result := _dict.get('result')) is not None:
            args['result'] = result
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListFieldsResp object from a json dictionary."""
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
            _dict['result'] = self.result
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListFieldsResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListFieldsResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListFieldsResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ListLogpushJobsResp:
    """
    List Logpush Jobs Response.

    :param bool success: success response.
    :param List[List[str]] errors: errors.
    :param List[List[str]] messages: messages.
    :param List[LogpushJobPack] result: result.
    """

    def __init__(
        self,
        success: bool,
        errors: List[List[str]],
        messages: List[List[str]],
        result: List['LogpushJobPack'],
    ) -> None:
        """
        Initialize a ListLogpushJobsResp object.

        :param bool success: success response.
        :param List[List[str]] errors: errors.
        :param List[List[str]] messages: messages.
        :param List[LogpushJobPack] result: result.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListLogpushJobsResp':
        """Initialize a ListLogpushJobsResp object from a json dictionary."""
        args = {}
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        else:
            raise ValueError('Required property \'success\' not present in ListLogpushJobsResp JSON')
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        else:
            raise ValueError('Required property \'errors\' not present in ListLogpushJobsResp JSON')
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        else:
            raise ValueError('Required property \'messages\' not present in ListLogpushJobsResp JSON')
        if (result := _dict.get('result')) is not None:
            args['result'] = [LogpushJobPack.from_dict(v) for v in result]
        else:
            raise ValueError('Required property \'result\' not present in ListLogpushJobsResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListLogpushJobsResp object from a json dictionary."""
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
            result_list = []
            for v in self.result:
                if isinstance(v, dict):
                    result_list.append(v)
                else:
                    result_list.append(v.to_dict())
            _dict['result'] = result_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListLogpushJobsResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListLogpushJobsResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListLogpushJobsResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class LogRetentionResp:
    """
    log retention result.

    :param LogRetentionRespResult result: (optional)
    :param bool success: (optional) success response.
    :param List[List[str]] errors: (optional) errors.
    :param List[List[str]] messages: (optional) messages.
    """

    def __init__(
        self,
        *,
        result: Optional['LogRetentionRespResult'] = None,
        success: Optional[bool] = None,
        errors: Optional[List[List[str]]] = None,
        messages: Optional[List[List[str]]] = None,
    ) -> None:
        """
        Initialize a LogRetentionResp object.

        :param LogRetentionRespResult result: (optional)
        :param bool success: (optional) success response.
        :param List[List[str]] errors: (optional) errors.
        :param List[List[str]] messages: (optional) messages.
        """
        self.result = result
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LogRetentionResp':
        """Initialize a LogRetentionResp object from a json dictionary."""
        args = {}
        if (result := _dict.get('result')) is not None:
            args['result'] = LogRetentionRespResult.from_dict(result)
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LogRetentionResp object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'result') and self.result is not None:
            if isinstance(self.result, dict):
                _dict['result'] = self.result
            else:
                _dict['result'] = self.result.to_dict()
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
        """Return a `str` version of this LogRetentionResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LogRetentionResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LogRetentionResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class LogpushJobPack:
    """
    logpush job pack.

    :param int id: Logpush Job ID.
    :param str name: Logpush Job Name.
    :param bool enabled: Whether the logpush job enabled or not.
    :param str dataset: Dataset to be pulled.
    :param str frequency: The frequency at which CIS sends batches of logs to your
          destination.
    :param str logpull_options: Configuration string.
    :param str destination_conf: Uniquely identifies a resource (such as an s3
          bucket) where data will be pushed.
    :param str last_complete: (optional) Records the last time for which logs have
          been successfully pushed.
    :param str last_error: (optional) Records the last time the job failed.
    :param str error_message: (optional) The last failure.
    """

    def __init__(
        self,
        id: int,
        name: str,
        enabled: bool,
        dataset: str,
        frequency: str,
        logpull_options: str,
        destination_conf: str,
        *,
        last_complete: Optional[str] = None,
        last_error: Optional[str] = None,
        error_message: Optional[str] = None,
    ) -> None:
        """
        Initialize a LogpushJobPack object.

        :param int id: Logpush Job ID.
        :param str name: Logpush Job Name.
        :param bool enabled: Whether the logpush job enabled or not.
        :param str dataset: Dataset to be pulled.
        :param str frequency: The frequency at which CIS sends batches of logs to
               your destination.
        :param str logpull_options: Configuration string.
        :param str destination_conf: Uniquely identifies a resource (such as an s3
               bucket) where data will be pushed.
        :param str last_complete: (optional) Records the last time for which logs
               have been successfully pushed.
        :param str last_error: (optional) Records the last time the job failed.
        :param str error_message: (optional) The last failure.
        """
        self.id = id
        self.name = name
        self.enabled = enabled
        self.dataset = dataset
        self.frequency = frequency
        self.logpull_options = logpull_options
        self.destination_conf = destination_conf
        self.last_complete = last_complete
        self.last_error = last_error
        self.error_message = error_message

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LogpushJobPack':
        """Initialize a LogpushJobPack object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in LogpushJobPack JSON')
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in LogpushJobPack JSON')
        if (enabled := _dict.get('enabled')) is not None:
            args['enabled'] = enabled
        else:
            raise ValueError('Required property \'enabled\' not present in LogpushJobPack JSON')
        if (dataset := _dict.get('dataset')) is not None:
            args['dataset'] = dataset
        else:
            raise ValueError('Required property \'dataset\' not present in LogpushJobPack JSON')
        if (frequency := _dict.get('frequency')) is not None:
            args['frequency'] = frequency
        else:
            raise ValueError('Required property \'frequency\' not present in LogpushJobPack JSON')
        if (logpull_options := _dict.get('logpull_options')) is not None:
            args['logpull_options'] = logpull_options
        else:
            raise ValueError('Required property \'logpull_options\' not present in LogpushJobPack JSON')
        if (destination_conf := _dict.get('destination_conf')) is not None:
            args['destination_conf'] = destination_conf
        else:
            raise ValueError('Required property \'destination_conf\' not present in LogpushJobPack JSON')
        if (last_complete := _dict.get('last_complete')) is not None:
            args['last_complete'] = last_complete
        if (last_error := _dict.get('last_error')) is not None:
            args['last_error'] = last_error
        if (error_message := _dict.get('error_message')) is not None:
            args['error_message'] = error_message
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LogpushJobPack object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'dataset') and self.dataset is not None:
            _dict['dataset'] = self.dataset
        if hasattr(self, 'frequency') and self.frequency is not None:
            _dict['frequency'] = self.frequency
        if hasattr(self, 'logpull_options') and self.logpull_options is not None:
            _dict['logpull_options'] = self.logpull_options
        if hasattr(self, 'destination_conf') and self.destination_conf is not None:
            _dict['destination_conf'] = self.destination_conf
        if hasattr(self, 'last_complete') and self.last_complete is not None:
            _dict['last_complete'] = self.last_complete
        if hasattr(self, 'last_error') and self.last_error is not None:
            _dict['last_error'] = self.last_error
        if hasattr(self, 'error_message') and self.error_message is not None:
            _dict['error_message'] = self.error_message
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this LogpushJobPack object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LogpushJobPack') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LogpushJobPack') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class LogpushJobsResp:
    """
    logpush job response.

    :param bool success: success response.
    :param List[List[str]] errors: errors.
    :param List[List[str]] messages: messages.
    :param LogpushJobPack result: logpush job pack.
    """

    def __init__(
        self,
        success: bool,
        errors: List[List[str]],
        messages: List[List[str]],
        result: 'LogpushJobPack',
    ) -> None:
        """
        Initialize a LogpushJobsResp object.

        :param bool success: success response.
        :param List[List[str]] errors: errors.
        :param List[List[str]] messages: messages.
        :param LogpushJobPack result: logpush job pack.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LogpushJobsResp':
        """Initialize a LogpushJobsResp object from a json dictionary."""
        args = {}
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        else:
            raise ValueError('Required property \'success\' not present in LogpushJobsResp JSON')
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        else:
            raise ValueError('Required property \'errors\' not present in LogpushJobsResp JSON')
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        else:
            raise ValueError('Required property \'messages\' not present in LogpushJobsResp JSON')
        if (result := _dict.get('result')) is not None:
            args['result'] = LogpushJobPack.from_dict(result)
        else:
            raise ValueError('Required property \'result\' not present in LogpushJobsResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LogpushJobsResp object from a json dictionary."""
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
            if isinstance(self.result, dict):
                _dict['result'] = self.result
            else:
                _dict['result'] = self.result.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this LogpushJobsResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LogpushJobsResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LogpushJobsResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class OwnershipChallengeResp:
    """
    Get Logpush Ownership Challenge Response.

    :param bool success: success response.
    :param List[List[str]] errors: errors.
    :param List[List[str]] messages: messages.
    :param OwnershipChallengeResult result: ownership challenge result.
    """

    def __init__(
        self,
        success: bool,
        errors: List[List[str]],
        messages: List[List[str]],
        result: 'OwnershipChallengeResult',
    ) -> None:
        """
        Initialize a OwnershipChallengeResp object.

        :param bool success: success response.
        :param List[List[str]] errors: errors.
        :param List[List[str]] messages: messages.
        :param OwnershipChallengeResult result: ownership challenge result.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'OwnershipChallengeResp':
        """Initialize a OwnershipChallengeResp object from a json dictionary."""
        args = {}
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        else:
            raise ValueError('Required property \'success\' not present in OwnershipChallengeResp JSON')
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        else:
            raise ValueError('Required property \'errors\' not present in OwnershipChallengeResp JSON')
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        else:
            raise ValueError('Required property \'messages\' not present in OwnershipChallengeResp JSON')
        if (result := _dict.get('result')) is not None:
            args['result'] = OwnershipChallengeResult.from_dict(result)
        else:
            raise ValueError('Required property \'result\' not present in OwnershipChallengeResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a OwnershipChallengeResp object from a json dictionary."""
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
            if isinstance(self.result, dict):
                _dict['result'] = self.result
            else:
                _dict['result'] = self.result.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this OwnershipChallengeResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'OwnershipChallengeResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'OwnershipChallengeResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class OwnershipChallengeResult:
    """
    ownership challenge result.

    :param str filename: file name.
    :param bool valid: valid.
    :param str messages: (optional) message.
    """

    def __init__(
        self,
        filename: str,
        valid: bool,
        *,
        messages: Optional[str] = None,
    ) -> None:
        """
        Initialize a OwnershipChallengeResult object.

        :param str filename: file name.
        :param bool valid: valid.
        :param str messages: (optional) message.
        """
        self.filename = filename
        self.valid = valid
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'OwnershipChallengeResult':
        """Initialize a OwnershipChallengeResult object from a json dictionary."""
        args = {}
        if (filename := _dict.get('filename')) is not None:
            args['filename'] = filename
        else:
            raise ValueError('Required property \'filename\' not present in OwnershipChallengeResult JSON')
        if (valid := _dict.get('valid')) is not None:
            args['valid'] = valid
        else:
            raise ValueError('Required property \'valid\' not present in OwnershipChallengeResult JSON')
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a OwnershipChallengeResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'filename') and self.filename is not None:
            _dict['filename'] = self.filename
        if hasattr(self, 'valid') and self.valid is not None:
            _dict['valid'] = self.valid
        if hasattr(self, 'messages') and self.messages is not None:
            _dict['messages'] = self.messages
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this OwnershipChallengeResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'OwnershipChallengeResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'OwnershipChallengeResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class OwnershipChallengeValidateResult:
    """
    ownership challenge validate result.

    :param bool valid: valid.
    """

    def __init__(
        self,
        valid: bool,
    ) -> None:
        """
        Initialize a OwnershipChallengeValidateResult object.

        :param bool valid: valid.
        """
        self.valid = valid

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'OwnershipChallengeValidateResult':
        """Initialize a OwnershipChallengeValidateResult object from a json dictionary."""
        args = {}
        if (valid := _dict.get('valid')) is not None:
            args['valid'] = valid
        else:
            raise ValueError('Required property \'valid\' not present in OwnershipChallengeValidateResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a OwnershipChallengeValidateResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'valid') and self.valid is not None:
            _dict['valid'] = self.valid
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this OwnershipChallengeValidateResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'OwnershipChallengeValidateResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'OwnershipChallengeValidateResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CreateLogpushJobV2RequestLogpushJobCosReq(CreateLogpushJobV2Request):
    """
    Create COS logpush job input.

    :param str name: (optional) Logpush Job Name.
    :param bool enabled: (optional) Whether the logpush job enabled or not.
    :param str logpull_options: (optional) Configuration string.
    :param dict cos: Information to identify the COS bucket where the data will be
          pushed.
    :param str ownership_challenge: Ownership challenge token to prove destination
          ownership.
    :param str dataset: (optional) Dataset to be pulled.
    :param str frequency: (optional) The frequency at which CIS sends batches of
          logs to your destination.
    """

    def __init__(
        self,
        cos: dict,
        ownership_challenge: str,
        *,
        name: Optional[str] = None,
        enabled: Optional[bool] = None,
        logpull_options: Optional[str] = None,
        dataset: Optional[str] = None,
        frequency: Optional[str] = None,
    ) -> None:
        """
        Initialize a CreateLogpushJobV2RequestLogpushJobCosReq object.

        :param dict cos: Information to identify the COS bucket where the data will
               be pushed.
        :param str ownership_challenge: Ownership challenge token to prove
               destination ownership.
        :param str name: (optional) Logpush Job Name.
        :param bool enabled: (optional) Whether the logpush job enabled or not.
        :param str logpull_options: (optional) Configuration string.
        :param str dataset: (optional) Dataset to be pulled.
        :param str frequency: (optional) The frequency at which CIS sends batches
               of logs to your destination.
        """
        # pylint: disable=super-init-not-called
        self.name = name
        self.enabled = enabled
        self.logpull_options = logpull_options
        self.cos = cos
        self.ownership_challenge = ownership_challenge
        self.dataset = dataset
        self.frequency = frequency

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CreateLogpushJobV2RequestLogpushJobCosReq':
        """Initialize a CreateLogpushJobV2RequestLogpushJobCosReq object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (enabled := _dict.get('enabled')) is not None:
            args['enabled'] = enabled
        if (logpull_options := _dict.get('logpull_options')) is not None:
            args['logpull_options'] = logpull_options
        if (cos := _dict.get('cos')) is not None:
            args['cos'] = cos
        else:
            raise ValueError('Required property \'cos\' not present in CreateLogpushJobV2RequestLogpushJobCosReq JSON')
        if (ownership_challenge := _dict.get('ownership_challenge')) is not None:
            args['ownership_challenge'] = ownership_challenge
        else:
            raise ValueError('Required property \'ownership_challenge\' not present in CreateLogpushJobV2RequestLogpushJobCosReq JSON')
        if (dataset := _dict.get('dataset')) is not None:
            args['dataset'] = dataset
        if (frequency := _dict.get('frequency')) is not None:
            args['frequency'] = frequency
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CreateLogpushJobV2RequestLogpushJobCosReq object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'logpull_options') and self.logpull_options is not None:
            _dict['logpull_options'] = self.logpull_options
        if hasattr(self, 'cos') and self.cos is not None:
            _dict['cos'] = self.cos
        if hasattr(self, 'ownership_challenge') and self.ownership_challenge is not None:
            _dict['ownership_challenge'] = self.ownership_challenge
        if hasattr(self, 'dataset') and self.dataset is not None:
            _dict['dataset'] = self.dataset
        if hasattr(self, 'frequency') and self.frequency is not None:
            _dict['frequency'] = self.frequency
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CreateLogpushJobV2RequestLogpushJobCosReq object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CreateLogpushJobV2RequestLogpushJobCosReq') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CreateLogpushJobV2RequestLogpushJobCosReq') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class DatasetEnum(str, Enum):
        """
        Dataset to be pulled.
        """

        HTTP_REQUESTS = 'http_requests'
        RANGE_EVENTS = 'range_events'
        FIREWALL_EVENTS = 'firewall_events'


    class FrequencyEnum(str, Enum):
        """
        The frequency at which CIS sends batches of logs to your destination.
        """

        HIGH = 'high'
        LOW = 'low'



class CreateLogpushJobV2RequestLogpushJobGenericReq(CreateLogpushJobV2Request):
    """
    Create logpush job for a generic destination.

    :param str name: (optional) Logpush Job Name.
    :param bool enabled: (optional) Whether the logpush job is enabled or not.
    :param str logpull_options: (optional) Configuration string.
    :param str destination_conf: Uniquely identifies a resource where data will be
          pushed. Additional configuration parameters supported by the destination may be
          included.
    :param str dataset: (optional) Dataset to be pulled.
    :param str frequency: (optional) The frequency at which CIS sends batches of
          logs to your destination.
    """

    def __init__(
        self,
        destination_conf: str,
        *,
        name: Optional[str] = None,
        enabled: Optional[bool] = None,
        logpull_options: Optional[str] = None,
        dataset: Optional[str] = None,
        frequency: Optional[str] = None,
    ) -> None:
        """
        Initialize a CreateLogpushJobV2RequestLogpushJobGenericReq object.

        :param str destination_conf: Uniquely identifies a resource where data will
               be pushed. Additional configuration parameters supported by the destination
               may be included.
        :param str name: (optional) Logpush Job Name.
        :param bool enabled: (optional) Whether the logpush job is enabled or not.
        :param str logpull_options: (optional) Configuration string.
        :param str dataset: (optional) Dataset to be pulled.
        :param str frequency: (optional) The frequency at which CIS sends batches
               of logs to your destination.
        """
        # pylint: disable=super-init-not-called
        self.name = name
        self.enabled = enabled
        self.logpull_options = logpull_options
        self.destination_conf = destination_conf
        self.dataset = dataset
        self.frequency = frequency

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CreateLogpushJobV2RequestLogpushJobGenericReq':
        """Initialize a CreateLogpushJobV2RequestLogpushJobGenericReq object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (enabled := _dict.get('enabled')) is not None:
            args['enabled'] = enabled
        if (logpull_options := _dict.get('logpull_options')) is not None:
            args['logpull_options'] = logpull_options
        if (destination_conf := _dict.get('destination_conf')) is not None:
            args['destination_conf'] = destination_conf
        else:
            raise ValueError('Required property \'destination_conf\' not present in CreateLogpushJobV2RequestLogpushJobGenericReq JSON')
        if (dataset := _dict.get('dataset')) is not None:
            args['dataset'] = dataset
        if (frequency := _dict.get('frequency')) is not None:
            args['frequency'] = frequency
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CreateLogpushJobV2RequestLogpushJobGenericReq object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'logpull_options') and self.logpull_options is not None:
            _dict['logpull_options'] = self.logpull_options
        if hasattr(self, 'destination_conf') and self.destination_conf is not None:
            _dict['destination_conf'] = self.destination_conf
        if hasattr(self, 'dataset') and self.dataset is not None:
            _dict['dataset'] = self.dataset
        if hasattr(self, 'frequency') and self.frequency is not None:
            _dict['frequency'] = self.frequency
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CreateLogpushJobV2RequestLogpushJobGenericReq object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CreateLogpushJobV2RequestLogpushJobGenericReq') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CreateLogpushJobV2RequestLogpushJobGenericReq') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class DatasetEnum(str, Enum):
        """
        Dataset to be pulled.
        """

        HTTP_REQUESTS = 'http_requests'
        RANGE_EVENTS = 'range_events'
        FIREWALL_EVENTS = 'firewall_events'


    class FrequencyEnum(str, Enum):
        """
        The frequency at which CIS sends batches of logs to your destination.
        """

        HIGH = 'high'
        LOW = 'low'



class CreateLogpushJobV2RequestLogpushJobIbmclReq(CreateLogpushJobV2Request):
    """
    Create IBM Cloud Logs logpush job input.

    :param str name: (optional) Logpush Job Name.
    :param bool enabled: (optional) Whether the logpush job is enabled or not.
    :param str logpull_options: (optional) Configuration string.
    :param LogpushJobIbmclReqIbmcl ibmcl: Required information to push logs to your
          Cloud Logs instance.
    :param str dataset: (optional) Dataset to be pulled.
    :param str frequency: (optional) The frequency at which CIS sends batches of
          logs to your destination.
    """

    def __init__(
        self,
        ibmcl: 'LogpushJobIbmclReqIbmcl',
        *,
        name: Optional[str] = None,
        enabled: Optional[bool] = None,
        logpull_options: Optional[str] = None,
        dataset: Optional[str] = None,
        frequency: Optional[str] = None,
    ) -> None:
        """
        Initialize a CreateLogpushJobV2RequestLogpushJobIbmclReq object.

        :param LogpushJobIbmclReqIbmcl ibmcl: Required information to push logs to
               your Cloud Logs instance.
        :param str name: (optional) Logpush Job Name.
        :param bool enabled: (optional) Whether the logpush job is enabled or not.
        :param str logpull_options: (optional) Configuration string.
        :param str dataset: (optional) Dataset to be pulled.
        :param str frequency: (optional) The frequency at which CIS sends batches
               of logs to your destination.
        """
        # pylint: disable=super-init-not-called
        self.name = name
        self.enabled = enabled
        self.logpull_options = logpull_options
        self.ibmcl = ibmcl
        self.dataset = dataset
        self.frequency = frequency

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CreateLogpushJobV2RequestLogpushJobIbmclReq':
        """Initialize a CreateLogpushJobV2RequestLogpushJobIbmclReq object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (enabled := _dict.get('enabled')) is not None:
            args['enabled'] = enabled
        if (logpull_options := _dict.get('logpull_options')) is not None:
            args['logpull_options'] = logpull_options
        if (ibmcl := _dict.get('ibmcl')) is not None:
            args['ibmcl'] = LogpushJobIbmclReqIbmcl.from_dict(ibmcl)
        else:
            raise ValueError('Required property \'ibmcl\' not present in CreateLogpushJobV2RequestLogpushJobIbmclReq JSON')
        if (dataset := _dict.get('dataset')) is not None:
            args['dataset'] = dataset
        if (frequency := _dict.get('frequency')) is not None:
            args['frequency'] = frequency
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CreateLogpushJobV2RequestLogpushJobIbmclReq object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'logpull_options') and self.logpull_options is not None:
            _dict['logpull_options'] = self.logpull_options
        if hasattr(self, 'ibmcl') and self.ibmcl is not None:
            if isinstance(self.ibmcl, dict):
                _dict['ibmcl'] = self.ibmcl
            else:
                _dict['ibmcl'] = self.ibmcl.to_dict()
        if hasattr(self, 'dataset') and self.dataset is not None:
            _dict['dataset'] = self.dataset
        if hasattr(self, 'frequency') and self.frequency is not None:
            _dict['frequency'] = self.frequency
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CreateLogpushJobV2RequestLogpushJobIbmclReq object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CreateLogpushJobV2RequestLogpushJobIbmclReq') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CreateLogpushJobV2RequestLogpushJobIbmclReq') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class DatasetEnum(str, Enum):
        """
        Dataset to be pulled.
        """

        HTTP_REQUESTS = 'http_requests'
        RANGE_EVENTS = 'range_events'
        FIREWALL_EVENTS = 'firewall_events'


    class FrequencyEnum(str, Enum):
        """
        The frequency at which CIS sends batches of logs to your destination.
        """

        HIGH = 'high'
        LOW = 'low'



class CreateLogpushJobV2RequestLogpushJobLogdnaReq(CreateLogpushJobV2Request):
    """
    Create LogDNA logpush job input.

    :param str name: (optional) Logpush Job Name.
    :param bool enabled: (optional) Whether the logpush job enabled or not.
    :param str logpull_options: (optional) Configuration string.
    :param dict logdna: Information to identify the LogDNA instance the data will be
          pushed.
    :param str dataset: (optional) Dataset to be pulled.
    :param str frequency: (optional) The frequency at which CIS sends batches of
          logs to your destination.
    """

    def __init__(
        self,
        logdna: dict,
        *,
        name: Optional[str] = None,
        enabled: Optional[bool] = None,
        logpull_options: Optional[str] = None,
        dataset: Optional[str] = None,
        frequency: Optional[str] = None,
    ) -> None:
        """
        Initialize a CreateLogpushJobV2RequestLogpushJobLogdnaReq object.

        :param dict logdna: Information to identify the LogDNA instance the data
               will be pushed.
        :param str name: (optional) Logpush Job Name.
        :param bool enabled: (optional) Whether the logpush job enabled or not.
        :param str logpull_options: (optional) Configuration string.
        :param str dataset: (optional) Dataset to be pulled.
        :param str frequency: (optional) The frequency at which CIS sends batches
               of logs to your destination.
        """
        # pylint: disable=super-init-not-called
        self.name = name
        self.enabled = enabled
        self.logpull_options = logpull_options
        self.logdna = logdna
        self.dataset = dataset
        self.frequency = frequency

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CreateLogpushJobV2RequestLogpushJobLogdnaReq':
        """Initialize a CreateLogpushJobV2RequestLogpushJobLogdnaReq object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (enabled := _dict.get('enabled')) is not None:
            args['enabled'] = enabled
        if (logpull_options := _dict.get('logpull_options')) is not None:
            args['logpull_options'] = logpull_options
        if (logdna := _dict.get('logdna')) is not None:
            args['logdna'] = logdna
        else:
            raise ValueError('Required property \'logdna\' not present in CreateLogpushJobV2RequestLogpushJobLogdnaReq JSON')
        if (dataset := _dict.get('dataset')) is not None:
            args['dataset'] = dataset
        if (frequency := _dict.get('frequency')) is not None:
            args['frequency'] = frequency
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CreateLogpushJobV2RequestLogpushJobLogdnaReq object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'logpull_options') and self.logpull_options is not None:
            _dict['logpull_options'] = self.logpull_options
        if hasattr(self, 'logdna') and self.logdna is not None:
            _dict['logdna'] = self.logdna
        if hasattr(self, 'dataset') and self.dataset is not None:
            _dict['dataset'] = self.dataset
        if hasattr(self, 'frequency') and self.frequency is not None:
            _dict['frequency'] = self.frequency
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CreateLogpushJobV2RequestLogpushJobLogdnaReq object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CreateLogpushJobV2RequestLogpushJobLogdnaReq') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CreateLogpushJobV2RequestLogpushJobLogdnaReq') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class DatasetEnum(str, Enum):
        """
        Dataset to be pulled.
        """

        HTTP_REQUESTS = 'http_requests'
        RANGE_EVENTS = 'range_events'
        FIREWALL_EVENTS = 'firewall_events'


    class FrequencyEnum(str, Enum):
        """
        The frequency at which CIS sends batches of logs to your destination.
        """

        HIGH = 'high'
        LOW = 'low'



class UpdateLogpushJobV2RequestLogpushJobsUpdateCosReq(UpdateLogpushJobV2Request):
    """
    Update COS logpush job input.

    :param bool enabled: (optional) Whether the logpush job enabled or not.
    :param str logpull_options: (optional) Configuration string.
    :param dict cos: (optional) Information to identify the COS bucket where the
          data will be pushed.
    :param str ownership_challenge: (optional) Ownership challenge token to prove
          destination ownership.
    :param str frequency: (optional) The frequency at which CIS sends batches of
          logs to your destination.
    """

    def __init__(
        self,
        *,
        enabled: Optional[bool] = None,
        logpull_options: Optional[str] = None,
        cos: Optional[dict] = None,
        ownership_challenge: Optional[str] = None,
        frequency: Optional[str] = None,
    ) -> None:
        """
        Initialize a UpdateLogpushJobV2RequestLogpushJobsUpdateCosReq object.

        :param bool enabled: (optional) Whether the logpush job enabled or not.
        :param str logpull_options: (optional) Configuration string.
        :param dict cos: (optional) Information to identify the COS bucket where
               the data will be pushed.
        :param str ownership_challenge: (optional) Ownership challenge token to
               prove destination ownership.
        :param str frequency: (optional) The frequency at which CIS sends batches
               of logs to your destination.
        """
        # pylint: disable=super-init-not-called
        self.enabled = enabled
        self.logpull_options = logpull_options
        self.cos = cos
        self.ownership_challenge = ownership_challenge
        self.frequency = frequency

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'UpdateLogpushJobV2RequestLogpushJobsUpdateCosReq':
        """Initialize a UpdateLogpushJobV2RequestLogpushJobsUpdateCosReq object from a json dictionary."""
        args = {}
        if (enabled := _dict.get('enabled')) is not None:
            args['enabled'] = enabled
        if (logpull_options := _dict.get('logpull_options')) is not None:
            args['logpull_options'] = logpull_options
        if (cos := _dict.get('cos')) is not None:
            args['cos'] = cos
        if (ownership_challenge := _dict.get('ownership_challenge')) is not None:
            args['ownership_challenge'] = ownership_challenge
        if (frequency := _dict.get('frequency')) is not None:
            args['frequency'] = frequency
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a UpdateLogpushJobV2RequestLogpushJobsUpdateCosReq object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'logpull_options') and self.logpull_options is not None:
            _dict['logpull_options'] = self.logpull_options
        if hasattr(self, 'cos') and self.cos is not None:
            _dict['cos'] = self.cos
        if hasattr(self, 'ownership_challenge') and self.ownership_challenge is not None:
            _dict['ownership_challenge'] = self.ownership_challenge
        if hasattr(self, 'frequency') and self.frequency is not None:
            _dict['frequency'] = self.frequency
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this UpdateLogpushJobV2RequestLogpushJobsUpdateCosReq object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'UpdateLogpushJobV2RequestLogpushJobsUpdateCosReq') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'UpdateLogpushJobV2RequestLogpushJobsUpdateCosReq') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class FrequencyEnum(str, Enum):
        """
        The frequency at which CIS sends batches of logs to your destination.
        """

        HIGH = 'high'
        LOW = 'low'



class UpdateLogpushJobV2RequestLogpushJobsUpdateGenericReq(UpdateLogpushJobV2Request):
    """
    Create logpush job for a generic destination.

    :param str name: (optional) Logpush Job Name.
    :param bool enabled: (optional) Whether the logpush job is enabled or not.
    :param str logpull_options: (optional) Configuration string.
    :param str destination_conf: (optional) Uniquely identifies a resource where
          data will be pushed. Additional configuration parameters supported by the
          destination may be included.
    :param str dataset: (optional) Dataset to be pulled.
    :param str frequency: (optional) The frequency at which CIS sends batches of
          logs to your destination.
    """

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        enabled: Optional[bool] = None,
        logpull_options: Optional[str] = None,
        destination_conf: Optional[str] = None,
        dataset: Optional[str] = None,
        frequency: Optional[str] = None,
    ) -> None:
        """
        Initialize a UpdateLogpushJobV2RequestLogpushJobsUpdateGenericReq object.

        :param str name: (optional) Logpush Job Name.
        :param bool enabled: (optional) Whether the logpush job is enabled or not.
        :param str logpull_options: (optional) Configuration string.
        :param str destination_conf: (optional) Uniquely identifies a resource
               where data will be pushed. Additional configuration parameters supported by
               the destination may be included.
        :param str dataset: (optional) Dataset to be pulled.
        :param str frequency: (optional) The frequency at which CIS sends batches
               of logs to your destination.
        """
        # pylint: disable=super-init-not-called
        self.name = name
        self.enabled = enabled
        self.logpull_options = logpull_options
        self.destination_conf = destination_conf
        self.dataset = dataset
        self.frequency = frequency

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'UpdateLogpushJobV2RequestLogpushJobsUpdateGenericReq':
        """Initialize a UpdateLogpushJobV2RequestLogpushJobsUpdateGenericReq object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (enabled := _dict.get('enabled')) is not None:
            args['enabled'] = enabled
        if (logpull_options := _dict.get('logpull_options')) is not None:
            args['logpull_options'] = logpull_options
        if (destination_conf := _dict.get('destination_conf')) is not None:
            args['destination_conf'] = destination_conf
        if (dataset := _dict.get('dataset')) is not None:
            args['dataset'] = dataset
        if (frequency := _dict.get('frequency')) is not None:
            args['frequency'] = frequency
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a UpdateLogpushJobV2RequestLogpushJobsUpdateGenericReq object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'logpull_options') and self.logpull_options is not None:
            _dict['logpull_options'] = self.logpull_options
        if hasattr(self, 'destination_conf') and self.destination_conf is not None:
            _dict['destination_conf'] = self.destination_conf
        if hasattr(self, 'dataset') and self.dataset is not None:
            _dict['dataset'] = self.dataset
        if hasattr(self, 'frequency') and self.frequency is not None:
            _dict['frequency'] = self.frequency
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this UpdateLogpushJobV2RequestLogpushJobsUpdateGenericReq object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'UpdateLogpushJobV2RequestLogpushJobsUpdateGenericReq') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'UpdateLogpushJobV2RequestLogpushJobsUpdateGenericReq') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class DatasetEnum(str, Enum):
        """
        Dataset to be pulled.
        """

        HTTP_REQUESTS = 'http_requests'
        RANGE_EVENTS = 'range_events'
        FIREWALL_EVENTS = 'firewall_events'


    class FrequencyEnum(str, Enum):
        """
        The frequency at which CIS sends batches of logs to your destination.
        """

        HIGH = 'high'
        LOW = 'low'



class UpdateLogpushJobV2RequestLogpushJobsUpdateIbmclReq(UpdateLogpushJobV2Request):
    """
    Update IBM Cloud Logs logpush job input.

    :param bool enabled: (optional) Whether the logpush job enabled or not.
    :param str logpull_options: (optional) Configuration string.
    :param LogpushJobsUpdateIbmclReqIbmcl ibmcl: (optional) Required information to
          push logs to your Cloud Logs instance.
    :param str frequency: (optional) The frequency at which CIS sends batches of
          logs to your destination.
    """

    def __init__(
        self,
        *,
        enabled: Optional[bool] = None,
        logpull_options: Optional[str] = None,
        ibmcl: Optional['LogpushJobsUpdateIbmclReqIbmcl'] = None,
        frequency: Optional[str] = None,
    ) -> None:
        """
        Initialize a UpdateLogpushJobV2RequestLogpushJobsUpdateIbmclReq object.

        :param bool enabled: (optional) Whether the logpush job enabled or not.
        :param str logpull_options: (optional) Configuration string.
        :param LogpushJobsUpdateIbmclReqIbmcl ibmcl: (optional) Required
               information to push logs to your Cloud Logs instance.
        :param str frequency: (optional) The frequency at which CIS sends batches
               of logs to your destination.
        """
        # pylint: disable=super-init-not-called
        self.enabled = enabled
        self.logpull_options = logpull_options
        self.ibmcl = ibmcl
        self.frequency = frequency

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'UpdateLogpushJobV2RequestLogpushJobsUpdateIbmclReq':
        """Initialize a UpdateLogpushJobV2RequestLogpushJobsUpdateIbmclReq object from a json dictionary."""
        args = {}
        if (enabled := _dict.get('enabled')) is not None:
            args['enabled'] = enabled
        if (logpull_options := _dict.get('logpull_options')) is not None:
            args['logpull_options'] = logpull_options
        if (ibmcl := _dict.get('ibmcl')) is not None:
            args['ibmcl'] = LogpushJobsUpdateIbmclReqIbmcl.from_dict(ibmcl)
        if (frequency := _dict.get('frequency')) is not None:
            args['frequency'] = frequency
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a UpdateLogpushJobV2RequestLogpushJobsUpdateIbmclReq object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'logpull_options') and self.logpull_options is not None:
            _dict['logpull_options'] = self.logpull_options
        if hasattr(self, 'ibmcl') and self.ibmcl is not None:
            if isinstance(self.ibmcl, dict):
                _dict['ibmcl'] = self.ibmcl
            else:
                _dict['ibmcl'] = self.ibmcl.to_dict()
        if hasattr(self, 'frequency') and self.frequency is not None:
            _dict['frequency'] = self.frequency
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this UpdateLogpushJobV2RequestLogpushJobsUpdateIbmclReq object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'UpdateLogpushJobV2RequestLogpushJobsUpdateIbmclReq') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'UpdateLogpushJobV2RequestLogpushJobsUpdateIbmclReq') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class FrequencyEnum(str, Enum):
        """
        The frequency at which CIS sends batches of logs to your destination.
        """

        HIGH = 'high'
        LOW = 'low'



class UpdateLogpushJobV2RequestLogpushJobsUpdateLogdnaReq(UpdateLogpushJobV2Request):
    """
    Update LogDNA logpush job input.

    :param bool enabled: (optional) Whether the logpush job enabled or not.
    :param str logpull_options: (optional) Configuration string.
    :param dict logdna: (optional) Information to identify the LogDNA instance the
          data will be pushed.
    :param str frequency: (optional) The frequency at which CIS sends batches of
          logs to your destination.
    """

    def __init__(
        self,
        *,
        enabled: Optional[bool] = None,
        logpull_options: Optional[str] = None,
        logdna: Optional[dict] = None,
        frequency: Optional[str] = None,
    ) -> None:
        """
        Initialize a UpdateLogpushJobV2RequestLogpushJobsUpdateLogdnaReq object.

        :param bool enabled: (optional) Whether the logpush job enabled or not.
        :param str logpull_options: (optional) Configuration string.
        :param dict logdna: (optional) Information to identify the LogDNA instance
               the data will be pushed.
        :param str frequency: (optional) The frequency at which CIS sends batches
               of logs to your destination.
        """
        # pylint: disable=super-init-not-called
        self.enabled = enabled
        self.logpull_options = logpull_options
        self.logdna = logdna
        self.frequency = frequency

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'UpdateLogpushJobV2RequestLogpushJobsUpdateLogdnaReq':
        """Initialize a UpdateLogpushJobV2RequestLogpushJobsUpdateLogdnaReq object from a json dictionary."""
        args = {}
        if (enabled := _dict.get('enabled')) is not None:
            args['enabled'] = enabled
        if (logpull_options := _dict.get('logpull_options')) is not None:
            args['logpull_options'] = logpull_options
        if (logdna := _dict.get('logdna')) is not None:
            args['logdna'] = logdna
        if (frequency := _dict.get('frequency')) is not None:
            args['frequency'] = frequency
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a UpdateLogpushJobV2RequestLogpushJobsUpdateLogdnaReq object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'logpull_options') and self.logpull_options is not None:
            _dict['logpull_options'] = self.logpull_options
        if hasattr(self, 'logdna') and self.logdna is not None:
            _dict['logdna'] = self.logdna
        if hasattr(self, 'frequency') and self.frequency is not None:
            _dict['frequency'] = self.frequency
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this UpdateLogpushJobV2RequestLogpushJobsUpdateLogdnaReq object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'UpdateLogpushJobV2RequestLogpushJobsUpdateLogdnaReq') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'UpdateLogpushJobV2RequestLogpushJobsUpdateLogdnaReq') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class FrequencyEnum(str, Enum):
        """
        The frequency at which CIS sends batches of logs to your destination.
        """

        HIGH = 'high'
        LOW = 'low'

