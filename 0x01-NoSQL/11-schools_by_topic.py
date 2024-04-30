#!/usr/bin/env python3
""" 11-main """


def schools_by_topic(mongo_collection, topic):
    """function that returns the list of school having a specific topic"""
    school = mongo_collection.find({"topic": topic})
    list_school = list(school)
    return list_school
