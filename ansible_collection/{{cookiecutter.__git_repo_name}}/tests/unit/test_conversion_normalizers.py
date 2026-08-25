from plugins.module_utils.normalizers.conversion_normalizers import (
    cidr_to_inverse_mask,
    ios_standard_acl_ipv4_subnet_normalizer,
    ios_extended_acl_ipv4_subnet_normalizer,
    iosxr_standard_acl_ipv4_subnet_normalizer,
    iosxr_extended_acl_ipv4_subnet_normalizer,
    eos_standard_acl_ipv4_subnet_normalizer,
    eos_extended_acl_ipv4_subnet_normalizer,
    eos_port_normalizer,
)
import pytest
from ansible.errors import AnsiblePluginError


cidr_to_inverse_mask_table = [
    ("192.168.1.1/32", "192.168.1.1 0.0.0.0", None),
    ("192.168.1.0/24", "192.168.1.0 0.0.0.255", None),
    ("192.168.0.0/16", "192.168.0.0 0.0.255.255", None),
    ("192.0.0.0/8", "192.0.0.0 0.255.255.255", None),
    ("other", None, AnsiblePluginError),
]


@pytest.mark.parametrize("value,response,exception_raise", cidr_to_inverse_mask_table)
def test_cidr_to_inverse_mask(value, response, exception_raise):
    if exception_raise:
        with pytest.raises(exception_raise):
            cidr_to_inverse_mask(value)

    else:
        assert cidr_to_inverse_mask(value) == response


ios_standard_acl_ipv4_subnet_normalizer_table = [
    ("192.168.1.1/32", "192.168.1.1", None),
    ("192.168.1.0/24", "192.168.1.0 0.0.0.255", None),
    ("192.168.0.0/16", "192.168.0.0 0.0.255.255", None),
    ("192.0.0.0/8", "192.0.0.0 0.255.255.255", None),
    ("other", None, AnsiblePluginError),
]


@pytest.mark.parametrize("value,response,exception_raise", ios_standard_acl_ipv4_subnet_normalizer_table)
def test_ios_standard_acl_ipv4_subnet_normalizer(value, response, exception_raise):
    if exception_raise:
        with pytest.raises(exception_raise):
            ios_standard_acl_ipv4_subnet_normalizer(value)

    else:
        assert ios_standard_acl_ipv4_subnet_normalizer(value) == response


ios_extended_acl_ipv4_subnet_normalizer_table = [
    ("192.168.1.1/32", "host 192.168.1.1", None),
    ("192.168.1.0/24", "192.168.1.0 0.0.0.255", None),
    ("192.168.0.0/16", "192.168.0.0 0.0.255.255", None),
    ("192.0.0.0/8", "192.0.0.0 0.255.255.255", None),
    ("other", None, AnsiblePluginError),
]


@pytest.mark.parametrize("value,response,exception_raise", ios_extended_acl_ipv4_subnet_normalizer_table)
def test_ios_extended_acl_ipv4_subnet_normalizer(value, response, exception_raise):
    if exception_raise:
        with pytest.raises(exception_raise):
            ios_extended_acl_ipv4_subnet_normalizer(value)

    else:
        assert ios_extended_acl_ipv4_subnet_normalizer(value) == response


iosxr_standard_acl_ipv4_subnet_normalizer_table = [
    ("192.168.1.1/32", "host 192.168.1.1", None),
    ("192.168.1.0/24", "192.168.1.0 0.0.0.255", None),
    ("192.168.0.0/16", "192.168.0.0 0.0.255.255", None),
    ("192.0.0.0/8", "192.0.0.0 0.255.255.255", None),
    ("other", None, AnsiblePluginError),
]


@pytest.mark.parametrize("value,response,exception_raise", iosxr_standard_acl_ipv4_subnet_normalizer_table)
def test_iosxr_standard_acl_ipv4_subnet_normalizer(value, response, exception_raise):
    if exception_raise:
        with pytest.raises(exception_raise):
            iosxr_standard_acl_ipv4_subnet_normalizer(value)

    else:
        assert iosxr_standard_acl_ipv4_subnet_normalizer(value) == response


iosxr_extended_acl_ipv4_subnet_normalizer_table = [
    ("192.168.1.1/32", "host 192.168.1.1", None),
    ("192.168.1.0/24", "192.168.1.0 0.0.0.255", None),
    ("192.168.0.0/16", "192.168.0.0 0.0.255.255", None),
    ("192.0.0.0/8", "192.0.0.0 0.255.255.255", None),
    ("other", None, AnsiblePluginError),
]


@pytest.mark.parametrize("value,response,exception_raise", iosxr_extended_acl_ipv4_subnet_normalizer_table)
def test_iosxr_extended_acl_ipv4_subnet_normalizer(value, response, exception_raise):
    if exception_raise:
        with pytest.raises(exception_raise):
            iosxr_extended_acl_ipv4_subnet_normalizer(value)

    else:
        assert iosxr_extended_acl_ipv4_subnet_normalizer(value) == response


eos_standard_acl_ipv4_subnet_normalizer_table = [
    ("192.168.1.1/32", "host 192.168.1.1", None),
    ("192.168.1.0/24", "192.168.1.0/24", None),
    ("192.168.0.0/16", "192.168.0.0/16", None),
    ("192.0.0.0/8", "192.0.0.0/8", None),
    ("other", None, AnsiblePluginError),
]


@pytest.mark.parametrize("value,response,exception_raise", eos_standard_acl_ipv4_subnet_normalizer_table)
def test_eos_standard_acl_ipv4_subnet_normalizer(value, response, exception_raise):
    if exception_raise:
        with pytest.raises(exception_raise):
            eos_standard_acl_ipv4_subnet_normalizer(value)

    else:
        assert eos_standard_acl_ipv4_subnet_normalizer(value) == response


eos_extended_acl_ipv4_subnet_normalizer_table = [
    ("192.168.1.1/32", "host 192.168.1.1", None),
    ("192.168.1.0/24", "192.168.1.0/24", None),
    ("192.168.0.0/16", "192.168.0.0/16", None),
    ("192.0.0.0/8", "192.0.0.0/8", None),
    ("other", None, AnsiblePluginError),
]


@pytest.mark.parametrize("value,response,exception_raise", eos_extended_acl_ipv4_subnet_normalizer_table)
def test_eos_extended_acl_ipv4_subnet_normalizer(value, response, exception_raise):
    if exception_raise:
        with pytest.raises(exception_raise):
            eos_extended_acl_ipv4_subnet_normalizer(value)

    else:
        assert eos_extended_acl_ipv4_subnet_normalizer(value) == response


eos_port_normalizer_table = [
    ("nfs", "nfs", None),
    ("sunrpc", "sunrpc", None),
    ("microsoft-ds", "microsoft-ds", None),
    ("111", "sunrpc", None),
    ("445", "microsoft-ds", None),
    ("2049", "nfs", None),
    (1225, 1225, None),
    ("other", None, AnsiblePluginError),
]


@pytest.mark.parametrize("value,response,exception_raise", eos_port_normalizer_table)
def test_eos_port_normalizer(value, response, exception_raise):
    if exception_raise:
        with pytest.raises(exception_raise):
            eos_port_normalizer(value)

    else:
        assert eos_port_normalizer(value) == response
