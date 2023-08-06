# scheduler.py

import os
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from sqlalchemy.orm import Session
import services

def delete_old_notifications(db: Session):
    # Calculate the timestamp for 1 minute ago
    one_minute_ago = datetime.utcnow() - timedelta(minutes=.1)

    # Get notifications older than 1 minute
    old_notifications = services.get_old_notifications(db, one_minute_ago)

    # Delete the old notifications
    for notification in old_notifications:
        db.delete(notification)

if __name__ == "__main__":
    # Create and configure the scheduler
    scheduler = BackgroundScheduler(daemon=True)
    db_url = os.environ.get("sqlite:///../sqlite.db")  # Replace with your database URL
    scheduler.add_job(delete_old_notifications, 'interval', args=[services.get_db(db_url)], minutes=.1)

    # Start the scheduler
    scheduler.start()

    try:
        # Keep the main thread alive
        while True:
            pass
    except (KeyboardInterrupt, SystemExit):
        # Shut down the scheduler gracefully when exiting the program
        scheduler.shutdown()
