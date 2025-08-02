from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

DATA_FILE = os.path.join(os.path.dirname(__file__), "data/mountains.json")

with open(DATA_FILE, "r", encoding="utf-8") as f:
  mountains = json.load(f)

@app.get("/")
def read_root():
  return {"message": "Welcome to Mountain Explorer API."}

@app.get("/api/mountains")
def get_all_mountains():
  return mountains

@app.get("/api/mountains/{mountain_id}")
def filter_mountain(mountain_id: int):
  for mountain in mountains:
    if mountain["id"] == mountain_id:
      return mountain
  return {"error": "Mountain not found"}