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


class StorageReplicationScheduleAllOf(object):
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
        'frequency': 'str',
        'name': 'str',
        'replication_time': 'str',
        'retention_time': 'str',
        'protection_group': 'StorageProtectionGroup',
        'storage_array': 'StorageGenericArray'
    }

    attribute_map = {
        'frequency': 'Frequency',
        'name': 'Name',
        'replication_time': 'ReplicationTime',
        'retention_time': 'RetentionTime',
        'protection_group': 'ProtectionGroup',
        'storage_array': 'StorageArray'
    }

    def __init__(self,
                 frequency=None,
                 name=None,
                 replication_time=None,
                 retention_time=None,
                 protection_group=None,
                 storage_array=None,
                 local_vars_configuration=None):  # noqa: E501
        """StorageReplicationScheduleAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._frequency = None
        self._name = None
        self._replication_time = None
        self._retention_time = None
        self._protection_group = None
        self._storage_array = None
        self.discriminator = None

        if frequency is not None:
            self.frequency = frequency
        if name is not None:
            self.name = name
        if replication_time is not None:
            self.replication_time = replication_time
        if retention_time is not None:
            self.retention_time = retention_time
        if protection_group is not None:
            self.protection_group = protection_group
        if storage_array is not None:
            self.storage_array = storage_array

    @property
    def frequency(self):
        """Gets the frequency of this StorageReplicationScheduleAllOf.  # noqa: E501

        Replication frequency. It is an interval on which replication is set to trigger. Examples:     PT2H, Snapshot is performed for every 2 hours.     P30D, Snapshot is scheduled for every 30 days.     PT2H34M56.123S is 2 hours, 34 minutes, 56 seconds and 123 milliseconds.     # noqa: E501

        :return: The frequency of this StorageReplicationScheduleAllOf.  # noqa: E501
        :rtype: str
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this StorageReplicationScheduleAllOf.

        Replication frequency. It is an interval on which replication is set to trigger. Examples:     PT2H, Snapshot is performed for every 2 hours.     P30D, Snapshot is scheduled for every 30 days.     PT2H34M56.123S is 2 hours, 34 minutes, 56 seconds and 123 milliseconds.     # noqa: E501

        :param frequency: The frequency of this StorageReplicationScheduleAllOf.  # noqa: E501
        :type: str
        """

        self._frequency = frequency

    @property
    def name(self):
        """Gets the name of this StorageReplicationScheduleAllOf.  # noqa: E501

        Replication schedule name.    # noqa: E501

        :return: The name of this StorageReplicationScheduleAllOf.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StorageReplicationScheduleAllOf.

        Replication schedule name.    # noqa: E501

        :param name: The name of this StorageReplicationScheduleAllOf.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def replication_time(self):
        """Gets the replication_time of this StorageReplicationScheduleAllOf.  # noqa: E501

        Preferred time of day at which to replicate the snapshots on target array. It is applicable only if the replication frequency is set for a day or more. Format: hh:mm:ss Example: 15:00:00, Replication is set for 3:00 PM.     # noqa: E501

        :return: The replication_time of this StorageReplicationScheduleAllOf.  # noqa: E501
        :rtype: str
        """
        return self._replication_time

    @replication_time.setter
    def replication_time(self, replication_time):
        """Sets the replication_time of this StorageReplicationScheduleAllOf.

        Preferred time of day at which to replicate the snapshots on target array. It is applicable only if the replication frequency is set for a day or more. Format: hh:mm:ss Example: 15:00:00, Replication is set for 3:00 PM.     # noqa: E501

        :param replication_time: The replication_time of this StorageReplicationScheduleAllOf.  # noqa: E501
        :type: str
        """

        self._replication_time = replication_time

    @property
    def retention_time(self):
        """Gets the retention_time of this StorageReplicationScheduleAllOf.  # noqa: E501

        Duration to keep the replicated snapshots on the targets. Replicated snapshots are deleted from target array once mentioned rentention period is elapsed. Examples: P30D, Snapshots are available for 30 days. PT2H34M56.123S, 2 hours, 34 minutes, 56 seconds and 123 milliseconds.      # noqa: E501

        :return: The retention_time of this StorageReplicationScheduleAllOf.  # noqa: E501
        :rtype: str
        """
        return self._retention_time

    @retention_time.setter
    def retention_time(self, retention_time):
        """Sets the retention_time of this StorageReplicationScheduleAllOf.

        Duration to keep the replicated snapshots on the targets. Replicated snapshots are deleted from target array once mentioned rentention period is elapsed. Examples: P30D, Snapshots are available for 30 days. PT2H34M56.123S, 2 hours, 34 minutes, 56 seconds and 123 milliseconds.      # noqa: E501

        :param retention_time: The retention_time of this StorageReplicationScheduleAllOf.  # noqa: E501
        :type: str
        """

        self._retention_time = retention_time

    @property
    def protection_group(self):
        """Gets the protection_group of this StorageReplicationScheduleAllOf.  # noqa: E501


        :return: The protection_group of this StorageReplicationScheduleAllOf.  # noqa: E501
        :rtype: StorageProtectionGroup
        """
        return self._protection_group

    @protection_group.setter
    def protection_group(self, protection_group):
        """Sets the protection_group of this StorageReplicationScheduleAllOf.


        :param protection_group: The protection_group of this StorageReplicationScheduleAllOf.  # noqa: E501
        :type: StorageProtectionGroup
        """

        self._protection_group = protection_group

    @property
    def storage_array(self):
        """Gets the storage_array of this StorageReplicationScheduleAllOf.  # noqa: E501


        :return: The storage_array of this StorageReplicationScheduleAllOf.  # noqa: E501
        :rtype: StorageGenericArray
        """
        return self._storage_array

    @storage_array.setter
    def storage_array(self, storage_array):
        """Sets the storage_array of this StorageReplicationScheduleAllOf.


        :param storage_array: The storage_array of this StorageReplicationScheduleAllOf.  # noqa: E501
        :type: StorageGenericArray
        """

        self._storage_array = storage_array

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
        if not isinstance(other, StorageReplicationScheduleAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StorageReplicationScheduleAllOf):
            return True

        return self.to_dict() != other.to_dict()
