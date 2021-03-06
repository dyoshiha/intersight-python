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


class VnicUsnicSettings(object):
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
        'cos': 'int',
        'count': 'int',
        'usnic_adapter_policy': 'str'
    }

    attribute_map = {
        'object_type': 'ObjectType',
        'cos': 'Cos',
        'count': 'Count',
        'usnic_adapter_policy': 'UsnicAdapterPolicy'
    }

    def __init__(self, object_type=None, cos=None, count=None, usnic_adapter_policy=None):
        """
        VnicUsnicSettings - a model defined in Swagger
        """

        self._object_type = None
        self._cos = None
        self._count = None
        self._usnic_adapter_policy = None

        if object_type is not None:
          self.object_type = object_type
        if cos is not None:
          self.cos = cos
        if count is not None:
          self.count = count
        if usnic_adapter_policy is not None:
          self.usnic_adapter_policy = usnic_adapter_policy

    @property
    def object_type(self):
        """
        Gets the object_type of this VnicUsnicSettings.
        The concrete type of this complex type.  The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.    

        :return: The object_type of this VnicUsnicSettings.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this VnicUsnicSettings.
        The concrete type of this complex type.  The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.    

        :param object_type: The object_type of this VnicUsnicSettings.
        :type: str
        """

        self._object_type = object_type

    @property
    def cos(self):
        """
        Gets the cos of this VnicUsnicSettings.
        Class of Service to be used for traffic on the usNIC.  

        :return: The cos of this VnicUsnicSettings.
        :rtype: int
        """
        return self._cos

    @cos.setter
    def cos(self, cos):
        """
        Sets the cos of this VnicUsnicSettings.
        Class of Service to be used for traffic on the usNIC.  

        :param cos: The cos of this VnicUsnicSettings.
        :type: int
        """

        self._cos = cos

    @property
    def count(self):
        """
        Gets the count of this VnicUsnicSettings.
        Number of usNIC interfaces to be created.  

        :return: The count of this VnicUsnicSettings.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this VnicUsnicSettings.
        Number of usNIC interfaces to be created.  

        :param count: The count of this VnicUsnicSettings.
        :type: int
        """

        self._count = count

    @property
    def usnic_adapter_policy(self):
        """
        Gets the usnic_adapter_policy of this VnicUsnicSettings.
        Ethernet Adapter policy to be associated with the usNICs.   

        :return: The usnic_adapter_policy of this VnicUsnicSettings.
        :rtype: str
        """
        return self._usnic_adapter_policy

    @usnic_adapter_policy.setter
    def usnic_adapter_policy(self, usnic_adapter_policy):
        """
        Sets the usnic_adapter_policy of this VnicUsnicSettings.
        Ethernet Adapter policy to be associated with the usNICs.   

        :param usnic_adapter_policy: The usnic_adapter_policy of this VnicUsnicSettings.
        :type: str
        """

        self._usnic_adapter_policy = usnic_adapter_policy

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
        if not isinstance(other, VnicUsnicSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
