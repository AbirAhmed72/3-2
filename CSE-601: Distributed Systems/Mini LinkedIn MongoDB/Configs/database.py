from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient


# Create a MongoDB client
mongo_url = "mongodb://localhost:27017/"
client = MongoClient(mongo_url)
# client = AsyncIOMotorClient(mongo_url)
db = client.MiniLinkedIn_DB


# Dependency function to get the MongoDB client
# def get_db():
#     try:
#         yield mongo_client.get_database()
#     finally:
#         mongo_client.close()

# from pymongo import MongoClient
# db = MongoClient("mongodb://localhost:27017/MiniLinkedIn_DB")
# database.py
# from pymongo import MongoClient
# from pymongo.errors import ConnectionFailure
# from motor.motor_asyncio import AsyncIOMotorClient

# # MongoDB connection details
# mongo_host = "localhost"  # Replace with your MongoDB server host
# mongo_port = 27017  # Replace with your MongoDB server port
# database_name = "MiniLinkedIn_DB"  # Replace with your MongoDB database name

# try:
#     # Create a MongoClient instance to connect to MongoDB
#     client = AsyncIOMotorClient(host=mongo_host, port=mongo_port)

#     # Access the specified database
#     db = client[database_name]

#     # Test the database connection
#     db.command("ismaster")
#     print("Connected to MongoDB")

# except ConnectionFailure as e:
#     print("Error connecting to MongoDB:", str(e))
#     # Handle the connection error gracefully here

