import os
import subprocess
import bottle
import pymongo

app = bottle.app()

# this is the handler for the default path of the web server

@bottle.route('/')
def index():
    
    # connect to mongoDB
    connection = pymongo.MongoClient('localhost', 27017)

    # attach to test database
    db = connection.test


    # get handle for names collection
    #name = db.names

    # find a single document
    #item = name.find_one()

    return '<b>Hello !</b>'


bottle.run(app=app,host='0.0.0.0', port=80, debug=True)
