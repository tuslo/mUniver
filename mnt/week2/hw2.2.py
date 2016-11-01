#!/usr/bin/env python
import pymongo

# no need to import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db = connection.students
grades = db.grades


def find():
    print "find, reporting for duty"
    query = {"type": "homework"}
    try:
        cursor = grades.find(query)
        #cursor.limit(12)
        # cursor.sort('score', pymongo.ASCENDING).skip(4).limit(1)
        cursor.sort([('student_id', pymongo.ASCENDING),
                     ('score', pymongo.DESCENDING)])

    except Exception as e:
        print "Unexpected error:", type(e), e

    doc_to_compare = {'student_id':0};
    for doc in cursor:
        print
        print "Saved id:", doc_to_compare['student_id']
        print "Real id:", doc['student_id']

        if doc_to_compare['student_id'] != doc['student_id']:
            result = grades.delete_one({'_id' : doc_to_compare['_id']})
            print result, result.deleted_count

        doc_to_compare = doc;

    result = grades.delete_one({'_id': doc['_id']})
    print result, result.deleted_count


if __name__ == '__main__':
    find()
