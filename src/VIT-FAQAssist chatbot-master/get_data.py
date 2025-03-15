# import os
# import pandas as pd
# from dotenv import load_dotenv
# import pymongo
# from pymongo import MongoClient

# load_dotenv()
# # mongo_uri = os.getenv("mongo_uri")
# # client = MongoClient(mongo_uri)
# # db = client.get_database("VIT-FAQAssist")
# # queries = db.user_input_queries
# # augmentedDataQueries = db.AugmentedVITData
# # data = pd.read_csv("C:/Users/mayan/OneDrive/Desktop/desk/Syllabus/Capstone/src/VIT-FAQAssist chatbot-master/tensorflow_src/augmented_data.csv")
# # result = augmentedDataQueries.insert_many(data)
# # # data = pd.DataFrame(list(queries.find()))
# # # data.drop(data.columns[0], axis=1, inplace=True)
# # # data = data.drop_duplicates(
# # #     subset=["input_query"], keep='first', inplace=False, ignore_index=True)
# # # data.dropna()
# # # data.to_csv("new_user_data_raw.csv")
# # def connect_to_mongodb(database_name, collection_name):
# #     client = pymongo.MongoClient("mongodb://localhost:27017/")
# #     db = client[database_name]
# #     collection = db[collection_name]
# #     return client, collection


# # Read the CSV file into a DataFrame
# data = pd.read_csv("C:/Users/mayan/OneDrive/Desktop/desk/Syllabus/Capstone/src/VIT-FAQAssist chatbot-master/tensorflow_src/augmented_data.csv")

# # Connect to MongoDB
# client = pymongo.MongoClient("mongodb://localhost:27017/")
# db = client["VIT-FAQAssist"]  # Replace 'your_database_name' with your actual database name

# # Convert DataFrame to a list of dictionaries (each dictionary represents a document)
# data_list = data.to_dict(orient='records')

# # Insert the data into MongoDB
# # result = AugmentedDataCollection.insert_many(data_list)

# def insert_data(collection,data):
#     result = collection.insert_many(data)
#     return result.inserted_ids

# # print(insert_data("AugmentedVITData"))
# # def query_data(collection, query):
# #     return collection.find_one(query)

# def query_all_data(collection):
#     return collection.find()

# # def update_data(collection, query, new_data):
# #     result = collection.update_one(query, {"$set": new_data})
# #     return result.modified_count

# # def delete_data(collection, query):
# #     result = collection.delete_one(query)
# #     return result.deleted_count

# # def close_connection(client):
# #     client.close()


# intent, questions = query_all_data(db["user_input_queries"])
# insert_data(db["vitdatacollection"], data)


import os
import pandas as pd
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
mongo_uri = os.getenv("mongo_uri")
client = MongoClient(mongo_uri)
db = client.get_database("ieee_faq_bot")
queries = db.user_input_queries

data = pd.DataFrame(list(queries.find()))
data.drop(data.columns[0], axis=1, inplace=True)
data = data.drop_duplicates(
    subset=["input_query"], keep='first', inplace=False, ignore_index=True)
data.dropna()
data.to_csv("new_user_data_raw.csv")