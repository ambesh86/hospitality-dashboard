function AlertsPanel({ alerts }) {
  return (
    <div>
      <h2>Alerts</h2>
      {alerts.length === 0 ? (
        <p>No issues detected</p>
      ) : (
        <ul>
          {alerts.map((alert, idx) => (
            <li key={idx} style={{ color: "red" }}>
              {alert.message}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default AlertsPanel;
