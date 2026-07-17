"""Repository for activity logs."""

from database.db import db
from models import Activity


class ActivityRepository:

    @staticmethod
    def create(activity):
        """Save a new activity."""
        db.session.add(activity)
        db.session.commit()
        return activity

    @staticmethod
    def get_recent(limit=10):
        """Return the most recent activities."""
        return (
            Activity.query
            .order_by(Activity.created_at.desc())
            .limit(limit)
            .all()
        )