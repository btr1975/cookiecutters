from plugins.module_utils.validators.range_validators import (
    is_bgp_as,
    is_private_bgp_as,
    is_public_bgp_as,
    is_vlan,
    is_ospf_area,
    is_vxlan_vni,
)
import pytest
from ansible.errors import AnsiblePluginError


bgp_as_table = [
    (1, 1, None),
    (65535, 65535, None),
    ("1", "1", None),
    ("65535", "65535", None),
    (0, None, AnsiblePluginError),
    (65536, None, AnsiblePluginError),
    ("0", None, AnsiblePluginError),
    ("65536", None, AnsiblePluginError),
]


@pytest.mark.parametrize("value,response,exception_raise", bgp_as_table)
def test_is_bgp_as(value, response, exception_raise):
    if exception_raise:
        with pytest.raises(exception_raise):
            is_bgp_as(value)

    else:
        assert is_bgp_as(value) == response


private_bgp_as_table = [
    (64512, 64512, None),
    (65535, 65535, None),
    ("64512", "64512", None),
    ("65535", "65535", None),
    (64511, None, AnsiblePluginError),
    (65536, None, AnsiblePluginError),
    ("64511", None, AnsiblePluginError),
    ("65536", None, AnsiblePluginError),
]


@pytest.mark.parametrize("value,response,exception_raise", private_bgp_as_table)
def test_is_private_bgp_as(value, response, exception_raise):
    if exception_raise:
        with pytest.raises(exception_raise):
            is_private_bgp_as(value)

    else:
        assert is_private_bgp_as(value) == response


public_bgp_as_table = [
    (1, 1, None),
    (64511, 64511, None),
    ("1", "1", None),
    ("64511", "64511", None),
    (0, None, AnsiblePluginError),
    (64512, None, AnsiblePluginError),
    ("0", None, AnsiblePluginError),
    ("64512", None, AnsiblePluginError),
]


@pytest.mark.parametrize("value,response,exception_raise", public_bgp_as_table)
def test_is_public_bgp_as(value, response, exception_raise):
    if exception_raise:
        with pytest.raises(exception_raise):
            is_public_bgp_as(value)

    else:
        assert is_public_bgp_as(value) == response


vlan_table = [
    (1, 1, None),
    (4094, 4094, None),
    ("1", "1", None),
    ("4094", "4094", None),
    (0, None, AnsiblePluginError),
    (4095, None, AnsiblePluginError),
    ("0", None, AnsiblePluginError),
    ("4095", None, AnsiblePluginError),
]


@pytest.mark.parametrize("value,response,exception_raise", vlan_table)
def test_is_vlan(value, response, exception_raise):
    if exception_raise:
        with pytest.raises(exception_raise):
            is_vlan(value)

    else:
        assert is_vlan(value) == response


ospf_area_table = [
    (0, 0, None),
    (65535, 65535, None),
    ("0", "0", None),
    ("65535", "65535", None),
    (-1, None, AnsiblePluginError),
    (65536, None, AnsiblePluginError),
    ("-1", None, AnsiblePluginError),
    ("65536", None, AnsiblePluginError),
]


@pytest.mark.parametrize("value,response,exception_raise", ospf_area_table)
def test_is_ospf_area(value, response, exception_raise):
    if exception_raise:
        with pytest.raises(exception_raise):
            is_ospf_area(value)

    else:
        assert is_ospf_area(value) == response


vxlan_vni_table = [
    (1, 1, None),
    (16777215, 16777215, None),
    ("1", "1", None),
    ("16777215", "16777215", None),
    (0, None, AnsiblePluginError),
    (16777216, None, AnsiblePluginError),
    ("0", None, AnsiblePluginError),
    ("16777216", None, AnsiblePluginError),
]


@pytest.mark.parametrize("value,response,exception_raise", vxlan_vni_table)
def test_is_vxlan_vni(value, response, exception_raise):
    if exception_raise:
        with pytest.raises(exception_raise):
            is_vxlan_vni(value)

    else:
        assert is_vxlan_vni(value) == response
