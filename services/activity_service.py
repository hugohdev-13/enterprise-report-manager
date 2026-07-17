"""Business logic for activity logs."""

from models import Activity
from repositories.activity_repository import ActivityRepository


class ActivityService:

    @staticmethod
    def log(action, description, user):
        """Register a new activity."""

        activity = Activity(
            action=action,
            description=description,
            user=user,
        )

        return ActivityRepository.create(activity)

    @staticmethod
    def get_recent(limit=10):
        """Return recent activities."""

        return ActivityRepository.get_recent(limit)
    @staticmethod
    def get_notifications(limit=5):
        return ActivityRepository.get_recent(limit)      