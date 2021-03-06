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


class HyperflexClusterAllOf(object):
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
        'capacity_runway': 'int',
        'cluster_name': 'str',
        'cluster_type': 'int',
        'cluster_uuid': 'str',
        'compute_node_count': 'int',
        'converged_node_count': 'int',
        'deployment_type': 'str',
        'device_id': 'str',
        'flt_aggr': 'int',
        'hx_version': 'str',
        'hxdp_build_version': 'str',
        'hypervisor_type': 'str',
        'hypervisor_version': 'str',
        'summary': 'HyperflexSummary',
        'utilization_percentage': 'float',
        'utilization_trend_percentage': 'float',
        'vm_count': 'int',
        'alarm': 'list[HyperflexAlarm]',
        'health': 'HyperflexHealth',
        'nodes': 'list[HyperflexNode]',
        'registered_device': 'AssetDeviceRegistration'
    }

    attribute_map = {
        'capacity_runway': 'CapacityRunway',
        'cluster_name': 'ClusterName',
        'cluster_type': 'ClusterType',
        'cluster_uuid': 'ClusterUuid',
        'compute_node_count': 'ComputeNodeCount',
        'converged_node_count': 'ConvergedNodeCount',
        'deployment_type': 'DeploymentType',
        'device_id': 'DeviceId',
        'flt_aggr': 'FltAggr',
        'hx_version': 'HxVersion',
        'hxdp_build_version': 'HxdpBuildVersion',
        'hypervisor_type': 'HypervisorType',
        'hypervisor_version': 'HypervisorVersion',
        'summary': 'Summary',
        'utilization_percentage': 'UtilizationPercentage',
        'utilization_trend_percentage': 'UtilizationTrendPercentage',
        'vm_count': 'VmCount',
        'alarm': 'Alarm',
        'health': 'Health',
        'nodes': 'Nodes',
        'registered_device': 'RegisteredDevice'
    }

    def __init__(self,
                 capacity_runway=None,
                 cluster_name=None,
                 cluster_type=None,
                 cluster_uuid=None,
                 compute_node_count=None,
                 converged_node_count=None,
                 deployment_type='NA',
                 device_id=None,
                 flt_aggr=None,
                 hx_version=None,
                 hxdp_build_version=None,
                 hypervisor_type='Unknown',
                 hypervisor_version=None,
                 summary=None,
                 utilization_percentage=None,
                 utilization_trend_percentage=None,
                 vm_count=None,
                 alarm=None,
                 health=None,
                 nodes=None,
                 registered_device=None,
                 local_vars_configuration=None):  # noqa: E501
        """HyperflexClusterAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._capacity_runway = None
        self._cluster_name = None
        self._cluster_type = None
        self._cluster_uuid = None
        self._compute_node_count = None
        self._converged_node_count = None
        self._deployment_type = None
        self._device_id = None
        self._flt_aggr = None
        self._hx_version = None
        self._hxdp_build_version = None
        self._hypervisor_type = None
        self._hypervisor_version = None
        self._summary = None
        self._utilization_percentage = None
        self._utilization_trend_percentage = None
        self._vm_count = None
        self._alarm = None
        self._health = None
        self._nodes = None
        self._registered_device = None
        self.discriminator = None

        if capacity_runway is not None:
            self.capacity_runway = capacity_runway
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if cluster_type is not None:
            self.cluster_type = cluster_type
        if cluster_uuid is not None:
            self.cluster_uuid = cluster_uuid
        if compute_node_count is not None:
            self.compute_node_count = compute_node_count
        if converged_node_count is not None:
            self.converged_node_count = converged_node_count
        if deployment_type is not None:
            self.deployment_type = deployment_type
        if device_id is not None:
            self.device_id = device_id
        if flt_aggr is not None:
            self.flt_aggr = flt_aggr
        if hx_version is not None:
            self.hx_version = hx_version
        if hxdp_build_version is not None:
            self.hxdp_build_version = hxdp_build_version
        if hypervisor_type is not None:
            self.hypervisor_type = hypervisor_type
        if hypervisor_version is not None:
            self.hypervisor_version = hypervisor_version
        if summary is not None:
            self.summary = summary
        if utilization_percentage is not None:
            self.utilization_percentage = utilization_percentage
        if utilization_trend_percentage is not None:
            self.utilization_trend_percentage = utilization_trend_percentage
        if vm_count is not None:
            self.vm_count = vm_count
        if alarm is not None:
            self.alarm = alarm
        if health is not None:
            self.health = health
        if nodes is not None:
            self.nodes = nodes
        if registered_device is not None:
            self.registered_device = registered_device

    @property
    def capacity_runway(self):
        """Gets the capacity_runway of this HyperflexClusterAllOf.  # noqa: E501

        The number of days remaining before the cluster's storage utilization reaches the recommended capacity limit of 76%.  Default value is math.MaxInt32 to indicate that the capacity runway is \"Unknown\" for a cluster that is not connected or with not sufficient data.     # noqa: E501

        :return: The capacity_runway of this HyperflexClusterAllOf.  # noqa: E501
        :rtype: int
        """
        return self._capacity_runway

    @capacity_runway.setter
    def capacity_runway(self, capacity_runway):
        """Sets the capacity_runway of this HyperflexClusterAllOf.

        The number of days remaining before the cluster's storage utilization reaches the recommended capacity limit of 76%.  Default value is math.MaxInt32 to indicate that the capacity runway is \"Unknown\" for a cluster that is not connected or with not sufficient data.     # noqa: E501

        :param capacity_runway: The capacity_runway of this HyperflexClusterAllOf.  # noqa: E501
        :type: int
        """

        self._capacity_runway = capacity_runway

    @property
    def cluster_name(self):
        """Gets the cluster_name of this HyperflexClusterAllOf.  # noqa: E501

        The name of this HyperFlex cluster.    # noqa: E501

        :return: The cluster_name of this HyperflexClusterAllOf.  # noqa: E501
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this HyperflexClusterAllOf.

        The name of this HyperFlex cluster.    # noqa: E501

        :param cluster_name: The cluster_name of this HyperflexClusterAllOf.  # noqa: E501
        :type: str
        """

        self._cluster_name = cluster_name

    @property
    def cluster_type(self):
        """Gets the cluster_type of this HyperflexClusterAllOf.  # noqa: E501

        The storage type of this cluster (All Flash or Hybrid).    # noqa: E501

        :return: The cluster_type of this HyperflexClusterAllOf.  # noqa: E501
        :rtype: int
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        """Sets the cluster_type of this HyperflexClusterAllOf.

        The storage type of this cluster (All Flash or Hybrid).    # noqa: E501

        :param cluster_type: The cluster_type of this HyperflexClusterAllOf.  # noqa: E501
        :type: int
        """

        self._cluster_type = cluster_type

    @property
    def cluster_uuid(self):
        """Gets the cluster_uuid of this HyperflexClusterAllOf.  # noqa: E501

        The unique identifier for this HyperFlex cluster.    # noqa: E501

        :return: The cluster_uuid of this HyperflexClusterAllOf.  # noqa: E501
        :rtype: str
        """
        return self._cluster_uuid

    @cluster_uuid.setter
    def cluster_uuid(self, cluster_uuid):
        """Sets the cluster_uuid of this HyperflexClusterAllOf.

        The unique identifier for this HyperFlex cluster.    # noqa: E501

        :param cluster_uuid: The cluster_uuid of this HyperflexClusterAllOf.  # noqa: E501
        :type: str
        """

        self._cluster_uuid = cluster_uuid

    @property
    def compute_node_count(self):
        """Gets the compute_node_count of this HyperflexClusterAllOf.  # noqa: E501

        The number of compute nodes that belong to this cluster.    # noqa: E501

        :return: The compute_node_count of this HyperflexClusterAllOf.  # noqa: E501
        :rtype: int
        """
        return self._compute_node_count

    @compute_node_count.setter
    def compute_node_count(self, compute_node_count):
        """Sets the compute_node_count of this HyperflexClusterAllOf.

        The number of compute nodes that belong to this cluster.    # noqa: E501

        :param compute_node_count: The compute_node_count of this HyperflexClusterAllOf.  # noqa: E501
        :type: int
        """

        self._compute_node_count = compute_node_count

    @property
    def converged_node_count(self):
        """Gets the converged_node_count of this HyperflexClusterAllOf.  # noqa: E501

        The number of converged nodes that belong to this cluster.    # noqa: E501

        :return: The converged_node_count of this HyperflexClusterAllOf.  # noqa: E501
        :rtype: int
        """
        return self._converged_node_count

    @converged_node_count.setter
    def converged_node_count(self, converged_node_count):
        """Sets the converged_node_count of this HyperflexClusterAllOf.

        The number of converged nodes that belong to this cluster.    # noqa: E501

        :param converged_node_count: The converged_node_count of this HyperflexClusterAllOf.  # noqa: E501
        :type: int
        """

        self._converged_node_count = converged_node_count

    @property
    def deployment_type(self):
        """Gets the deployment_type of this HyperflexClusterAllOf.  # noqa: E501

        The deployment type of the HyperFlex cluster.  The cluster can have one of the following configurations: 1. Datacenter: The HyperFlex cluster consists of UCS Fabric Interconnect-attached nodes on a single site. 2. Stretched Cluster: The HyperFlex cluster consists of UCS Fabric Interconnect-attached nodes distributed across multiple sites. 3. Edge: The HyperFlex cluster consists of 2-4 standalone nodes.  If the cluster is running a HyperFlex Data Platform version less than 4.0 or if the deployment type cannot be determined, the deployment type is set as 'NA' (not available).     # noqa: E501

        :return: The deployment_type of this HyperflexClusterAllOf.  # noqa: E501
        :rtype: str
        """
        return self._deployment_type

    @deployment_type.setter
    def deployment_type(self, deployment_type):
        """Sets the deployment_type of this HyperflexClusterAllOf.

        The deployment type of the HyperFlex cluster.  The cluster can have one of the following configurations: 1. Datacenter: The HyperFlex cluster consists of UCS Fabric Interconnect-attached nodes on a single site. 2. Stretched Cluster: The HyperFlex cluster consists of UCS Fabric Interconnect-attached nodes distributed across multiple sites. 3. Edge: The HyperFlex cluster consists of 2-4 standalone nodes.  If the cluster is running a HyperFlex Data Platform version less than 4.0 or if the deployment type cannot be determined, the deployment type is set as 'NA' (not available).     # noqa: E501

        :param deployment_type: The deployment_type of this HyperflexClusterAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["NA", "Datacenter", "Stretched Cluster",
                          "Edge"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and deployment_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `deployment_type` ({0}), must be one of {1}"  # noqa: E501
                .format(deployment_type, allowed_values))

        self._deployment_type = deployment_type

    @property
    def device_id(self):
        """Gets the device_id of this HyperflexClusterAllOf.  # noqa: E501

        The unique identifier of the device registration that represents this HyperFlex cluster's connection to Intersight.    # noqa: E501

        :return: The device_id of this HyperflexClusterAllOf.  # noqa: E501
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this HyperflexClusterAllOf.

        The unique identifier of the device registration that represents this HyperFlex cluster's connection to Intersight.    # noqa: E501

        :param device_id: The device_id of this HyperflexClusterAllOf.  # noqa: E501
        :type: str
        """

        self._device_id = device_id

    @property
    def flt_aggr(self):
        """Gets the flt_aggr of this HyperflexClusterAllOf.  # noqa: E501

        The number of yellow (warning) and red (critical) alarms stored as an aggregate.  The first 16 bits indicate the number of red alarms, and the last 16 bits contain the number of yellow alarms.     # noqa: E501

        :return: The flt_aggr of this HyperflexClusterAllOf.  # noqa: E501
        :rtype: int
        """
        return self._flt_aggr

    @flt_aggr.setter
    def flt_aggr(self, flt_aggr):
        """Sets the flt_aggr of this HyperflexClusterAllOf.

        The number of yellow (warning) and red (critical) alarms stored as an aggregate.  The first 16 bits indicate the number of red alarms, and the last 16 bits contain the number of yellow alarms.     # noqa: E501

        :param flt_aggr: The flt_aggr of this HyperflexClusterAllOf.  # noqa: E501
        :type: int
        """

        self._flt_aggr = flt_aggr

    @property
    def hx_version(self):
        """Gets the hx_version of this HyperflexClusterAllOf.  # noqa: E501

        The HyperFlex Data Platform version of this cluster.    # noqa: E501

        :return: The hx_version of this HyperflexClusterAllOf.  # noqa: E501
        :rtype: str
        """
        return self._hx_version

    @hx_version.setter
    def hx_version(self, hx_version):
        """Sets the hx_version of this HyperflexClusterAllOf.

        The HyperFlex Data Platform version of this cluster.    # noqa: E501

        :param hx_version: The hx_version of this HyperflexClusterAllOf.  # noqa: E501
        :type: str
        """

        self._hx_version = hx_version

    @property
    def hxdp_build_version(self):
        """Gets the hxdp_build_version of this HyperflexClusterAllOf.  # noqa: E501

        The version and build number of the HyperFlex Data Platform for this cluster.  After a cluster upgrade, this version string will be updated on the next inventory cycle to reflect the newly installed version.     # noqa: E501

        :return: The hxdp_build_version of this HyperflexClusterAllOf.  # noqa: E501
        :rtype: str
        """
        return self._hxdp_build_version

    @hxdp_build_version.setter
    def hxdp_build_version(self, hxdp_build_version):
        """Sets the hxdp_build_version of this HyperflexClusterAllOf.

        The version and build number of the HyperFlex Data Platform for this cluster.  After a cluster upgrade, this version string will be updated on the next inventory cycle to reflect the newly installed version.     # noqa: E501

        :param hxdp_build_version: The hxdp_build_version of this HyperflexClusterAllOf.  # noqa: E501
        :type: str
        """

        self._hxdp_build_version = hxdp_build_version

    @property
    def hypervisor_type(self):
        """Gets the hypervisor_type of this HyperflexClusterAllOf.  # noqa: E501

        The type of hypervisor running on this cluster.    # noqa: E501

        :return: The hypervisor_type of this HyperflexClusterAllOf.  # noqa: E501
        :rtype: str
        """
        return self._hypervisor_type

    @hypervisor_type.setter
    def hypervisor_type(self, hypervisor_type):
        """Sets the hypervisor_type of this HyperflexClusterAllOf.

        The type of hypervisor running on this cluster.    # noqa: E501

        :param hypervisor_type: The hypervisor_type of this HyperflexClusterAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["Unknown", "Hyper-V", "ESXi"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and hypervisor_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `hypervisor_type` ({0}), must be one of {1}"  # noqa: E501
                .format(hypervisor_type, allowed_values))

        self._hypervisor_type = hypervisor_type

    @property
    def hypervisor_version(self):
        """Gets the hypervisor_version of this HyperflexClusterAllOf.  # noqa: E501

        The version of hypervisor running on this cluster.    # noqa: E501

        :return: The hypervisor_version of this HyperflexClusterAllOf.  # noqa: E501
        :rtype: str
        """
        return self._hypervisor_version

    @hypervisor_version.setter
    def hypervisor_version(self, hypervisor_version):
        """Sets the hypervisor_version of this HyperflexClusterAllOf.

        The version of hypervisor running on this cluster.    # noqa: E501

        :param hypervisor_version: The hypervisor_version of this HyperflexClusterAllOf.  # noqa: E501
        :type: str
        """

        self._hypervisor_version = hypervisor_version

    @property
    def summary(self):
        """Gets the summary of this HyperflexClusterAllOf.  # noqa: E501


        :return: The summary of this HyperflexClusterAllOf.  # noqa: E501
        :rtype: HyperflexSummary
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this HyperflexClusterAllOf.


        :param summary: The summary of this HyperflexClusterAllOf.  # noqa: E501
        :type: HyperflexSummary
        """

        self._summary = summary

    @property
    def utilization_percentage(self):
        """Gets the utilization_percentage of this HyperflexClusterAllOf.  # noqa: E501

        The storage utilization percentage is computed based on total capacity and current capacity utilization.    # noqa: E501

        :return: The utilization_percentage of this HyperflexClusterAllOf.  # noqa: E501
        :rtype: float
        """
        return self._utilization_percentage

    @utilization_percentage.setter
    def utilization_percentage(self, utilization_percentage):
        """Sets the utilization_percentage of this HyperflexClusterAllOf.

        The storage utilization percentage is computed based on total capacity and current capacity utilization.    # noqa: E501

        :param utilization_percentage: The utilization_percentage of this HyperflexClusterAllOf.  # noqa: E501
        :type: float
        """

        self._utilization_percentage = utilization_percentage

    @property
    def utilization_trend_percentage(self):
        """Gets the utilization_trend_percentage of this HyperflexClusterAllOf.  # noqa: E501

        The storage utilization trend percentage represents the trend in percentage computed using the first and last point from historical data.    # noqa: E501

        :return: The utilization_trend_percentage of this HyperflexClusterAllOf.  # noqa: E501
        :rtype: float
        """
        return self._utilization_trend_percentage

    @utilization_trend_percentage.setter
    def utilization_trend_percentage(self, utilization_trend_percentage):
        """Sets the utilization_trend_percentage of this HyperflexClusterAllOf.

        The storage utilization trend percentage represents the trend in percentage computed using the first and last point from historical data.    # noqa: E501

        :param utilization_trend_percentage: The utilization_trend_percentage of this HyperflexClusterAllOf.  # noqa: E501
        :type: float
        """

        self._utilization_trend_percentage = utilization_trend_percentage

    @property
    def vm_count(self):
        """Gets the vm_count of this HyperflexClusterAllOf.  # noqa: E501

        The number of virtual machines present on this cluster.     # noqa: E501

        :return: The vm_count of this HyperflexClusterAllOf.  # noqa: E501
        :rtype: int
        """
        return self._vm_count

    @vm_count.setter
    def vm_count(self, vm_count):
        """Sets the vm_count of this HyperflexClusterAllOf.

        The number of virtual machines present on this cluster.     # noqa: E501

        :param vm_count: The vm_count of this HyperflexClusterAllOf.  # noqa: E501
        :type: int
        """

        self._vm_count = vm_count

    @property
    def alarm(self):
        """Gets the alarm of this HyperflexClusterAllOf.  # noqa: E501

        A reference to a hyperflexAlarm resource. When the $expand query parameter is specified, the referenced resource is returned inline. The alarms that have been raised for this HyperFlex cluster.  New alarms are added to this collection, and existing alarms are updated if the severity changes. Deleted alarms are not removed but are cleared by marking them as green.   # noqa: E501

        :return: The alarm of this HyperflexClusterAllOf.  # noqa: E501
        :rtype: list[HyperflexAlarm]
        """
        return self._alarm

    @alarm.setter
    def alarm(self, alarm):
        """Sets the alarm of this HyperflexClusterAllOf.

        A reference to a hyperflexAlarm resource. When the $expand query parameter is specified, the referenced resource is returned inline. The alarms that have been raised for this HyperFlex cluster.  New alarms are added to this collection, and existing alarms are updated if the severity changes. Deleted alarms are not removed but are cleared by marking them as green.   # noqa: E501

        :param alarm: The alarm of this HyperflexClusterAllOf.  # noqa: E501
        :type: list[HyperflexAlarm]
        """

        self._alarm = alarm

    @property
    def health(self):
        """Gets the health of this HyperflexClusterAllOf.  # noqa: E501


        :return: The health of this HyperflexClusterAllOf.  # noqa: E501
        :rtype: HyperflexHealth
        """
        return self._health

    @health.setter
    def health(self, health):
        """Sets the health of this HyperflexClusterAllOf.


        :param health: The health of this HyperflexClusterAllOf.  # noqa: E501
        :type: HyperflexHealth
        """

        self._health = health

    @property
    def nodes(self):
        """Gets the nodes of this HyperflexClusterAllOf.  # noqa: E501

        A reference to a hyperflexNode resource. When the $expand query parameter is specified, the referenced resource is returned inline. The nodes belonging to this HyperFlex cluster.  The node object contains inventory information about a specific HyperFlex node, such as host IP address, hypervisor type and version, and operational status.   # noqa: E501

        :return: The nodes of this HyperflexClusterAllOf.  # noqa: E501
        :rtype: list[HyperflexNode]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this HyperflexClusterAllOf.

        A reference to a hyperflexNode resource. When the $expand query parameter is specified, the referenced resource is returned inline. The nodes belonging to this HyperFlex cluster.  The node object contains inventory information about a specific HyperFlex node, such as host IP address, hypervisor type and version, and operational status.   # noqa: E501

        :param nodes: The nodes of this HyperflexClusterAllOf.  # noqa: E501
        :type: list[HyperflexNode]
        """

        self._nodes = nodes

    @property
    def registered_device(self):
        """Gets the registered_device of this HyperflexClusterAllOf.  # noqa: E501


        :return: The registered_device of this HyperflexClusterAllOf.  # noqa: E501
        :rtype: AssetDeviceRegistration
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """Sets the registered_device of this HyperflexClusterAllOf.


        :param registered_device: The registered_device of this HyperflexClusterAllOf.  # noqa: E501
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
        if not isinstance(other, HyperflexClusterAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HyperflexClusterAllOf):
            return True

        return self.to_dict() != other.to_dict()
