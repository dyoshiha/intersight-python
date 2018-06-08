# coding: utf-8

"""
    Intersight REST API

    This is Intersight REST API 

    OpenAPI spec version: 1.0.5-612
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class IaasUcsdInfo(object):
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
        'account_moid': 'str',
        'ancestors': 'list[MoBaseMoRef]',
        'create_time': 'datetime',
        'mod_time': 'datetime',
        'moid': 'str',
        'object_type': 'str',
        'owners': 'list[str]',
        'parent': 'MoBaseMoRef',
        'tags': 'list[MoTag]',
        'connector_pack': 'list[IaasConnectorPackRef]',
        'device_id': 'str',
        'device_status': 'list[IaasDeviceStatusRef]',
        'guid': 'str',
        'host_name': 'str',
        'ip': 'str',
        'license_info': 'IaasLicenseInfoRef',
        'product_name': 'str',
        'product_vendor': 'str',
        'product_version': 'str',
        'registered_device': 'AssetDeviceRegistrationRef',
        'status': 'str'
    }

    attribute_map = {
        'account_moid': 'AccountMoid',
        'ancestors': 'Ancestors',
        'create_time': 'CreateTime',
        'mod_time': 'ModTime',
        'moid': 'Moid',
        'object_type': 'ObjectType',
        'owners': 'Owners',
        'parent': 'Parent',
        'tags': 'Tags',
        'connector_pack': 'ConnectorPack',
        'device_id': 'DeviceId',
        'device_status': 'DeviceStatus',
        'guid': 'Guid',
        'host_name': 'HostName',
        'ip': 'Ip',
        'license_info': 'LicenseInfo',
        'product_name': 'ProductName',
        'product_vendor': 'ProductVendor',
        'product_version': 'ProductVersion',
        'registered_device': 'RegisteredDevice',
        'status': 'Status'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, connector_pack=None, device_id=None, device_status=None, guid=None, host_name=None, ip=None, license_info=None, product_name=None, product_vendor=None, product_version=None, registered_device=None, status=None):
        """
        IaasUcsdInfo - a model defined in Swagger
        """

        self._account_moid = None
        self._ancestors = None
        self._create_time = None
        self._mod_time = None
        self._moid = None
        self._object_type = None
        self._owners = None
        self._parent = None
        self._tags = None
        self._connector_pack = None
        self._device_id = None
        self._device_status = None
        self._guid = None
        self._host_name = None
        self._ip = None
        self._license_info = None
        self._product_name = None
        self._product_vendor = None
        self._product_version = None
        self._registered_device = None
        self._status = None

        if account_moid is not None:
          self.account_moid = account_moid
        if ancestors is not None:
          self.ancestors = ancestors
        if create_time is not None:
          self.create_time = create_time
        if mod_time is not None:
          self.mod_time = mod_time
        if moid is not None:
          self.moid = moid
        if object_type is not None:
          self.object_type = object_type
        if owners is not None:
          self.owners = owners
        if parent is not None:
          self.parent = parent
        if tags is not None:
          self.tags = tags
        if connector_pack is not None:
          self.connector_pack = connector_pack
        if device_id is not None:
          self.device_id = device_id
        if device_status is not None:
          self.device_status = device_status
        if guid is not None:
          self.guid = guid
        if host_name is not None:
          self.host_name = host_name
        if ip is not None:
          self.ip = ip
        if license_info is not None:
          self.license_info = license_info
        if product_name is not None:
          self.product_name = product_name
        if product_vendor is not None:
          self.product_vendor = product_vendor
        if product_version is not None:
          self.product_version = product_version
        if registered_device is not None:
          self.registered_device = registered_device
        if status is not None:
          self.status = status

    @property
    def account_moid(self):
        """
        Gets the account_moid of this IaasUcsdInfo.
        The Account ID for this managed object.  

        :return: The account_moid of this IaasUcsdInfo.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this IaasUcsdInfo.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this IaasUcsdInfo.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this IaasUcsdInfo.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this IaasUcsdInfo.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this IaasUcsdInfo.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this IaasUcsdInfo.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this IaasUcsdInfo.
        The time when this managed object was created.  

        :return: The create_time of this IaasUcsdInfo.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this IaasUcsdInfo.
        The time when this managed object was created.  

        :param create_time: The create_time of this IaasUcsdInfo.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this IaasUcsdInfo.
        The time when this managed object was last modified.  

        :return: The mod_time of this IaasUcsdInfo.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this IaasUcsdInfo.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this IaasUcsdInfo.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this IaasUcsdInfo.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this IaasUcsdInfo.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this IaasUcsdInfo.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this IaasUcsdInfo.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this IaasUcsdInfo.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this IaasUcsdInfo.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this IaasUcsdInfo.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this IaasUcsdInfo.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this IaasUcsdInfo.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this IaasUcsdInfo.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this IaasUcsdInfo.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this IaasUcsdInfo.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this IaasUcsdInfo.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this IaasUcsdInfo.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this IaasUcsdInfo.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this IaasUcsdInfo.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this IaasUcsdInfo.
        An array of tags, which allow to add key, value meta-data to managed objects.   

        :return: The tags of this IaasUcsdInfo.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this IaasUcsdInfo.
        An array of tags, which allow to add key, value meta-data to managed objects.   

        :param tags: The tags of this IaasUcsdInfo.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def connector_pack(self):
        """
        Gets the connector_pack of this IaasUcsdInfo.

        :return: The connector_pack of this IaasUcsdInfo.
        :rtype: list[IaasConnectorPackRef]
        """
        return self._connector_pack

    @connector_pack.setter
    def connector_pack(self, connector_pack):
        """
        Sets the connector_pack of this IaasUcsdInfo.

        :param connector_pack: The connector_pack of this IaasUcsdInfo.
        :type: list[IaasConnectorPackRef]
        """

        self._connector_pack = connector_pack

    @property
    def device_id(self):
        """
        Gets the device_id of this IaasUcsdInfo.
        Moid of the UCSD device connector's asset.DeviceRegistration  

        :return: The device_id of this IaasUcsdInfo.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """
        Sets the device_id of this IaasUcsdInfo.
        Moid of the UCSD device connector's asset.DeviceRegistration  

        :param device_id: The device_id of this IaasUcsdInfo.
        :type: str
        """

        self._device_id = device_id

    @property
    def device_status(self):
        """
        Gets the device_status of this IaasUcsdInfo.

        :return: The device_status of this IaasUcsdInfo.
        :rtype: list[IaasDeviceStatusRef]
        """
        return self._device_status

    @device_status.setter
    def device_status(self, device_status):
        """
        Sets the device_status of this IaasUcsdInfo.

        :param device_status: The device_status of this IaasUcsdInfo.
        :type: list[IaasDeviceStatusRef]
        """

        self._device_status = device_status

    @property
    def guid(self):
        """
        Gets the guid of this IaasUcsdInfo.
        Unique ID of UCSD getting registerd with Intersight  

        :return: The guid of this IaasUcsdInfo.
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """
        Sets the guid of this IaasUcsdInfo.
        Unique ID of UCSD getting registerd with Intersight  

        :param guid: The guid of this IaasUcsdInfo.
        :type: str
        """

        self._guid = guid

    @property
    def host_name(self):
        """
        Gets the host_name of this IaasUcsdInfo.
        The UCSD host name  

        :return: The host_name of this IaasUcsdInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """
        Sets the host_name of this IaasUcsdInfo.
        The UCSD host name  

        :param host_name: The host_name of this IaasUcsdInfo.
        :type: str
        """

        self._host_name = host_name

    @property
    def ip(self):
        """
        Gets the ip of this IaasUcsdInfo.
        The UCSD IP address  

        :return: The ip of this IaasUcsdInfo.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """
        Sets the ip of this IaasUcsdInfo.
        The UCSD IP address  

        :param ip: The ip of this IaasUcsdInfo.
        :type: str
        """

        self._ip = ip

    @property
    def license_info(self):
        """
        Gets the license_info of this IaasUcsdInfo.

        :return: The license_info of this IaasUcsdInfo.
        :rtype: IaasLicenseInfoRef
        """
        return self._license_info

    @license_info.setter
    def license_info(self, license_info):
        """
        Sets the license_info of this IaasUcsdInfo.

        :param license_info: The license_info of this IaasUcsdInfo.
        :type: IaasLicenseInfoRef
        """

        self._license_info = license_info

    @property
    def product_name(self):
        """
        Gets the product_name of this IaasUcsdInfo.
        The UCSD product name  

        :return: The product_name of this IaasUcsdInfo.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """
        Sets the product_name of this IaasUcsdInfo.
        The UCSD product name  

        :param product_name: The product_name of this IaasUcsdInfo.
        :type: str
        """

        self._product_name = product_name

    @property
    def product_vendor(self):
        """
        Gets the product_vendor of this IaasUcsdInfo.
        The UCSD product vendor  

        :return: The product_vendor of this IaasUcsdInfo.
        :rtype: str
        """
        return self._product_vendor

    @product_vendor.setter
    def product_vendor(self, product_vendor):
        """
        Sets the product_vendor of this IaasUcsdInfo.
        The UCSD product vendor  

        :param product_vendor: The product_vendor of this IaasUcsdInfo.
        :type: str
        """

        self._product_vendor = product_vendor

    @property
    def product_version(self):
        """
        Gets the product_version of this IaasUcsdInfo.
        The UCSD product/platform version  

        :return: The product_version of this IaasUcsdInfo.
        :rtype: str
        """
        return self._product_version

    @product_version.setter
    def product_version(self, product_version):
        """
        Sets the product_version of this IaasUcsdInfo.
        The UCSD product/platform version  

        :param product_version: The product_version of this IaasUcsdInfo.
        :type: str
        """

        self._product_version = product_version

    @property
    def registered_device(self):
        """
        Gets the registered_device of this IaasUcsdInfo.

        :return: The registered_device of this IaasUcsdInfo.
        :rtype: AssetDeviceRegistrationRef
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """
        Sets the registered_device of this IaasUcsdInfo.

        :param registered_device: The registered_device of this IaasUcsdInfo.
        :type: AssetDeviceRegistrationRef
        """

        self._registered_device = registered_device

    @property
    def status(self):
        """
        Gets the status of this IaasUcsdInfo.
        The UCSD status. Possible values are Active,In-Active,Unknown   

        :return: The status of this IaasUcsdInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this IaasUcsdInfo.
        The UCSD status. Possible values are Active,In-Active,Unknown   

        :param status: The status of this IaasUcsdInfo.
        :type: str
        """

        self._status = status

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
        if not isinstance(other, IaasUcsdInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other