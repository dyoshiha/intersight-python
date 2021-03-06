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


class IamResourceRolesAllOf(object):
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
        'end_point_roles': 'list[IamEndPointRole]',
        'permission': 'IamPermission',
        'resource': 'MoBaseMo',
        'roles': 'list[IamRole]'
    }

    attribute_map = {
        'end_point_roles': 'EndPointRoles',
        'permission': 'Permission',
        'resource': 'Resource',
        'roles': 'Roles'
    }

    def __init__(self,
                 end_point_roles=None,
                 permission=None,
                 resource=None,
                 roles=None,
                 local_vars_configuration=None):  # noqa: E501
        """IamResourceRolesAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._end_point_roles = None
        self._permission = None
        self._resource = None
        self._roles = None
        self.discriminator = None

        if end_point_roles is not None:
            self.end_point_roles = end_point_roles
        if permission is not None:
            self.permission = permission
        if resource is not None:
            self.resource = resource
        if roles is not None:
            self.roles = roles

    @property
    def end_point_roles(self):
        """Gets the end_point_roles of this IamResourceRolesAllOf.  # noqa: E501

        A reference to a iamEndPointRole resource. When the $expand query parameter is specified, the referenced resource is returned inline. The end point roles assigned to this permission. The user can perform end point operations like GUI/CLI cross launch.   # noqa: E501

        :return: The end_point_roles of this IamResourceRolesAllOf.  # noqa: E501
        :rtype: list[IamEndPointRole]
        """
        return self._end_point_roles

    @end_point_roles.setter
    def end_point_roles(self, end_point_roles):
        """Sets the end_point_roles of this IamResourceRolesAllOf.

        A reference to a iamEndPointRole resource. When the $expand query parameter is specified, the referenced resource is returned inline. The end point roles assigned to this permission. The user can perform end point operations like GUI/CLI cross launch.   # noqa: E501

        :param end_point_roles: The end_point_roles of this IamResourceRolesAllOf.  # noqa: E501
        :type: list[IamEndPointRole]
        """

        self._end_point_roles = end_point_roles

    @property
    def permission(self):
        """Gets the permission of this IamResourceRolesAllOf.  # noqa: E501


        :return: The permission of this IamResourceRolesAllOf.  # noqa: E501
        :rtype: IamPermission
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this IamResourceRolesAllOf.


        :param permission: The permission of this IamResourceRolesAllOf.  # noqa: E501
        :type: IamPermission
        """

        self._permission = permission

    @property
    def resource(self):
        """Gets the resource of this IamResourceRolesAllOf.  # noqa: E501


        :return: The resource of this IamResourceRolesAllOf.  # noqa: E501
        :rtype: MoBaseMo
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this IamResourceRolesAllOf.


        :param resource: The resource of this IamResourceRolesAllOf.  # noqa: E501
        :type: MoBaseMo
        """

        self._resource = resource

    @property
    def roles(self):
        """Gets the roles of this IamResourceRolesAllOf.  # noqa: E501

        A reference to a iamRole resource. When the $expand query parameter is specified, the referenced resource is returned inline. The roles assigned to this resource. Role is a collection of privilege sets. Roles are assigned to a user or group using the permission object.   # noqa: E501

        :return: The roles of this IamResourceRolesAllOf.  # noqa: E501
        :rtype: list[IamRole]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this IamResourceRolesAllOf.

        A reference to a iamRole resource. When the $expand query parameter is specified, the referenced resource is returned inline. The roles assigned to this resource. Role is a collection of privilege sets. Roles are assigned to a user or group using the permission object.   # noqa: E501

        :param roles: The roles of this IamResourceRolesAllOf.  # noqa: E501
        :type: list[IamRole]
        """

        self._roles = roles

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
        if not isinstance(other, IamResourceRolesAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IamResourceRolesAllOf):
            return True

        return self.to_dict() != other.to_dict()
