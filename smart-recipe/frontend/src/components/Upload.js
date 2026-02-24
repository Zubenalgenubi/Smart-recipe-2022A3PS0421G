import React from "react";
import { detectIngredients } from "../api";

export default function Upload({ setIngredients }) {
  const handleUpload = async (e) => {
    const file = e.target.files[0];
    const ingredients = await detectIngredients(file);
    setIngredients(ingredients);
  };

  return <input type="file" onChange={handleUpload} />;
}