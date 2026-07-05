import React, { useEffect, useState } from "react";
import axios from "axios";

function Dashboard() {
  const [venueSales, setVenueSales] = useState([]);
  const [topItems, setTopItems] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/transactions/venue-sales/")
      .then(res => setVenueSales(res.data))
      .catch(err => console.error(err));

    axios.get("http://127.0.0.1:8000/api/transactions/top-items/")
      .then(res => setTopItems(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h1>Ops Dashboard</h1>

      <h2>Total Sales by Venue</h2>
      <ul>
        {venueSales.map(v => (
          <li key={v.venue__name}>{v.venue__name}: ₹{v.total_sales}</li>
        ))}
      </ul>

      <h2>Top Selling Items</h2>
      <ul>
        {topItems.map(i => (
          <li key={i.item__name}>{i.item__name}: {i.total_sold}</li>
        ))}
      </ul>

      <h2>Alerts</h2>
      <p>No issues detected</p>
    </div>
  );
}

export default Dashboard;
