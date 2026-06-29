# from openai import OpenAI 
import psycopg2
# import streamlit as st
from psycopg2.extensions import register_adapter, AsIs
import os
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

#load env vars
load_dotenv()

database_url = os.getenv("DB_URL")

conn = psycopg2.connect(database_url)

#intiate
model = SentenceTransformer("all-MiniLM-L6-v2")

#generate embeddings

input = "i am learning gen-ai"

embedding = model.encode(input)

print(embedding)

print(type(embedding))
print(embedding.shape)
cursor = conn.cursor()

