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


class OnpremSchedule(object):
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
        'day_of_month': 'int',
        'day_of_week': 'int',
        'month_of_year': 'int',
        'repeat_interval': 'int',
        'time_of_day': 'int',
        'time_zone': 'str',
        'week_of_month': 'int'
    }

    attribute_map = {
        'object_type': 'ObjectType',
        'day_of_month': 'DayOfMonth',
        'day_of_week': 'DayOfWeek',
        'month_of_year': 'MonthOfYear',
        'repeat_interval': 'RepeatInterval',
        'time_of_day': 'TimeOfDay',
        'time_zone': 'TimeZone',
        'week_of_month': 'WeekOfMonth'
    }

    def __init__(self, object_type=None, day_of_month=None, day_of_week=None, month_of_year=None, repeat_interval=None, time_of_day=None, time_zone='Pacific/Niue', week_of_month=None):
        """
        OnpremSchedule - a model defined in Swagger
        """

        self._object_type = None
        self._day_of_month = None
        self._day_of_week = None
        self._month_of_year = None
        self._repeat_interval = None
        self._time_of_day = None
        self._time_zone = None
        self._week_of_month = None

        if object_type is not None:
          self.object_type = object_type
        if day_of_month is not None:
          self.day_of_month = day_of_month
        if day_of_week is not None:
          self.day_of_week = day_of_week
        if month_of_year is not None:
          self.month_of_year = month_of_year
        if repeat_interval is not None:
          self.repeat_interval = repeat_interval
        if time_of_day is not None:
          self.time_of_day = time_of_day
        if time_zone is not None:
          self.time_zone = time_zone
        if week_of_month is not None:
          self.week_of_month = week_of_month

    @property
    def object_type(self):
        """
        Gets the object_type of this OnpremSchedule.
        The concrete type of this complex type.  The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.    

        :return: The object_type of this OnpremSchedule.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this OnpremSchedule.
        The concrete type of this complex type.  The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.    

        :param object_type: The object_type of this OnpremSchedule.
        :type: str
        """

        self._object_type = object_type

    @property
    def day_of_month(self):
        """
        Gets the day_of_month of this OnpremSchedule.
        Schedule a task on a specific day of the month. Valid values are 1 through 31. If monthOfYear is specified, then dayOfMonth value must be valid for that month. DayOfMonth may not be set when dayOfWeek is specfied.  

        :return: The day_of_month of this OnpremSchedule.
        :rtype: int
        """
        return self._day_of_month

    @day_of_month.setter
    def day_of_month(self, day_of_month):
        """
        Sets the day_of_month of this OnpremSchedule.
        Schedule a task on a specific day of the month. Valid values are 1 through 31. If monthOfYear is specified, then dayOfMonth value must be valid for that month. DayOfMonth may not be set when dayOfWeek is specfied.  

        :param day_of_month: The day_of_month of this OnpremSchedule.
        :type: int
        """

        self._day_of_month = day_of_month

    @property
    def day_of_week(self):
        """
        Gets the day_of_week of this OnpremSchedule.
        Schedule a task on a specific day of the week. Valid values are 1 through 7, with 1 being Sunday. DayOfWeek may not be specfied when dayOfMonth is specified.  

        :return: The day_of_week of this OnpremSchedule.
        :rtype: int
        """
        return self._day_of_week

    @day_of_week.setter
    def day_of_week(self, day_of_week):
        """
        Sets the day_of_week of this OnpremSchedule.
        Schedule a task on a specific day of the week. Valid values are 1 through 7, with 1 being Sunday. DayOfWeek may not be specfied when dayOfMonth is specified.  

        :param day_of_week: The day_of_week of this OnpremSchedule.
        :type: int
        """

        self._day_of_week = day_of_week

    @property
    def month_of_year(self):
        """
        Gets the month_of_year of this OnpremSchedule.
        Schedule a task on a specific month of the year. Valid values are 1 through 12, with 1 being January.  

        :return: The month_of_year of this OnpremSchedule.
        :rtype: int
        """
        return self._month_of_year

    @month_of_year.setter
    def month_of_year(self, month_of_year):
        """
        Sets the month_of_year of this OnpremSchedule.
        Schedule a task on a specific month of the year. Valid values are 1 through 12, with 1 being January.  

        :param month_of_year: The month_of_year of this OnpremSchedule.
        :type: int
        """

        self._month_of_year = month_of_year

    @property
    def repeat_interval(self):
        """
        Gets the repeat_interval of this OnpremSchedule.
        Schedule a task to run periodically at an interval. Default unit of the RepeatInterval is in minutes. If the RepeateInterval value is set, then all other properties are ignored by the scheduler. RepeateInterval constraints are enforced by the services that use the schedule. Each service has pre-configured service specific properties for enforcing minimum and maximum values of the RepeatInterval.  

        :return: The repeat_interval of this OnpremSchedule.
        :rtype: int
        """
        return self._repeat_interval

    @repeat_interval.setter
    def repeat_interval(self, repeat_interval):
        """
        Sets the repeat_interval of this OnpremSchedule.
        Schedule a task to run periodically at an interval. Default unit of the RepeatInterval is in minutes. If the RepeateInterval value is set, then all other properties are ignored by the scheduler. RepeateInterval constraints are enforced by the services that use the schedule. Each service has pre-configured service specific properties for enforcing minimum and maximum values of the RepeatInterval.  

        :param repeat_interval: The repeat_interval of this OnpremSchedule.
        :type: int
        """

        self._repeat_interval = repeat_interval

    @property
    def time_of_day(self):
        """
        Gets the time_of_day of this OnpremSchedule.
        Time of the day in seconds. TimeOfDay is required for all schedule configurations, except when the RepeateInterval field is specified.  

        :return: The time_of_day of this OnpremSchedule.
        :rtype: int
        """
        return self._time_of_day

    @time_of_day.setter
    def time_of_day(self, time_of_day):
        """
        Sets the time_of_day of this OnpremSchedule.
        Time of the day in seconds. TimeOfDay is required for all schedule configurations, except when the RepeateInterval field is specified.  

        :param time_of_day: The time_of_day of this OnpremSchedule.
        :type: int
        """

        self._time_of_day = time_of_day

    @property
    def time_zone(self):
        """
        Gets the time_zone of this OnpremSchedule.
        Timezone to use for the schedule calculation. If a timezone value is not speficied, then the schedule calculation will be based on UTC.  

        :return: The time_zone of this OnpremSchedule.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """
        Sets the time_zone of this OnpremSchedule.
        Timezone to use for the schedule calculation. If a timezone value is not speficied, then the schedule calculation will be based on UTC.  

        :param time_zone: The time_zone of this OnpremSchedule.
        :type: str
        """
        allowed_values = ["Pacific/Niue", "Pacific/Pago_Pago", "Pacific/Honolulu", "Pacific/Rarotonga", "Pacific/Tahiti", "Pacific/Marquesas", "America/Anchorage", "Pacific/Gambier", "America/Los_Angeles", "America/Tijuana", "America/Vancouver", "America/Whitehorse", "Pacific/Pitcairn", "America/Dawson_Creek", "America/Denver", "America/Edmonton", "America/Hermosillo", "America/Mazatlan", "America/Phoenix", "America/Yellowknife", "America/Belize", "America/Chicago", "America/Costa_Rica", "America/El_Salvador", "America/Guatemala", "America/Managua", "America/Mexico_City", "America/Regina", "America/Tegucigalpa", "America/Winnipeg", "Pacific/Galapagos", "America/Bogota", "America/Cancun", "America/Cayman", "America/Guayaquil", "America/Havana", "America/Iqaluit", "America/Jamaica", "America/Lima", "America/Nassau", "America/New_York", "America/Panama", "America/Port-au-Prince", "America/Rio_Branco", "America/Toronto", "Pacific/Easter", "America/Caracas", "America/Asuncion", "America/Barbados", "America/Boa_Vista", "America/Campo_Grande", "America/Cuiaba", "America/Curacao", "America/Grand_Turk", "America/Guyana", "America/Halifax", "America/La_Paz", "America/Manaus", "America/Martinique", "America/Port_of_Spain", "America/Porto_Velho", "America/Puerto_Rico", "America/Santo_Domingo", "America/Thule", "Atlantic/Bermuda", "America/St_Johns", "America/Araguaina", "America/Argentina/Buenos_Aires", "America/Bahia", "America/Belem", "America/Cayenne", "America/Fortaleza", "America/Godthab", "America/Maceio", "America/Miquelon", "America/Montevideo", "America/Paramaribo", "America/Recife", "America/Santiago", "America/Sao_Paulo", "Antarctica/Palmer", "Antarctica/Rothera", "Atlantic/Stanley", "America/Noronha", "Atlantic/South_Georgia", "America/Scoresbysund", "Atlantic/Azores", "Atlantic/Cape_Verde", "Africa/Abidjan", "Africa/Accra", "Africa/Bissau", "Africa/Casablanca", "Africa/El_Aaiun", "Africa/Monrovia", "America/Danmarkshavn", "Atlantic/Canary", "Atlantic/Faroe", "Atlantic/Reykjavik", "Etc/GMT", "Europe/Dublin", "Europe/Lisbon", "Europe/London", "Africa/Algiers", "Africa/Ceuta", "Africa/Lagos", "Africa/Ndjamena", "Africa/Tunis", "Africa/Windhoek", "Europe/Amsterdam", "Europe/Andorra", "Europe/Belgrade", "Europe/Berlin", "Europe/Brussels", "Europe/Budapest", "Europe/Copenhagen", "Europe/Gibraltar", "Europe/Luxembourg", "Europe/Madrid", "Europe/Malta", "Europe/Monaco", "Europe/Oslo", "Europe/Paris", "Europe/Prague", "Europe/Rome", "Europe/Stockholm", "Europe/Tirane", "Europe/Vienna", "Europe/Warsaw", "Europe/Zurich", "Africa/Cairo", "Africa/Johannesburg", "Africa/Maputo", "Africa/Tripoli", "Asia/Amman", "Asia/Beirut", "Asia/Damascus", "Asia/Gaza", "Asia/Jerusalem", "Asia/Nicosia", "Europe/Athens", "Europe/Bucharest", "Europe/Chisinau", "Europe/Helsinki", "Europe/Istanbul", "Europe/Kaliningrad", "Europe/Kiev", "Europe/Riga", "Europe/Sofia", "Europe/Tallinn", "Europe/Vilnius", "Africa/Khartoum", "Africa/Nairobi", "Antarctica/Syowa", "Asia/Baghdad", "Asia/Qatar", "Asia/Riyadh", "Europe/Minsk", "Europe/Moscow", "Asia/Tehran", "Asia/Baku", "Asia/Dubai", "Asia/Tbilisi", "Asia/Yerevan", "Europe/Samara", "Indian/Mahe", "Indian/Mauritius", "Indian/Reunion", "Asia/Kabul", "Antarctica/Mawson", "Asia/Aqtau", "Asia/Aqtobe", "Asia/Ashgabat", "Asia/Dushanbe", "Asia/Karachi", "Asia/Tashkent", "Asia/Yekaterinburg", "Indian/Kerguelen", "Indian/Maldives", "Asia/Calcutta", "Asia/Kolkata", "Asia/Colombo", "Asia/Katmandu", "Antarctica/Vostok", "Asia/Almaty", "Asia/Bishkek", "Asia/Dhaka", "Asia/Omsk", "Asia/Thimphu", "Indian/Chagos", "Asia/Rangoon", "Indian/Cocos", "Antarctica/Davis", "Asia/Bangkok", "Asia/Hovd", "Asia/Jakarta", "Asia/Krasnoyarsk", "Asia/Saigon", "Indian/Christmas", "Antarctica/Casey", "Asia/Brunei", "Asia/Choibalsan", "Asia/Hong_Kong", "Asia/Irkutsk", "Asia/Kuala_Lumpur", "Asia/Macau", "Asia/Makassar", "Asia/Manila", "Asia/Shanghai", "Asia/Singapore", "Asia/Taipei", "Asia/Ulaanbaatar", "Australia/Perth", "Asia/Pyongyang", "Asia/Dili", "Asia/Jayapura", "Asia/Seoul", "Asia/Tokyo", "Asia/Yakutsk", "Pacific/Palau", "Australia/Adelaide", "Australia/Darwin", "Antarctica/DumontDUrville", "Asia/Magadan", "Asia/Vladivostok", "Australia/Brisbane", "Australia/Hobart", "Australia/Sydney", "Pacific/Chuuk", "Pacific/Guam", "Pacific/Port_Moresby", "Pacific/Efate", "Pacific/Guadalcanal", "Pacific/Kosrae", "Pacific/Norfolk", "Pacific/Noumea", "Pacific/Pohnpei", "Asia/Kamchatka", "Pacific/Auckland", "Pacific/Fiji", "Pacific/Funafuti", "Pacific/Kwajalein", "Pacific/Majuro", "Pacific/Nauru", "Pacific/Tarawa", "Pacific/Wake", "Pacific/Wallis", "Pacific/Apia", "Pacific/Enderbury", "Pacific/Fakaofo", "Pacific/Tongatapu", "Pacific/Kiritimati"]
        if time_zone not in allowed_values:
            raise ValueError(
                "Invalid value for `time_zone` ({0}), must be one of {1}"
                .format(time_zone, allowed_values)
            )

        self._time_zone = time_zone

    @property
    def week_of_month(self):
        """
        Gets the week_of_month of this OnpremSchedule.
        Schedule a task on a specific week of the month. Valid values are 1 through 5. Value of 5 means last week of the month. WeekOfMonth may not be set when dayOfMonth is specified.   

        :return: The week_of_month of this OnpremSchedule.
        :rtype: int
        """
        return self._week_of_month

    @week_of_month.setter
    def week_of_month(self, week_of_month):
        """
        Sets the week_of_month of this OnpremSchedule.
        Schedule a task on a specific week of the month. Valid values are 1 through 5. Value of 5 means last week of the month. WeekOfMonth may not be set when dayOfMonth is specified.   

        :param week_of_month: The week_of_month of this OnpremSchedule.
        :type: int
        """

        self._week_of_month = week_of_month

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
        if not isinstance(other, OnpremSchedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
