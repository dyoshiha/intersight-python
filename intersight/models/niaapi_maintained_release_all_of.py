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


class NiaapiMaintainedReleaseAllOf(object):
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
        'maintained_release': 'str',
        'software_release': 'str',
        'version_tag': 'str'
    }

    attribute_map = {
        'maintained_release': 'MaintainedRelease',
        'software_release': 'SoftwareRelease',
        'version_tag': 'VersionTag'
    }

    def __init__(self,
                 maintained_release=None,
                 software_release=None,
                 version_tag=None,
                 local_vars_configuration=None):  # noqa: E501
        """NiaapiMaintainedReleaseAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._maintained_release = None
        self._software_release = None
        self._version_tag = None
        self.discriminator = None

        if maintained_release is not None:
            self.maintained_release = maintained_release
        if software_release is not None:
            self.software_release = software_release
        if version_tag is not None:
            self.version_tag = version_tag

    @property
    def maintained_release(self):
        """Gets the maintained_release of this NiaapiMaintainedReleaseAllOf.  # noqa: E501

        Lastest maintained release.    # noqa: E501

        :return: The maintained_release of this NiaapiMaintainedReleaseAllOf.  # noqa: E501
        :rtype: str
        """
        return self._maintained_release

    @maintained_release.setter
    def maintained_release(self, maintained_release):
        """Sets the maintained_release of this NiaapiMaintainedReleaseAllOf.

        Lastest maintained release.    # noqa: E501

        :param maintained_release: The maintained_release of this NiaapiMaintainedReleaseAllOf.  # noqa: E501
        :type: str
        """

        self._maintained_release = maintained_release

    @property
    def software_release(self):
        """Gets the software_release of this NiaapiMaintainedReleaseAllOf.  # noqa: E501

        Software release version string.    # noqa: E501

        :return: The software_release of this NiaapiMaintainedReleaseAllOf.  # noqa: E501
        :rtype: str
        """
        return self._software_release

    @software_release.setter
    def software_release(self, software_release):
        """Sets the software_release of this NiaapiMaintainedReleaseAllOf.

        Software release version string.    # noqa: E501

        :param software_release: The software_release of this NiaapiMaintainedReleaseAllOf.  # noqa: E501
        :type: str
        """

        self._software_release = software_release

    @property
    def version_tag(self):
        """Gets the version_tag of this NiaapiMaintainedReleaseAllOf.  # noqa: E501

        Long lived version or short lived version.     # noqa: E501

        :return: The version_tag of this NiaapiMaintainedReleaseAllOf.  # noqa: E501
        :rtype: str
        """
        return self._version_tag

    @version_tag.setter
    def version_tag(self, version_tag):
        """Sets the version_tag of this NiaapiMaintainedReleaseAllOf.

        Long lived version or short lived version.     # noqa: E501

        :param version_tag: The version_tag of this NiaapiMaintainedReleaseAllOf.  # noqa: E501
        :type: str
        """

        self._version_tag = version_tag

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
        if not isinstance(other, NiaapiMaintainedReleaseAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NiaapiMaintainedReleaseAllOf):
            return True

        return self.to_dict() != other.to_dict()
