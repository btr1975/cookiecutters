"""
tools
"""

from {{cookiecutter.__app_name}}.web_app import mcp


@mcp.tool
def add(a: int, b: int) -> int:
    """Adds two integer numbers together."""
    return a + b
