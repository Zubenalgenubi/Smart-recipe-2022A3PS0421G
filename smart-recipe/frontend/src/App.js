import React, { useState } from "react";
import Upload from "./components/Upload";
import RecipeCard from "./components/RecipeCard";
import Filters from "./components/Filters";
import { fetchRecipes } from "./api";

export default function App() {
  const [ingredients, setIngredients] = useState([]);
  const [recipes, setRecipes] = useState([]);
  const [filters, setFilters] = useState({ diet: "", difficulty: "", time: 60 });

  const search = async () => {
    const data = await fetchRecipes(ingredients, filters);
    setRecipes(data);
  };

  return (
    <div className="p-4">
      <h1 className="text-xl font-bold">Smart Recipe Generator</h1>

      <Upload setIngredients={setIngredients} />

      <Filters setFilters={setFilters} />

      <button onClick={search} className="bg-green-500 p-2 text-white">
        Find Recipes
      </button>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mt-4">
        {recipes.map((r, i) => (
          <RecipeCard key={i} recipe={r} />
        ))}
      </div>
    </div>
  );
}