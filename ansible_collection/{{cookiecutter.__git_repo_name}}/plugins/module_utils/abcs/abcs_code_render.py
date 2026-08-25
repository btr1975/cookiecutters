"""
Abstract Base Classes for actions rendering using code
"""

from abc import ABC, abstractmethod


class RenderConfigFromCodeABC(ABC):
    """Abstract Base Class for a render config from code class"""

    def __init__(self, module_params: dict) -> None:
        self.module_params = module_params

        self.validate_module_params(module_params=self.module_params)

    @abstractmethod
    def _render_config(self) -> str:
        """Protected Method to render the config"""

    @staticmethod
    @abstractmethod
    def validate_module_params(module_params: dict) -> None:
        """Static Method to validate the params data as you see fit"""
