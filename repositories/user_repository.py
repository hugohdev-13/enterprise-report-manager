from models import User
from database.db import db


class UserRepository:
    """Repository layer for User model."""

    @staticmethod
    def get_all():
        """Return all users."""
        return User.query.order_by(User.first_name.asc()).all()

    @staticmethod
    def get(user_id):
        """Return a user by ID."""
        return User.query.get(user_id)

    @staticmethod
    def get_by_email(email):
        """Return a user by email."""
        return User.query.filter_by(email=email).first()

    @staticmethod
    def create(user):
        """Create a new user."""
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def update():
        """Save changes."""
        db.session.commit()

    @staticmethod
    def delete(user):
        """Delete a user."""
        db.session.delete(user)
        db.session.commit()

    @staticmethod
    def exists():
        """Check if there are users."""
        return User.query.count() > 0

    @staticmethod
    def count():
        """Return total users."""
        return User.query.count()