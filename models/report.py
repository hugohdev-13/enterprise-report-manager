"""Database model for enterprise reports."""

from database.db import db


class Report(db.Model):
    """Represent a report stored by the application."""

    __tablename__ = "reports"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    format = db.Column(db.String(20))
    created_at = db.Column(db.String(20))
