"""Persistence operations for reports."""

from database.db import db
from models import Report


class ReportRepository:
    """Provide a single access point for report persistence."""

    @staticmethod
    def get_all():
        """Return all reports."""
        return Report.query.all()

    @staticmethod
    def get_by_id(report_id):
        """Return a report by identifier, or ``None`` when not found."""
        return db.session.get(Report, report_id)

    @staticmethod
    def create(report):
        """Persist a new report and return it."""
        db.session.add(report)
        db.session.commit()
        return report

    @staticmethod
    def update():
        """Commit changes made to persisted reports."""
        db.session.commit()

    @staticmethod
    def delete(report):
        """Delete a report from persistence."""
        db.session.delete(report)
        db.session.commit()

    @staticmethod
    def count():
        """Return the number of persisted reports."""
        return Report.query.count()
