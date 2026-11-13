from pathlib import Path
import sys
import pytest
from fastapi.testclient import TestClient

base_path = Path(__file__).parent.parent
sys.path.append(base_path.resolve().as_posix())
from {{cookiecutter.__app_name}}.web_app import web_app


@pytest.fixture
def fastapi_mock_client():
    yield TestClient(web_app)
