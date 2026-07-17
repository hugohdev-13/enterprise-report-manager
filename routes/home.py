"""Dashboard routes."""

from datetime import datetime

from flask import Blueprint, render_template
from flask_login import login_required

from services.dashboard_service import DashboardService


home = Blueprint("home", __name__)


@home.route("/")
@login_required
def index():

    dashboard = DashboardService.get_dashboard()

    return render_template(
        "dashboard/index.html",
        dashboard=dashboard,
        today=datetime.now()
    )