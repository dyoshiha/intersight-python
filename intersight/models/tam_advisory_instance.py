# coding: utf-8

"""
    Intersight REST API

    This is Intersight REST API 

    OpenAPI spec version: 1.0.9-961
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class TamAdvisoryInstance(object):
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
        'domain_group_moid': 'str',
        'mod_time': 'datetime',
        'moid': 'str',
        'object_type': 'str',
        'owners': 'list[str]',
        'parent': 'MoBaseMoRef',
        'shared_scope': 'str',
        'tags': 'list[MoTag]',
        'version_context': 'MoVersionContext',
        'advisory': 'TamAdvisoryRef',
        'affected_object_moid': 'str',
        'affected_object_type': 'str',
        'last_state_change_time': 'datetime',
        'last_verified_time': 'datetime',
        'organization': 'IamAccountRef',
        'state': 'str'
    }

    attribute_map = {
        'account_moid': 'AccountMoid',
        'ancestors': 'Ancestors',
        'create_time': 'CreateTime',
        'domain_group_moid': 'DomainGroupMoid',
        'mod_time': 'ModTime',
        'moid': 'Moid',
        'object_type': 'ObjectType',
        'owners': 'Owners',
        'parent': 'Parent',
        'shared_scope': 'SharedScope',
        'tags': 'Tags',
        'version_context': 'VersionContext',
        'advisory': 'Advisory',
        'affected_object_moid': 'AffectedObjectMoid',
        'affected_object_type': 'AffectedObjectType',
        'last_state_change_time': 'LastStateChangeTime',
        'last_verified_time': 'LastVerifiedTime',
        'organization': 'Organization',
        'state': 'State'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, shared_scope=None, tags=None, version_context=None, advisory=None, affected_object_moid=None, affected_object_type=None, last_state_change_time=None, last_verified_time=None, organization=None, state='unknown'):
        """
        TamAdvisoryInstance - a model defined in Swagger
        """

        self._account_moid = None
        self._ancestors = None
        self._create_time = None
        self._domain_group_moid = None
        self._mod_time = None
        self._moid = None
        self._object_type = None
        self._owners = None
        self._parent = None
        self._shared_scope = None
        self._tags = None
        self._version_context = None
        self._advisory = None
        self._affected_object_moid = None
        self._affected_object_type = None
        self._last_state_change_time = None
        self._last_verified_time = None
        self._organization = None
        self._state = None

        if account_moid is not None:
          self.account_moid = account_moid
        if ancestors is not None:
          self.ancestors = ancestors
        if create_time is not None:
          self.create_time = create_time
        if domain_group_moid is not None:
          self.domain_group_moid = domain_group_moid
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
        if shared_scope is not None:
          self.shared_scope = shared_scope
        if tags is not None:
          self.tags = tags
        if version_context is not None:
          self.version_context = version_context
        if advisory is not None:
          self.advisory = advisory
        if affected_object_moid is not None:
          self.affected_object_moid = affected_object_moid
        if affected_object_type is not None:
          self.affected_object_type = affected_object_type
        if last_state_change_time is not None:
          self.last_state_change_time = last_state_change_time
        if last_verified_time is not None:
          self.last_verified_time = last_verified_time
        if organization is not None:
          self.organization = organization
        if state is not None:
          self.state = state

    @property
    def account_moid(self):
        """
        Gets the account_moid of this TamAdvisoryInstance.
        The Account ID for this managed object.  

        :return: The account_moid of this TamAdvisoryInstance.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this TamAdvisoryInstance.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this TamAdvisoryInstance.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this TamAdvisoryInstance.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this TamAdvisoryInstance.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this TamAdvisoryInstance.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this TamAdvisoryInstance.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this TamAdvisoryInstance.
        The time when this managed object was created.  

        :return: The create_time of this TamAdvisoryInstance.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this TamAdvisoryInstance.
        The time when this managed object was created.  

        :param create_time: The create_time of this TamAdvisoryInstance.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this TamAdvisoryInstance.
        The DomainGroup ID for this managed object.  

        :return: The domain_group_moid of this TamAdvisoryInstance.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this TamAdvisoryInstance.
        The DomainGroup ID for this managed object.  

        :param domain_group_moid: The domain_group_moid of this TamAdvisoryInstance.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this TamAdvisoryInstance.
        The time when this managed object was last modified.  

        :return: The mod_time of this TamAdvisoryInstance.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this TamAdvisoryInstance.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this TamAdvisoryInstance.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this TamAdvisoryInstance.
        The unique identifier of this Managed Object instance.  

        :return: The moid of this TamAdvisoryInstance.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this TamAdvisoryInstance.
        The unique identifier of this Managed Object instance.  

        :param moid: The moid of this TamAdvisoryInstance.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this TamAdvisoryInstance.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this TamAdvisoryInstance.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this TamAdvisoryInstance.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this TamAdvisoryInstance.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this TamAdvisoryInstance.
        The array of owners which represent effective ownership of this object.   

        :return: The owners of this TamAdvisoryInstance.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this TamAdvisoryInstance.
        The array of owners which represent effective ownership of this object.   

        :param owners: The owners of this TamAdvisoryInstance.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this TamAdvisoryInstance.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this TamAdvisoryInstance.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this TamAdvisoryInstance.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this TamAdvisoryInstance.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this TamAdvisoryInstance.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :return: The shared_scope of this TamAdvisoryInstance.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this TamAdvisoryInstance.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :param shared_scope: The shared_scope of this TamAdvisoryInstance.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this TamAdvisoryInstance.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this TamAdvisoryInstance.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this TamAdvisoryInstance.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this TamAdvisoryInstance.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this TamAdvisoryInstance.
        The versioning info for this managed object.   

        :return: The version_context of this TamAdvisoryInstance.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this TamAdvisoryInstance.
        The versioning info for this managed object.   

        :param version_context: The version_context of this TamAdvisoryInstance.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def advisory(self):
        """
        Gets the advisory of this TamAdvisoryInstance.
        Reference to the Intersight advisory affecting the managed object. 

        :return: The advisory of this TamAdvisoryInstance.
        :rtype: TamAdvisoryRef
        """
        return self._advisory

    @advisory.setter
    def advisory(self, advisory):
        """
        Sets the advisory of this TamAdvisoryInstance.
        Reference to the Intersight advisory affecting the managed object. 

        :param advisory: The advisory of this TamAdvisoryInstance.
        :type: TamAdvisoryRef
        """

        self._advisory = advisory

    @property
    def affected_object_moid(self):
        """
        Gets the affected_object_moid of this TamAdvisoryInstance.
        Moid of the Intersight MO affected by the alert.  

        :return: The affected_object_moid of this TamAdvisoryInstance.
        :rtype: str
        """
        return self._affected_object_moid

    @affected_object_moid.setter
    def affected_object_moid(self, affected_object_moid):
        """
        Sets the affected_object_moid of this TamAdvisoryInstance.
        Moid of the Intersight MO affected by the alert.  

        :param affected_object_moid: The affected_object_moid of this TamAdvisoryInstance.
        :type: str
        """

        self._affected_object_moid = affected_object_moid

    @property
    def affected_object_type(self):
        """
        Gets the affected_object_type of this TamAdvisoryInstance.
        Object type of the Intersight MO affected by the alert.  

        :return: The affected_object_type of this TamAdvisoryInstance.
        :rtype: str
        """
        return self._affected_object_type

    @affected_object_type.setter
    def affected_object_type(self, affected_object_type):
        """
        Sets the affected_object_type of this TamAdvisoryInstance.
        Object type of the Intersight MO affected by the alert.  

        :param affected_object_type: The affected_object_type of this TamAdvisoryInstance.
        :type: str
        """

        self._affected_object_type = affected_object_type

    @property
    def last_state_change_time(self):
        """
        Gets the last_state_change_time of this TamAdvisoryInstance.
        Timestamp when a state change was observed on this advisory instnace.  

        :return: The last_state_change_time of this TamAdvisoryInstance.
        :rtype: datetime
        """
        return self._last_state_change_time

    @last_state_change_time.setter
    def last_state_change_time(self, last_state_change_time):
        """
        Sets the last_state_change_time of this TamAdvisoryInstance.
        Timestamp when a state change was observed on this advisory instnace.  

        :param last_state_change_time: The last_state_change_time of this TamAdvisoryInstance.
        :type: datetime
        """

        self._last_state_change_time = last_state_change_time

    @property
    def last_verified_time(self):
        """
        Gets the last_verified_time of this TamAdvisoryInstance.
        Timestamp when this advisory was last evaluated.  

        :return: The last_verified_time of this TamAdvisoryInstance.
        :rtype: datetime
        """
        return self._last_verified_time

    @last_verified_time.setter
    def last_verified_time(self, last_verified_time):
        """
        Sets the last_verified_time of this TamAdvisoryInstance.
        Timestamp when this advisory was last evaluated.  

        :param last_verified_time: The last_verified_time of this TamAdvisoryInstance.
        :type: datetime
        """

        self._last_verified_time = last_verified_time

    @property
    def organization(self):
        """
        Gets the organization of this TamAdvisoryInstance.
        Relationship to the Organization that owns the Managed Object. 

        :return: The organization of this TamAdvisoryInstance.
        :rtype: IamAccountRef
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """
        Sets the organization of this TamAdvisoryInstance.
        Relationship to the Organization that owns the Managed Object. 

        :param organization: The organization of this TamAdvisoryInstance.
        :type: IamAccountRef
        """

        self._organization = organization

    @property
    def state(self):
        """
        Gets the state of this TamAdvisoryInstance.
        Current state of the advisory instance (Active/Cleared/Unknown etc.).   

        :return: The state of this TamAdvisoryInstance.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this TamAdvisoryInstance.
        Current state of the advisory instance (Active/Cleared/Unknown etc.).   

        :param state: The state of this TamAdvisoryInstance.
        :type: str
        """
        allowed_values = ["unknown", "active", "cleared"]
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state

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
        if not isinstance(other, TamAdvisoryInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other