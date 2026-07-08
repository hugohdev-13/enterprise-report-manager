"""Business operations for reports."""

from models import Report
from repositories import ReportRepository


class ReportService:
    """Coordinate report use cases and persistence operations."""

    @staticmethod
    def get_reports():
        """Return all reports."""
        return ReportRepository.get_all()

    @staticmethod
    def get_report(report_id):
        """Return a report by identifier."""
        return ReportRepository.get_by_id(report_id)

    @staticmethod
    def create_report(name, format, created_at):
        """Create and persist a report."""
        report = Report(name=name, format=format, created_at=created_at)
        return ReportRepository.create(report)

    @staticmethod
    def update_report(report_id, name, format):
        """Update a report when it exists."""
        report = ReportRepository.get_by_id(report_id)
        if report is None:
            return None

        report.name = name
        report.format = format
        ReportRepository.update()
        return report

    @staticmethod
    def delete_report(report_id):
        """Delete a report when it exists."""
        report = ReportRepository.get_by_id(report_id)
        if report is None:
            return False

        ReportRepository.delete(report)
        return True

    @staticmethod
    def total_reports():
        """Return the total number of reports."""
        return ReportRepository.count()
