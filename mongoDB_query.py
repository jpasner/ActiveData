import pymongo
import pprint
from bson.json_util import dumps #pymongo utilities

mongoConnection = pymongo.MongoClient("localhost",27017) # Connect to pymongo server
myDB = mongoConnection["Norton4NID_Database"] #specify database
collection = myDB.Div5_Voter_Roll_Jake_Prioritization #specify collection

#Create dictionary of queries
query = {}

# Find returns an array of mongoDB documents (entries) that match your query
#mongoResults = collection.find(query, {"_id":0}) # Return Full List
mongoResults = collection.find(query, {"_id":0}).limit(10) # Limit Output to specified number

#create list of mongoResults
mongoList = list(mongoResults)

print(len(mongoList))

# Return Object you want
print(mongoList[1]['name_last'])

if(mongoList):
    #Create a json array out of our mongoResults
    jsonArray = (dumps(mongoList))
    print(len(jsonArray))

# Now we can manipulate the colletion


#for doc in mongoResults:
#        print(doc)
