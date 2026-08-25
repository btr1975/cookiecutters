# Ansible Modules

* This directory is used for your custom Ansible modules

### Notes

* Modules typically execute on the remote host
* They **CAN NOT** use hostvars, if you want to use hostvars
  you will need to write an action to inject them
* Modules have a defined Argument Specification for more information
  see the [Argument Spce Docs](https://docs.ansible.com/ansible/latest/dev_guide/developing_program_flow_modules.html#argument-spec)
* [Common Return Values](https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html)
