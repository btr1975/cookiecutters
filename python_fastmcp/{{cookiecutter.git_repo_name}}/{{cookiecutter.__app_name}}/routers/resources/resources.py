"""
resources
"""

from {{cookiecutter.__app_name}}.web_app import mcp

@mcp.resource("resource://greeting")
def get_greeting() -> str:
    """Provides a simple greeting message."""
    return "Hello from FastMCP Resources!"
