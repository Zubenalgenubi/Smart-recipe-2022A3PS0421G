import axios from "axios";

const API = "http://localhost:8000";

export const fetchRecipes = async (ingredients, filters) => {
  const res = await axios.get(`${API}/recipes`, {
    params: {
      ingredients: ingredients.join(","),
      diet: filters.diet,
      difficulty: filters.difficulty,
      max_time: filters.time
    }
  });
  return res.data.recipes;
};

export const detectIngredients = async (file) => {
  const form = new FormData();
  form.append("file", file);

  const res = await axios.post(`${API}/detect`, form);
  return res.data.ingredients;
};