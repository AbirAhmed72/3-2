from bson import ObjectId
from fastapi import APIRouter, HTTPException
import pymongo
from Models.user import UserCreate
from Configs.database import db
from Schemas.user import serializeDict, serializeList, userEntity, usersEntity

user = APIRouter()

@user.get('/')
async def find_all_users():
    # return db.find()
    # print (db.Users.find())
    # print (usersEntity(db.Users.find()))
    all_users = serializeList(db.Users.find())
    return (all_users)

@user.post('/')
async def create_user(user: UserCreate):
    user_dict = user.model_dump()

    # Insert the dictionary into the MongoDB collection
    inserted_user = db.Users.insert_one(user_dict)

    # Check if the insertion was successful
    if inserted_user.acknowledged:
        # Return the inserted user data with the generated ObjectId
        return (usersEntity(db.Users.find()))

    else:
        # If insertion failed, raise an HTTP exception
        raise HTTPException(status_code=500, detail="User creation failed")
    # return (usersEntity(db.Users.find()))

@user.get('/{id}')
async def find_one_user(id):
    return serializeDict(db.Users.find_one({"_id":ObjectId(id)}))


@user.put('/{id}')
async def update_user(id, user: UserCreate):
    print(id)
    updated_user = db.Users.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": dict(user)},
        return_document=pymongo.ReturnDocument.AFTER  # Return the updated document
    )
    
    if updated_user:
        return serializeDict(updated_user)
    
    return {"message": "User not found"}

@user.delete('/{id}')
async def delete_user(id):
    deleted_user = db.Users.find_one_and_delete({"_id": ObjectId(id)})
    
    if deleted_user:
        return serializeDict(deleted_user)
    
    return {"message": "User not found"}


@user.get('/')
async def find_all_users():
    # return db.find()
    # print (db.Users.find())
    # print (usersEntity(db.Users.find()))
    # all_users = serializeList(await db.Users.find())
    # return (all_users)
    cursor = db.Users.find()
    users = await cursor.to_list(length=None)
    
    # Serialize the list of documents
    serialized_users = serializeList(users)
    
    return serialized_users

@user.post('/')
async def create_user(user: UserCreate):
    user_dict = user.model_dump()

    # Insert the dictionary into the MongoDB collection
    inserted_user = db.Users.insert_one(user_dict)

    # Check if the insertion was successful
    if inserted_user.acknowledged:
        # Return the inserted user data with the generated ObjectId
        return (usersEntity(db.Users.find()))

    else:
        # If insertion failed, raise an HTTP exception
        raise HTTPException(status_code=500, detail="User creation failed")
    # return (usersEntity(db.Users.find()))

@user.get('/{id}')
async def find_one_user(id):
    return serializeDict(db.Users.find_one({"_id":ObjectId(id)}))


@user.put('/{id}')
async def update_user(id, user: UserCreate):
    print(id)
    updated_user = db.Users.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": dict(user)},
        return_document=pymongo.ReturnDocument.AFTER  # Return the updated document
    )
    
    if updated_user:
        return serializeDict(updated_user)
    
    return {"message": "User not found"}

@user.delete('/{id}')
async def delete_user(id):
    deleted_user = db.Users.find_one_and_delete({"_id": ObjectId(id)})
    
    if deleted_user:
        return serializeDict(deleted_user)
    
    return {"message": "User not found"}
