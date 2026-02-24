from fastapi import FastAPI, UploadFile, File, Query
from matcher import match_recipes
from image_recognition import detect_ingredients
import json

app = FastAPI()

with open("recipes_clean.json") as f:
    recipes = json.load(f)


@app.get("/")
def home():
    return {"message": "Smart Recipe API running"}


@app.post("/detect")
async def detect(file: UploadFile = File(...)):
    ingredients = detect_ingredients(await file.read())
    return {"ingredients": ingredients}


@app.get("/recipes")
def get_recipes(
    ingredients: str,
    diet: str = "",
    difficulty: str = "",
    max_time: int = 1000
):
    ing_list = ingredients.lower().split(",")

    matches = match_recipes(recipes, ing_list, diet, difficulty, max_time)

    return {"recipes": matches[:5]}