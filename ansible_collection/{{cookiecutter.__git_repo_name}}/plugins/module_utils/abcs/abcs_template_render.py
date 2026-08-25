"""
Abstract Base Classes for actions rendering using templates

NOTES: Had to be a separate file cause modules can not even import from 'ansible.utils'
"""

from abc import ABC, abstractmethod
import os
from typing import Union, Optional
from ansible.utils.display import Display
from ansible.template import Templar

from ansible_collections.{{ cookiecutter.__git_repo_name }}.plugins.module_utils.normalizers.ansible_network_os_normalizers import (
    network_os_normalize,
)


class RenderConfigFromTemplate(ABC):
    """Abstract Base Class for a render config from template class

    :type templar: ansible.template.Templar
    :param templar: The passed in templar fro the action
    :type template_variables: Dict
    :param template_variables: The variables to fill the template with
    :type ansible_network_os: String
    :param ansible_network_os: The ansible network os

    :rtype: None
    :returns: Nothing

    :raises TypeError: If templar, or template_variables is not of the right type
    """

    def __init__(self, templar: Templar, template_variables: dict, ansible_network_os: str) -> None:
        if not isinstance(templar, Templar):
            raise TypeError(f"'templar' must be of type Templar but received a {type(templar)}")

        if not isinstance(template_variables, dict):
            raise TypeError(f"'template_variables' must be of type dict but received a {type(template_variables)}")

        self._templar = templar
        self._ansible_network_os = network_os_normalize(ansible_network_os)
        template_variables["ansible_network_os"] = network_os_normalize(ansible_network_os)
        self.validate_module_params(template_variables=template_variables)
        self._template_variables = template_variables
        self._display = Display()

    def _render_template(self, template_path: str) -> str:
        """Render a Jinja2 Template

        :type template_path: String
        :param template_path: The path to the template to render

        :rtype: String
        :returns: The rendered template

        :raises TypeError: If templar is not a Templar
        """
        with open(template_path, "r") as template_file:
            template_data = template_file.read()

            self._templar.available_variables = self._template_variables

            rendered = self._templar.template(
                variable=template_data,
                preserve_trailing_newlines=True,
                escape_backslashes=False,
                fail_on_undefined=True,
            )

        return rendered

    def _find_templates_directory(self) -> Union[str, None]:
        """Tries to find the path to this collection templates directory

        :rtype: Union[str, None]
        :returns: A found path, or None
        """
        namespace = "btr1975"
        collection = "render"

        possible_paths = []

        #  SEE: https://docs.ansible.com/ansible/latest/reference_appendices/config.html#collections-paths
        if os.getenv("ANSIBLE_COLLECTIONS_PATH"):
            ansible_collections_paths = os.getenv("ANSIBLE_COLLECTIONS_PATH").split(":")

            if isinstance(ansible_collections_paths, list):
                possible_paths.extend(ansible_collections_paths)

            else:
                possible_paths.append(ansible_collections_paths)

        else:
            possible_paths.append("/usr/share/ansible/collections")

        additional_paths = [
            "/usr/local/share/ansible/collections",
            "/etc/ansible/collections",
            os.path.join(os.path.expanduser("~"), ".ansible", "collections"),
            os.path.join(os.path.abspath("."), "collections"),
        ]

        possible_paths.extend(additional_paths)

        for base_path in possible_paths:
            templates_dir = os.path.join(base_path, "ansible_collections", namespace, collection, "templates")
            self._display.v(f"CHECK: templates_dir {templates_dir}")
            if os.path.isdir(templates_dir):
                self._display.v(f"FOUND: templates_dir {templates_dir}")
                return templates_dir

        self._display.v(f"NOT FOUND: templates_dir {None}")
        return None

    def _find_template(
        self,
        src: Optional[str] = None,
        template_name: Optional[str] = None,
        solution: Optional[str] = None,
        family: Optional[str] = None,
        model: Optional[str] = None,
    ) -> Union[str, None]:
        """Tries to find the path to this collection templates

        :type src: Optional[str]
        :param src: If src is given no lookups are done, and it is assumed it is an exact path to a template
        :type template_name: Optional[str]
        :param template_name: The name of the template
        :type solution: Optional[str]
        :param solution: A specific solution of config
        :type family: Optional[str]
        :param family: A specific family of hardware, like Cat9K, or something
        :type model: Optional[str]
        :param model: The hardware model, like WS-C3560G-48TS-E or something

        :rtype: Union[str, None]
        :returns: A found path, or None
        """
        if src:
            self._display.v(f"'src' used {src}")
            template_relative_paths = [src]

        else:
            templates_directory = self._find_templates_directory()

            template_relative_paths = [
                f"{templates_directory}/{self._ansible_network_os}/{solution}/{family}/{model}/{template_name}",
                f"{templates_directory}/{self._ansible_network_os}/{solution}/{family}/main/{template_name}",
                f"{templates_directory}/{self._ansible_network_os}/{solution}/main/{template_name}",
                f"{templates_directory}/{self._ansible_network_os}/{family}/{model}/{template_name}",
                f"{templates_directory}/{self._ansible_network_os}/{family}/main/{template_name}",
                f"{templates_directory}/{self._ansible_network_os}/main/{template_name}",
            ]

        for templates_path in template_relative_paths:
            self._display.v(f"CHECK: templates_path {templates_path}")
            if os.path.isfile(templates_path):
                self._display.v(f"FOUND: templates_path {templates_path}")
                return templates_path

        self._display.v(f"NOT FOUND: templates_path {None}")
        return None

    @staticmethod
    @abstractmethod
    def validate_module_params(template_variables: dict) -> None:
        """Static Method to validate the template variable data as you see fit"""

    def render_config(
        self,
        src: Optional[str] = None,
        template_name: Optional[str] = None,
        solution: Optional[str] = None,
        family: Optional[str] = None,
        model: Optional[str] = None,
    ) -> str:
        """Render config from a template

        :type src: Optional[str]
        :param src: If src is given no lookups are done, and it is assumed it is an exact path to a template
        :type template_name: Optional[str]
        :param template_name: The name of the template
        :type solution: Optional[str]
        :param solution: A specific solution of config
        :type family: Optional[str]
        :param family: A specific family of hardware, like Cat9K, or something
        :type model: Optional[str]
        :param model: The hardware model, like WS-C3560G-48TS-E or something

        :rtype: String
        :returns: The rendered config
        """
        found_template = self._find_template(
            src=src,
            template_name=template_name,
            solution=solution,
            family=family,
            model=model,
        )
        if not found_template:
            raise FileNotFoundError(f"could not locate template_name: '{template_name}' or src: '{src}'!")

        rendered_template = self._render_template(template_path=found_template)

        return rendered_template
