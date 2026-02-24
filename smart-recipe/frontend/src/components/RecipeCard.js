export default function RecipeCard({ recipe }) {
  return (
    <div className="border p-3 rounded shadow">
      <h2 className="font-bold">{recipe.name}</h2>
      <p>Calories: {recipe.nutrition.calories}</p>
      <p>Protein: {recipe.nutrition.protein}</p>
      <p>Time: {recipe.time} min</p>

      <h3 className="font-semibold mt-2">Steps:</h3>
      <ul>
        {recipe.steps.map((s, i) => (
          <li key={i}>• {s}</li>
        ))}
      </ul>
    </div>
  );
}