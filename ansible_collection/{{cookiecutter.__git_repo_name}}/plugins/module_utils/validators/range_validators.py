"""
Integer range validators
"""

import inspect
from typing import Union
from ansible.errors import AnsiblePluginError


def is_bgp_as(value: Union[str, int]) -> Union[str, int]:
    """Function to check if a value is in the BGP AS Number range

    :type value: Union[str,int]
    :param value: Value to check Example: 1 or 64000

    :rtype: Union[str,int]
    :returns: The validated value

    :raises AnsiblePluginError: If the value is not a valid BGP AS Number
    """
    try:
        if int(value) not in range(1, 65536):
            raise ValueError(f"BGP AS must be 1..65535 but was {value}")

    except Exception as error:
        raise AnsiblePluginError(f"exception: {inspect.currentframe().f_code.co_name} error: {error}") from error

    return value


def is_public_bgp_as(value: Union[str, int]) -> Union[str, int]:
    """Function to check if a value is in the BGP AS Public Number range

    :type value: Union[str,int]
    :param value: Value to check Example: 1 or 64000

    :rtype: Union[str,int]
    :returns: The validated value

    :raises AnsiblePluginError: If the value is not a valid BGP AS Public Number
    """
    try:
        if int(value) not in range(1, 64512):
            raise ValueError(f"Public BGP AS must be 1..64511 but was {value}")

    except Exception as error:
        raise AnsiblePluginError(f"exception: {inspect.currentframe().f_code.co_name} error: {error}") from error

    return value


def is_private_bgp_as(value: Union[str, int]) -> Union[str, int]:
    """Function to check if a value is in the BGP AS Private Number range

    :type value: Union[str,int]
    :param value: Value to check Example: 65000 or 65100

    :rtype: Union[str,int]
    :returns: The validated value

    :raises AnsiblePluginError: If the value is not a valid BGP AS Private Number
    """
    try:
        if int(value) not in range(64512, 65536):
            raise ValueError(f"Private BGP AS must be 64512..65535 but was {value}")

    except Exception as error:
        raise AnsiblePluginError(f"exception: {inspect.currentframe().f_code.co_name} error: {error}") from error

    return value


def is_ospf_area(value: Union[str, int]) -> Union[str, int]:
    """Function to check if a value is in the OSPF Area Number range

    :type value: Union[str,int]
    :param value: Value to check Example: 0 or 64000

    :rtype: Union[str,int]
    :returns: The validated value

    :raises AnsiblePluginError: If the value is not a valid OSPF Area Number
    """
    try:
        if int(value) not in range(0, 65536):
            raise ValueError(f"OSPF Area must be 0..65535 but was {value}")

    except Exception as error:
        raise AnsiblePluginError(f"exception: {inspect.currentframe().f_code.co_name} error: {error}") from error

    return value


def is_vlan(value: Union[str, int]) -> Union[str, int]:
    """Function to check if a value is in the VLAN Number range

    :type value: Union[str,int]
    :param value: Value to check Example: 1 or 10

    :rtype: Union[str,int]
    :returns: The validated value

    :raises AnsiblePluginError: If the value is not a valid VLAN Number range
    """
    try:
        if int(value) not in range(1, 4095):
            raise ValueError(f"VLAN must be 1..4094 but was {value}")

    except Exception as error:
        raise AnsiblePluginError(f"exception: {inspect.currentframe().f_code.co_name} error: {error}") from error

    return value


def is_vxlan_vni(value: Union[str, int]) -> Union[str, int]:
    """Function to check if a value is in the VxLAN VNI Number range

    :type value: Union[str,int]
    :param value: Value to check Example: 101010 or 765343

    :rtype: Union[str,int]
    :returns: The validated value

    :raises AnsiblePluginError: If the value is not a valid VxLAN VNI Number range
    """
    try:
        if int(value) not in range(1, 16777216):
            raise ValueError(f"VxLAN VNI must be 1..16777215 but was {value}")

    except Exception as error:
        raise AnsiblePluginError(f"exception: {inspect.currentframe().f_code.co_name} error: {error}") from error

    return value
