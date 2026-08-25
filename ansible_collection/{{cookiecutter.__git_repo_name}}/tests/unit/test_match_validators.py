from plugins.module_utils.validators.match_validators import (
    is_le_ge,
    is_eq_gt_lt_neq_range,
)
import pytest
from ansible.errors import AnsiblePluginError


le_ge_table = [
    ("le", "le", None),
    ("ge", "ge", None),
    ("other", None, AnsiblePluginError),
]


@pytest.mark.parametrize("value,response,exception_raise", le_ge_table)
def test_is_le_ge(value, response, exception_raise):
    if exception_raise:
        with pytest.raises(exception_raise):
            is_le_ge(value)

    else:
        assert is_le_ge(value) == response


eq_gt_lt_neq_range_table = [
    ("eq", "eq", None),
    ("gt", "gt", None),
    ("lt", "lt", None),
    ("neq", "neq", None),
    ("range", "range", None),
    ("other", None, AnsiblePluginError),
]


@pytest.mark.parametrize("value,response,exception_raise", eq_gt_lt_neq_range_table)
def test_is_eq_gt_lt_neq_range(value, response, exception_raise):
    if exception_raise:
        with pytest.raises(exception_raise):
            is_eq_gt_lt_neq_range(value)

    else:
        assert is_eq_gt_lt_neq_range(value) == response
