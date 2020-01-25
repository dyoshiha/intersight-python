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


class FaultInstanceAllOf(object):
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
        'acknowledged': 'str',
        'affected_dn': 'str',
        'affected_mo_id': 'str',
        'affected_mo_type': 'str',
        'ancestor_mo_id': 'str',
        'ancestor_mo_type': 'str',
        'code': 'str',
        'creation_time': 'str',
        'description': 'str',
        'last_transition_time': 'str',
        'num_occurrences': 'int',
        'original_severity': 'str',
        'previous_severity': 'str',
        'rule': 'str',
        'severity': 'str',
        'registered_device': 'AssetDeviceRegistration'
    }

    attribute_map = {
        'acknowledged': 'Acknowledged',
        'affected_dn': 'AffectedDn',
        'affected_mo_id': 'AffectedMoId',
        'affected_mo_type': 'AffectedMoType',
        'ancestor_mo_id': 'AncestorMoId',
        'ancestor_mo_type': 'AncestorMoType',
        'code': 'Code',
        'creation_time': 'CreationTime',
        'description': 'Description',
        'last_transition_time': 'LastTransitionTime',
        'num_occurrences': 'NumOccurrences',
        'original_severity': 'OriginalSeverity',
        'previous_severity': 'PreviousSeverity',
        'rule': 'Rule',
        'severity': 'Severity',
        'registered_device': 'RegisteredDevice'
    }

    def __init__(self,
                 acknowledged=None,
                 affected_dn=None,
                 affected_mo_id=None,
                 affected_mo_type=None,
                 ancestor_mo_id=None,
                 ancestor_mo_type=None,
                 code=None,
                 creation_time=None,
                 description=None,
                 last_transition_time=None,
                 num_occurrences=None,
                 original_severity=None,
                 previous_severity=None,
                 rule=None,
                 severity=None,
                 registered_device=None,
                 local_vars_configuration=None):  # noqa: E501
        """FaultInstanceAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._acknowledged = None
        self._affected_dn = None
        self._affected_mo_id = None
        self._affected_mo_type = None
        self._ancestor_mo_id = None
        self._ancestor_mo_type = None
        self._code = None
        self._creation_time = None
        self._description = None
        self._last_transition_time = None
        self._num_occurrences = None
        self._original_severity = None
        self._previous_severity = None
        self._rule = None
        self._severity = None
        self._registered_device = None
        self.discriminator = None

        if acknowledged is not None:
            self.acknowledged = acknowledged
        if affected_dn is not None:
            self.affected_dn = affected_dn
        if affected_mo_id is not None:
            self.affected_mo_id = affected_mo_id
        if affected_mo_type is not None:
            self.affected_mo_type = affected_mo_type
        if ancestor_mo_id is not None:
            self.ancestor_mo_id = ancestor_mo_id
        if ancestor_mo_type is not None:
            self.ancestor_mo_type = ancestor_mo_type
        if code is not None:
            self.code = code
        if creation_time is not None:
            self.creation_time = creation_time
        if description is not None:
            self.description = description
        if last_transition_time is not None:
            self.last_transition_time = last_transition_time
        if num_occurrences is not None:
            self.num_occurrences = num_occurrences
        if original_severity is not None:
            self.original_severity = original_severity
        if previous_severity is not None:
            self.previous_severity = previous_severity
        if rule is not None:
            self.rule = rule
        if severity is not None:
            self.severity = severity
        if registered_device is not None:
            self.registered_device = registered_device

    @property
    def acknowledged(self):
        """Gets the acknowledged of this FaultInstanceAllOf.  # noqa: E501


        :return: The acknowledged of this FaultInstanceAllOf.  # noqa: E501
        :rtype: str
        """
        return self._acknowledged

    @acknowledged.setter
    def acknowledged(self, acknowledged):
        """Sets the acknowledged of this FaultInstanceAllOf.


        :param acknowledged: The acknowledged of this FaultInstanceAllOf.  # noqa: E501
        :type: str
        """

        self._acknowledged = acknowledged

    @property
    def affected_dn(self):
        """Gets the affected_dn of this FaultInstanceAllOf.  # noqa: E501


        :return: The affected_dn of this FaultInstanceAllOf.  # noqa: E501
        :rtype: str
        """
        return self._affected_dn

    @affected_dn.setter
    def affected_dn(self, affected_dn):
        """Sets the affected_dn of this FaultInstanceAllOf.


        :param affected_dn: The affected_dn of this FaultInstanceAllOf.  # noqa: E501
        :type: str
        """

        self._affected_dn = affected_dn

    @property
    def affected_mo_id(self):
        """Gets the affected_mo_id of this FaultInstanceAllOf.  # noqa: E501

        Managed object Id which was affected.    # noqa: E501

        :return: The affected_mo_id of this FaultInstanceAllOf.  # noqa: E501
        :rtype: str
        """
        return self._affected_mo_id

    @affected_mo_id.setter
    def affected_mo_id(self, affected_mo_id):
        """Sets the affected_mo_id of this FaultInstanceAllOf.

        Managed object Id which was affected.    # noqa: E501

        :param affected_mo_id: The affected_mo_id of this FaultInstanceAllOf.  # noqa: E501
        :type: str
        """

        self._affected_mo_id = affected_mo_id

    @property
    def affected_mo_type(self):
        """Gets the affected_mo_type of this FaultInstanceAllOf.  # noqa: E501

        Managed object type which was affected.    # noqa: E501

        :return: The affected_mo_type of this FaultInstanceAllOf.  # noqa: E501
        :rtype: str
        """
        return self._affected_mo_type

    @affected_mo_type.setter
    def affected_mo_type(self, affected_mo_type):
        """Sets the affected_mo_type of this FaultInstanceAllOf.

        Managed object type which was affected.    # noqa: E501

        :param affected_mo_type: The affected_mo_type of this FaultInstanceAllOf.  # noqa: E501
        :type: str
        """

        self._affected_mo_type = affected_mo_type

    @property
    def ancestor_mo_id(self):
        """Gets the ancestor_mo_id of this FaultInstanceAllOf.  # noqa: E501


        :return: The ancestor_mo_id of this FaultInstanceAllOf.  # noqa: E501
        :rtype: str
        """
        return self._ancestor_mo_id

    @ancestor_mo_id.setter
    def ancestor_mo_id(self, ancestor_mo_id):
        """Sets the ancestor_mo_id of this FaultInstanceAllOf.


        :param ancestor_mo_id: The ancestor_mo_id of this FaultInstanceAllOf.  # noqa: E501
        :type: str
        """

        self._ancestor_mo_id = ancestor_mo_id

    @property
    def ancestor_mo_type(self):
        """Gets the ancestor_mo_type of this FaultInstanceAllOf.  # noqa: E501


        :return: The ancestor_mo_type of this FaultInstanceAllOf.  # noqa: E501
        :rtype: str
        """
        return self._ancestor_mo_type

    @ancestor_mo_type.setter
    def ancestor_mo_type(self, ancestor_mo_type):
        """Sets the ancestor_mo_type of this FaultInstanceAllOf.


        :param ancestor_mo_type: The ancestor_mo_type of this FaultInstanceAllOf.  # noqa: E501
        :type: str
        """

        self._ancestor_mo_type = ancestor_mo_type

    @property
    def code(self):
        """Gets the code of this FaultInstanceAllOf.  # noqa: E501


        :return: The code of this FaultInstanceAllOf.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this FaultInstanceAllOf.


        :param code: The code of this FaultInstanceAllOf.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def creation_time(self):
        """Gets the creation_time of this FaultInstanceAllOf.  # noqa: E501


        :return: The creation_time of this FaultInstanceAllOf.  # noqa: E501
        :rtype: str
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this FaultInstanceAllOf.


        :param creation_time: The creation_time of this FaultInstanceAllOf.  # noqa: E501
        :type: str
        """

        self._creation_time = creation_time

    @property
    def description(self):
        """Gets the description of this FaultInstanceAllOf.  # noqa: E501

        Short summary of the fault found.    # noqa: E501

        :return: The description of this FaultInstanceAllOf.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FaultInstanceAllOf.

        Short summary of the fault found.    # noqa: E501

        :param description: The description of this FaultInstanceAllOf.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def last_transition_time(self):
        """Gets the last_transition_time of this FaultInstanceAllOf.  # noqa: E501


        :return: The last_transition_time of this FaultInstanceAllOf.  # noqa: E501
        :rtype: str
        """
        return self._last_transition_time

    @last_transition_time.setter
    def last_transition_time(self, last_transition_time):
        """Sets the last_transition_time of this FaultInstanceAllOf.


        :param last_transition_time: The last_transition_time of this FaultInstanceAllOf.  # noqa: E501
        :type: str
        """

        self._last_transition_time = last_transition_time

    @property
    def num_occurrences(self):
        """Gets the num_occurrences of this FaultInstanceAllOf.  # noqa: E501


        :return: The num_occurrences of this FaultInstanceAllOf.  # noqa: E501
        :rtype: int
        """
        return self._num_occurrences

    @num_occurrences.setter
    def num_occurrences(self, num_occurrences):
        """Sets the num_occurrences of this FaultInstanceAllOf.


        :param num_occurrences: The num_occurrences of this FaultInstanceAllOf.  # noqa: E501
        :type: int
        """

        self._num_occurrences = num_occurrences

    @property
    def original_severity(self):
        """Gets the original_severity of this FaultInstanceAllOf.  # noqa: E501


        :return: The original_severity of this FaultInstanceAllOf.  # noqa: E501
        :rtype: str
        """
        return self._original_severity

    @original_severity.setter
    def original_severity(self, original_severity):
        """Sets the original_severity of this FaultInstanceAllOf.


        :param original_severity: The original_severity of this FaultInstanceAllOf.  # noqa: E501
        :type: str
        """

        self._original_severity = original_severity

    @property
    def previous_severity(self):
        """Gets the previous_severity of this FaultInstanceAllOf.  # noqa: E501


        :return: The previous_severity of this FaultInstanceAllOf.  # noqa: E501
        :rtype: str
        """
        return self._previous_severity

    @previous_severity.setter
    def previous_severity(self, previous_severity):
        """Sets the previous_severity of this FaultInstanceAllOf.


        :param previous_severity: The previous_severity of this FaultInstanceAllOf.  # noqa: E501
        :type: str
        """

        self._previous_severity = previous_severity

    @property
    def rule(self):
        """Gets the rule of this FaultInstanceAllOf.  # noqa: E501


        :return: The rule of this FaultInstanceAllOf.  # noqa: E501
        :rtype: str
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """Sets the rule of this FaultInstanceAllOf.


        :param rule: The rule of this FaultInstanceAllOf.  # noqa: E501
        :type: str
        """

        self._rule = rule

    @property
    def severity(self):
        """Gets the severity of this FaultInstanceAllOf.  # noqa: E501

        Severity of the fault found.     # noqa: E501

        :return: The severity of this FaultInstanceAllOf.  # noqa: E501
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this FaultInstanceAllOf.

        Severity of the fault found.     # noqa: E501

        :param severity: The severity of this FaultInstanceAllOf.  # noqa: E501
        :type: str
        """

        self._severity = severity

    @property
    def registered_device(self):
        """Gets the registered_device of this FaultInstanceAllOf.  # noqa: E501


        :return: The registered_device of this FaultInstanceAllOf.  # noqa: E501
        :rtype: AssetDeviceRegistration
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """Sets the registered_device of this FaultInstanceAllOf.


        :param registered_device: The registered_device of this FaultInstanceAllOf.  # noqa: E501
        :type: AssetDeviceRegistration
        """

        self._registered_device = registered_device

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
        if not isinstance(other, FaultInstanceAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FaultInstanceAllOf):
            return True

        return self.to_dict() != other.to_dict()