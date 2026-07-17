"""Report management routes."""

from datetime import date

from flask import Blueprint, flash, redirect, render_template, request, url_for

from services import ReportService
from flask_login import login_required, current_user
from services.activity_service import ActivityService

reports_bp = Blueprint(
    "reports",
    __name__,
    url_prefix="/reports",
)


@reports_bp.route("/")
def list_reports():
    """Render a searchable, filtered and paginated report list."""
    search = request.args.get("search", "")
    report_format = request.args.get("format", "")
    sort_by = request.args.get("sort_by", "created_at")
    direction = request.args.get("direction", "desc")
    page = request.args.get("page", 1, type=int)

    pagination = ReportService.get_paginated_reports(
        search=search,
        report_format=report_format,
        sort_by=sort_by,
        direction=direction,
        page=page,
    )

    return render_template(
        "reports.html",
        reports=pagination.items,
        pagination=pagination,
        search=search,
        selected_format=report_format,
        sort_by=sort_by,
        direction=direction,
        formats=ReportService.ALLOWED_FORMATS,
    )


@reports_bp.route("/new", methods=["GET", "POST"])
def new_report():
    """Render the form or create a report from submitted data."""
    form_data = {"name": "", "format": "Excel"}

    if request.method == "POST":
        form_data = request.form.to_dict()
        try:
            report = ReportService.create_report(
                request.form.get("name", ""),
                request.form.get("format", ""),
                str(date.today()),
            )

            ActivityService.log(
                action="CREATE_REPORT",
                description=f"Se creó el reporte '{report.name}'",
                user=current_user.email
            )
        except ValueError as error:
            flash(str(error), "danger")
            return render_template(
                "report_form.html",
                form_data=form_data,
                formats=ReportService.ALLOWED_FORMATS,
                form_title="New Report",
                submit_label="Create report",
            ), 400

        flash("Report created successfully", "success")
        return redirect(url_for("reports.list_reports"))

    return render_template(
        "report_form.html",
        form_data=form_data,
        formats=ReportService.ALLOWED_FORMATS,
        form_title="New Report",
        submit_label="Create report",
    )


@reports_bp.route("/<int:report_id>/edit", methods=["GET", "POST"])
def edit_report(report_id: int):
    """Render the edit form or update an existing report."""
    report = ReportService.get_report(report_id)
    if report is None:
        flash("Report not found", "warning")
        return redirect(url_for("reports.list_reports"))

    form_data = {"name": report.name, "format": report.format}
    if request.method == "POST":
        form_data = request.form.to_dict()
        try:
            report = ReportService.update_report(
            report_id,
            request.form.get("name", ""),
            request.form.get("format", ""),
        )

            ActivityService.log(
            action="UPDATE_REPORT",
            description=f"Se actualizó el reporte '{report.name}'",
            user=current_user.email
        )
        except ValueError as error:
            flash(str(error), "danger")
            return render_template(
                "report_form.html",
                form_data=form_data,
                formats=ReportService.ALLOWED_FORMATS,
                form_title="Edit Report",
                submit_label="Save changes",
            ), 400

        flash("Report updated successfully", "success")
        return redirect(url_for("reports.list_reports"))

    return render_template(
        "report_form.html",
        form_data=form_data,
        formats=ReportService.ALLOWED_FORMATS,
        form_title="Edit Report",
        submit_label="Save changes",
    )


@reports_bp.route("/<int:report_id>/delete", methods=["POST"])
@login_required
def delete_report(report_id):

    report = ReportService.get_report(report_id)

    if report is None:

        flash("Reporte no encontrado.", "warning")

        return redirect(url_for("reports.list_reports"))

    ActivityService.log(
        action="DELETE_REPORT",
        description=f"Se eliminó el reporte '{report.name}'",
        user=current_user.email
    )

    ReportService.delete_report(report_id)

    flash(
        "Reporte eliminado correctamente.",
        "success"
    )

    return redirect(url_for("reports.list_reports"))