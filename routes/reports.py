"""Report management routes."""

from datetime import date

from flask import Blueprint, redirect, render_template, request

from services import ReportService

reports_bp = Blueprint(
    "reports",
    __name__,
    url_prefix="/reports",
)


# Mostrar todos los reportes
@reports_bp.route("/")
def list_reports():
    """Render the report list."""
    reports = ReportService.get_reports()

    return render_template(
        "reports.html",
        reports=reports,
    )


# Crear un nuevo reporte
@reports_bp.route("/new", methods=["GET", "POST"])
def new_report():
    """Render the form or create a report from submitted data."""
    if request.method == "POST":
        ReportService.create_report(
            request.form["name"],
            request.form["format"],
            str(date.today()),
        )
        return redirect("/reports")

    return render_template("report_form.html")
