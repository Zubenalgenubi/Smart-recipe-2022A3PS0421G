export default function Filters({ setFilters }) {
  return (
    <div className="my-2">
      <select onChange={(e) => setFilters(f => ({ ...f, diet: e.target.value }))}>
        <option value="">All</option>
        <option value="vegetarian">Vegetarian</option>
      </select>

      <select onChange={(e) => setFilters(f => ({ ...f, difficulty: e.target.value }))}>
        <option value="">Any</option>
        <option value="Easy">Easy</option>
        <option value="Medium">Medium</option>
      </select>
    </div>
  );
}