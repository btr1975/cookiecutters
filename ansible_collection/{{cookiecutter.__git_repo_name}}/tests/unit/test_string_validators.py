from plugins.module_utils.validators.string_validators import (
    is_string_no_spaces,
    is_string_no_spaces_begin_end,
)
import pytest
from ansible.errors import AnsiblePluginError


string_no_spaces_table = [
    ("a-b-c", "a-b-c", None),
    ("this-is-good", "this-is-good", None),
    ("this_is_fine_also", "this_is_fine_also", None),
    ("this is bad", None, AnsiblePluginError),
    (" this_is_also_bad", None, AnsiblePluginError),
    ("and_this_is_also_bad ", None, AnsiblePluginError),
]


@pytest.mark.parametrize("value,response,exception_raise", string_no_spaces_table)
def test_is_string_no_spaces(value, response, exception_raise):
    if exception_raise:
        with pytest.raises(exception_raise):
            is_string_no_spaces(value)

    else:
        assert is_string_no_spaces(value) == response


string_no_spaces_begin_end_table = [
    ("this is good", "this is good", None),
    ("this_is_good", "this_is_good", None),
    (" this is bad ", None, AnsiblePluginError),
    ("this is bad also ", None, AnsiblePluginError),
]


@pytest.mark.parametrize("value,response,exception_raise", string_no_spaces_begin_end_table)
def test_is_string_no_spaces_begin_end(value, response, exception_raise):
    if exception_raise:
        with pytest.raises(exception_raise):
            is_string_no_spaces_begin_end(value)

    else:
        assert is_string_no_spaces_begin_end(value) == response
