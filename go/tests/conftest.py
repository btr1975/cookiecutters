from pathlib import Path
import sys
import pytest

base_path = Path(__file__).parent.parent.parent.resolve()
sys.path.append(base_path.as_posix())


@pytest.fixture
def bake_project_app_data() -> dict:
    options = {
        "git_repo_name": "go-app",
        "git_url": "https://github.com/some-username/python-with-cli",
        "library_only": "n",
    }

    return options


@pytest.fixture
def bake_project_library_data() -> dict:
    options = {
        "git_repo_name": "go-library",
        "git_url": "https://github.com/some-username/python-with-cli",
        "library_only": "y",
    }

    return options
