"""
FastMCP WebApp
"""
from pathlib import Path

from fastmcp import FastMCP
{% if cookiecutter.package_manager == 'pip' %}
from {{cookiecutter.__app_name}}.version import __version__
{% elif cookiecutter.package_manager == 'uv' %}
from importlib.metadata import version
{% endif %}
{% if cookiecutter.serve_skills == 'y' %}
from fastmcp.server.providers.skills import SkillsDirectoryProvider


skills_directory = Path(__file__).parent.joinpath("skills").resolve()

skills_directory_provider = SkillsDirectoryProvider(roots=skills_directory)
{% endif %}

{% if cookiecutter.package_manager == 'pip' %}
{% if cookiecutter.serve_skills == 'y' %}
mcp = FastMCP(
    name='{{ cookiecutter.git_repo_name }}',
    version=__version__,
    providers=[skills_directory_provider],
)
{% else %}
mcp = FastMCP(
    name='{{ cookiecutter.git_repo_name }}',
    version=__version__,
)
{% endif %}
{% elif cookiecutter.package_manager == 'uv' %}
{% if cookiecutter.serve_skills == 'y' %}
mcp = FastMCP(
    name='{{ cookiecutter.git_repo_name }}',
    version=version("{{cookiecutter.git_repo_name}}"),
    providers=[skills_directory_provider],
)
{% else %}
mcp = FastMCP(
    name='{{ cookiecutter.git_repo_name }}',
    version=version("{{cookiecutter.git_repo_name}}"),
)
{% endif %}
{% endif %}
