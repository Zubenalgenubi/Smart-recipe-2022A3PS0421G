SUBS = {
    "milk": ["almond milk", "soy milk"],
    "egg": ["banana", "yogurt"],
    "butter": ["olive oil"],
    "sugar": ["honey", "jaggery"]
}

def get_substitutions(missing_ingredients):
    result = {}
    for ing in missing_ingredients:
        if ing in SUBS:
            result[ing] = SUBS[ing]
    return result