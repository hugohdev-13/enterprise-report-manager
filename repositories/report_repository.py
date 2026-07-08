"""Persistence operations for reports."""

from typing import Any

from sqlalchemy import func

from database.db import db
from models import Report


class ReportRepository:
    """Provide a single access point for report persistence."""

    _SORT_COLUMNS = {
        "name": Report.name,
        "created_at": Report.created_at,
        "format": Report.format,
    }

    @staticmethod
    def get_all() -> list[Report]:
        """Return all reports ordered by newest identifier first."""
        return Report.query.order_by(Report.id.desc()).all()

    @staticmethod
    def get_recent(limit: int = 5) -> list[Report]:
        """Return a limited collection of the newest reports."""
        return Report.query.order_by(Report.id.desc()).limit(limit).all()

    @staticmethod
    def get_paginated(
        search: str,
        report_format: str,
        sort_by: str,
        direction: str,
        page: int,
        per_page: int,
    ) -> Any:
        """Return a filtered, sorted and paginated report collection."""
        query = Report.query

        if search:
            query = query.filter(Report.name.ilike(f"%{search}%"))

        if report_format:
            query = query.filter(Report.format == report_format)

        sort_column = ReportRepository._SORT_COLUMNS.get(
            sort_by,
            Report.created_at,
        )
        order_expression = (
            sort_column.asc() if direction == "asc" else sort_column.desc()
        )

        return query.order_by(order_expression, Report.id.desc()).paginate(
            page=page,
            per_page=per_page,
            error_out=False,
        )

    @staticmethod
    def get_by_id(report_id: int) -> Report | None:
        """Return a report by identifier, or ``None`` when not found."""
        return db.session.get(Report, report_id)

    @staticmethod
    def create(report: Report) -> Report:
        """Persist a new report and return it."""
        db.session.add(report)
        db.session.commit()
        return report

    @staticmethod
    def update() -> None:
        """Commit changes made to persisted reports."""
        db.session.commit()

    @staticmethod
    def delete(report: Report) -> None:
        """Delete a report from persistence."""
        db.session.delete(report)
        db.session.commit()

    @staticmethod
    def count() -> int:
        """Return the number of persisted reports."""
        return Report.query.count()

    @staticmethod
    def count_by_format() -> dict[str, int]:
        """Return report totals grouped by format."""
        rows = (
            db.session.query(Report.format, func.count(Report.id))
            .group_by(Report.format)
            .all()
        )
        return {report_format: total for report_format, total in rows}
