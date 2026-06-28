function SalesSummary({ sales, onVenueClick }) {
  return (
    <div>
      <h2>Total Sales by Venue</h2>
      <ul>
        {sales.map((venue) => (
          <li key={venue.id} onClick={() => onVenueClick(venue)}>
            {venue.name}: ${venue.total}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default SalesSummary;
