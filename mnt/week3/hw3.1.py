#!/usr/bin/env python
import pymongo
import pprint

# no need to import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db = connection.school
students = db.students


def find():
    print "find, reporting for duty"
    query = {"scores": {"$elemMatch" : {"type" : "homework"}}};
    try:
        cursor = students.find(query)
        # cursor.limit(1)
        # cursor.sort('score', pymongo.ASCENDING).skip(4).limit(1)
        # cursor.sort([('student_id', pymongo.ASCENDING),
        #              ('score', pymongo.DESCENDING)])

    except Exception as e:
        print "Unexpected error:", type(e), e

    for doc in cursor:
        prev_score = 0;
        # pprint.pprint(doc['scores'])
        for score in doc['scores']:
            if score['type'] == 'homework' and (score['score'] <= prev_score):
                print "To remove: ", score['score']
                doc['scores'].remove(score);
            else :
                prev_score = score['score']
        result = students.update_one({'_id': doc['_id']},
                                   {'$set': {'scores': doc['scores']}})
        pprint.pprint(result)

    #pprint.pprint(result)


if __name__ == '__main__':
    find()
