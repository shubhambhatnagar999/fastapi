# backend/database.py
from pymongo import MongoClient

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")

# Select DB
db = client["codingcloud"]

