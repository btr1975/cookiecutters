from plugins.module_utils.validators.action_validators import (
    is_permit_deny,
    is_permit_deny_remark,
)
import pytest
from ansible.errors import AnsiblePluginError


permit_deny_table = [
    ("permit", "permit", None),
    ("deny", "deny", None),
    ("other", None, AnsiblePluginError),
]


@pytest.mark.parametrize("value,response,exception_raise", permit_deny_table)
def test_is_permit_deny(value, response, exception_raise):
    if exception_raise:
        with pytest.raises(exception_raise):
            is_permit_deny(value)

    else:
        assert is_permit_deny(value) == response


permit_deny_remark_table = [
    ("permit", "permit", None),
    ("deny", "deny", None),
    ("remark", "remark", None),
    ("other", None, AnsiblePluginError),
]


@pytest.mark.parametrize("value,response,exception_raise", permit_deny_remark_table)
def test_is_permit_deny_remark(value, response, exception_raise):
    if exception_raise:
        with pytest.raises(exception_raise):
            is_permit_deny_remark(value)

    else:
        assert is_permit_deny_remark(value) == response
