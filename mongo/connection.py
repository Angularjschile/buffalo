from pymongo import MongoClient

# make the actual client connection to the local db. should change for  \
#	production and be values written out to the environment or something\
#	like a globals config file. so that it can point to the live db and \
#	not the test db.
client = MongoClient('localhost', 27017)

# you can pull this into anywhere and start using it like this:
#	from mongo.connection import DB
DB = client['buffalo-dev']