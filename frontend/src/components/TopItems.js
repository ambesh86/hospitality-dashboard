function TopItems({ items }) {
  return (
    <div>
      <h2>Top Selling Items</h2>
      <ul>
        {items.map((item) => (
          <li key={item.item_id}>
            {item.name} ({item.qty} sold)
          </li>
        ))}
      </ul>
    </div>
  );
}

export default TopItems;
