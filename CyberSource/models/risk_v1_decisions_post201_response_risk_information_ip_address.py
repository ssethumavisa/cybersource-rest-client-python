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


class RiskV1DecisionsPost201ResponseRiskInformationIpAddress(object):
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
        'anonymizer_status': 'str',
        'locality': 'str',
        'country': 'str',
        'administrative_area': 'str',
        'routing_method': 'str'
    }

    attribute_map = {
        'anonymizer_status': 'anonymizerStatus',
        'locality': 'locality',
        'country': 'country',
        'administrative_area': 'administrativeArea',
        'routing_method': 'routingMethod'
    }

    def __init__(self, anonymizer_status=None, locality=None, country=None, administrative_area=None, routing_method=None):
        """
        RiskV1DecisionsPost201ResponseRiskInformationIpAddress - a model defined in Swagger
        """

        self._anonymizer_status = None
        self._locality = None
        self._country = None
        self._administrative_area = None
        self._routing_method = None

        if anonymizer_status is not None:
          self.anonymizer_status = anonymizer_status
        if locality is not None:
          self.locality = locality
        if country is not None:
          self.country = country
        if administrative_area is not None:
          self.administrative_area = administrative_area
        if routing_method is not None:
          self.routing_method = routing_method

    @property
    def anonymizer_status(self):
        """
        Gets the anonymizer_status of this RiskV1DecisionsPost201ResponseRiskInformationIpAddress.
        Indicates whether the transaction IP address is associated with a known anonymous proxy.  For all possible values, see the `score_ip_anonymizer_status` field description in the _Decision Manager Using the SCMP API Developer Guide_ on the [CyberSource Business Center.](https://ebc2.cybersource.com/ebc2/) Click **Decision Manager** > **Documentation** > **Guides** > _Decision Manager Using the SCMP API Developer Guide_ (PDF link). 

        :return: The anonymizer_status of this RiskV1DecisionsPost201ResponseRiskInformationIpAddress.
        :rtype: str
        """
        return self._anonymizer_status

    @anonymizer_status.setter
    def anonymizer_status(self, anonymizer_status):
        """
        Sets the anonymizer_status of this RiskV1DecisionsPost201ResponseRiskInformationIpAddress.
        Indicates whether the transaction IP address is associated with a known anonymous proxy.  For all possible values, see the `score_ip_anonymizer_status` field description in the _Decision Manager Using the SCMP API Developer Guide_ on the [CyberSource Business Center.](https://ebc2.cybersource.com/ebc2/) Click **Decision Manager** > **Documentation** > **Guides** > _Decision Manager Using the SCMP API Developer Guide_ (PDF link). 

        :param anonymizer_status: The anonymizer_status of this RiskV1DecisionsPost201ResponseRiskInformationIpAddress.
        :type: str
        """
        if anonymizer_status is not None and len(anonymizer_status) > 255:
            raise ValueError("Invalid value for `anonymizer_status`, length must be less than or equal to `255`")

        self._anonymizer_status = anonymizer_status

    @property
    def locality(self):
        """
        Gets the locality of this RiskV1DecisionsPost201ResponseRiskInformationIpAddress.
        Name of the city decoded from the IP address used directly or indirectly by the customer to send the order.  For all possible values, see the `score_ip_city` field description in the _Decision Manager Using the SCMP API Developer Guide_ on the [CyberSource Business Center.](https://ebc2.cybersource.com/ebc2/) Click **Decision Manager** > **Documentation** > **Guides** > _Decision Manager Using the SCMP API Developer Guide_ (PDF link). 

        :return: The locality of this RiskV1DecisionsPost201ResponseRiskInformationIpAddress.
        :rtype: str
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        """
        Sets the locality of this RiskV1DecisionsPost201ResponseRiskInformationIpAddress.
        Name of the city decoded from the IP address used directly or indirectly by the customer to send the order.  For all possible values, see the `score_ip_city` field description in the _Decision Manager Using the SCMP API Developer Guide_ on the [CyberSource Business Center.](https://ebc2.cybersource.com/ebc2/) Click **Decision Manager** > **Documentation** > **Guides** > _Decision Manager Using the SCMP API Developer Guide_ (PDF link). 

        :param locality: The locality of this RiskV1DecisionsPost201ResponseRiskInformationIpAddress.
        :type: str
        """
        if locality is not None and len(locality) > 255:
            raise ValueError("Invalid value for `locality`, length must be less than or equal to `255`")

        self._locality = locality

    @property
    def country(self):
        """
        Gets the country of this RiskV1DecisionsPost201ResponseRiskInformationIpAddress.
        Name of the country decoded from the IP address used directly or indirectly by the customer to send the order.  For all possible values, see the `score_ip_country` field description in the _Decision Manager Using the SCMP API Developer Guide_ on the [CyberSource Business Center.](https://ebc2.cybersource.com/ebc2/) Click **Decision Manager** > **Documentation** > **Guides** > _Decision Manager Using the SCMP API Developer Guide_ (PDF link). 

        :return: The country of this RiskV1DecisionsPost201ResponseRiskInformationIpAddress.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this RiskV1DecisionsPost201ResponseRiskInformationIpAddress.
        Name of the country decoded from the IP address used directly or indirectly by the customer to send the order.  For all possible values, see the `score_ip_country` field description in the _Decision Manager Using the SCMP API Developer Guide_ on the [CyberSource Business Center.](https://ebc2.cybersource.com/ebc2/) Click **Decision Manager** > **Documentation** > **Guides** > _Decision Manager Using the SCMP API Developer Guide_ (PDF link). 

        :param country: The country of this RiskV1DecisionsPost201ResponseRiskInformationIpAddress.
        :type: str
        """
        if country is not None and len(country) > 255:
            raise ValueError("Invalid value for `country`, length must be less than or equal to `255`")

        self._country = country

    @property
    def administrative_area(self):
        """
        Gets the administrative_area of this RiskV1DecisionsPost201ResponseRiskInformationIpAddress.
        Name of the country decoded from the IP address used directly or indirectly by the customer to send the order.  For all possible values, see the `score_ip_country` field description in the _Decision Manager Using the SCMP API Developer Guide_ on the [CyberSource Business Center.](https://ebc2.cybersource.com/ebc2/) Click **Decision Manager** > **Documentation** > **Guides** > _Decision Manager Using the SCMP API Developer Guide_ (PDF link). 

        :return: The administrative_area of this RiskV1DecisionsPost201ResponseRiskInformationIpAddress.
        :rtype: str
        """
        return self._administrative_area

    @administrative_area.setter
    def administrative_area(self, administrative_area):
        """
        Sets the administrative_area of this RiskV1DecisionsPost201ResponseRiskInformationIpAddress.
        Name of the country decoded from the IP address used directly or indirectly by the customer to send the order.  For all possible values, see the `score_ip_country` field description in the _Decision Manager Using the SCMP API Developer Guide_ on the [CyberSource Business Center.](https://ebc2.cybersource.com/ebc2/) Click **Decision Manager** > **Documentation** > **Guides** > _Decision Manager Using the SCMP API Developer Guide_ (PDF link). 

        :param administrative_area: The administrative_area of this RiskV1DecisionsPost201ResponseRiskInformationIpAddress.
        :type: str
        """
        if administrative_area is not None and len(administrative_area) > 255:
            raise ValueError("Invalid value for `administrative_area`, length must be less than or equal to `255`")

        self._administrative_area = administrative_area

    @property
    def routing_method(self):
        """
        Gets the routing_method of this RiskV1DecisionsPost201ResponseRiskInformationIpAddress.
        Routing method decoded from the IP address used directly or indirectly by the customer to send the order.  For all possible values, see the `score_ip_routing_method` field description in the _Decision Manager Using the SCMP API Developer Guide_ on the [CyberSource Business Center.](https://ebc2.cybersource.com/ebc2/) Click **Decision Manager** > **Documentation** > **Guides** > _Decision Manager Using the SCMP API Developer Guide_ (PDF link). 

        :return: The routing_method of this RiskV1DecisionsPost201ResponseRiskInformationIpAddress.
        :rtype: str
        """
        return self._routing_method

    @routing_method.setter
    def routing_method(self, routing_method):
        """
        Sets the routing_method of this RiskV1DecisionsPost201ResponseRiskInformationIpAddress.
        Routing method decoded from the IP address used directly or indirectly by the customer to send the order.  For all possible values, see the `score_ip_routing_method` field description in the _Decision Manager Using the SCMP API Developer Guide_ on the [CyberSource Business Center.](https://ebc2.cybersource.com/ebc2/) Click **Decision Manager** > **Documentation** > **Guides** > _Decision Manager Using the SCMP API Developer Guide_ (PDF link). 

        :param routing_method: The routing_method of this RiskV1DecisionsPost201ResponseRiskInformationIpAddress.
        :type: str
        """
        if routing_method is not None and len(routing_method) > 255:
            raise ValueError("Invalid value for `routing_method`, length must be less than or equal to `255`")

        self._routing_method = routing_method

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
        if not isinstance(other, RiskV1DecisionsPost201ResponseRiskInformationIpAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
