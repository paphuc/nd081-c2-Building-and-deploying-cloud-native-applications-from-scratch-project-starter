import pymongo

url = "mongodb+srv://paphuc:123456Abc@neighborly-app-db.mongocluster.cosmos.azure.com/?tls=true&authMechanism=SCRAM-SHA-256&retrywrites=false&maxIdleTimeMS=120000"
client = pymongo.MongoClient(url)
database = client['azure']
collection = database['advertisements']
result = collection.find({})
print("List of collections\n--------------------")
#list the collections
for coll in result:
    print(coll)