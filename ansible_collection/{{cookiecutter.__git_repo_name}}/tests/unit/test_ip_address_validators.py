from plugins.module_utils.validators.ip_address_validators import (
    is_ipv4_host,
    is_ipv4_subnet,
    is_ipv4_prefix,
    is_cidr_range,
)
import pytest
from ansible.errors import AnsiblePluginError


ipv4_host_table = [
    ("192.168.1.1", "192.168.1.1", None),
    ("172.16.1.25", "172.16.1.25", None),
    ("10.1.1.200", "10.1.1.200", None),
    ("1925.1.12.5", None, AnsiblePluginError),
    ("192.1.12.5/32", None, AnsiblePluginError),
    ("192.1.12.5 255.255.255.255", None, AnsiblePluginError),
    ("2001:0000:130F:0000:0000:09C0:876A:130B", None, AnsiblePluginError),
]


@pytest.mark.parametrize("value,response,exception_raise", ipv4_host_table)
def test_is_ipv4_host(value, response, exception_raise):
    if exception_raise:
        with pytest.raises(exception_raise):
            is_ipv4_host(value)

    else:
        assert is_ipv4_host(value) == response


ipv4_subnet_table = [
    ("192.168.1.0/24", "192.168.1.0/24", None),
    ("172.16.0.0/18", "172.16.0.0/18", None),
    ("10.1.0.0/16", "10.1.0.0/16", None),
    ("192.1.12.5/32", "192.1.12.5/32", None),
    ("1925.1.12.5/24", None, AnsiblePluginError),
    ("192.1.12.5 255.255.255.255", None, AnsiblePluginError),
    ("2001:0000:130F:0000:0000:09C0:876A:130B", None, AnsiblePluginError),
    ("10.1.0.0", None, AnsiblePluginError),
]


@pytest.mark.parametrize("value,response,exception_raise", ipv4_subnet_table)
def test_is_ipv4_subnet(value, response, exception_raise):
    if exception_raise:
        with pytest.raises(exception_raise):
            is_ipv4_subnet(value)

    else:
        assert is_ipv4_subnet(value) == response


ipv4_prefix_table = [
    ("192.168.1.1/24", "192.168.1.1/24", None),
    ("172.16.1.25/32", "172.16.1.25/32", None),
    ("10.1.1.200/23", "10.1.1.200/23", None),
    ("1925.1.12.5", None, AnsiblePluginError),
    ("192.1.12.5 255.255.255.255", None, AnsiblePluginError),
    ("2001:0000:130F:0000:0000:09C0:876A:130B/128", None, AnsiblePluginError),
    ("10.1.0.0/255.255.255.0", None, AnsiblePluginError),
]


@pytest.mark.parametrize("value,response,exception_raise", ipv4_prefix_table)
def test_is_ipv4_prefix(value, response, exception_raise):
    if exception_raise:
        with pytest.raises(exception_raise):
            is_ipv4_prefix(value)

    else:
        assert is_ipv4_prefix(value) == response


cidr_range_table = [
    (0, 0, None),
    (32, 32, None),
    ("0", "0", None),
    ("32", "32", None),
    (-1, None, AnsiblePluginError),
    (33, None, AnsiblePluginError),
    ("-1", None, AnsiblePluginError),
    ("33", None, AnsiblePluginError),
]


@pytest.mark.parametrize("value,response,exception_raise", cidr_range_table)
def test_is_cidr_range(value, response, exception_raise):
    if exception_raise:
        with pytest.raises(exception_raise):
            is_cidr_range(value)

    else:
        assert is_cidr_range(value) == response
