"""
Render filters
"""

import inspect
import ipaddress
from typing import Dict, Callable, Union


import jinja2
from ansible.module_utils.common.text.converters import to_native
from ansible.errors import AnsibleUndefinedVariable, AnsibleFilterError

from ansible_collections.{{ cookiecutter.__git_repo_name }}.plugins.module_utils.validators.ip_address_validators import (
    is_ipv4_host,
    is_ipv4_subnet,
    is_ipv4_prefix,
    is_cidr_range,
)

from ansible_collections.{{ cookiecutter.__git_repo_name }}.plugins.module_utils.validators.general_validators import (
    is_protocol,
    is_sequence_number,
)


from ansible_collections.{{ cookiecutter.__git_repo_name }}.plugins.module_utils.validators.action_validators import (
    is_permit_deny_remark,
    is_permit_deny,
)

from ansible_collections.{{ cookiecutter.__git_repo_name }}.plugins.module_utils.validators.string_validators import (
    is_string_no_spaces,
    is_string_no_spaces_begin_end,
)

from ansible_collections.{{ cookiecutter.__git_repo_name }}.plugins.module_utils.validators.match_validators import (
    is_eq_gt_lt_neq_range,
    is_le_ge,
)

from ansible_collections.{{ cookiecutter.__git_repo_name }}.plugins.module_utils.normalizers.conversion_normalizers import (
    ios_standard_acl_ipv4_subnet_normalizer,
    ios_extended_acl_ipv4_subnet_normalizer,
    iosxr_standard_acl_ipv4_subnet_normalizer,
    iosxr_extended_acl_ipv4_subnet_normalizer,
    eos_standard_acl_ipv4_subnet_normalizer,
    eos_extended_acl_ipv4_subnet_normalizer,
    eos_port_normalizer,
)

from ansible_collections.{{ cookiecutter.__git_repo_name }}.plugins.module_utils.normalizers.ansible_network_os_normalizers import (
    network_os_normalize,
)


def ipv4_host(value: str) -> str:
    """Filter plugin to validate a value is a ipv4_host address Example: 192.168.1.1

    :type value: String
    :param value: The value to validate

    :rtype: String
    :returns: The validated value

    :raises AnsibleUndefinedVariable: If jinja2 undefined variable
    :raises AnsibleFilterError: If any other exceptions occur
    """
    try:
        is_ipv4_host(value)

    except jinja2.exceptions.UndefinedError as error:  # pragma: no cover
        raise AnsibleUndefinedVariable(f"jinja2 exception happened in ipv4_host: {to_native(error)}") from error

    except Exception as error:
        raise AnsibleFilterError(
            f"exception: {inspect.currentframe().f_code.co_name} error: invalid ipv4_host {to_native(error)}"
        ) from error

    return value


def ipv4_subnet(value: str) -> str:
    """Filter plugin to validate a value is a ipv4_subnet address Example: 192.168.1.0/24

    :type value: String
    :param value: The value to validate

    :rtype: String
    :returns: The validated value

    :raises AnsibleUndefinedVariable: If jinja2 undefined variable
    :raises AnsibleFilterError: If any other exceptions occur
    """
    try:
        is_ipv4_subnet(value)

    except jinja2.exceptions.UndefinedError as error:  # pragma: no cover
        raise AnsibleUndefinedVariable(f"jinja2 exception happened in ipv4_subnet: {to_native(error)}") from error

    except Exception as error:
        raise AnsibleFilterError(
            f"exception: {inspect.currentframe().f_code.co_name} error: invalid ipv4_subnet {to_native(error)}"
        ) from error

    return value


def standard_acl_ipv4_subnet_normalizer(value: str, nos: str) -> str:
    """Normalize subnets in a standard acl for various network operating system's

    :type value: String
    :param value: The value to validate
    :type nos: String
    :param nos: The network operating system to normalize for

    :rtype: String
    :returns: The validated value

    :raises AnsibleUndefinedVariable: If jinja2 undefined variable
    :raises AnsibleFilterError: If any other exceptions occur
    """
    try:
        if value == "any":
            new_value = value

        else:
            is_ipv4_prefix(value)

            ipaddress.ip_network(value, strict=True)

            if network_os_normalize(nos) == "ios":
                new_value = ios_standard_acl_ipv4_subnet_normalizer(value)

            elif network_os_normalize(nos) == "iosxr":
                new_value = iosxr_standard_acl_ipv4_subnet_normalizer(value)

            elif network_os_normalize(nos) == "eos":
                new_value = eos_standard_acl_ipv4_subnet_normalizer(value)

            else:
                new_value = value

    except jinja2.exceptions.UndefinedError as error:  # pragma: no cover
        raise AnsibleUndefinedVariable(f"jinja2 exception: {to_native(error)}") from error

    except Exception as error:
        raise AnsibleFilterError(
            f"exception: {inspect.currentframe().f_code.co_name} error: {to_native(error)}"
        ) from error

    return new_value


def extended_acl_ipv4_subnet_normalizer(value: str, nos: str) -> str:
    """Normalize subnets in a extended acl for various network operating system's

    :type value: String
    :param value: The value to validate
    :type nos: String
    :param nos: The network operating system to normalize for

    :rtype: String
    :returns: The validated value

    :raises AnsibleUndefinedVariable: If jinja2 undefined variable
    :raises AnsibleFilterError: If any other exceptions occur
    """
    try:
        if value == "any":
            new_value = value

        else:
            is_ipv4_prefix(value)

            ipaddress.ip_network(value, strict=True)

            if network_os_normalize(nos) == "ios":
                new_value = ios_extended_acl_ipv4_subnet_normalizer(value)

            elif network_os_normalize(nos) == "iosxr":
                new_value = iosxr_extended_acl_ipv4_subnet_normalizer(value)

            elif network_os_normalize(nos) == "eos":
                new_value = eos_extended_acl_ipv4_subnet_normalizer(value)

            else:
                new_value = value

    except jinja2.exceptions.UndefinedError as error:  # pragma: no cover
        raise AnsibleUndefinedVariable(f"jinja2 exception: {to_native(error)}") from error

    except Exception as error:
        raise AnsibleFilterError(
            f"exception: {inspect.currentframe().f_code.co_name} error: {to_native(error)}"
        ) from error

    return new_value


def protocol(value: str) -> str:
    """Check for a valid protocol

    :type value: String
    :param value: The value to validate

    :rtype: String
    :returns: The validated value

    :raises AnsibleUndefinedVariable: If jinja2 undefined variable
    :raises AnsibleFilterError: If any other exceptions occur
    """
    try:
        is_protocol(value)

    except jinja2.exceptions.UndefinedError as error:  # pragma: no cover
        raise AnsibleUndefinedVariable(f"jinja2 exception: {to_native(error)}") from error

    except Exception as error:
        raise AnsibleFilterError(
            f"exception: {inspect.currentframe().f_code.co_name} error: {to_native(error)}"
        ) from error

    return value


def port_match(value: str) -> str:
    """Check for a valid port matching option

    :type value: String
    :param value: The value to validate

    :rtype: String
    :returns: The validated value

    :raises AnsibleUndefinedVariable: If jinja2 undefined variable
    :raises AnsibleFilterError: If any other exceptions occur
    """
    try:
        is_eq_gt_lt_neq_range(value)

    except jinja2.exceptions.UndefinedError as error:  # pragma: no cover
        raise AnsibleUndefinedVariable(f"jinja2 exception: {to_native(error)}") from error

    except Exception as error:
        raise AnsibleFilterError(
            f"exception: {inspect.currentframe().f_code.co_name} error: {to_native(error)}"
        ) from error

    return value


def port_or_ports(value: Union[str, int], port_match_value: str, nos: str) -> Union[str, int]:
    """Check for a valid port or ports, based on port_natch

    :type value: String
    :param value: The value to validate
    :type port_match_value: String
    :param port_match_value: The port match type
    :type nos: String
    :param nos: The network operating system to normalize for

    :rtype: Union[str,int]
    :returns: The validated value

    :raises AnsibleUndefinedVariable: If jinja2 undefined variable
    :raises AnsibleFilterError: If any other exceptions occur
    """
    try:
        validated_port_match_value = is_eq_gt_lt_neq_range(port_match_value)

        if validated_port_match_value == "range":
            split_value = value.split(",")

            if len(split_value) != 2:
                raise ValueError(f"port or ports is not valid '{value}'")

            if int(split_value[0]) > int(split_value[1]):
                raise ValueError(f"port or ports is not valid '{value}' first port greater than second")

            new_value = f"{split_value[0]} {split_value[1]}"

        else:
            if network_os_normalize(nos) == "eos":
                new_value = eos_port_normalizer(value)

            else:
                new_value = int(value)

    except jinja2.exceptions.UndefinedError as error:  # pragma: no cover
        raise AnsibleUndefinedVariable(f"jinja2 exception: {to_native(error)}") from error

    except Exception as error:
        raise AnsibleFilterError(
            f"exception: {inspect.currentframe().f_code.co_name} error: {to_native(error)}"
        ) from error

    return new_value


def acl_append_options_to_end(value: Union[list, None]) -> str:
    """Append options to ACL at the end of the statement

    :type value: Union[list, None]
    :param value: The value to validate

    :rtype: String
    :returns: The validated value

    :raises AnsibleUndefinedVariable: If jinja2 undefined variable
    :raises AnsibleFilterError: If any other exceptions occur
    """
    try:
        allowed_values = ["log"]

        if not value:
            new_value = ""

        elif isinstance(value, list):
            for item in value:
                if item not in allowed_values:
                    raise ValueError(f"'{item} is not a valid option, the valid options are {allowed_values}")

            new_value = f' {" ".join(value)}'

        else:
            raise TypeError(f"'{value}' if supplied must be of type list but received a {type(value)}")

    except jinja2.exceptions.UndefinedError as error:  # pragma: no cover
        raise AnsibleUndefinedVariable(f"jinja2 exception: {to_native(error)}") from error

    except Exception as error:
        raise AnsibleFilterError(
            f"exception: {inspect.currentframe().f_code.co_name} error: {to_native(error)}"
        ) from error

    return new_value


def permit_deny_remark(value: str) -> str:
    """Check for a valid action option

    :type value: String
    :param value: The value to validate

    :rtype: String
    :returns: The validated value

    :raises AnsibleUndefinedVariable: If jinja2 undefined variable
    :raises AnsibleFilterError: If any other exceptions occur
    """
    try:
        is_permit_deny_remark(value)

    except jinja2.exceptions.UndefinedError as error:  # pragma: no cover
        raise AnsibleUndefinedVariable(f"jinja2 exception: {to_native(error)}") from error

    except Exception as error:
        raise AnsibleFilterError(
            f"exception: {inspect.currentframe().f_code.co_name} error: {to_native(error)}"
        ) from error

    return value


def permit_deny(value: str) -> str:
    """Check for a valid action option

    :type value: String
    :param value: The value to validate

    :rtype: String
    :returns: The validated value

    :raises AnsibleUndefinedVariable: If jinja2 undefined variable
    :raises AnsibleFilterError: If any other exceptions occur
    """
    try:
        is_permit_deny(value)

    except jinja2.exceptions.UndefinedError as error:  # pragma: no cover
        raise AnsibleUndefinedVariable(f"jinja2 exception: {to_native(error)}") from error

    except Exception as error:
        raise AnsibleFilterError(
            f"exception: {inspect.currentframe().f_code.co_name} error: {to_native(error)}"
        ) from error

    return value


def sequence_number(value: str) -> str:
    """Check for a valid sequence number

    :type value: String
    :param value: The value to validate

    :rtype: String
    :returns: The validated value

    :raises AnsibleUndefinedVariable: If jinja2 undefined variable
    :raises AnsibleFilterError: If any other exceptions occur
    """
    try:
        is_sequence_number(value)

    except jinja2.exceptions.UndefinedError as error:  # pragma: no cover
        raise AnsibleUndefinedVariable(f"jinja2 exception: {to_native(error)}") from error

    except Exception as error:
        raise AnsibleFilterError(
            f"exception: {inspect.currentframe().f_code.co_name} error: {to_native(error)}"
        ) from error

    return value


def required_string_no_spaces(value: str) -> str:
    """Check for a valid string with no spaces in it

    :type value: String
    :param value: The value to validate

    :rtype: String
    :returns: The validated value

    :raises AnsibleUndefinedVariable: If jinja2 undefined variable
    :raises AnsibleFilterError: If any other exceptions occur
    """
    try:
        is_string_no_spaces(value)

    except jinja2.exceptions.UndefinedError as error:  # pragma: no cover
        raise AnsibleUndefinedVariable(f"jinja2 exception: {to_native(error)}") from error

    except Exception as error:
        raise AnsibleFilterError(
            f"exception: {inspect.currentframe().f_code.co_name} error: {to_native(error)}"
        ) from error

    return value


def required_string_no_spaces_begin_or_end(value: str) -> str:
    """Check for a valid string with no spaces at the beginning or end

    :type value: String
    :param value: The value to validate

    :rtype: String
    :returns: The validated value

    :raises AnsibleUndefinedVariable: If jinja2 undefined variable
    :raises AnsibleFilterError: If any other exceptions occur
    """
    try:
        is_string_no_spaces_begin_end(value)

    except jinja2.exceptions.UndefinedError as error:  # pragma: no cover
        raise AnsibleUndefinedVariable(f"jinja2 exception: {to_native(error)}") from error

    except Exception as error:
        raise AnsibleFilterError(
            f"exception: {inspect.currentframe().f_code.co_name} error: {to_native(error)}"
        ) from error

    return value


def le_ge(value: str) -> str:
    """Check for a valid action option

    :type value: String
    :param value: The value to validate

    :rtype: String
    :returns: The validated value

    :raises AnsibleUndefinedVariable: If jinja2 undefined variable
    :raises AnsibleFilterError: If any other exceptions occur
    """
    try:
        is_le_ge(value)

    except jinja2.exceptions.UndefinedError as error:  # pragma: no cover
        raise AnsibleUndefinedVariable(f"jinja2 exception: {to_native(error)}") from error

    except Exception as error:
        raise AnsibleFilterError(
            f"exception: {inspect.currentframe().f_code.co_name} error: {to_native(error)}"
        ) from error

    return value


def cidr_range(value: str) -> str:
    """Check for a valid action option

    :type value: String
    :param value: The value to validate

    :rtype: String
    :returns: The validated value

    :raises AnsibleUndefinedVariable: If jinja2 undefined variable
    :raises AnsibleFilterError: If any other exceptions occur
    """
    try:
        is_cidr_range(value)

    except jinja2.exceptions.UndefinedError as error:  # pragma: no cover
        raise AnsibleUndefinedVariable(f"jinja2 exception: {to_native(error)}") from error

    except Exception as error:
        raise AnsibleFilterError(
            f"exception: {inspect.currentframe().f_code.co_name} error: {to_native(error)}"
        ) from error

    return value


class FilterModule:  # pylint: disable=too-few-public-methods
    """Class required by Ansible to load filters"""

    def filters(self) -> Dict[str, Callable]:
        """Method to return a KV pair of the filter

        :rtype: Dict[str, Callable]
        :returns: The dictionary of keys to callables
        """
        return {
            "ipv4_host": ipv4_host,
            "ipv4_subnet": ipv4_subnet,
            "standard_acl_ipv4_subnet_normalizer": standard_acl_ipv4_subnet_normalizer,
            "extended_acl_ipv4_subnet_normalizer": extended_acl_ipv4_subnet_normalizer,
            "protocol": protocol,
            "port_match": port_match,
            "port_or_ports": port_or_ports,
            "acl_append_options_to_end": acl_append_options_to_end,
            "permit_deny_remark": permit_deny_remark,
            "sequence_number": sequence_number,
            "required_string_no_spaces": required_string_no_spaces,
            "required_string_no_spaces_begin_or_end": required_string_no_spaces_begin_or_end,
            "permit_deny": permit_deny,
            "le_ge": le_ge,
            "cidr_range": cidr_range,
        }
