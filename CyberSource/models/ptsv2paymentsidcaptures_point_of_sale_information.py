# coding: utf-8

"""
    CyberSource Merged Spec

    All CyberSource API specs merged together. These are available at https://developer.cybersource.com/api/reference/api-reference.html

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Ptsv2paymentsidcapturesPointOfSaleInformation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'emv': 'Ptsv2paymentsidcapturesPointOfSaleInformationEmv',
        'amex_capn_data': 'str'
    }

    attribute_map = {
        'emv': 'emv',
        'amex_capn_data': 'amexCapnData'
    }

    def __init__(self, emv=None, amex_capn_data=None):
        """
        Ptsv2paymentsidcapturesPointOfSaleInformation - a model defined in Swagger
        """

        self._emv = None
        self._amex_capn_data = None

        if emv is not None:
          self.emv = emv
        if amex_capn_data is not None:
          self.amex_capn_data = amex_capn_data

    @property
    def emv(self):
        """
        Gets the emv of this Ptsv2paymentsidcapturesPointOfSaleInformation.

        :return: The emv of this Ptsv2paymentsidcapturesPointOfSaleInformation.
        :rtype: Ptsv2paymentsidcapturesPointOfSaleInformationEmv
        """
        return self._emv

    @emv.setter
    def emv(self, emv):
        """
        Sets the emv of this Ptsv2paymentsidcapturesPointOfSaleInformation.

        :param emv: The emv of this Ptsv2paymentsidcapturesPointOfSaleInformation.
        :type: Ptsv2paymentsidcapturesPointOfSaleInformationEmv
        """

        self._emv = emv

    @property
    def amex_capn_data(self):
        """
        Gets the amex_capn_data of this Ptsv2paymentsidcapturesPointOfSaleInformation.
        Point-of-sale details for the transaction. This value is returned only for **American Express Direct**. CyberSource generates this value, which consists of a series of codes that identify terminal capability, security data, and specific conditions present at the time the transaction occurred. To comply with the CAPN requirements, this value must be included in all subsequent follow-on requests, such as captures and follow-on credits.  When you perform authorizations, captures, and credits through CyberSource, CyberSource passes this value from the authorization service to the subsequent services for you. However, when you perform authorizations through CyberSource and perform subsequent services through other financial institutions, you must ensure that your requests for captures and credits include this value.  For details, see `auth_pos_data` field description in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm) 

        :return: The amex_capn_data of this Ptsv2paymentsidcapturesPointOfSaleInformation.
        :rtype: str
        """
        return self._amex_capn_data

    @amex_capn_data.setter
    def amex_capn_data(self, amex_capn_data):
        """
        Sets the amex_capn_data of this Ptsv2paymentsidcapturesPointOfSaleInformation.
        Point-of-sale details for the transaction. This value is returned only for **American Express Direct**. CyberSource generates this value, which consists of a series of codes that identify terminal capability, security data, and specific conditions present at the time the transaction occurred. To comply with the CAPN requirements, this value must be included in all subsequent follow-on requests, such as captures and follow-on credits.  When you perform authorizations, captures, and credits through CyberSource, CyberSource passes this value from the authorization service to the subsequent services for you. However, when you perform authorizations through CyberSource and perform subsequent services through other financial institutions, you must ensure that your requests for captures and credits include this value.  For details, see `auth_pos_data` field description in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm) 

        :param amex_capn_data: The amex_capn_data of this Ptsv2paymentsidcapturesPointOfSaleInformation.
        :type: str
        """
        if amex_capn_data is not None and len(amex_capn_data) > 12:
            raise ValueError("Invalid value for `amex_capn_data`, length must be less than or equal to `12`")

        self._amex_capn_data = amex_capn_data

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Ptsv2paymentsidcapturesPointOfSaleInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
