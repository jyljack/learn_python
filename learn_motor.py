##https://motor.readthedocs.io/en/stable/tutorial-asyncio.html
import asyncio

from motor.motor_asyncio import AsyncIOMotorClient

## Creating a Client
conn_str = "mongodb://{username}:{password}@{host}:{port}/{dbname}".format(username='admin',
                                                                           password='admin',
                                                                           host='*****',
                                                                           port=27017,
                                                                           dbname="demo")
client = AsyncIOMotorClient(conn_str, connectTimeoutMS=5000, serverSelectionTimeoutMS=5000)

## Getting a Database
db = client['quant']

## Getting a Collection
collection = db['test_collection']
collection = db.test_collection


async def get_server_info():
    server_info = await client.server_info()
    print(server_info)


async def list():
    ns = await client.list_database_names()
    print(ns)


## Inserting a Document
async def insert():
    document = {"item": "canvas"}
    result = await collection.insert_one(document)
    print('result %s' % repr(result.inserted_id))

    documents = [
        {"item": "journal",
         "qty": 25,
         "tags": ["blank", "red"],
         "size": {"h": 14, "w": 21, "uom": "cm"}},
        {"item": "mat",
         "qty": 85,
         "tags": ["gray"],
         "size": {"h": 27.9, "w": 35.5, "uom": "cm"}},
        {"item": "mousepad",
         "qty": 25,
         "tags": ["gel", "blue"],
         "size": {"h": 19, "w": 22.85, "uom": "cm"}}]
    result = await db.test_collection.insert_many(documents)
    print('insert %d docs' % (len(result.inserted_ids),))


## Getting a Single Document
async def find_one():
    document = await collection.find_one({'item': 'canvas'})
    print(document)


## Querying for More Than One Document
async def find():
    cursor = collection.find({'item': {"$in": ["journal", "mat"]}}).sort("qty").skip(1).limit(2)
    for document in await cursor.to_list(length=100):
        print(document)

    async for document in collection.find({'item': {"$in": ["mousepad"]}}):
        print(document)


## Counting Documents
async def count():
    n = await collection.count_documents({'qty': {'$gt': 50}})
    print('%s documents where i > 50' % n)


## Updating Documents
async def update():
    await collection.update_many({'item': 'journal'}, {'$set': {'qty': '35'}})
    async for new_document in collection.find({'item': 'journal'}):
        print(new_document)


## Delete Documents
async def delete():
    await collection.delete_many({'item': 'canvas'})
    new_document = await collection.find_one({'item': 'canvas'})
    print(new_document)


if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    # event_loop.run_until_complete(get_server_info())
    event_loop.run_until_complete(list())
    # event_loop.run_until_complete(insert())
    # event_loop.run_until_complete(find_one())
    # event_loop.run_until_complete(find())
    # event_loop.run_until_complete(count())
    # event_loop.run_until_complete(update())
    # event_loop.run_until_complete(delete())
