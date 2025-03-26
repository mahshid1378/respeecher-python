# coding: utf-8

"""
    Respeecher API

    API for interacting with Respeecher services, including key and session management, and calibration functionalities.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class FolderStatistics(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'folder_id': 'str',
        'stats': 'FolderStatisticsStats'
    }

    attribute_map = {
        'folder_id': 'folder_id',
        'stats': 'stats'
    }

    def __init__(self, folder_id=None, stats=None):  # noqa: E501
        """FolderStatistics - a model defined in Swagger"""  # noqa: E501
        self._folder_id = None
        self._stats = None
        self.discriminator = None
        if folder_id is not None:
            self.folder_id = folder_id
        if stats is not None:
            self.stats = stats

    @property
    def folder_id(self):
        """Gets the folder_id of this FolderStatistics.  # noqa: E501

        The unique identifier of the folder.  # noqa: E501

        :return: The folder_id of this FolderStatistics.  # noqa: E501
        :rtype: str
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        """Sets the folder_id of this FolderStatistics.

        The unique identifier of the folder.  # noqa: E501

        :param folder_id: The folder_id of this FolderStatistics.  # noqa: E501
        :type: str
        """

        self._folder_id = folder_id

    @property
    def stats(self):
        """Gets the stats of this FolderStatistics.  # noqa: E501


        :return: The stats of this FolderStatistics.  # noqa: E501
        :rtype: FolderStatisticsStats
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        """Sets the stats of this FolderStatistics.


        :param stats: The stats of this FolderStatistics.  # noqa: E501
        :type: FolderStatisticsStats
        """

        self._stats = stats

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(FolderStatistics, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FolderStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
