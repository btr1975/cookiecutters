"""
Some conversion normalizers
"""

import ipaddress
import inspect
from typing import Union

from ansible.errors import AnsiblePluginError


from ansible_collections.{{ cookiecutter.__git_repo_name }}.plugins.module_utils.validators.ip_address_validators import (
    is_ipv4_subnet,
)


def cidr_to_inverse_mask(value: str) -> str:
    """Function to convert a CIDR notation to a inverse mask notation

    :type value: String
    :param value: Value to convert Example: 192.168.1.0/24

    :rtype: String
    :returns: The converted value Example: 192.168.1.0 0.0.0.255

    :raises AnsiblePluginError: If exceptions occur
    """
    try:
        is_ipv4_subnet(value)

        ipv4_obj = ipaddress.ip_network(value)

    except Exception as error:
        raise AnsiblePluginError(f"exception: {inspect.currentframe().f_code.co_name} error: {error}") from error

    return f"{ipv4_obj.network_address} {ipv4_obj.hostmask}"


def ios_standard_acl_ipv4_subnet_normalizer(value: str) -> str:
    """Function to convert ACL subnets for Cisco IOS Devices for Standard ACLs

    :type value: String
    :param value: Value to convert Example: 192.168.1.0/24, or 192.168.1.1/32

    :rtype: String
    :returns: The converted value Example: 192.168.1.0 0.0.0.255, or 192.168.1.1

    :raises AnsiblePluginError: If exceptions occur
    """
    try:
        split_value = value.split("/")

        if int(split_value[1]) == 32:
            value = split_value[0]

        else:
            value = cidr_to_inverse_mask(value)

    except Exception as error:
        raise AnsiblePluginError(f"exception: {inspect.currentframe().f_code.co_name} error: {error}") from error

    return value


def ios_extended_acl_ipv4_subnet_normalizer(value: str) -> str:
    """Function to convert ACL subnets for Cisco IOS Devices for Extended ACLs

    :type value: String
    :param value: Value to convert Example: 192.168.1.0/24, or 192.168.1.1/32

    :rtype: String
    :returns: The converted value Example: 192.168.1.0 0.0.0.255, or host 192.168.1.1

    :raises AnsiblePluginError: If exceptions occur
    """
    try:
        split_value = value.split("/")

        if int(split_value[1]) == 32:
            value = f"host {split_value[0]}"

        else:
            value = cidr_to_inverse_mask(value)

    except Exception as error:
        raise AnsiblePluginError(f"exception: {inspect.currentframe().f_code.co_name} error: {error}") from error

    return value


def iosxr_standard_acl_ipv4_subnet_normalizer(value: str) -> str:
    """Function to convert ACL subnets for Cisco IOS-XR Devices for Standard ACLs

    :type value: String
    :param value: Value to convert Example: 192.168.1.0/24, or 192.168.1.1/32

    :rtype: String
    :returns: The converted value Example: 192.168.1.0 0.0.0.255, or host 192.168.1.1

    :raises AnsiblePluginError: If exceptions occur
    """
    try:
        split_value = value.split("/")

        if int(split_value[1]) == 32:
            value = f"host {split_value[0]}"

        else:
            value = cidr_to_inverse_mask(value)

    except Exception as error:
        raise AnsiblePluginError(f"exception: {inspect.currentframe().f_code.co_name} error: {error}") from error

    return value


def iosxr_extended_acl_ipv4_subnet_normalizer(value: str) -> str:
    """Function to convert ACL subnets for Cisco IOS-XR Devices for Extended ACLs

    :type value: String
    :param value: Value to convert Example: 192.168.1.0/24, or 192.168.1.1/32

    :rtype: String
    :returns: The converted value Example: 192.168.1.0 0.0.0.255, or host 192.168.1.1

    :raises AnsiblePluginError: If exceptions occur
    """
    try:
        split_value = value.split("/")

        if int(split_value[1]) == 32:
            value = f"host {split_value[0]}"

        else:
            value = cidr_to_inverse_mask(value)

    except Exception as error:
        raise AnsiblePluginError(f"exception: {inspect.currentframe().f_code.co_name} error: {error}") from error

    return value


def eos_standard_acl_ipv4_subnet_normalizer(value: str) -> str:
    """Function to convert ACL subnets for Arista EOS Devices for Standard ACLs

    :type value: String
    :param value: Value to convert Example: 192.168.1.0/24, or 192.168.1.1/32

    :rtype: String
    :returns: The converted value Example: 192.168.1.0/24, or host 192.168.1.1

    :raises AnsiblePluginError: If exceptions occur
    """
    try:
        split_value = value.split("/")

        if int(split_value[1]) == 32:
            value = f"host {split_value[0]}"

    except Exception as error:
        raise AnsiblePluginError(f"exception: {inspect.currentframe().f_code.co_name} error: {error}") from error

    return value


def eos_extended_acl_ipv4_subnet_normalizer(value: str) -> str:
    """Function to convert ACL subnets for Arista EOS Devices for Extended ACLs

    :type value: String
    :param value: Value to convert Example: 192.168.1.0/24, or 192.168.1.1/32

    :rtype: String
    :returns: The converted value Example: 192.168.1.0/24, or host 192.168.1.1

    :raises AnsiblePluginError: If exceptions occur
    """
    try:
        split_value = value.split("/")

        if int(split_value[1]) == 32:
            value = f"host {split_value[0]}"

    except Exception as error:
        raise AnsiblePluginError(f"exception: {inspect.currentframe().f_code.co_name} error: {error}") from error

    return value


def eos_port_normalizer(value: Union[str, int]) -> Union[str, int]:
    """Function to convert named, or numbered Protocol ports for Arista EOS Devices

    :type value: String
    :param value: Value to convert Example: sunrpc, or 111

    :rtype: String
    :returns: The converted value Example: sunrpc, or sunrpc

    :raises AnsiblePluginError: If exceptions occur
    """
    try:
        allowed_named_values = ["nfs", "sunrpc", "microsoft-ds"]

        port_number_to_name_values = {111: "sunrpc", 445: "microsoft-ds", 2049: "nfs"}

        if value in allowed_named_values:
            new_value = value

        elif port_number_to_name_values.get(int(value)):
            new_value = port_number_to_name_values.get(int(value))

        else:
            new_value = value

    except Exception as error:
        raise AnsiblePluginError(f"exception: {inspect.currentframe().f_code.co_name} error: {error}") from error

    return new_value
