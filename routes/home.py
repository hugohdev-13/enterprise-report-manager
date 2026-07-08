"""Dashboard routes."""

from flask import Blueprint, render_template
from flask_login import login_required

from services import ReportService

home = Blueprint("home", __name__)


@home.route("/")
@login_required
def index():

    reports = ReportService.get_reports()

    metrics = ReportService.get_dashboard_metrics()

    return render_template(
        "dashboard.html",
        reports=reports,
        metrics=metrics
    )