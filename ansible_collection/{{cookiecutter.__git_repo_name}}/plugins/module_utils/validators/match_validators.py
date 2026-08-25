"""
Validators for and 'match' option
"""

import inspect
from ansible.errors import AnsiblePluginError


def is_le_ge(value: str) -> str:
    """Function to check if a value is 'le' or 'ge'

    :type value: String
    :param value: Value to check Example: le

    :rtype: String
    :returns: The validated value

    :raises AnsiblePluginError: If the value is not 'le' or 'ge'
    """
    allowed_values = ["le", "ge"]
    try:
        if value not in allowed_values:
            raise ValueError(f"{value} is not one of the following {allowed_values}")

    except Exception as error:
        raise AnsiblePluginError(f"exception: {inspect.currentframe().f_code.co_name} error: {error}") from error

    return value


def is_eq_gt_lt_neq_range(value: str) -> str:
    """Function to check if a value is 'eq', 'gt', 'lt', 'neq', or 'range'

    :type value: String
    :param value: Value to check Example: eq

    :rtype: String
    :returns: The validated value

    :raises AnsiblePluginError: If the value is not 'eq', 'gt', 'lt', 'neq', or 'range'
    """
    allowed_values = ["eq", "gt", "lt", "neq", "range"]
    try:
        if value not in allowed_values:
            raise ValueError(f"{value} is not one of the following {allowed_values}")

    except Exception as error:
        raise AnsiblePluginError(f"exception: {inspect.currentframe().f_code.co_name} error: {error}") from error

    return value
