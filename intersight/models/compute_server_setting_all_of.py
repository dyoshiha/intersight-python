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


class ComputeServerSettingAllOf(object):
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
        'admin_locator_led_state': 'str',
        'admin_power_state': 'str',
        'config_state': 'str',
        'one_time_boot_device': 'str',
        'server_config': 'ComputeServerConfig',
        'locator_led': 'EquipmentLocatorLed',
        'registered_device': 'AssetDeviceRegistration',
        'server': 'ComputeRackUnit'
    }

    attribute_map = {
        'admin_locator_led_state': 'AdminLocatorLedState',
        'admin_power_state': 'AdminPowerState',
        'config_state': 'ConfigState',
        'one_time_boot_device': 'OneTimeBootDevice',
        'server_config': 'ServerConfig',
        'locator_led': 'LocatorLed',
        'registered_device': 'RegisteredDevice',
        'server': 'Server'
    }

    def __init__(self,
                 admin_locator_led_state='None',
                 admin_power_state='Policy',
                 config_state='Applied',
                 one_time_boot_device=None,
                 server_config=None,
                 locator_led=None,
                 registered_device=None,
                 server=None,
                 local_vars_configuration=None):  # noqa: E501
        """ComputeServerSettingAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._admin_locator_led_state = None
        self._admin_power_state = None
        self._config_state = None
        self._one_time_boot_device = None
        self._server_config = None
        self._locator_led = None
        self._registered_device = None
        self._server = None
        self.discriminator = None

        if admin_locator_led_state is not None:
            self.admin_locator_led_state = admin_locator_led_state
        if admin_power_state is not None:
            self.admin_power_state = admin_power_state
        if config_state is not None:
            self.config_state = config_state
        if one_time_boot_device is not None:
            self.one_time_boot_device = one_time_boot_device
        if server_config is not None:
            self.server_config = server_config
        if locator_led is not None:
            self.locator_led = locator_led
        if registered_device is not None:
            self.registered_device = registered_device
        if server is not None:
            self.server = server

    @property
    def admin_locator_led_state(self):
        """Gets the admin_locator_led_state of this ComputeServerSettingAllOf.  # noqa: E501

        User configured state of the locator LED for the server.    # noqa: E501

        :return: The admin_locator_led_state of this ComputeServerSettingAllOf.  # noqa: E501
        :rtype: str
        """
        return self._admin_locator_led_state

    @admin_locator_led_state.setter
    def admin_locator_led_state(self, admin_locator_led_state):
        """Sets the admin_locator_led_state of this ComputeServerSettingAllOf.

        User configured state of the locator LED for the server.    # noqa: E501

        :param admin_locator_led_state: The admin_locator_led_state of this ComputeServerSettingAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "true", "false"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and admin_locator_led_state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `admin_locator_led_state` ({0}), must be one of {1}"  # noqa: E501
                .format(admin_locator_led_state, allowed_values))

        self._admin_locator_led_state = admin_locator_led_state

    @property
    def admin_power_state(self):
        """Gets the admin_power_state of this ComputeServerSettingAllOf.  # noqa: E501

        User configured power state of the server.    # noqa: E501

        :return: The admin_power_state of this ComputeServerSettingAllOf.  # noqa: E501
        :rtype: str
        """
        return self._admin_power_state

    @admin_power_state.setter
    def admin_power_state(self, admin_power_state):
        """Sets the admin_power_state of this ComputeServerSettingAllOf.

        User configured power state of the server.    # noqa: E501

        :param admin_power_state: The admin_power_state of this ComputeServerSettingAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "Policy", "PowerOn", "PowerOff", "PowerCycle", "HardReset",
            "Shutdown", "Reboot"
        ]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and admin_power_state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `admin_power_state` ({0}), must be one of {1}"  # noqa: E501
                .format(admin_power_state, allowed_values))

        self._admin_power_state = admin_power_state

    @property
    def config_state(self):
        """Gets the config_state of this ComputeServerSettingAllOf.  # noqa: E501

        The configured state of these settings in the target server. The value is any one of Applied, Applying, Failed. Applied - This state denotes that the settings are applied successfully in the target server. Applying - This state denotes that the settings are being applied in the target server. Failed - This state denotes that the settings could not be applied in the target server.    # noqa: E501

        :return: The config_state of this ComputeServerSettingAllOf.  # noqa: E501
        :rtype: str
        """
        return self._config_state

    @config_state.setter
    def config_state(self, config_state):
        """Sets the config_state of this ComputeServerSettingAllOf.

        The configured state of these settings in the target server. The value is any one of Applied, Applying, Failed. Applied - This state denotes that the settings are applied successfully in the target server. Applying - This state denotes that the settings are being applied in the target server. Failed - This state denotes that the settings could not be applied in the target server.    # noqa: E501

        :param config_state: The config_state of this ComputeServerSettingAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["Applied", "Applying", "Failed"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and config_state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `config_state` ({0}), must be one of {1}"  # noqa: E501
                .format(config_state, allowed_values))

        self._config_state = config_state

    @property
    def one_time_boot_device(self):
        """Gets the one_time_boot_device of this ComputeServerSettingAllOf.  # noqa: E501

        The name of the device chosen by user for configuring One-Time Boot device.    # noqa: E501

        :return: The one_time_boot_device of this ComputeServerSettingAllOf.  # noqa: E501
        :rtype: str
        """
        return self._one_time_boot_device

    @one_time_boot_device.setter
    def one_time_boot_device(self, one_time_boot_device):
        """Sets the one_time_boot_device of this ComputeServerSettingAllOf.

        The name of the device chosen by user for configuring One-Time Boot device.    # noqa: E501

        :param one_time_boot_device: The one_time_boot_device of this ComputeServerSettingAllOf.  # noqa: E501
        :type: str
        """

        self._one_time_boot_device = one_time_boot_device

    @property
    def server_config(self):
        """Gets the server_config of this ComputeServerSettingAllOf.  # noqa: E501


        :return: The server_config of this ComputeServerSettingAllOf.  # noqa: E501
        :rtype: ComputeServerConfig
        """
        return self._server_config

    @server_config.setter
    def server_config(self, server_config):
        """Sets the server_config of this ComputeServerSettingAllOf.


        :param server_config: The server_config of this ComputeServerSettingAllOf.  # noqa: E501
        :type: ComputeServerConfig
        """

        self._server_config = server_config

    @property
    def locator_led(self):
        """Gets the locator_led of this ComputeServerSettingAllOf.  # noqa: E501


        :return: The locator_led of this ComputeServerSettingAllOf.  # noqa: E501
        :rtype: EquipmentLocatorLed
        """
        return self._locator_led

    @locator_led.setter
    def locator_led(self, locator_led):
        """Sets the locator_led of this ComputeServerSettingAllOf.


        :param locator_led: The locator_led of this ComputeServerSettingAllOf.  # noqa: E501
        :type: EquipmentLocatorLed
        """

        self._locator_led = locator_led

    @property
    def registered_device(self):
        """Gets the registered_device of this ComputeServerSettingAllOf.  # noqa: E501


        :return: The registered_device of this ComputeServerSettingAllOf.  # noqa: E501
        :rtype: AssetDeviceRegistration
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """Sets the registered_device of this ComputeServerSettingAllOf.


        :param registered_device: The registered_device of this ComputeServerSettingAllOf.  # noqa: E501
        :type: AssetDeviceRegistration
        """

        self._registered_device = registered_device

    @property
    def server(self):
        """Gets the server of this ComputeServerSettingAllOf.  # noqa: E501


        :return: The server of this ComputeServerSettingAllOf.  # noqa: E501
        :rtype: ComputeRackUnit
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this ComputeServerSettingAllOf.


        :param server: The server of this ComputeServerSettingAllOf.  # noqa: E501
        :type: ComputeRackUnit
        """

        self._server = server

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
        if not isinstance(other, ComputeServerSettingAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComputeServerSettingAllOf):
            return True

        return self.to_dict() != other.to_dict()
