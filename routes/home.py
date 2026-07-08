"""Dashboard routes."""

from flask import Blueprint, render_template

from services import ReportService

home = Blueprint("home", __name__)


@home.route("/")
def index():
    """Render the dashboard with report summary data."""
    reports = ReportService.get_reports()

    return render_template(
        "dashboard.html",
        reports=reports,
        total_reports=ReportService.total_reports(),
    )
