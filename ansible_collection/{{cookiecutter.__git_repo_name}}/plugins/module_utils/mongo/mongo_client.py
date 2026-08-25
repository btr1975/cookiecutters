"""
Mongo client
"""

from typing import Optional, Literal
from pymongo.cursor import Cursor
from pymongo import MongoClient
from pymongo.database import Database
from pymongo.command_cursor import CommandCursor
from pymongo.collection import Collection, DeleteResult, UpdateResult, InsertOneResult


class MongoAnsibleClient:
    """Class for a Mongo client

    :type client: MongoClient
    :param client: Mongo Client from Pymongo, or mongomock for testing

    :rtype: None
    :returns: Nothing it creates a client
    """

    def __init__(self, client: MongoClient) -> None:
        self._client = client
        self._database_name = "ansible_inventory"
        self._collections = {"hosts": "hosts", "groups": "groups"}

    def get_database(self) -> Database:
        """Method to get the database

        :rtype: pymongo.database.Database
        :returns: The database
        """
        return self._client.get_database(name=self._database_name)

    def close_client(self) -> None:
        """Method to close the pymongo client

        :rtype: None
        :returns: Nothing it closes the client
        """
        self._client.close()

    def get_collections_list(self) -> CommandCursor:
        """Method to get a list of collections in the database

        :rtype: pymongo.command_cursor.CommandCursor
        :returns: The command cursor
        """
        return self.get_database().list_collections()

    def get_collection(self, collection: Literal["hosts", "groups"]) -> Collection:
        """Method to get a collection

        :type collection: Literal["hosts", "groups"]
        :param collection: The collection to use

        :rtype: pymongo.collection.Collection
        :returns: The collection
        """
        if not self._collections.get(collection):
            raise ValueError(f"'{collection}' is not a valid collection name")

        return self.get_database().get_collection(name=self._collections.get(collection))

    def create_document(self, collection: Literal["hosts", "groups"], document_data: dict) -> InsertOneResult:
        """Method to create a document in the collection

        :type collection: Literal["hosts", "groups"]
        :param collection: The collection to use
        :type document_data: Dict
        :param document_data: The data for the new document

        :rtype: pymongo.collection.InsertOneResult
        :returns: The ID of the new document
        """
        return self.get_collection(collection=collection).insert_one(document=document_data)

    def delete_one_document(self, collection: Literal["hosts", "groups"], data_filter: dict) -> DeleteResult:
        """Method to delete one document from the collection

        :type collection: Literal["hosts", "groups"]
        :param collection: The collection to use
        :type data_filter: Dict
        :param data_filter: The filter data

        :rtype: pymongo.collection.DeleteResult
        :returns: The response from mongo
        """
        return self.get_collection(collection=collection).delete_one(filter=data_filter)

    def find_documents(
        self,
        collection: Literal["hosts", "groups"],
        data_filter: Optional[dict] = None,
        projection: Optional[dict] = None,
        skip: Optional[int] = 0,
        limit: Optional[int] = 0,
    ) -> Cursor:
        """Method to find documents in the collection

        :type collection: Literal["hosts", "groups"]
        :param collection: The collection to use
        :type data_filter: Optional[dict] = None
        :param data_filter: The filter data
        :type projection: Optional[dict] = None
        :param projection: The mongo projection
        :type skip: Optional[int] = 0
        :param skip: The number of documents to skip
        :type limit: Optional[int] = 0
        :param limit: The number of documents to limit

        :rtype: pymongo.collection.Cursor
        :returns: The response from mongo

        :raises ValueError: If collection name is not set in class
        """
        return self.get_collection(collection=collection).find(
            filter=data_filter, projection=projection, skip=skip, limit=limit
        )

    def find_one_document(
        self,
        collection: Literal["hosts", "groups"],
        data_filter: Optional[dict] = None,
        projection: Optional[dict] = None,
    ) -> dict:
        """Method to find one document in the collection

        :type collection: Literal["hosts", "groups"]
        :param collection: The collection to use
        :type data_filter: Optional[dict] = None
        :param data_filter: The filter data
        :type projection: Optional[dict] = None
        :param projection: The mongo projection

        :rtype: Dict
        :returns: The response from mongo

        :raises ValueError: If collection name is not set in class
        """
        return self.get_collection(collection=collection).find_one(filter=data_filter, projection=projection)

    def update_one_document(
        self,
        collection: Literal["hosts", "groups"],
        data_filter: dict,
        update_data: dict,
        upsert: Optional[bool] = True,
    ) -> UpdateResult:
        """Method to find one document in the collection

        :type collection: Literal["hosts", "groups"]
        :param collection: The collection to use
        :type data_filter: Dict
        :param data_filter: The filter data
        :type update_data: Dict
        :param update_data: The data to update
        :type upsert: Optional[bool] = True
        :param upsert: Set False to not use upsert

        :rtype: UpdateResult
        :returns: The response from mongo

        :raises ValueError: If collection name is not set in class
        """
        return self.get_collection(collection=collection).update_one(
            filter=data_filter, update=update_data, upsert=upsert
        )

    def aggregation(self, collection: Literal["hosts", "groups"], pipeline: list) -> CommandCursor:
        """Method to run an aggregation pipeline

        :type collection: Literal["hosts", "groups"]
        :param collection: The collection to use
        :type pipeline: List
        :param pipeline: The aggregation pipeline

        :rtype: pymongo.command_cursor.CommandCursor
        :returns: The response from mongo
        """
        return self.get_collection(collection=collection).aggregate(pipeline=pipeline)
