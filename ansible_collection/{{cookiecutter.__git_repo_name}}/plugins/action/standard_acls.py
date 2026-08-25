"""
prefix_lists_from_template action plugin
"""

__metaclass__ = type

from typing import Optional, Tuple, List, Union
from ansible.plugins.action import ActionBase
from ansible.errors import AnsibleActionFail

from ansible_collections.{{ cookiecutter.__git_repo_name }}.plugins.module_utils.abcs.abcs_template_render import (
    RenderConfigFromTemplate,
)


class StandardAclRenderConfigFromTemplate(RenderConfigFromTemplate):

    @staticmethod
    def validate_module_params(template_variables: dict) -> None:
        pass


class ActionModule(ActionBase):

    def _render_config(
        self, current_hostvars: dict, config_data: List[dict], src: Optional[str] = None
    ) -> Tuple[List[str], List[str]]:
        """Protected method to render the config

        :type current_hostvars: Dict
        :param current_hostvars: The current devices hostvars
        :type config_data: List[dict]
        :param config_data: The variables to render the template with
        :type src: src: Optional[str] = None
        :param src: A template path for a specific template not built in to the collection

        :rtype: Tuple[List[str], List[str]]
        :returns: rendered, rendered_lines
        """
        rendered = []
        rendered_lines = []

        for single_config in config_data:
            renderer = StandardAclRenderConfigFromTemplate(
                templar=self._templar,
                template_variables=single_config,
                ansible_network_os=current_hostvars.get("ansible_network_os"),
            )

            rendered_template = renderer.render_config(
                src=src,
                template_name="standard_acl.j2",
                solution=current_hostvars.get("solution"),
                family=current_hostvars.get("family"),
                model=current_hostvars.get("model"),
            )

            rendered.append(rendered_template)
            rendered_lines.extend(rendered_template.splitlines())

        return rendered, rendered_lines

    def _get_config_data(self, from_hostvars_arg: Union[bool, None], current_hostvars: dict) -> List[dict]:
        """Protected method to get the config data from hostvars or from given data

        :type from_hostvars_arg: Union[bool, None]
        :param from_hostvars_arg: The option if set true will get the data from hostvars
        :type current_hostvars: Dict
        :param current_hostvars: The current devices hostvars

        :rtype: List[dict]
        :returns: The config data

        :raises KeyError: If data can not be retrieved from task option 'data'
        :raises ValueError: If the data is empty
        """

        if not from_hostvars_arg:
            try:
                config_data = self._task.args["data"]

            except KeyError as error:
                raise KeyError(
                    "required option 'data' was not supplied, set option 'from_hostvars' to true if "
                    "you want to get data from the hostvars"
                ) from error

        else:
            config_data = current_hostvars.get("standard_acls")

        if not config_data:
            raise ValueError("could not find config_data")

        return config_data

    def run(self, tmp=None, task_vars=None):
        super(ActionModule, self).run(tmp, task_vars)

        try:
            src_arg = self._task.args.get("src")
            from_hostvars_arg = self._task.args.get("from_hostvars")

            inventory_hostname = task_vars["inventory_hostname"]
            current_hostvars = task_vars["hostvars"].get(inventory_hostname, {})

            config_data = self._get_config_data(from_hostvars_arg=from_hostvars_arg, current_hostvars=current_hostvars)

            rendered, rendered_lines = self._render_config(
                current_hostvars=current_hostvars, config_data=config_data, src=src_arg
            )

        except Exception as error:
            raise AnsibleActionFail(f"{error}")

        return {
            "changed": False,
            "rendered": rendered,
            "rendered_lines": rendered_lines,
        }
