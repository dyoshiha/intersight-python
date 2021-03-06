# coding: utf-8

"""
    Cisco Intersight OpenAPI specification.

    The Cisco Intersight OpenAPI specification.

    OpenAPI spec version: 1.0.9-1295
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class BootBootloader(object):
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
        'object_type': 'str',
        'description': 'str',
        'name': 'str',
        'path': 'str'
    }

    attribute_map = {
        'object_type': 'ObjectType',
        'description': 'Description',
        'name': 'Name',
        'path': 'Path'
    }

    def __init__(self, object_type=None, description=None, name=None, path=None):
        """
        BootBootloader - a model defined in Swagger
        """

        self._object_type = None
        self._description = None
        self._name = None
        self._path = None

        if object_type is not None:
          self.object_type = object_type
        if description is not None:
          self.description = description
        if name is not None:
          self.name = name
        if path is not None:
          self.path = path

    @property
    def object_type(self):
        """
        Gets the object_type of this BootBootloader.
        The concrete type of this complex type.  The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.    

        :return: The object_type of this BootBootloader.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this BootBootloader.
        The concrete type of this complex type.  The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.    

        :param object_type: The object_type of this BootBootloader.
        :type: str
        """

        self._object_type = object_type

    @property
    def description(self):
        """
        Gets the description of this BootBootloader.
        Carries more information about the bootloader.  

        :return: The description of this BootBootloader.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this BootBootloader.
        Carries more information about the bootloader.  

        :param description: The description of this BootBootloader.
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """
        Gets the name of this BootBootloader.
        Name of the bootloader.  

        :return: The name of this BootBootloader.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BootBootloader.
        Name of the bootloader.  

        :param name: The name of this BootBootloader.
        :type: str
        """

        self._name = name

    @property
    def path(self):
        """
        Gets the path of this BootBootloader.
        Path to the bootloader image.   

        :return: The path of this BootBootloader.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this BootBootloader.
        Path to the bootloader image.   

        :param path: The path of this BootBootloader.
        :type: str
        """

        self._path = path

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
        if not isinstance(other, BootBootloader):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
