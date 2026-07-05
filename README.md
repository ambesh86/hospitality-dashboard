# Hospitality Dashboard
##Please follow the below steps for set up and configuration
## Setup

### Backend
1. `cd backend`
2. `pip install -r requirements.txt`
3. Configure PostgreSQL in `settings.py`
4. `python manage.py migrate`
5. `python manage.py runserver`

### Frontend
1. `cd frontend`
2. `npm install`
3. `npm start`

## Design Decisions
- **PostgreSQL**: relational, scalable, JSON support for items.
- **Django Channels**: real-time WebSocket updates.
- **React SPA**: single dashboard view, live updates.

## Trade-offs
- Focused on real-time aggregation, not UI polish.
- Alerts are simple thresholds; could evolve into predictive analytics.

## Next Steps
- Add inventory alerts.
- Deploy with Docker.
- Improve anomaly detection with ML.
