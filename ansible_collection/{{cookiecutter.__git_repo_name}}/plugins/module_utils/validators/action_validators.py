"""
Validators for and 'action' option
"""

import inspect
from ansible.errors import AnsiblePluginError


def is_permit_deny(value: str) -> str:
    """Function to check if a value is 'permit' or 'deny'

    :type value: String
    :param value: Value to check Example: permit

    :rtype: String
    :returns: The validated value

    :raises AnsiblePluginError: If the value is not 'permit' or 'deny'
    """
    allowed_values = ["permit", "deny"]
    try:
        if value not in allowed_values:
            raise ValueError(f"{value} is not one of the following {allowed_values}")

    except Exception as error:
        raise AnsiblePluginError(f"exception: {inspect.currentframe().f_code.co_name} error: {error}") from error

    return value


def is_permit_deny_remark(value: str) -> str:
    """Function to check if a value is 'permit' or 'deny' or 'remark'

    :type value: String
    :param value: Value to check Example: permit

    :rtype: String
    :returns: The validated value

    :raises AnsiblePluginError: If the value is not 'permit' or 'deny' or 'remark'
    """
    allowed_values = ["permit", "deny", "remark"]
    try:
        if value not in allowed_values:
            raise ValueError(f"{value} is not one of the following {allowed_values}")

    except Exception as error:
        raise AnsiblePluginError(f"exception: {inspect.currentframe().f_code.co_name} error: {error}") from error

    return value
