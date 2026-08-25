"""
String validators
"""

import inspect
import re
from ansible.errors import AnsiblePluginError


def is_string_no_spaces(value: str) -> str:
    """Function to check if a value is a string with no spaces

    :type value: String
    :param value: Value to check Example: this-is-a-string

    :rtype: String
    :returns: The validated value

    :raises AnsiblePluginError: If the value is a string with spaces
    """
    try:
        regex = re.compile(r"^\S+$")

        if not re.match(regex, value):
            raise ValueError(f"'{value}' is not a string with no spaces")

    except Exception as error:
        raise AnsiblePluginError(f"exception: {inspect.currentframe().f_code.co_name} error: {error}") from error

    return value


def is_string_no_spaces_begin_end(value: str) -> str:
    """Function to check if a value is a string with no spaces in the beginning or ending

    :type value: String
    :param value: Value to check Example: 'this is  a string'

    :rtype: String
    :returns: The validated value

    :raises AnsiblePluginError: If the value is a string with spaces in the beginning or ending
    """
    try:
        regex = re.compile(r"^\S.*\S$")

        if not re.match(regex, value):
            raise ValueError(f"'{value}' is not a string with no spaces at the beginning or ending")

    except Exception as error:
        raise AnsiblePluginError(f"exception: {inspect.currentframe().f_code.co_name} error: {error}") from error

    return value
