"""Business operations for dashboard."""

from services.user_service import UserService
from services.report_service import ReportService
from services.activity_service import ActivityService


class DashboardService:
    """Collect dashboard information."""

    @staticmethod
    def get_dashboard():

        report_metrics = ReportService.get_dashboard_metrics()

        return {

            "total_users": UserService.total_users(),

            "total_reports": report_metrics["total_reports"],

            "excel_reports": report_metrics["excel_reports"],

            "pdf_reports": report_metrics["pdf_reports"],

            "csv_reports": report_metrics["csv_reports"],

            "chart_labels": report_metrics["chart_labels"],

            "chart_values": report_metrics["chart_values"],

            "recent_reports": ReportService.get_recent_reports(),

            "recent_activities": ActivityService.get_recent(8)

        }