from datetime import datetime

from database.db import db


class Activity(db.Model):
    """Activity log model."""

    __tablename__ = "activities"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    action = db.Column(
        db.String(100),
        nullable=False
    )

    description = db.Column(
        db.String(255),
        nullable=False
    )

    user = db.Column(
        db.String(120),
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    def __repr__(self):

        return f"<Activity {self.action}>"