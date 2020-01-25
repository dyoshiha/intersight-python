# coding: utf-8
"""
    Cisco Intersight

    Cisco Intersight is a management platform delivered as a service with embedded analytics for your Cisco and 3rd party IT infrastructure. This platform offers an intelligent level of management that enables IT organizations to analyze, simplify, and automate their environments in more advanced ways than the prior generations of tools. Cisco Intersight provides an integrated and intuitive management experience for resources in the traditional data center as well as at the edge. With flexible deployment options to address complex security needs, getting started with Intersight is quick and easy. Cisco Intersight has deep integration with Cisco UCS and HyperFlex systems allowing for remote deployment, configuration, and ongoing maintenance. The model-based deployment works for a single system in a remote location or hundreds of systems in a data center and enables rapid, standardized configuration and deployment. It also streamlines maintaining those systems whether you are working with small or very large configurations.   # noqa: E501

    The version of the OpenAPI document: 1.0.9-1295
    Contact: intersight@cisco.com
    Generated by: https://openapi-generator.tech
"""

import pprint
import re  # noqa: F401

import six

from intersight.configuration import Configuration


class AssetAddressInformationAllOf(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'address1': 'str',
        'address2': 'str',
        'city': 'str',
        'country': 'str',
        'location': 'str',
        'name': 'str',
        'postal_code': 'str',
        'state': 'str'
    }

    attribute_map = {
        'address1': 'Address1',
        'address2': 'Address2',
        'city': 'City',
        'country': 'Country',
        'location': 'Location',
        'name': 'Name',
        'postal_code': 'PostalCode',
        'state': 'State'
    }

    def __init__(self,
                 address1=None,
                 address2=None,
                 city=None,
                 country=None,
                 location=None,
                 name=None,
                 postal_code=None,
                 state=None,
                 local_vars_configuration=None):  # noqa: E501
        """AssetAddressInformationAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._address1 = None
        self._address2 = None
        self._city = None
        self._country = None
        self._location = None
        self._name = None
        self._postal_code = None
        self._state = None
        self.discriminator = None

        if address1 is not None:
            self.address1 = address1
        if address2 is not None:
            self.address2 = address2
        if city is not None:
            self.city = city
        if country is not None:
            self.country = country
        if location is not None:
            self.location = location
        if name is not None:
            self.name = name
        if postal_code is not None:
            self.postal_code = postal_code
        if state is not None:
            self.state = state

    @property
    def address1(self):
        """Gets the address1 of this AssetAddressInformationAllOf.  # noqa: E501

        Address Line one of the address information. example \"PO BOX 641570\".    # noqa: E501

        :return: The address1 of this AssetAddressInformationAllOf.  # noqa: E501
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """Sets the address1 of this AssetAddressInformationAllOf.

        Address Line one of the address information. example \"PO BOX 641570\".    # noqa: E501

        :param address1: The address1 of this AssetAddressInformationAllOf.  # noqa: E501
        :type: str
        """

        self._address1 = address1

    @property
    def address2(self):
        """Gets the address2 of this AssetAddressInformationAllOf.  # noqa: E501

        Address Line two of the address information. example \"Cisco Systems\".    # noqa: E501

        :return: The address2 of this AssetAddressInformationAllOf.  # noqa: E501
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """Sets the address2 of this AssetAddressInformationAllOf.

        Address Line two of the address information. example \"Cisco Systems\".    # noqa: E501

        :param address2: The address2 of this AssetAddressInformationAllOf.  # noqa: E501
        :type: str
        """

        self._address2 = address2

    @property
    def city(self):
        """Gets the city of this AssetAddressInformationAllOf.  # noqa: E501

        City in which the address resides. example \"San Jose\".    # noqa: E501

        :return: The city of this AssetAddressInformationAllOf.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this AssetAddressInformationAllOf.

        City in which the address resides. example \"San Jose\".    # noqa: E501

        :param city: The city of this AssetAddressInformationAllOf.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def country(self):
        """Gets the country of this AssetAddressInformationAllOf.  # noqa: E501

        Country in which the address resides. example \"US\".    # noqa: E501

        :return: The country of this AssetAddressInformationAllOf.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this AssetAddressInformationAllOf.

        Country in which the address resides. example \"US\".    # noqa: E501

        :param country: The country of this AssetAddressInformationAllOf.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def location(self):
        """Gets the location of this AssetAddressInformationAllOf.  # noqa: E501

        Location in which the address resides. example \"14852\".    # noqa: E501

        :return: The location of this AssetAddressInformationAllOf.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this AssetAddressInformationAllOf.

        Location in which the address resides. example \"14852\".    # noqa: E501

        :param location: The location of this AssetAddressInformationAllOf.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def name(self):
        """Gets the name of this AssetAddressInformationAllOf.  # noqa: E501

        Name of the user whose address is being populated.    # noqa: E501

        :return: The name of this AssetAddressInformationAllOf.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AssetAddressInformationAllOf.

        Name of the user whose address is being populated.    # noqa: E501

        :param name: The name of this AssetAddressInformationAllOf.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def postal_code(self):
        """Gets the postal_code of this AssetAddressInformationAllOf.  # noqa: E501

        Postal Code in which the address resides. example \"95164-1570\".    # noqa: E501

        :return: The postal_code of this AssetAddressInformationAllOf.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this AssetAddressInformationAllOf.

        Postal Code in which the address resides. example \"95164-1570\".    # noqa: E501

        :param postal_code: The postal_code of this AssetAddressInformationAllOf.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def state(self):
        """Gets the state of this AssetAddressInformationAllOf.  # noqa: E501

        State in which the address resides. example \"CA\".     # noqa: E501

        :return: The state of this AssetAddressInformationAllOf.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this AssetAddressInformationAllOf.

        State in which the address resides. example \"CA\".     # noqa: E501

        :param state: The state of this AssetAddressInformationAllOf.  # noqa: E501
        :type: str
        """

        self._state = state

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict()
                        if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict") else item,
                        value.items()))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AssetAddressInformationAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AssetAddressInformationAllOf):
            return True

        return self.to_dict() != other.to_dict()