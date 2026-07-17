from flask import Blueprint, render_template
from flask_login import login_required

from services.activity_service import ActivityService
from utils.decorators import role_required

activity_bp = Blueprint(
    "activity",
    __name__,
    url_prefix="/activity"
)


@activity_bp.route("/")
@login_required
@role_required("Administrator")
def index():

    activities = ActivityService.get_recent(100)

    return render_template(
        "activity/index.html",
        activities=activities
    )