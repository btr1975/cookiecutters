"""
MongoDB inventory plugin
"""

from ansible.plugins.inventory import BaseInventoryPlugin, Constructable, Cacheable
from ansible.errors import AnsiblePluginError, AnsibleParserError
from pymongo import MongoClient

from ansible_collections.{{ cookiecutter.__git_repo_name }}.plugins.module_utils.mongo.mongo_client import (
    MongoAnsibleClient,
)


class InventoryModule(BaseInventoryPlugin, Constructable, Cacheable):

    NAME = "{{ cookiecutter.__git_repo_name }}.mongo_inventory"

    def verify_file(self, path: str) -> bool:
        """Verify config file can be found

        :type path: String
        :param path: The path to the inventory config file

        :rtype: Boolean
        :returns: If the config can be found
        """
        file_verified = False
        if super().verify_file(path=path):
            if path.endswith(("yaml", "yml")):
                file_verified = True

        return file_verified

    def add_host_to_all_group(self, name: str) -> None:
        """Add a host to the 'all' group

        :type name: String
        :param name: The device name

        :rtype: None
        :returns: Nothing it adds the 'all' group to a device
        """
        self.inventory.add_host(name.lower(), "all")

    def add_host_to_group(self, name: str, group_name: str) -> None:
        """Add a host to a named group

        :type name: String
        :param name: The device name
        :type group_name: String
        :param group_name: The name of the group

        :rtype: None
        :returns: Nothing it adds a group to a device
        """
        self.inventory.add_group(group_name.lower())
        self.inventory.add_host(name.lower(), group_name.lower())

    def set_entity_variable(self, entity: str, variable: str, value: str) -> None:
        """Set a named variable with a value on a host

        :type entity: String
        :param entity: The host or group
        :type variable: String
        :param variable: The name of the variable
        :type value: String
        :param value: The variable value

        :rtype: None
        :returns: Nothing it sets a variable on a host
        """
        self.inventory.set_variable(entity.lower(), variable.lower(), value)

    def set_mongo_client(self, config: dict) -> None:
        """Set mongo client needs

        :type config: Dict
        :param config: The plugin config

        :rtype: None
        :returns: Nothing it sets needed self variables
        """
        client = MongoClient(
            host=config.get("mongo_host"),
            port=int(config.get("mongo_port")),
            username=str(config.get("mongo_username")),
            password=str(config.get("mongo_password")),
        )

        self.mongo_client = MongoAnsibleClient(client=client)

    def verify_mongo_reachability(self) -> None:
        """Verify mongo reachability

        :rtype: None
        :returns: Nothing verifies reachability
        """
        response = self.mongo_client.get_database().command("ping")

        if response.get("ok"):
            if response.get("ok") == 1.0:
                self.display.v("connection to mongo verified")
                return

        self.display.v("connection to mongo failed")
        raise AnsiblePluginError("could not connect to MongoDB")

    def load_all_devices(self) -> None:
        """Load all devices

        :rtype: None
        :returns: Nothing it loads all the inventory
        """
        for device in self.mongo_client.find_documents(collection="hosts", projection={"_id": False}):
            name = device.get("name").lower()
            self.add_host_to_all_group(name=name)

            for variable, value in device.get("variables").items():
                self.set_entity_variable(entity=name, variable=variable.lower(), value=value)

            for group_name in device.get("groups"):
                self.add_host_to_group(name=name, group_name=group_name.lower())

    def load_all_groups(self) -> None:
        """Load all groups

        :rtype: None
        :returns: Nothing it loads all the groups in the inventory
        """
        for group in self.mongo_client.find_documents(collection="groups", projection={"_id": False}):
            name = group.get("name").lower()

            self.inventory.add_group(name)

            for variable, value in group.get("variables").items():
                self.set_entity_variable(entity=name, variable=variable.lower(), value=value)

    def load_devices_by_data_filter(self, data_filter: dict) -> None:
        """Load devices using a mongo filter

        :type data_filter: Dict
        :param data_filter: The MongoDB filter

        :rtype: None
        :returns: Nothing it loads devices from a Mongo filter
        """
        for device in self.mongo_client.find_documents(
            collection="hosts", projection={"_id": False}, data_filter=data_filter
        ):
            name = device.get("name").lower()
            self.add_host_to_all_group(name=name)

            for variable, value in device.get("variables").items():
                self.set_entity_variable(entity=name, variable=variable.lower(), value=value)

            for group_name in device.get("groups"):
                self.add_host_to_group(name=name, group_name=group_name.lower())

    def load_groups_by_data_filter(self, data_filter: dict) -> None:
        """Load groups using a mongo filter

        :type data_filter: Dict
        :param data_filter: The MongoDB filter

        :rtype: None
        :returns: Nothing it loads groups from a Mongo filter
        """
        for group in self.mongo_client.find_documents(
            collection="groups", projection={"_id": False}, data_filter=data_filter
        ):
            name = group.get("name").lower()

            self.inventory.add_group(name)

            for variable, value in group.get("variables").items():
                self.set_entity_variable(entity=name, variable=variable.lower(), value=value)

    def parse(self, inventory, loader, path, cache=True):
        super().parse(inventory, loader, path, cache)

        self.display.v(f"inventory config path: {path}")

        try:
            config = loader.load_from_file(path)

        except AnsibleParserError as error:
            raise AnsibleParserError(f"failed to parse {path}: {error}")

        self.set_mongo_client(config=config)

        self.verify_mongo_reachability()

        if not config.get("mongo_all_groups") and not config.get("mongo_filter_groups"):
            raise AnsiblePluginError("either mongo_all_groups or mongo_filter_groups is required")

        if not config.get("mongo_all_devices") and not config.get("mongo_filter_devices"):
            raise AnsiblePluginError("either mongo_all_devices or mongo_filter_devices is required")

        if config.get("mongo_all_groups") and isinstance(config.get("mongo_all_groups"), bool):
            if config.get("mongo_all_groups"):
                self.load_all_groups()

        elif config.get("mongo_filter_groups") and isinstance(config.get("mongo_filter_groups"), dict):
            self.load_groups_by_data_filter(data_filter=config.get("mongo_filter_groups"))

        if config.get("mongo_all_devices") and isinstance(config.get("mongo_all_devices"), bool):
            if config.get("mongo_all_devices"):
                self.load_all_devices()

        elif config.get("mongo_filter_devices") and isinstance(config.get("mongo_filter_devices"), dict):
            self.load_devices_by_data_filter(data_filter=config.get("mongo_filter_devices"))

        self.mongo_client.close_client()
