# coding: utf-8

"""
    Cisco Intersight OpenAPI specification.

    The Cisco Intersight OpenAPI specification.

    OpenAPI spec version: 1.0.9-1295
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class WorkflowWebApi(object):
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
        'object_type': 'str',
        'body': 'str',
        'content_type': 'str',
        'name': 'str',
        'outcomes': 'object',
        'response_spec': 'ContentGrammar',
        'skip_on_condition': 'str',
        'timeout': 'int',
        'headers': 'object',
        'method': 'str',
        'protocol': 'str',
        'target_type': 'str',
        'url': 'str'
    }

    attribute_map = {
        'object_type': 'ObjectType',
        'body': 'Body',
        'content_type': 'ContentType',
        'name': 'Name',
        'outcomes': 'Outcomes',
        'response_spec': 'ResponseSpec',
        'skip_on_condition': 'SkipOnCondition',
        'timeout': 'Timeout',
        'headers': 'Headers',
        'method': 'Method',
        'protocol': 'Protocol',
        'target_type': 'TargetType',
        'url': 'Url'
    }

    def __init__(self, object_type=None, body=None, content_type='json', name=None, outcomes=None, response_spec=None, skip_on_condition=None, timeout=None, headers=None, method=None, protocol=None, target_type='Endpoint', url=None):
        """
        WorkflowWebApi - a model defined in Swagger
        """

        self._object_type = None
        self._body = None
        self._content_type = None
        self._name = None
        self._outcomes = None
        self._response_spec = None
        self._skip_on_condition = None
        self._timeout = None
        self._headers = None
        self._method = None
        self._protocol = None
        self._target_type = None
        self._url = None

        if object_type is not None:
          self.object_type = object_type
        if body is not None:
          self.body = body
        if content_type is not None:
          self.content_type = content_type
        if name is not None:
          self.name = name
        if outcomes is not None:
          self.outcomes = outcomes
        if response_spec is not None:
          self.response_spec = response_spec
        if skip_on_condition is not None:
          self.skip_on_condition = skip_on_condition
        if timeout is not None:
          self.timeout = timeout
        if headers is not None:
          self.headers = headers
        if method is not None:
          self.method = method
        if protocol is not None:
          self.protocol = protocol
        if target_type is not None:
          self.target_type = target_type
        if url is not None:
          self.url = url

    @property
    def object_type(self):
        """
        Gets the object_type of this WorkflowWebApi.
        The concrete type of this complex type.  The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.    

        :return: The object_type of this WorkflowWebApi.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this WorkflowWebApi.
        The concrete type of this complex type.  The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.    

        :param object_type: The object_type of this WorkflowWebApi.
        :type: str
        """

        self._object_type = object_type

    @property
    def body(self):
        """
        Gets the body of this WorkflowWebApi.
        The optional request body that is sent as part of this API request.  The request body can contain a golang template that can be populated with task input parameters and previous API output parameters.   

        :return: The body of this WorkflowWebApi.
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """
        Sets the body of this WorkflowWebApi.
        The optional request body that is sent as part of this API request.  The request body can contain a golang template that can be populated with task input parameters and previous API output parameters.   

        :param body: The body of this WorkflowWebApi.
        :type: str
        """

        self._body = body

    @property
    def content_type(self):
        """
        Gets the content_type of this WorkflowWebApi.
        Intersight Orchestrator, with the support of response parser specification, can extract the values from API responses and map them to task output parameters. The value extraction is supported for response content types XML and JSON.  The type of the content that gets passed as payload and response in this API.   

        :return: The content_type of this WorkflowWebApi.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """
        Sets the content_type of this WorkflowWebApi.
        Intersight Orchestrator, with the support of response parser specification, can extract the values from API responses and map them to task output parameters. The value extraction is supported for response content types XML and JSON.  The type of the content that gets passed as payload and response in this API.   

        :param content_type: The content_type of this WorkflowWebApi.
        :type: str
        """
        allowed_values = ["json", "xml", "text"]
        if content_type not in allowed_values:
            raise ValueError(
                "Invalid value for `content_type` ({0}), must be one of {1}"
                .format(content_type, allowed_values)
            )

        self._content_type = content_type

    @property
    def name(self):
        """
        Gets the name of this WorkflowWebApi.
        A reference name for this API request within the batch API request.  This name shall be used to map the API output parameters to subsequent API input parameters within a batch API task.   

        :return: The name of this WorkflowWebApi.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this WorkflowWebApi.
        A reference name for this API request within the batch API request.  This name shall be used to map the API output parameters to subsequent API input parameters within a batch API task.   

        :param name: The name of this WorkflowWebApi.
        :type: str
        """

        self._name = name

    @property
    def outcomes(self):
        """
        Gets the outcomes of this WorkflowWebApi.
        All the possible outcomes of this API are captured here. Outcomes property is a collection property of type workflow.Outcome objects.  The outcomes can be mapped to the message to be shown. The outcomes are evaluated in the order they are given. At the end of the outcomes list, an catchall success/fail outcome can be added with condition as 'true'.  This is an optional property and if not specified the task will be marked as success.   

        :return: The outcomes of this WorkflowWebApi.
        :rtype: object
        """
        return self._outcomes

    @outcomes.setter
    def outcomes(self, outcomes):
        """
        Sets the outcomes of this WorkflowWebApi.
        All the possible outcomes of this API are captured here. Outcomes property is a collection property of type workflow.Outcome objects.  The outcomes can be mapped to the message to be shown. The outcomes are evaluated in the order they are given. At the end of the outcomes list, an catchall success/fail outcome can be added with condition as 'true'.  This is an optional property and if not specified the task will be marked as success.   

        :param outcomes: The outcomes of this WorkflowWebApi.
        :type: object
        """

        self._outcomes = outcomes

    @property
    def response_spec(self):
        """
        Gets the response_spec of this WorkflowWebApi.
        The optional grammar specification for parsing the response to extract the required values.  The specification should have extraction specification specified for all the API output parameters.   

        :return: The response_spec of this WorkflowWebApi.
        :rtype: ContentGrammar
        """
        return self._response_spec

    @response_spec.setter
    def response_spec(self, response_spec):
        """
        Sets the response_spec of this WorkflowWebApi.
        The optional grammar specification for parsing the response to extract the required values.  The specification should have extraction specification specified for all the API output parameters.   

        :param response_spec: The response_spec of this WorkflowWebApi.
        :type: ContentGrammar
        """

        self._response_spec = response_spec

    @property
    def skip_on_condition(self):
        """
        Gets the skip_on_condition of this WorkflowWebApi.
        The skip expression, if provided, allows the batch API executor to skip the api execution when the given expression evaluates to true.  The expression is given as such a golang template that has to be evaluated to a final content true/false. The expression is an optional and in case not provided, the API will always be executed.   

        :return: The skip_on_condition of this WorkflowWebApi.
        :rtype: str
        """
        return self._skip_on_condition

    @skip_on_condition.setter
    def skip_on_condition(self, skip_on_condition):
        """
        Sets the skip_on_condition of this WorkflowWebApi.
        The skip expression, if provided, allows the batch API executor to skip the api execution when the given expression evaluates to true.  The expression is given as such a golang template that has to be evaluated to a final content true/false. The expression is an optional and in case not provided, the API will always be executed.   

        :param skip_on_condition: The skip_on_condition of this WorkflowWebApi.
        :type: str
        """

        self._skip_on_condition = skip_on_condition

    @property
    def timeout(self):
        """
        Gets the timeout of this WorkflowWebApi.
        The duration in seconds by which the API response is expected from the API target.  If the end point does not respond for the API request within this timeout duration, the task will be marked as failed.    

        :return: The timeout of this WorkflowWebApi.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """
        Sets the timeout of this WorkflowWebApi.
        The duration in seconds by which the API response is expected from the API target.  If the end point does not respond for the API request within this timeout duration, the task will be marked as failed.    

        :param timeout: The timeout of this WorkflowWebApi.
        :type: int
        """

        self._timeout = timeout

    @property
    def headers(self):
        """
        Gets the headers of this WorkflowWebApi.
        Collection of key value pairs to set in the request header.   

        :return: The headers of this WorkflowWebApi.
        :rtype: object
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """
        Sets the headers of this WorkflowWebApi.
        Collection of key value pairs to set in the request header.   

        :param headers: The headers of this WorkflowWebApi.
        :type: object
        """

        self._headers = headers

    @property
    def method(self):
        """
        Gets the method of this WorkflowWebApi.
        The HTTP method to be executed in the given URL (GET, POST, PUT, etc). If the value is not specified, GET will be used as default.   

        :return: The method of this WorkflowWebApi.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """
        Sets the method of this WorkflowWebApi.
        The HTTP method to be executed in the given URL (GET, POST, PUT, etc). If the value is not specified, GET will be used as default.   

        :param method: The method of this WorkflowWebApi.
        :type: str
        """

        self._method = method

    @property
    def protocol(self):
        """
        Gets the protocol of this WorkflowWebApi.
        The accepted web protocol values are http and https.   

        :return: The protocol of this WorkflowWebApi.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this WorkflowWebApi.
        The accepted web protocol values are http and https.   

        :param protocol: The protocol of this WorkflowWebApi.
        :type: str
        """

        self._protocol = protocol

    @property
    def target_type(self):
        """
        Gets the target_type of this WorkflowWebApi.
        If the web API is to be executed in a remote device connected to the Intersight through device connector, 'Endpoint' is expected as the value whereas if the API is an Intersight API, 'Local' is expected as the value.   

        :return: The target_type of this WorkflowWebApi.
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        """
        Sets the target_type of this WorkflowWebApi.
        If the web API is to be executed in a remote device connected to the Intersight through device connector, 'Endpoint' is expected as the value whereas if the API is an Intersight API, 'Local' is expected as the value.   

        :param target_type: The target_type of this WorkflowWebApi.
        :type: str
        """
        allowed_values = ["Endpoint", "Local"]
        if target_type not in allowed_values:
            raise ValueError(
                "Invalid value for `target_type` ({0}), must be one of {1}"
                .format(target_type, allowed_values)
            )

        self._target_type = target_type

    @property
    def url(self):
        """
        Gets the url of this WorkflowWebApi.
        The URL of the resource in the target to which the API request is made.    

        :return: The url of this WorkflowWebApi.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this WorkflowWebApi.
        The URL of the resource in the target to which the API request is made.    

        :param url: The url of this WorkflowWebApi.
        :type: str
        """

        self._url = url

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
        if not isinstance(other, WorkflowWebApi):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
