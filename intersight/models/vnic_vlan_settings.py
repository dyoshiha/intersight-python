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


class VnicVlanSettings(object):
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
        'default_vlan': 'int',
        'mode': 'str'
    }

    attribute_map = {
        'object_type': 'ObjectType',
        'default_vlan': 'DefaultVlan',
        'mode': 'Mode'
    }

    def __init__(self, object_type=None, default_vlan=None, mode='ACCESS'):
        """
        VnicVlanSettings - a model defined in Swagger
        """

        self._object_type = None
        self._default_vlan = None
        self._mode = None

        if object_type is not None:
          self.object_type = object_type
        if default_vlan is not None:
          self.default_vlan = default_vlan
        if mode is not None:
          self.mode = mode

    @property
    def object_type(self):
        """
        Gets the object_type of this VnicVlanSettings.
        The concrete type of this complex type.  The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.    

        :return: The object_type of this VnicVlanSettings.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this VnicVlanSettings.
        The concrete type of this complex type.  The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.    

        :param object_type: The object_type of this VnicVlanSettings.
        :type: str
        """

        self._object_type = object_type

    @property
    def default_vlan(self):
        """
        Gets the default_vlan of this VnicVlanSettings.
        Default VLAN ID of the virtual interface. Setting the ID to 0 will not associate any default VLAN to the traffic on the virtual interface.  

        :return: The default_vlan of this VnicVlanSettings.
        :rtype: int
        """
        return self._default_vlan

    @default_vlan.setter
    def default_vlan(self, default_vlan):
        """
        Sets the default_vlan of this VnicVlanSettings.
        Default VLAN ID of the virtual interface. Setting the ID to 0 will not associate any default VLAN to the traffic on the virtual interface.  

        :param default_vlan: The default_vlan of this VnicVlanSettings.
        :type: int
        """

        self._default_vlan = default_vlan

    @property
    def mode(self):
        """
        Gets the mode of this VnicVlanSettings.
        Option to determine if the port can carry single VLAN (Access) or multiple VLANs (Trunk) traffic.   

        :return: The mode of this VnicVlanSettings.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """
        Sets the mode of this VnicVlanSettings.
        Option to determine if the port can carry single VLAN (Access) or multiple VLANs (Trunk) traffic.   

        :param mode: The mode of this VnicVlanSettings.
        :type: str
        """
        allowed_values = ["ACCESS", "TRUNK"]
        if mode not in allowed_values:
            raise ValueError(
                "Invalid value for `mode` ({0}), must be one of {1}"
                .format(mode, allowed_values)
            )

        self._mode = mode

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
        if not isinstance(other, VnicVlanSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
