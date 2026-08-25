from plugins.module_utils.normalizers.ansible_network_os_normalizers import (
    network_os_normalize,
)
import pytest
from ansible.errors import AnsiblePluginError


network_os_normalize_table = [
    ("ios", "ios", None),
    ("cisco.ios.ios", "ios", None),
    ("nxos", "nxos", None),
    ("cisco.nxos.nxos", "nxos", None),
    ("other", "", AnsiblePluginError),
]


@pytest.mark.parametrize("value,result,exception_raise", network_os_normalize_table)
def test_network_os_normalize(value, result, exception_raise):
    if exception_raise:
        with pytest.raises(exception_raise):
            network_os_normalize(value)

    else:
        new_value = network_os_normalize(value)

        assert new_value == result
