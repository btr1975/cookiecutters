"""
init for {{cookiecutter.__app_name}}
"""
from {{cookiecutter.__app_name}}.web_app import mcp

web_app = mcp.http_app(path="/mcp")
import {{cookiecutter.__app_name}}.routers.prompts.prompts
import {{cookiecutter.__app_name}}.routers.reources.reources
import {{cookiecutter.__app_name}}.routers.tools.tools
from {{cookiecutter.__app_name}}.{{cookiecutter.__app_name}}_cli import cli
