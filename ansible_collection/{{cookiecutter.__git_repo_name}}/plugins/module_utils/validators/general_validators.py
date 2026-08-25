"""
Validators for general items option
"""

import inspect
from typing import Union
from ansible.errors import AnsiblePluginError


def is_sequence_number(value: Union[str, int]) -> Union[str, int]:
    """Function to check if a value is an integer for a sequence number

    :type value: Union[str, int]
    :param value: Value to check

    :rtype: Union[str, int]
    :returns: The validated value

    :raises AnsiblePluginError: If the value is not an integer for a sequence number
    """
    try:
        int(value)

    except Exception as error:
        raise AnsiblePluginError(f"exception: {inspect.currentframe().f_code.co_name} error: {error}") from error

    return value


def is_protocol(value: str) -> str:
    """Function to check if a value is valid protocol

    :type value: String
    :param value: Value to check

    :rtype: String
    :returns: The validated value

    :raises AnsiblePluginError: If the value is not a valid protocol
    """
    allowed_values = ["icmp", "ip", "tcp", "udp"]

    try:
        if value not in allowed_values:
            raise ValueError(f"protocol: '{value}' is not a valid option. the valid options ar {allowed_values}")

    except Exception as error:
        raise AnsiblePluginError(f"exception: {inspect.currentframe().f_code.co_name} error: {error}") from error

    return value
