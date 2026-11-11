"""
prompts
"""

from {{cookiecutter.__app_name}}.web_app import mcp


@mcp.prompt
def ask_about_topic(topic: str) -> str:
    """Generates a user message asking for an explanation of a topic."""
    return f"Can you please explain the concept of '{topic}'?"
