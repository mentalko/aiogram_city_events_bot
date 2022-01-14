from typing import Dict, List, Union, Optional
from unicodedata import category
from data.config import DB_HOST, DB_NAME
from utils.models.user import User


from motor.motor_asyncio import AsyncIOMotorClient

uri = "mongodb://localhost/" + \
        "?retryWrites=false".format(DB_HOST=DB_HOST, DB_NAME=DB_NAME)

print('Connection to MongoDB...')
client = AsyncIOMotorClient(uri)
db = client.get_database(DB_NAME)
print(db)
print('Connection success!')


async def do_insert_one(collection_name: str, document: Union[User, Dict]):
    collection = db.get_collection(collection_name)
    await collection.insert_one(document)
    
    
async def do_find_one(collection_name: str, document: Union[User, Dict]) -> Optional[Dict]:
    collection = db.get_collection(collection_name)
    return await collection.find_one(document)

async def do_find(collection_name: str, document: Union[User, Dict], sort_param=None, limit=None) -> List[Dict]:
    collection = db.get_collection(collection_name)
    cursor = collection.find(document)
    
    if sort_param is not None:
        cursor.sort(sort_param['sort_by'], sort_param['sort_type'])
        
    if limit is not None:
        cursor.limit(limit)
        
    result = []
    async for item in cursor:
        result.append(item)
    return result


async def check_db_exists(*args, **kwargs):
    collist = await db.list_collection_names()
    # categories = await db_find()
    
    print('DB CONECTED ', collist)