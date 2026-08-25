from plugins.filter.render_filters import (
    FilterModule,
    ipv4_host,
    ipv4_subnet,
    standard_acl_ipv4_subnet_normalizer,
    extended_acl_ipv4_subnet_normalizer,
    protocol,
    port_match,
    port_or_ports,
    acl_append_options_to_end,
    permit_deny_remark,
    sequence_number,
    required_string_no_spaces,
    required_string_no_spaces_begin_or_end,
    permit_deny,
    le_ge,
    cidr_range,
)
import pytest
from ansible.errors import AnsibleFilterError


ipv4_host_table = [
    ("192.168.1.1", "192.168.1.1", None),
    ("172.16.1.25", "172.16.1.25", None),
    ("10.1.1.200", "10.1.1.200", None),
    ("1925.1.12.5", None, AnsibleFilterError),
    ("192.1.12.5/32", None, AnsibleFilterError),
    ("192.1.12.5 255.255.255.255", None, AnsibleFilterError),
    ("2001:0000:130F:0000:0000:09C0:876A:130B", None, AnsibleFilterError),
]


@pytest.mark.parametrize("value,response,exception_raise", ipv4_host_table)
def test_ipv4_host_filter(value, response, exception_raise):
    if exception_raise:
        with pytest.raises(exception_raise):
            ipv4_host(value)

    else:
        assert ipv4_host(value) == response


ipv4_subnet_table = [
    ("192.168.1.0/24", "192.168.1.0/24", None),
    ("172.16.0.0/18", "172.16.0.0/18", None),
    ("10.1.0.0/16", "10.1.0.0/16", None),
    ("192.1.12.5/32", "192.1.12.5/32", None),
    ("1925.1.12.5/24", None, AnsibleFilterError),
    ("192.1.12.5 255.255.255.255", None, AnsibleFilterError),
    ("2001:0000:130F:0000:0000:09C0:876A:130B", None, AnsibleFilterError),
    ("10.1.0.0", None, AnsibleFilterError),
]


@pytest.mark.parametrize("value,response,exception_raise", ipv4_subnet_table)
def test_ipv4_subnet_filter(value, response, exception_raise):
    if exception_raise:
        with pytest.raises(exception_raise):
            ipv4_subnet(value)

    else:
        assert ipv4_subnet(value) == response


standard_acl_ipv4_subnet_normalizer_table = [
    ("any", "ios", "any", None),
    ("192.168.1.1/32", "ios", "192.168.1.1", None),
    ("172.16.0.0/18", "ios", "172.16.0.0 0.0.63.255", None),
    ("10.1.0.0/16", "ios", "10.1.0.0 0.0.255.255", None),
    ("any", "iosxr", "any", None),
    ("192.168.1.1/32", "iosxr", "host 192.168.1.1", None),
    ("172.16.0.0/18", "iosxr", "172.16.0.0 0.0.63.255", None),
    ("10.1.0.0/16", "iosxr", "10.1.0.0 0.0.255.255", None),
    ("any", "eos", "any", None),
    ("192.168.1.1/32", "eos", "host 192.168.1.1", None),
    ("172.16.0.0/18", "eos", "172.16.0.0/18", None),
    ("10.1.0.0/16", "eos", "10.1.0.0/16", None),
    ("any", "nxos", "any", None),
    ("192.168.1.1/32", "nxos", "192.168.1.1/32", None),
    ("172.16.0.0/18", "nxos", "172.16.0.0/18", None),
    ("10.1.0.0/16", "nxos", "10.1.0.0/16", None),
    ("1925.1.12.5/24", "ios", None, AnsibleFilterError),
    ("192.1.12.5 255.255.255.255", "ios", None, AnsibleFilterError),
    ("2001:0000:130F:0000:0000:09C0:876A:130B", "ios", None, AnsibleFilterError),
    ("10.1.0.0", "ios", None, AnsibleFilterError),
]


@pytest.mark.parametrize("value,nos,response,exception_raise", standard_acl_ipv4_subnet_normalizer_table)
def test_standard_acl_ipv4_subnet_normalizer_filter(value, nos, response, exception_raise):
    if exception_raise:
        with pytest.raises(exception_raise):
            standard_acl_ipv4_subnet_normalizer(value, nos)

    else:
        assert standard_acl_ipv4_subnet_normalizer(value, nos) == response


extended_acl_ipv4_subnet_normalizer_table = [
    ("any", "ios", "any", None),
    ("192.168.1.1/32", "ios", "host 192.168.1.1", None),
    ("172.16.0.0/18", "ios", "172.16.0.0 0.0.63.255", None),
    ("10.1.0.0/16", "ios", "10.1.0.0 0.0.255.255", None),
    ("any", "iosxr", "any", None),
    ("192.168.1.1/32", "iosxr", "host 192.168.1.1", None),
    ("172.16.0.0/18", "iosxr", "172.16.0.0 0.0.63.255", None),
    ("10.1.0.0/16", "iosxr", "10.1.0.0 0.0.255.255", None),
    ("any", "eos", "any", None),
    ("192.168.1.1/32", "eos", "host 192.168.1.1", None),
    ("172.16.0.0/18", "eos", "172.16.0.0/18", None),
    ("10.1.0.0/16", "eos", "10.1.0.0/16", None),
    ("any", "nxos", "any", None),
    ("192.168.1.1/32", "nxos", "192.168.1.1/32", None),
    ("172.16.0.0/18", "nxos", "172.16.0.0/18", None),
    ("10.1.0.0/16", "nxos", "10.1.0.0/16", None),
    ("1925.1.12.5/24", "ios", None, AnsibleFilterError),
    ("192.1.12.5 255.255.255.255", "ios", None, AnsibleFilterError),
    ("2001:0000:130F:0000:0000:09C0:876A:130B", "ios", None, AnsibleFilterError),
    ("10.1.0.0", "ios", None, AnsibleFilterError),
]


@pytest.mark.parametrize("value,nos,response,exception_raise", extended_acl_ipv4_subnet_normalizer_table)
def test_extended_acl_ipv4_subnet_normalizer_filter(value, nos, response, exception_raise):
    if exception_raise:
        with pytest.raises(exception_raise):
            extended_acl_ipv4_subnet_normalizer(value, nos)

    else:
        assert extended_acl_ipv4_subnet_normalizer(value, nos) == response


protocol_table = [
    ("icmp", "icmp", None),
    ("ip", "ip", None),
    ("tcp", "tcp", None),
    ("udp", "udp", None),
    ("other", None, AnsibleFilterError),
]


@pytest.mark.parametrize("value,response,exception_raise", protocol_table)
def test_protocol_filter(value, response, exception_raise):
    if exception_raise:
        with pytest.raises(exception_raise):
            protocol(value)

    else:
        assert protocol(value) == response


port_match_table = [
    ("eq", "eq", None),
    ("gt", "gt", None),
    ("lt", "lt", None),
    ("neq", "neq", None),
    ("range", "range", None),
    ("other", None, AnsibleFilterError),
]


@pytest.mark.parametrize("value,response,exception_raise", port_match_table)
def test_port_match_filter(value, response, exception_raise):
    if exception_raise:
        with pytest.raises(exception_raise):
            port_match(value)

    else:
        assert port_match(value) == response


port_or_ports_table = [
    ("1000", "eq", "ios", 1000, None),
    ("1000", "gt", "ios", 1000, None),
    ("1000", "lt", "ios", 1000, None),
    ("1000", "neq", "ios", 1000, None),
    ("1000,2000", "range", "ios", "1000 2000", None),
    ("1000", "neq", "eos", "1000", None),
    ("111", "neq", "eos", "sunrpc", None),
    ("2000,1000", "range", "ios", None, AnsibleFilterError),
    ("2000", "range", "ios", None, AnsibleFilterError),
    ("2001:0000:130F:0000:0000:09C0:876A:130B", "eq", "ios", None, AnsibleFilterError),
    ("10.1.0.0", "eq", "ios", None, AnsibleFilterError),
]


@pytest.mark.parametrize("value,port_match_value,nos,response,exception_raise", port_or_ports_table)
def test_port_or_ports_filter(value, port_match_value, nos, response, exception_raise):
    if exception_raise:
        with pytest.raises(exception_raise):
            port_or_ports(value, port_match_value, nos)

    else:
        assert port_or_ports(value, port_match_value, nos) == response


acl_append_options_to_end_table = [
    (None, "", None),
    (["log"], " log", None),
    (["other"], None, AnsibleFilterError),
    ("other", None, AnsibleFilterError),
]


@pytest.mark.parametrize("value,response,exception_raise", acl_append_options_to_end_table)
def test_acl_append_options_to_end_filter(value, response, exception_raise):
    if exception_raise:
        with pytest.raises(exception_raise):
            acl_append_options_to_end(value)

    else:
        assert acl_append_options_to_end(value) == response


permit_deny_remark_table = [
    ("permit", "permit", None),
    ("deny", "deny", None),
    ("remark", "remark", None),
    ("other", None, AnsibleFilterError),
]


@pytest.mark.parametrize("value,response,exception_raise", permit_deny_remark_table)
def test_permit_deny_remark_filter(value, response, exception_raise):
    if exception_raise:
        with pytest.raises(exception_raise):
            permit_deny_remark(value)

    else:
        assert permit_deny_remark(value) == response


sequence_number_table = [
    (1, 1, None),
    ("123123", "123123", None),
    (6589654, 6589654, None),
    ("564465645", "564465645", None),
    ("nope", None, AnsibleFilterError),
    ("1 1 258 5", None, AnsibleFilterError),
]


@pytest.mark.parametrize("value,response,exception_raise", sequence_number_table)
def test_sequence_number_filter(value, response, exception_raise):
    if exception_raise:
        with pytest.raises(exception_raise):
            sequence_number(value)

    else:
        assert sequence_number(value) == response


required_string_no_spaces_table = [
    ("a-b-c", "a-b-c", None),
    ("this-is-good", "this-is-good", None),
    ("this_is_fine_also", "this_is_fine_also", None),
    ("this is bad", None, AnsibleFilterError),
    (" this_is_also_bad", None, AnsibleFilterError),
    ("and_this_is_also_bad ", None, AnsibleFilterError),
]


@pytest.mark.parametrize("value,response,exception_raise", required_string_no_spaces_table)
def test_required_string_no_spaces_filter(value, response, exception_raise):
    if exception_raise:
        with pytest.raises(exception_raise):
            required_string_no_spaces(value)

    else:
        assert required_string_no_spaces(value) == response


required_string_no_spaces_begin_or_end_table = [
    ("this is good", "this is good", None),
    ("this_is_good", "this_is_good", None),
    (" this is bad ", None, AnsibleFilterError),
    ("this is bad also ", None, AnsibleFilterError),
]


@pytest.mark.parametrize("value,response,exception_raise", required_string_no_spaces_begin_or_end_table)
def test_required_string_no_spaces_begin_or_end_filter(value, response, exception_raise):
    if exception_raise:
        with pytest.raises(exception_raise):
            required_string_no_spaces_begin_or_end(value)

    else:
        assert required_string_no_spaces_begin_or_end(value) == response


permit_deny_table = [
    ("permit", "permit", None),
    ("deny", "deny", None),
    ("other ", None, AnsibleFilterError),
]


@pytest.mark.parametrize("value,response,exception_raise", permit_deny_table)
def test_permit_deny_filter(value, response, exception_raise):
    if exception_raise:
        with pytest.raises(exception_raise):
            permit_deny(value)

    else:
        assert permit_deny(value) == response


le_ge_table = [
    ("le", "le", None),
    ("ge", "ge", None),
    ("other ", None, AnsibleFilterError),
]


@pytest.mark.parametrize("value,response,exception_raise", le_ge_table)
def test_le_ge_filter(value, response, exception_raise):
    if exception_raise:
        with pytest.raises(exception_raise):
            le_ge(value)

    else:
        assert le_ge(value) == response


cidr_range_table = [
    (0, 0, None),
    (32, 32, None),
    ("0", "0", None),
    ("32", "32", None),
    (-1, None, AnsibleFilterError),
    (33, None, AnsibleFilterError),
    ("-1", None, AnsibleFilterError),
    ("33", None, AnsibleFilterError),
]


@pytest.mark.parametrize("value,response,exception_raise", cidr_range_table)
def test_cidr_range_filter(value, response, exception_raise):
    if exception_raise:
        with pytest.raises(exception_raise):
            cidr_range(value)

    else:
        assert cidr_range(value) == response


filter_module_table = [
    ("ipv4_host", ipv4_host),
    ("ipv4_subnet", ipv4_subnet),
    ("standard_acl_ipv4_subnet_normalizer", standard_acl_ipv4_subnet_normalizer),
    ("extended_acl_ipv4_subnet_normalizer", extended_acl_ipv4_subnet_normalizer),
    ("protocol", protocol),
    ("port_match", port_match),
    ("port_or_ports", port_or_ports),
    ("acl_append_options_to_end", acl_append_options_to_end),
    ("permit_deny_remark", permit_deny_remark),
    ("sequence_number", sequence_number),
    ("required_string_no_spaces", required_string_no_spaces),
    ("required_string_no_spaces_begin_or_end", required_string_no_spaces_begin_or_end),
    ("permit_deny", permit_deny),
    ("le_ge", le_ge),
    ("cidr_range", cidr_range),
]


@pytest.mark.parametrize("filter_name,filter_callable", filter_module_table)
def test_filter_module(filter_name, filter_callable):
    obj = FilterModule()

    assert obj.filters().get(filter_name)

    returned_filter_callable = obj.filters().get(filter_name)

    assert type(returned_filter_callable) == type(filter_callable)
