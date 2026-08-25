"""
Normalizer for ansible_network_os
"""

import inspect
from ansible.errors import AnsiblePluginError


def network_os_normalize(value: str) -> str:
    """Normalize the ansible_network_os variable

    :type value: String
    :param value: The value to normalize

    :rtype: String
    :returns: The normalized value

    :raises AnsiblePluginError: If the ansible_network_os can not be normalized
    """
    net_os = {
        "cisco.ios.ios": "ios",
        "ios": "ios",
        "cisco.nxos.nxos": "nxos",
        "nxos": "nxos",
        "cisco.iosxr.iosxr": "iosxr",
        "iosxr": "iosxr",
        "arista.eos.eos": "eos",
        "eos": "eos",
    }

    if not net_os.get(value):
        raise AnsiblePluginError(
            f"exception: {inspect.currentframe().f_code.co_name} error: {value}' is not a supported ansible_network_os"
        )

    return net_os.get(value)
