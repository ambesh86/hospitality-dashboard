import React, { useEffect, useState } from "react";
import SalesSummary from "./SalesSummary";
import TopItems from "./TopItems";
import AlertsPanel from "./AlertsPanel";
import VenueModal from "./VenueModal";


function Dashboard() {
  const [salesData, setSalesData] = useState([]);
  const [topItems, setTopItems] = useState([]);
  const [alerts, setAlerts] = useState([]);
  const [selectedVenue, setSelectedVenue] = useState(null);

  useEffect(() => {
    const socket = new WebSocket("ws://localhost:8000/ws/dashboard/");

    socket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      if (data.sales) setSalesData(data.sales);
      if (data.top_items) setTopItems(data.top_items);
      if (data.alerts) setAlerts(data.alerts);
    };

    return () => socket.close();
  }, []);

  return (
    <div className="dashboard">
      <h1>Ops Dashboard</h1>
      <SalesSummary sales={salesData} onVenueClick={setSelectedVenue} />
      <TopItems items={topItems} />
      <AlertsPanel alerts={alerts} />
      {selectedVenue && (
        <VenueModal venue={selectedVenue} onClose={() => setSelectedVenue(null)} />
      )}
    </div>
  );
}

export default Dashboard;
