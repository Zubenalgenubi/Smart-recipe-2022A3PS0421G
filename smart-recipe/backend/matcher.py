def score_recipe(recipe, ingredients, diet_pref):
    ing_match = len(set(recipe["ingredients"]) & set(ingredients)) / max(len(recipe["ingredients"]), 1)
    diet_match = 1 if not diet_pref or diet_pref in recipe["diet"] else 0
    return 0.8 * ing_match + 0.2 * diet_match


def match_recipes(recipes, ingredients, diet, difficulty, max_time):
    results = []

    for r in recipes:
        if difficulty and r["difficulty"] != difficulty:
            continue
        if r["time"] > max_time:
            continue

        score = score_recipe(r, ingredients, diet)
        r["score"] = score
        results.append(r)

    return sorted(results, key=lambda x: x["score"], reverse=True)

def fuzzy_match(ingredient, ingredient_list):
    for i in ingredient_list:
        if ingredient in i or i in ingredient:
            return True
    return False


def score_recipe(recipe, ingredients, diet_pref):
    match_count = 0
    for ing in ingredients:
        if fuzzy_match(ing, recipe["ingredients"]):
            match_count += 1

    ing_score = match_count / max(len(recipe["ingredients"]), 1)
    diet_score = 1 if not diet_pref or diet_pref in recipe["diet"] else 0

    return 0.8 * ing_score + 0.2 * diet_score