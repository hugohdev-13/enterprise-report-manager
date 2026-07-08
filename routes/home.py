"""Dashboard routes."""

from flask import Blueprint, render_template

from services import ReportService

home = Blueprint("home", __name__)


@home.route("/")
def index():
    """Render the dashboard with report summary data."""
    return render_template(
        "dashboard.html",
        reports=ReportService.get_recent_reports(),
        metrics=ReportService.get_dashboard_metrics(),
    )
