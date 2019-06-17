# coding: utf-8

"""
    CyberSource Merged Spec

    All CyberSource API specs merged together. These are available at https://developer.cybersource.com/api/reference/api-reference.html

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class PayerAuthenticationApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """
	
    def __init__(self, merchant_config, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client
        self.api_client.set_configuration(merchant_config) 


    def check_payer_auth_enrollment(self, check_payer_auth_enrollment_request, **kwargs):
        """
        Check payer auth enrollment
        This call verifies that the card is enrolled in a card authentication program.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.check_payer_auth_enrollment(check_payer_auth_enrollment_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CheckPayerAuthEnrollmentRequest check_payer_auth_enrollment_request: (required)
        :return: RiskV1AuthenticationsPost201Response
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.check_payer_auth_enrollment_with_http_info(check_payer_auth_enrollment_request, **kwargs)
        else:
            (data) = self.check_payer_auth_enrollment_with_http_info(check_payer_auth_enrollment_request, **kwargs)
            return data

    def check_payer_auth_enrollment_with_http_info(self, check_payer_auth_enrollment_request, **kwargs):
        """
        Check payer auth enrollment
        This call verifies that the card is enrolled in a card authentication program.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.check_payer_auth_enrollment_with_http_info(check_payer_auth_enrollment_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CheckPayerAuthEnrollmentRequest check_payer_auth_enrollment_request: (required)
        :return: RiskV1AuthenticationsPost201Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['check_payer_auth_enrollment_request']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method check_payer_auth_enrollment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'check_payer_auth_enrollment_request' is set
        if ('check_payer_auth_enrollment_request' not in params) or (params['check_payer_auth_enrollment_request'] is None):
            raise ValueError("Missing the required parameter `check_payer_auth_enrollment_request` when calling `check_payer_auth_enrollment`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'check_payer_auth_enrollment_request' in params:
            body_params = params['check_payer_auth_enrollment_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/hal+json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/risk/v1/authentications', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='RiskV1AuthenticationsPost201Response',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def validate_authentication_results(self, request, **kwargs):
        """
        Validate authentication results
        This call retrieves and validates the authentication results from issuer and allows the merchant to proceed with processing the payment. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.validate_authentication_results(request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Request request: (required)
        :return: RiskV1AuthenticationResultsPost201Response
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.validate_authentication_results_with_http_info(request, **kwargs)
        else:
            (data) = self.validate_authentication_results_with_http_info(request, **kwargs)
            return data

    def validate_authentication_results_with_http_info(self, request, **kwargs):
        """
        Validate authentication results
        This call retrieves and validates the authentication results from issuer and allows the merchant to proceed with processing the payment. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.validate_authentication_results_with_http_info(request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Request request: (required)
        :return: RiskV1AuthenticationResultsPost201Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method validate_authentication_results" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request' is set
        if ('request' not in params) or (params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `validate_authentication_results`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/hal+json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/risk/v1/authentication-results', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='RiskV1AuthenticationResultsPost201Response',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
