"""
Validators for IPv4 and IPv6 Addresses
"""

import inspect
from typing import Union
import ipaddress
from ansible.errors import AnsiblePluginError


def is_ipv4_host(value: str) -> str:
    """Function to check if a value is an IPv4 host

    :type value: String
    :param value: Value to check Example: 192.168.1.1

    :rtype: String
    :returns: The validated value

    :raises AnsiblePluginError: If the value is not a valid IPv4 host
    """
    try:
        ipv4_obj = ipaddress.ip_address(value)

        if ipv4_obj.version != 4:
            raise ValueError(f"{value} is not a valid ipv4 host address")

    except Exception as error:
        raise AnsiblePluginError(f"exception: {inspect.currentframe().f_code.co_name} error: {error}") from error

    return value


def is_ipv4_prefix(value: str) -> str:
    """Function to check if a value is an IPv4 Prefix

    :type value: String
    :param value: Value to check Example: 192.168.1.1/24

    :rtype: String
    :returns: The validated value

    :raises AnsiblePluginError: If the value is not a valid IPv4 prefix
    """
    try:
        if "/" not in value:
            raise ValueError(f"{value} is not a valid ipv4 prefix address in CIDR format")

        ipv4_obj = ipaddress.ip_interface(value)

        if ipv4_obj.version != 4:
            raise ValueError(f"{value} is not a valid ipv4 prefix address")

        if ipv4_obj.with_prefixlen != value:
            raise ValueError(f"{value} is not a valid ipv4 prefix address")

    except Exception as error:
        raise AnsiblePluginError(f"exception: {inspect.currentframe().f_code.co_name} error: {error}") from error

    return value


def is_ipv4_subnet(value: str):
    """Function to check if a value is a IPv4 Subnet

    :type value: String
    :param value: Value to check Example: 192.168.1.0/24

    :rtype: String
    :returns: The validated value

    :raises AnsiblePluginError: If the value is not a valid IPv4 subnet
    """
    try:
        ipv4_obj = ipaddress.ip_network(value, strict=True)

        if ipv4_obj.version != 4:
            raise ValueError(f"{value} is not a valid ipv4 subnet address")

        if ipv4_obj.with_prefixlen != value:
            raise ValueError(f"{value} is not a valid ipv4 subnet address")

    except Exception as error:
        raise AnsiblePluginError(f"exception: {inspect.currentframe().f_code.co_name} error: {error}") from error

    return value


def is_cidr_range(value: Union[str, int]) -> Union[str, int]:
    """Function to check if a value is in the CIDR range

    :type value: Union[str,int]
    :param value: Value to check Example: 1 or 30

    :rtype: Union[str,int]
    :returns: The validated value

    :raises AnsiblePluginError: If the value is not a valid CIDR value
    """
    try:
        if int(value) not in range(0, 33):
            raise ValueError(f"cidr must be 0..32 but was {value}")

    except Exception as error:
        raise AnsiblePluginError(f"exception: {inspect.currentframe().f_code.co_name} error: {error}") from error

    return value
