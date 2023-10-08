# database.py
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from motor.motor_asyncio import AsyncIOMotorClient

# MongoDB connection details
mongo_host = "localhost"  # Replace with your MongoDB server host
mongo_port = 27017  # Replace with your MongoDB server port
database_name = "MiniLinkedIn_DB"  # Replace with your MongoDB database name

try:
    # Create a MongoClient instance to connect to MongoDB
    client = AsyncIOMotorClient(host=mongo_host, port=mongo_port)

    # Access the specified database
    db = client[database_name]

    # Test the database connection
    db.command("ismaster")
    print("Connected to MongoDB")

except ConnectionFailure as e:
    print("Error connecting to MongoDB:", str(e))
    # Handle the connection error gracefully here
