from typing import Dict, List, Union, Optional
from unicodedata import category
from data.config import DB_HOST, DB_NAME, DB_USER, DB_PASS
from utils.models.user import User


from motor.motor_asyncio import AsyncIOMotorClient


if DB_USER:
    url = "mongodb+srv://{}:{}@{}/{}".format(DB_USER, DB_PASS, DB_HOST, DB_NAME)   
else:
    url = "mongodb://localhost/" + \
            "?retryWrites=false".format(DB_HOST=DB_HOST, DB_NAME=DB_NAME)


print('Connection to MongoDB...')
client = AsyncIOMotorClient(url)
db = client.get_database(DB_NAME)
# print(db)
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

async def do_update_one(collection_name: str, document: Union[User, Dict], set_document: Dict):
    collection = db.get_collection(collection_name)
    await collection.update_one(document, set_document)
    
async def do_delete_one(collection_name: str, document: Union[User, Dict]):
    collection = db.get_collection(collection_name)
    await collection.delete_one(document)


async def check_db_exists(*args, **kwargs):
    # collist = await db.list_collection_names()
    # categories = await db_find()
    
    print('DB CONECTED ')