# coding: utf-8

"""
    Intersight REST API

    This is Intersight REST API 

    OpenAPI spec version: 1.0.9-961
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PkixDistinguishedName(object):
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
        'common_name': 'str',
        'country': 'list[str]',
        'locality': 'list[str]',
        'organization': 'list[str]',
        'organizational_unit': 'list[str]',
        'state': 'list[str]'
    }

    attribute_map = {
        'common_name': 'CommonName',
        'country': 'Country',
        'locality': 'Locality',
        'organization': 'Organization',
        'organizational_unit': 'OrganizationalUnit',
        'state': 'State'
    }

    def __init__(self, common_name=None, country=None, locality=None, organization=None, organizational_unit=None, state=None):
        """
        PkixDistinguishedName - a model defined in Swagger
        """

        self._common_name = None
        self._country = None
        self._locality = None
        self._organization = None
        self._organizational_unit = None
        self._state = None

        if common_name is not None:
          self.common_name = common_name
        if country is not None:
          self.country = country
        if locality is not None:
          self.locality = locality
        if organization is not None:
          self.organization = organization
        if organizational_unit is not None:
          self.organizational_unit = organizational_unit
        if state is not None:
          self.state = state

    @property
    def common_name(self):
        """
        Gets the common_name of this PkixDistinguishedName.
        A required component that identifies a person or an object.  

        :return: The common_name of this PkixDistinguishedName.
        :rtype: str
        """
        return self._common_name

    @common_name.setter
    def common_name(self, common_name):
        """
        Sets the common_name of this PkixDistinguishedName.
        A required component that identifies a person or an object.  

        :param common_name: The common_name of this PkixDistinguishedName.
        :type: str
        """

        self._common_name = common_name

    @property
    def country(self):
        """
        Gets the country of this PkixDistinguishedName.
        Identifier for the country in which the entity resides.  

        :return: The country of this PkixDistinguishedName.
        :rtype: list[str]
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this PkixDistinguishedName.
        Identifier for the country in which the entity resides.  

        :param country: The country of this PkixDistinguishedName.
        :type: list[str]
        """

        self._country = country

    @property
    def locality(self):
        """
        Gets the locality of this PkixDistinguishedName.
        Identifier for the place where the entry resides. The locality can be a city, county, township, or other geographic region.  

        :return: The locality of this PkixDistinguishedName.
        :rtype: list[str]
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        """
        Sets the locality of this PkixDistinguishedName.
        Identifier for the place where the entry resides. The locality can be a city, county, township, or other geographic region.  

        :param locality: The locality of this PkixDistinguishedName.
        :type: list[str]
        """

        self._locality = locality

    @property
    def organization(self):
        """
        Gets the organization of this PkixDistinguishedName.
        Identifier for the organization in which the entity resides.  

        :return: The organization of this PkixDistinguishedName.
        :rtype: list[str]
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """
        Sets the organization of this PkixDistinguishedName.
        Identifier for the organization in which the entity resides.  

        :param organization: The organization of this PkixDistinguishedName.
        :type: list[str]
        """

        self._organization = organization

    @property
    def organizational_unit(self):
        """
        Gets the organizational_unit of this PkixDistinguishedName.
        Identifier for a unit within the organization.  

        :return: The organizational_unit of this PkixDistinguishedName.
        :rtype: list[str]
        """
        return self._organizational_unit

    @organizational_unit.setter
    def organizational_unit(self, organizational_unit):
        """
        Sets the organizational_unit of this PkixDistinguishedName.
        Identifier for a unit within the organization.  

        :param organizational_unit: The organizational_unit of this PkixDistinguishedName.
        :type: list[str]
        """

        self._organizational_unit = organizational_unit

    @property
    def state(self):
        """
        Gets the state of this PkixDistinguishedName.
        Identifier for the state or province of the entity.   

        :return: The state of this PkixDistinguishedName.
        :rtype: list[str]
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this PkixDistinguishedName.
        Identifier for the state or province of the entity.   

        :param state: The state of this PkixDistinguishedName.
        :type: list[str]
        """

        self._state = state

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
        if not isinstance(other, PkixDistinguishedName):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other