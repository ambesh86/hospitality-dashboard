function VenueModal({ venue, onClose }) {
  return (
    <div className="modal">
      <h2>{venue.name} - Hourly Trade</h2>
      <ul>
        {venue.hourly.map((hour, idx) => (
          <li key={idx}>
            {hour.time}: ${hour.total}
          </li>
        ))}
      </ul>
      <button onClick={onClose}>Close</button>
    </div>
  );
}

export default VenueModal;
