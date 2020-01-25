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


class LicenseCustomerOpAllOf(object):
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
        'deregister_device': 'bool',
        'renew_authorization': 'bool',
        'renew_id_certificate': 'bool',
        'show_agent_tech_support': 'bool',
        'account_license_data': 'LicenseAccountLicenseData'
    }

    attribute_map = {
        'deregister_device': 'DeregisterDevice',
        'renew_authorization': 'RenewAuthorization',
        'renew_id_certificate': 'RenewIdCertificate',
        'show_agent_tech_support': 'ShowAgentTechSupport',
        'account_license_data': 'AccountLicenseData'
    }

    def __init__(self,
                 deregister_device=None,
                 renew_authorization=None,
                 renew_id_certificate=None,
                 show_agent_tech_support=None,
                 account_license_data=None,
                 local_vars_configuration=None):  # noqa: E501
        """LicenseCustomerOpAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._deregister_device = None
        self._renew_authorization = None
        self._renew_id_certificate = None
        self._show_agent_tech_support = None
        self._account_license_data = None
        self.discriminator = None

        if deregister_device is not None:
            self.deregister_device = deregister_device
        if renew_authorization is not None:
            self.renew_authorization = renew_authorization
        if renew_id_certificate is not None:
            self.renew_id_certificate = renew_id_certificate
        if show_agent_tech_support is not None:
            self.show_agent_tech_support = show_agent_tech_support
        if account_license_data is not None:
            self.account_license_data = account_license_data

    @property
    def deregister_device(self):
        """Gets the deregister_device of this LicenseCustomerOpAllOf.  # noqa: E501

        Trigger de-registration/disable.    # noqa: E501

        :return: The deregister_device of this LicenseCustomerOpAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._deregister_device

    @deregister_device.setter
    def deregister_device(self, deregister_device):
        """Sets the deregister_device of this LicenseCustomerOpAllOf.

        Trigger de-registration/disable.    # noqa: E501

        :param deregister_device: The deregister_device of this LicenseCustomerOpAllOf.  # noqa: E501
        :type: bool
        """

        self._deregister_device = deregister_device

    @property
    def renew_authorization(self):
        """Gets the renew_authorization of this LicenseCustomerOpAllOf.  # noqa: E501

        Trigger renew authorization.    # noqa: E501

        :return: The renew_authorization of this LicenseCustomerOpAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._renew_authorization

    @renew_authorization.setter
    def renew_authorization(self, renew_authorization):
        """Sets the renew_authorization of this LicenseCustomerOpAllOf.

        Trigger renew authorization.    # noqa: E501

        :param renew_authorization: The renew_authorization of this LicenseCustomerOpAllOf.  # noqa: E501
        :type: bool
        """

        self._renew_authorization = renew_authorization

    @property
    def renew_id_certificate(self):
        """Gets the renew_id_certificate of this LicenseCustomerOpAllOf.  # noqa: E501

        Trigger renew registration.    # noqa: E501

        :return: The renew_id_certificate of this LicenseCustomerOpAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._renew_id_certificate

    @renew_id_certificate.setter
    def renew_id_certificate(self, renew_id_certificate):
        """Sets the renew_id_certificate of this LicenseCustomerOpAllOf.

        Trigger renew registration.    # noqa: E501

        :param renew_id_certificate: The renew_id_certificate of this LicenseCustomerOpAllOf.  # noqa: E501
        :type: bool
        """

        self._renew_id_certificate = renew_id_certificate

    @property
    def show_agent_tech_support(self):
        """Gets the show_agent_tech_support of this LicenseCustomerOpAllOf.  # noqa: E501

        Trigger show tech support feature.     # noqa: E501

        :return: The show_agent_tech_support of this LicenseCustomerOpAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._show_agent_tech_support

    @show_agent_tech_support.setter
    def show_agent_tech_support(self, show_agent_tech_support):
        """Sets the show_agent_tech_support of this LicenseCustomerOpAllOf.

        Trigger show tech support feature.     # noqa: E501

        :param show_agent_tech_support: The show_agent_tech_support of this LicenseCustomerOpAllOf.  # noqa: E501
        :type: bool
        """

        self._show_agent_tech_support = show_agent_tech_support

    @property
    def account_license_data(self):
        """Gets the account_license_data of this LicenseCustomerOpAllOf.  # noqa: E501


        :return: The account_license_data of this LicenseCustomerOpAllOf.  # noqa: E501
        :rtype: LicenseAccountLicenseData
        """
        return self._account_license_data

    @account_license_data.setter
    def account_license_data(self, account_license_data):
        """Sets the account_license_data of this LicenseCustomerOpAllOf.


        :param account_license_data: The account_license_data of this LicenseCustomerOpAllOf.  # noqa: E501
        :type: LicenseAccountLicenseData
        """

        self._account_license_data = account_license_data

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
        if not isinstance(other, LicenseCustomerOpAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LicenseCustomerOpAllOf):
            return True

        return self.to_dict() != other.to_dict()