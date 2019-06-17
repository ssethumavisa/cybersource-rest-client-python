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


class Riskv1authenticationsRecurringPaymentInformation(object):
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
        'end_date': 'str',
        'frequency': 'int',
        'original_purchase_date': 'str'
    }

    attribute_map = {
        'end_date': 'endDate',
        'frequency': 'frequency',
        'original_purchase_date': 'originalPurchaseDate'
    }

    def __init__(self, end_date=None, frequency=None, original_purchase_date=None):
        """
        Riskv1authenticationsRecurringPaymentInformation - a model defined in Swagger
        """

        self._end_date = None
        self._frequency = None
        self._original_purchase_date = None

        if end_date is not None:
          self.end_date = end_date
        if frequency is not None:
          self.frequency = frequency
        if original_purchase_date is not None:
          self.original_purchase_date = original_purchase_date

    @property
    def end_date(self):
        """
        Gets the end_date of this Riskv1authenticationsRecurringPaymentInformation.
        The date after which no further recurring authorizations should be performed. Format: `YYYYMMDD` **Note** This field is required for recurring transactions. 

        :return: The end_date of this Riskv1authenticationsRecurringPaymentInformation.
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """
        Sets the end_date of this Riskv1authenticationsRecurringPaymentInformation.
        The date after which no further recurring authorizations should be performed. Format: `YYYYMMDD` **Note** This field is required for recurring transactions. 

        :param end_date: The end_date of this Riskv1authenticationsRecurringPaymentInformation.
        :type: str
        """
        if end_date is not None and len(end_date) > 10:
            raise ValueError("Invalid value for `end_date`, length must be less than or equal to `10`")

        self._end_date = end_date

    @property
    def frequency(self):
        """
        Gets the frequency of this Riskv1authenticationsRecurringPaymentInformation.
        Integer value indicating the minimum number of days between recurring authorizations. A frequency of monthly is indicated by the value 28. Multiple of 28 days will be used to indicate months. Example: 6 months = 168 **Note** This field is required for recurring transactions. 

        :return: The frequency of this Riskv1authenticationsRecurringPaymentInformation.
        :rtype: int
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """
        Sets the frequency of this Riskv1authenticationsRecurringPaymentInformation.
        Integer value indicating the minimum number of days between recurring authorizations. A frequency of monthly is indicated by the value 28. Multiple of 28 days will be used to indicate months. Example: 6 months = 168 **Note** This field is required for recurring transactions. 

        :param frequency: The frequency of this Riskv1authenticationsRecurringPaymentInformation.
        :type: int
        """

        self._frequency = frequency

    @property
    def original_purchase_date(self):
        """
        Gets the original_purchase_date of this Riskv1authenticationsRecurringPaymentInformation.
        Date of original purchase. Required for recurring transactions. Format: `YYYYMMDD:HH:MM:SS` **Note**: If this field is empty, the current date is used. 

        :return: The original_purchase_date of this Riskv1authenticationsRecurringPaymentInformation.
        :rtype: str
        """
        return self._original_purchase_date

    @original_purchase_date.setter
    def original_purchase_date(self, original_purchase_date):
        """
        Sets the original_purchase_date of this Riskv1authenticationsRecurringPaymentInformation.
        Date of original purchase. Required for recurring transactions. Format: `YYYYMMDD:HH:MM:SS` **Note**: If this field is empty, the current date is used. 

        :param original_purchase_date: The original_purchase_date of this Riskv1authenticationsRecurringPaymentInformation.
        :type: str
        """
        if original_purchase_date is not None and len(original_purchase_date) > 17:
            raise ValueError("Invalid value for `original_purchase_date`, length must be less than or equal to `17`")

        self._original_purchase_date = original_purchase_date

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
        if not isinstance(other, Riskv1authenticationsRecurringPaymentInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
