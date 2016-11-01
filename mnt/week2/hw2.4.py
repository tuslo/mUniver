#!/usr/bin/env python
import pymongo
import pprint

# no need to import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db = connection.video
movies = db.movies
movieDetails = db.movieDetails


def find():
    print "find, reporting for duty"
    # query = {"type": "homework"}
    # query = {"awards": 0}
    query = {"year": 2013, "rated":"PG-13", "awards.nominations" : 0}
    try:
        result = movieDetails.find(query)
    except Exception as e:
        print "Unexpected error:", type(e), e

    pprint.pprint(result)
    for doc in result:
        pprint.pprint(doc)


if __name__ == '__main__':
    find()
