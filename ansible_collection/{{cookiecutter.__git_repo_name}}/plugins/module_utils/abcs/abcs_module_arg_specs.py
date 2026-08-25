"""
Abstract base classes for Modules Specs

NOTES: Had to be a separate file cause modules can not even import from 'ansible.utils'
"""

from abc import ABC, abstractmethod


class ArgumentAndResultsSpecABC(ABC):
    """Abstract Base Class for an argument spec"""

    def __init__(self) -> None:
        self.argument_spec = {}

        self.init_results = {
            "changed": False,
            "failed": False,
            "rendered": "",
            "rendered_lines": None,
        }

        self._argument_spec()

    @abstractmethod
    def _argument_spec(self) -> None:
        """Protected Abstract method to create the argument spec using the class protected methods"""

    def _create_option(self, option: str, constraint: dict) -> None:
        """Protected Method Create an option for the spec

        :type option: String
        :param option: The option name
        :type constraint: Dict
        :param constraint: The argument constraint dictionary

        :rtype: None
        :returns: Nothing it adds an argument to the spec

        :raise KeyError: If the param already exists
        """
        if self.argument_spec.get(option):
            raise KeyError(f"option: {option} already exists!")

        self.argument_spec[option] = constraint

    def _update_option(self, option: str, constraint: dict) -> None:
        """Protected Method Update an option for the spec

        :type option: String
        :param option: The option name
        :type constraint: Dict
        :param constraint: The argument constraint dictionary

        :rtype: None
        :returns: Nothing it updates an argument to the spec

        :raise KeyError: If the param does not already exist
        """
        if not self.argument_spec.get(option):
            raise KeyError(f"option: {option} does not exist exists!")

        self.argument_spec[option] = constraint

    def _delete_option(self, option: str) -> None:
        """Protected Method Delete an option from the spec

        :type option: String
        :param option: The option name

        :rtype: None
        :returns: Nothing it deletes an argument to the spec

        :raise KeyError: If the param does not already exist
        """
        if not self.argument_spec.get(option):
            raise KeyError(f"option: {option} does not exist exists!")

        del self.argument_spec[option]

    def get_argument_spec(self) -> dict:
        """Get the argument spec

        :rtype: Dict
        :returns: The argument spec
        """
        return self.argument_spec

    def get_init_results(self) -> dict:
        """Get the initial results response

        :rtype: Dict
        :returns: The initial results response
        """
        return self.init_results
