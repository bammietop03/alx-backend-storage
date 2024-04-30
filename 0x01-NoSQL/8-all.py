#!/usr/bin/env python3
"""a Python function that lists all documents in a collection"""


def list_all(mongo_collection):
    """ Use find() to retrieve all documents in the collection """
    all_documents = mongo_collection.find({})
    documents_list = list(all_documents)

    return documents_list
