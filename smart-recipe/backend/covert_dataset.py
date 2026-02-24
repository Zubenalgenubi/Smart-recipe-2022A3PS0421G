import pandas as pd
import json
import ast

df = pd.read_csv("your_dataset.csv")

recipes = []

for _, row in df.iterrows():
    try:
        ingredients = []
        if isinstance(row["ingredients"], str):
            ingredients = [i.strip().lower() for i in row["ingredients"].split(",")]

        diet = []
        if row["vegetarian"]: diet.append("vegetarian")
        if row["vegan"]: diet.append("vegan")
        if row["glutenFree"]: diet.append("glutenFree")
        if row["dairyFree"]: diet.append("dairyFree")
        if row["ketogenic"]: diet.append("ketogenic")

        recipe = {
            "name": row["title"],
            "ingredients": ingredients,
            "diet": diet,
            "difficulty": "Easy" if row["readyInMinutes"] < 20 else "Medium" if row["readyInMinutes"] < 45 else "Hard",
            "time": int(row["readyInMinutes"]),
            "nutrition": {
                "calories": float(row["calories"]),
                "protein": float(row["Protein/g"]),
                "fat": float(row["Fat/g"]),
                "carbs": float(row["Carbohydrates/g"])
            }
        }

        recipes.append(recipe)

    except:
        continue

with open("recipes_clean.json", "w") as f:
    json.dump(recipes, f, indent=2)

print("Converted:", len(recipes), "recipes")