# Smart Recipe Generator

Smart Recipe Generator is a full-stack web application that suggests recipes based on available ingredients (text or image input). The system matches recipes intelligently, applies dietary and nutrition filters, and provides detailed cooking information in a clean, mobile-friendly interface.

---

## How the Recipe Database Works

The application uses a **static recipe database (`recipes.json`)**.

* `recipes.json` is **not generated during runtime**
* It must exist **before starting the backend**
* The backend **loads it once at startup**
* The app only **reads from it** (read-only)
* It does **not change automatically**

### Workflow

1. Convert dataset → `recipes_clean.json`
2. Rename or load it as `recipes.json`
3. Backend loads recipes into memory
4. User queries → Recipes matched → Results returned

---

## Dataset Conversion

Run the conversion script once:

```bash
python convert_dataset.py
```

This generates:

```
recipes_clean.json
```

Rename to:

```
recipes.json
```

or update backend loader accordingly.

---

## Recipe JSON Format

Each recipe must follow this structure:

```json
{
  "name": "Recipe Name",
  "ingredients": ["ingredient1", "ingredient2"],
  "diet": ["vegetarian", "vegan"],
  "difficulty": "Easy",
  "time": 30,
  "nutrition": {
    "calories": 300,
    "protein": 20,
    "fat": 10,
    "carbs": 35
  }
}
```

---

## Features

### Ingredient Input

* Text input
* Image → ingredient detection (stub / ML ready)

### Recipe Matching

* Ingredient overlap scoring
* Diet preference matching
* Ranked recipe suggestions

### Filters

* Diet (vegetarian, vegan, gluten-free, etc.)
* Cooking time
* Difficulty
* Nutrition (protein, calories)

### Nutrition Information

* Calories
* Protein
* Fat
* Carbohydrates

### UI/UX

* Clean interface
* Mobile responsive
* Loading and error handling

---

## Project Structure

```
smart-recipe/
│
├── backend/
│   ├── main.py
│   ├── matcher.py
│   ├── convert_dataset.py
│   ├── recipes.json
│
└── frontend/
    ├── src/
    │   ├── App.js
    │   ├── components/
    │   └── index.css
```

---

## How to Run

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

Backend runs at:

```
http://localhost:8000
```

---

### Frontend

```bash
cd frontend
npm install
npm start
```

Frontend runs at:

```
http://localhost:3000
```

---

## Important Notes

* `recipes.json` is **static input data**
* It is **not generated automatically**
* The backend **must find it before starting**
* If file is missing → backend will fail
* If file is empty → no recipes will be returned

---

## Evaluation Highlights

* Ingredient classification approach
* Recipe matching logic
* Dataset cleaning pipeline
* Nutrition-aware filtering
* Error handling
* Mobile-responsive UI

---

## Future Improvements

* Real ML ingredient detection (YOLO / MobileNet)
* MongoDB recipe storage
* User ratings & recommendation system
* Grocery list generator
* Advanced substitution engine
* Deployment (Render + Vercel)

---

## Author

Smart Recipe Generator — Full-stack AI/ML project.
