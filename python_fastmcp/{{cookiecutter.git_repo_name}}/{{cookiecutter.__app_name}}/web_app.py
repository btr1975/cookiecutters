"""
FastMCP WebApp
"""
from fastmcp import FastMCP
{% if cookiecutter.package_manager == 'pip' %}
from {{cookiecutter.__app_name}}.version import __version__
{% elif cookiecutter.package_manager == 'uv' %}
from importlib.metadata import version
{% endif %}


{% if cookiecutter.package_manager == 'pip' %}
mcp = FastMCP(
    name='{{ cookiecutter.git_repo_name }}',
    version=__version__,
    description='{{ cookiecutter.app_description }}',
)
{% elif cookiecutter.package_manager == 'uv' %}
mcp = FastMCP(
    name='{{ cookiecutter.git_repo_name }}',
    version=version("{{cookiecutter.git_repo_name}}"),
    description='{{ cookiecutter.app_description }}',
)
{% endif %}
