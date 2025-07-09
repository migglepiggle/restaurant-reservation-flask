from app import create_app, db
from app.models import Reservation

app = create_app()

# Run database creation inside the app context
with app.app_context():
    db.create_all()
    print("✅ Database initialized successfully.")
