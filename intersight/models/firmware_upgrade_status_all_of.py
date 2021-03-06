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


class FirmwareUpgradeStatusAllOf(object):
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
        'download_error': 'str',
        'download_percentage': 'int',
        'download_stage': 'str',
        'download_status': 'str',
        'ep_power_status': 'str',
        'overall_error': 'str',
        'overall_percentage': 'int',
        'overallstatus': 'str',
        'pending_type': 'str',
        'upgrade': 'FirmwareUpgrade'
    }

    attribute_map = {
        'download_error': 'DownloadError',
        'download_percentage': 'DownloadPercentage',
        'download_stage': 'DownloadStage',
        'download_status': 'DownloadStatus',
        'ep_power_status': 'EpPowerStatus',
        'overall_error': 'OverallError',
        'overall_percentage': 'OverallPercentage',
        'overallstatus': 'Overallstatus',
        'pending_type': 'PendingType',
        'upgrade': 'Upgrade'
    }

    def __init__(self,
                 download_error=None,
                 download_percentage=None,
                 download_stage=None,
                 download_status=None,
                 ep_power_status='none',
                 overall_error=None,
                 overall_percentage=None,
                 overallstatus='none',
                 pending_type='none',
                 upgrade=None,
                 local_vars_configuration=None):  # noqa: E501
        """FirmwareUpgradeStatusAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._download_error = None
        self._download_percentage = None
        self._download_stage = None
        self._download_status = None
        self._ep_power_status = None
        self._overall_error = None
        self._overall_percentage = None
        self._overallstatus = None
        self._pending_type = None
        self._upgrade = None
        self.discriminator = None

        if download_error is not None:
            self.download_error = download_error
        if download_percentage is not None:
            self.download_percentage = download_percentage
        if download_stage is not None:
            self.download_stage = download_stage
        if download_status is not None:
            self.download_status = download_status
        if ep_power_status is not None:
            self.ep_power_status = ep_power_status
        if overall_error is not None:
            self.overall_error = overall_error
        if overall_percentage is not None:
            self.overall_percentage = overall_percentage
        if overallstatus is not None:
            self.overallstatus = overallstatus
        if pending_type is not None:
            self.pending_type = pending_type
        if upgrade is not None:
            self.upgrade = upgrade

    @property
    def download_error(self):
        """Gets the download_error of this FirmwareUpgradeStatusAllOf.  # noqa: E501

        The error message from the endpoint during the download.    # noqa: E501

        :return: The download_error of this FirmwareUpgradeStatusAllOf.  # noqa: E501
        :rtype: str
        """
        return self._download_error

    @download_error.setter
    def download_error(self, download_error):
        """Sets the download_error of this FirmwareUpgradeStatusAllOf.

        The error message from the endpoint during the download.    # noqa: E501

        :param download_error: The download_error of this FirmwareUpgradeStatusAllOf.  # noqa: E501
        :type: str
        """

        self._download_error = download_error

    @property
    def download_percentage(self):
        """Gets the download_percentage of this FirmwareUpgradeStatusAllOf.  # noqa: E501

        The percentage of the image downloaded in the endpoint.    # noqa: E501

        :return: The download_percentage of this FirmwareUpgradeStatusAllOf.  # noqa: E501
        :rtype: int
        """
        return self._download_percentage

    @download_percentage.setter
    def download_percentage(self, download_percentage):
        """Sets the download_percentage of this FirmwareUpgradeStatusAllOf.

        The percentage of the image downloaded in the endpoint.    # noqa: E501

        :param download_percentage: The download_percentage of this FirmwareUpgradeStatusAllOf.  # noqa: E501
        :type: int
        """

        self._download_percentage = download_percentage

    @property
    def download_stage(self):
        """Gets the download_stage of this FirmwareUpgradeStatusAllOf.  # noqa: E501

        The image download stages. Example:downloading, flashing.    # noqa: E501

        :return: The download_stage of this FirmwareUpgradeStatusAllOf.  # noqa: E501
        :rtype: str
        """
        return self._download_stage

    @download_stage.setter
    def download_stage(self, download_stage):
        """Sets the download_stage of this FirmwareUpgradeStatusAllOf.

        The image download stages. Example:downloading, flashing.    # noqa: E501

        :param download_stage: The download_stage of this FirmwareUpgradeStatusAllOf.  # noqa: E501
        :type: str
        """

        self._download_stage = download_stage

    @property
    def download_status(self):
        """Gets the download_status of this FirmwareUpgradeStatusAllOf.  # noqa: E501

        The download status of the image in the endpoint.    # noqa: E501

        :return: The download_status of this FirmwareUpgradeStatusAllOf.  # noqa: E501
        :rtype: str
        """
        return self._download_status

    @download_status.setter
    def download_status(self, download_status):
        """Sets the download_status of this FirmwareUpgradeStatusAllOf.

        The download status of the image in the endpoint.    # noqa: E501

        :param download_status: The download_status of this FirmwareUpgradeStatusAllOf.  # noqa: E501
        :type: str
        """

        self._download_status = download_status

    @property
    def ep_power_status(self):
        """Gets the ep_power_status of this FirmwareUpgradeStatusAllOf.  # noqa: E501

        The server power status after the upgrade request is submitted in the endpoint.    # noqa: E501

        :return: The ep_power_status of this FirmwareUpgradeStatusAllOf.  # noqa: E501
        :rtype: str
        """
        return self._ep_power_status

    @ep_power_status.setter
    def ep_power_status(self, ep_power_status):
        """Sets the ep_power_status of this FirmwareUpgradeStatusAllOf.

        The server power status after the upgrade request is submitted in the endpoint.    # noqa: E501

        :param ep_power_status: The ep_power_status of this FirmwareUpgradeStatusAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["none", "powered on", "powered off"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and ep_power_status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `ep_power_status` ({0}), must be one of {1}"  # noqa: E501
                .format(ep_power_status, allowed_values))

        self._ep_power_status = ep_power_status

    @property
    def overall_error(self):
        """Gets the overall_error of this FirmwareUpgradeStatusAllOf.  # noqa: E501

        The reason for the operation failure.    # noqa: E501

        :return: The overall_error of this FirmwareUpgradeStatusAllOf.  # noqa: E501
        :rtype: str
        """
        return self._overall_error

    @overall_error.setter
    def overall_error(self, overall_error):
        """Sets the overall_error of this FirmwareUpgradeStatusAllOf.

        The reason for the operation failure.    # noqa: E501

        :param overall_error: The overall_error of this FirmwareUpgradeStatusAllOf.  # noqa: E501
        :type: str
        """

        self._overall_error = overall_error

    @property
    def overall_percentage(self):
        """Gets the overall_percentage of this FirmwareUpgradeStatusAllOf.  # noqa: E501

        The overall percentage of the operation.    # noqa: E501

        :return: The overall_percentage of this FirmwareUpgradeStatusAllOf.  # noqa: E501
        :rtype: int
        """
        return self._overall_percentage

    @overall_percentage.setter
    def overall_percentage(self, overall_percentage):
        """Sets the overall_percentage of this FirmwareUpgradeStatusAllOf.

        The overall percentage of the operation.    # noqa: E501

        :param overall_percentage: The overall_percentage of this FirmwareUpgradeStatusAllOf.  # noqa: E501
        :type: int
        """

        self._overall_percentage = overall_percentage

    @property
    def overallstatus(self):
        """Gets the overallstatus of this FirmwareUpgradeStatusAllOf.  # noqa: E501

        The overall status of the operation.    # noqa: E501

        :return: The overallstatus of this FirmwareUpgradeStatusAllOf.  # noqa: E501
        :rtype: str
        """
        return self._overallstatus

    @overallstatus.setter
    def overallstatus(self, overallstatus):
        """Sets the overallstatus of this FirmwareUpgradeStatusAllOf.

        The overall status of the operation.    # noqa: E501

        :param overallstatus: The overallstatus of this FirmwareUpgradeStatusAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "none", "started", "download initiating", "download initiated",
            "downloading", "downloaded", "upgrade initiating",
            "upgrade initiated", "upgrading", "upgraded", "success", "failed",
            "pending"
        ]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and overallstatus not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `overallstatus` ({0}), must be one of {1}"  # noqa: E501
                .format(overallstatus, allowed_values))

        self._overallstatus = overallstatus

    @property
    def pending_type(self):
        """Gets the pending_type of this FirmwareUpgradeStatusAllOf.  # noqa: E501

        Pending reason for the upgrade waiting.     # noqa: E501

        :return: The pending_type of this FirmwareUpgradeStatusAllOf.  # noqa: E501
        :rtype: str
        """
        return self._pending_type

    @pending_type.setter
    def pending_type(self, pending_type):
        """Sets the pending_type of this FirmwareUpgradeStatusAllOf.

        Pending reason for the upgrade waiting.     # noqa: E501

        :param pending_type: The pending_type of this FirmwareUpgradeStatusAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["none", "pending for next reboot"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and pending_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `pending_type` ({0}), must be one of {1}"  # noqa: E501
                .format(pending_type, allowed_values))

        self._pending_type = pending_type

    @property
    def upgrade(self):
        """Gets the upgrade of this FirmwareUpgradeStatusAllOf.  # noqa: E501


        :return: The upgrade of this FirmwareUpgradeStatusAllOf.  # noqa: E501
        :rtype: FirmwareUpgrade
        """
        return self._upgrade

    @upgrade.setter
    def upgrade(self, upgrade):
        """Sets the upgrade of this FirmwareUpgradeStatusAllOf.


        :param upgrade: The upgrade of this FirmwareUpgradeStatusAllOf.  # noqa: E501
        :type: FirmwareUpgrade
        """

        self._upgrade = upgrade

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
        if not isinstance(other, FirmwareUpgradeStatusAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FirmwareUpgradeStatusAllOf):
            return True

        return self.to_dict() != other.to_dict()
