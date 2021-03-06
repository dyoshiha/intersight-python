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


class StorageStorageArrayUtilizationAllOf(object):
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
        'data_reduction': 'float',
        'parity': 'float',
        'provisioned': 'int',
        'shared': 'int',
        'snapshot': 'int',
        'system': 'int',
        'thin_provisioned': 'float',
        'total_reduction': 'float',
        'volume': 'int'
    }

    attribute_map = {
        'data_reduction': 'DataReduction',
        'parity': 'Parity',
        'provisioned': 'Provisioned',
        'shared': 'Shared',
        'snapshot': 'Snapshot',
        'system': 'System',
        'thin_provisioned': 'ThinProvisioned',
        'total_reduction': 'TotalReduction',
        'volume': 'Volume'
    }

    def __init__(self,
                 data_reduction=None,
                 parity=None,
                 provisioned=None,
                 shared=None,
                 snapshot=None,
                 system=None,
                 thin_provisioned=None,
                 total_reduction=None,
                 volume=None,
                 local_vars_configuration=None):  # noqa: E501
        """StorageStorageArrayUtilizationAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._data_reduction = None
        self._parity = None
        self._provisioned = None
        self._shared = None
        self._snapshot = None
        self._system = None
        self._thin_provisioned = None
        self._total_reduction = None
        self._volume = None
        self.discriminator = None

        if data_reduction is not None:
            self.data_reduction = data_reduction
        if parity is not None:
            self.parity = parity
        if provisioned is not None:
            self.provisioned = provisioned
        if shared is not None:
            self.shared = shared
        if snapshot is not None:
            self.snapshot = snapshot
        if system is not None:
            self.system = system
        if thin_provisioned is not None:
            self.thin_provisioned = thin_provisioned
        if total_reduction is not None:
            self.total_reduction = total_reduction
        if volume is not None:
            self.volume = volume

    @property
    def data_reduction(self):
        """Gets the data_reduction of this StorageStorageArrayUtilizationAllOf.  # noqa: E501

        Ratio of mapped sectors within a volume versus the amount of physical space the data occupies after data compression and deduplication. The data reduction ratio does not include thin provisioning savings. For example, a data reduction ratio of 5.0 means that for every 5 MB the host writes to the array, 1 MB is stored on the array's flash modules.    # noqa: E501

        :return: The data_reduction of this StorageStorageArrayUtilizationAllOf.  # noqa: E501
        :rtype: float
        """
        return self._data_reduction

    @data_reduction.setter
    def data_reduction(self, data_reduction):
        """Sets the data_reduction of this StorageStorageArrayUtilizationAllOf.

        Ratio of mapped sectors within a volume versus the amount of physical space the data occupies after data compression and deduplication. The data reduction ratio does not include thin provisioning savings. For example, a data reduction ratio of 5.0 means that for every 5 MB the host writes to the array, 1 MB is stored on the array's flash modules.    # noqa: E501

        :param data_reduction: The data_reduction of this StorageStorageArrayUtilizationAllOf.  # noqa: E501
        :type: float
        """

        self._data_reduction = data_reduction

    @property
    def parity(self):
        """Gets the parity of this StorageStorageArrayUtilizationAllOf.  # noqa: E501

        Percentage of data that is fully protected. The percentage value will drop below 100% if the data is not fully protected.    # noqa: E501

        :return: The parity of this StorageStorageArrayUtilizationAllOf.  # noqa: E501
        :rtype: float
        """
        return self._parity

    @parity.setter
    def parity(self, parity):
        """Sets the parity of this StorageStorageArrayUtilizationAllOf.

        Percentage of data that is fully protected. The percentage value will drop below 100% if the data is not fully protected.    # noqa: E501

        :param parity: The parity of this StorageStorageArrayUtilizationAllOf.  # noqa: E501
        :type: float
        """

        self._parity = parity

    @property
    def provisioned(self):
        """Gets the provisioned of this StorageStorageArrayUtilizationAllOf.  # noqa: E501

        Total provisioned storage capacity in Pure FlashArray, represented in bytes.    # noqa: E501

        :return: The provisioned of this StorageStorageArrayUtilizationAllOf.  # noqa: E501
        :rtype: int
        """
        return self._provisioned

    @provisioned.setter
    def provisioned(self, provisioned):
        """Sets the provisioned of this StorageStorageArrayUtilizationAllOf.

        Total provisioned storage capacity in Pure FlashArray, represented in bytes.    # noqa: E501

        :param provisioned: The provisioned of this StorageStorageArrayUtilizationAllOf.  # noqa: E501
        :type: int
        """

        self._provisioned = provisioned

    @property
    def shared(self):
        """Gets the shared of this StorageStorageArrayUtilizationAllOf.  # noqa: E501

        Physical space occupied by deduplicated data, represented in bytes. The space is shared with other volumes and snapshots as a result of data deduplication.    # noqa: E501

        :return: The shared of this StorageStorageArrayUtilizationAllOf.  # noqa: E501
        :rtype: int
        """
        return self._shared

    @shared.setter
    def shared(self, shared):
        """Sets the shared of this StorageStorageArrayUtilizationAllOf.

        Physical space occupied by deduplicated data, represented in bytes. The space is shared with other volumes and snapshots as a result of data deduplication.    # noqa: E501

        :param shared: The shared of this StorageStorageArrayUtilizationAllOf.  # noqa: E501
        :type: int
        """

        self._shared = shared

    @property
    def snapshot(self):
        """Gets the snapshot of this StorageStorageArrayUtilizationAllOf.  # noqa: E501

        Physical space occupied by the snapshots, represented in bytes.    # noqa: E501

        :return: The snapshot of this StorageStorageArrayUtilizationAllOf.  # noqa: E501
        :rtype: int
        """
        return self._snapshot

    @snapshot.setter
    def snapshot(self, snapshot):
        """Sets the snapshot of this StorageStorageArrayUtilizationAllOf.

        Physical space occupied by the snapshots, represented in bytes.    # noqa: E501

        :param snapshot: The snapshot of this StorageStorageArrayUtilizationAllOf.  # noqa: E501
        :type: int
        """

        self._snapshot = snapshot

    @property
    def system(self):
        """Gets the system of this StorageStorageArrayUtilizationAllOf.  # noqa: E501

        Physical space occupied by internal array metadata, represented in bytes.    # noqa: E501

        :return: The system of this StorageStorageArrayUtilizationAllOf.  # noqa: E501
        :rtype: int
        """
        return self._system

    @system.setter
    def system(self, system):
        """Sets the system of this StorageStorageArrayUtilizationAllOf.

        Physical space occupied by internal array metadata, represented in bytes.    # noqa: E501

        :param system: The system of this StorageStorageArrayUtilizationAllOf.  # noqa: E501
        :type: int
        """

        self._system = system

    @property
    def thin_provisioned(self):
        """Gets the thin_provisioned of this StorageStorageArrayUtilizationAllOf.  # noqa: E501

        Percentage of volume sectors that do not contain host-written data because the hosts have not written data to them or the sectors have been explicitly trimmed.    # noqa: E501

        :return: The thin_provisioned of this StorageStorageArrayUtilizationAllOf.  # noqa: E501
        :rtype: float
        """
        return self._thin_provisioned

    @thin_provisioned.setter
    def thin_provisioned(self, thin_provisioned):
        """Sets the thin_provisioned of this StorageStorageArrayUtilizationAllOf.

        Percentage of volume sectors that do not contain host-written data because the hosts have not written data to them or the sectors have been explicitly trimmed.    # noqa: E501

        :param thin_provisioned: The thin_provisioned of this StorageStorageArrayUtilizationAllOf.  # noqa: E501
        :type: float
        """

        self._thin_provisioned = thin_provisioned

    @property
    def total_reduction(self):
        """Gets the total_reduction of this StorageStorageArrayUtilizationAllOf.  # noqa: E501

        Ratio of provisioned sectors within a volume versus the amount of physical space the data occupies after reduction via data compression and deduplication and with thin provisioning savings. Total reduction is data reduction with thin provisioning savings. For example, a total reduction ratio of 10.0 means that for every 10 MB of provisioned space, 1 MB is stored on the array's flash modules.    # noqa: E501

        :return: The total_reduction of this StorageStorageArrayUtilizationAllOf.  # noqa: E501
        :rtype: float
        """
        return self._total_reduction

    @total_reduction.setter
    def total_reduction(self, total_reduction):
        """Sets the total_reduction of this StorageStorageArrayUtilizationAllOf.

        Ratio of provisioned sectors within a volume versus the amount of physical space the data occupies after reduction via data compression and deduplication and with thin provisioning savings. Total reduction is data reduction with thin provisioning savings. For example, a total reduction ratio of 10.0 means that for every 10 MB of provisioned space, 1 MB is stored on the array's flash modules.    # noqa: E501

        :param total_reduction: The total_reduction of this StorageStorageArrayUtilizationAllOf.  # noqa: E501
        :type: float
        """

        self._total_reduction = total_reduction

    @property
    def volume(self):
        """Gets the volume of this StorageStorageArrayUtilizationAllOf.  # noqa: E501

        Physical space occupied by volume data, excluding shared, array metadata and snapshots. Size is represented in bytes.     # noqa: E501

        :return: The volume of this StorageStorageArrayUtilizationAllOf.  # noqa: E501
        :rtype: int
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this StorageStorageArrayUtilizationAllOf.

        Physical space occupied by volume data, excluding shared, array metadata and snapshots. Size is represented in bytes.     # noqa: E501

        :param volume: The volume of this StorageStorageArrayUtilizationAllOf.  # noqa: E501
        :type: int
        """

        self._volume = volume

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
        if not isinstance(other, StorageStorageArrayUtilizationAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StorageStorageArrayUtilizationAllOf):
            return True

        return self.to_dict() != other.to_dict()
