from pathlib import Path
import sys
import pytest

base_path = Path(__file__).parent.parent.parent.resolve()
sys.path.append(base_path.as_posix())


@pytest.fixture
def bake_project_api_only_podman() -> dict:
    options = {
        "git_repo_name": "api-only",
        "include_webpages": "n",
        "email": "name@example.com",
        "git_username": "some-username",
        "git_url": "https://github.com/some-username/python-with-cli",
        "package_manager": "pip",
    }

    return options


@pytest.fixture
def bake_project_uv_api_only_podman() -> dict:
    options = {
        "git_repo_name": "api-only",
        "include_webpages": "n",
        "email": "name@example.com",
        "git_username": "some-username",
        "git_url": "https://github.com/some-username/python-with-cli",
        "package_manager": "uv",
    }

    return options


@pytest.fixture
def bake_project_api_only_docker() -> dict:
    options = {
        "git_repo_name": "api-only",
        "include_webpages": "n",
        "email": "name@example.com",
        "git_username": "some-username",
        "git_url": "https://github.com/some-username/python-with-cli",
        "container_runtime": "docker",
        "package_manager": "pip",
    }

    return options


@pytest.fixture
def bake_project_uv_api_only_docker() -> dict:
    options = {
        "git_repo_name": "api-only",
        "include_webpages": "n",
        "email": "name@example.com",
        "git_username": "some-username",
        "git_url": "https://github.com/some-username/python-with-cli",
        "container_runtime": "docker",
        "package_manager": "uv",
    }

    return options


@pytest.fixture
def bake_project_api_with_webpages_podman() -> dict:
    options = {
        "git_repo_name": "api-with-webpages",
        "include_webpages": "y",
        "email": "name@example.com",
        "git_username": "some-username",
        "git_url": "https://github.com/some-username/python-with-cli",
        "package_manager": "pip",
    }

    return options


@pytest.fixture
def bake_project_uv_api_with_webpages_podman() -> dict:
    options = {
        "git_repo_name": "api-with-webpages",
        "include_webpages": "y",
        "email": "name@example.com",
        "git_username": "some-username",
        "git_url": "https://github.com/some-username/python-with-cli",
        "package_manager": "uv",
    }

    return options


@pytest.fixture
def bake_project_api_with_webpages_docker() -> dict:
    options = {
        "git_repo_name": "api-with-webpages",
        "include_webpages": "y",
        "email": "name@example.com",
        "git_username": "some-username",
        "git_url": "https://github.com/some-username/python-with-cli",
        "container_runtime": "docker",
        "package_manager": "pip",
    }

    return options


@pytest.fixture
def bake_project_uv_api_with_webpages_docker() -> dict:
    options = {
        "git_repo_name": "api-with-webpages",
        "include_webpages": "y",
        "email": "name@example.com",
        "git_username": "some-username",
        "git_url": "https://github.com/some-username/python-with-cli",
        "container_runtime": "docker",
        "package_manager": "uv",
    }

    return options
