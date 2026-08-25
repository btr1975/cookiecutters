from pathlib import Path
import sys
import pytest

base_path = Path(__file__).parent.parent.parent.resolve()
sys.path.append(base_path.as_posix())


@pytest.fixture
def bake_project_cli_podman_data() -> dict:
    options = {
        "git_repo_name": "python-with-cli",
        "include_cli": "y",
        "email": "name@example.com",
        "git_username": "some-username",
        "git_url": "https://github.com/some-username/python-with-cli",
        "package_manager": "pip",
    }

    return options


@pytest.fixture
def bake_project_uv_cli_podman_data() -> dict:
    options = {
        "git_repo_name": "python-with-cli",
        "include_cli": "y",
        "email": "name@example.com",
        "git_username": "some-username",
        "git_url": "https://github.com/some-username/python-with-cli",
        "package_manager": "uv",
    }

    return options


@pytest.fixture
def bake_project_cli_docker_data() -> dict:
    options = {
        "git_repo_name": "python-with-cli",
        "include_cli": "y",
        "email": "name@example.com",
        "git_username": "some-username",
        "git_url": "https://github.com/some-username/python-with-cli",
        "container_runtime": "docker",
        "package_manager": "pip",
    }

    return options


@pytest.fixture
def bake_project_uv_cli_docker_data() -> dict:
    options = {
        "git_repo_name": "python-with-cli",
        "include_cli": "y",
        "email": "name@example.com",
        "git_username": "some-username",
        "git_url": "https://github.com/some-username/python-with-cli",
        "container_runtime": "docker",
        "package_manager": "uv",
    }

    return options


@pytest.fixture
def bake_project_no_cli_podman_data() -> dict:
    options = {
        "git_repo_name": "python-no-cli",
        "include_cli": "n",
        "email": "name@example.com",
        "git_username": "some-username",
        "git_url": "https://github.com/some-username/python-no-cli",
        "package_manager": "pip",
    }

    return options


@pytest.fixture
def bake_project_uv_no_cli_podman_data() -> dict:
    options = {
        "git_repo_name": "python-no-cli",
        "include_cli": "n",
        "email": "name@example.com",
        "git_username": "some-username",
        "git_url": "https://github.com/some-username/python-no-cli",
        "package_manager": "uv",
    }

    return options


@pytest.fixture
def bake_project_no_cli_docker_data() -> dict:
    options = {
        "git_repo_name": "python-no-cli",
        "include_cli": "n",
        "email": "name@example.com",
        "git_username": "some-username",
        "git_url": "https://github.com/some-username/python-no-cli",
        "container_runtime": "docker",
        "package_manager": "pip",
    }

    return options


@pytest.fixture
def bake_project_uv_no_cli_docker_data() -> dict:
    options = {
        "git_repo_name": "python-no-cli",
        "include_cli": "n",
        "email": "name@example.com",
        "git_username": "some-username",
        "git_url": "https://github.com/some-username/python-no-cli",
        "container_runtime": "docker",
        "package_manager": "uv",
    }

    return options
