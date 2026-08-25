from plugins.module_utils.validators.general_validators import is_protocol, is_sequence_number
import pytest
from ansible.errors import AnsiblePluginError


is_protocol_table = [
    ("icmp", "icmp", None),
    ("ip", "ip", None),
    ("tcp", "tcp", None),
    ("udp", "udp", None),
    ("other", None, AnsiblePluginError),
]


@pytest.mark.parametrize("value,response,exception_raise", is_protocol_table)
def test_is_protocol(value, response, exception_raise):
    if exception_raise:
        with pytest.raises(exception_raise):
            is_protocol(value)

    else:
        assert is_protocol(value) == response


is_sequence_number_table = [
    (1, 1, None),
    ("123123", "123123", None),
    (6589654, 6589654, None),
    ("564465645", "564465645", None),
    ("nope", None, AnsiblePluginError),
    ("1 1 258 5", None, AnsiblePluginError),
]


@pytest.mark.parametrize("value,response,exception_raise", is_sequence_number_table)
def test_is_sequence_number(value, response, exception_raise):
    if exception_raise:
        with pytest.raises(exception_raise):
            is_sequence_number(value)

    else:
        assert is_sequence_number(value) == response
