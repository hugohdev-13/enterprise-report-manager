"""Business operations for reports."""

from typing import Any

from models import Report
from repositories import ReportRepository


class ReportService:
    """Business logic for report management."""

    ALLOWED_FORMATS = ("Excel", "PDF", "CSV")
    ALLOWED_SORT_FIELDS = ("name", "created_at", "format")
    ALLOWED_DIRECTIONS = ("asc", "desc")
    REPORTS_PER_PAGE = 10

    @staticmethod
    def get_reports() -> list[Report]:
        """Return all reports."""
        return ReportRepository.get_all()

    @staticmethod
    def get_recent_reports(limit: int = 5) -> list[Report]:
        """Return the most recent reports."""
        return ReportRepository.get_recent(limit)

    @classmethod
    def get_paginated_reports(
        cls,
        search: str = "",
        report_format: str = "",
        sort_by: str = "created_at",
        direction: str = "desc",
        page: int = 1,
    ) -> Any:
        """Return paginated reports."""

        normalized_search = search.strip()

        normalized_format = (
            report_format
            if report_format in cls.ALLOWED_FORMATS
            else ""
        )

        normalized_sort = (
            sort_by
            if sort_by in cls.ALLOWED_SORT_FIELDS
            else "created_at"
        )

        normalized_direction = (
            direction
            if direction in cls.ALLOWED_DIRECTIONS
            else "desc"
        )

        return ReportRepository.get_paginated(
            search=normalized_search,
            report_format=normalized_format,
            sort_by=normalized_sort,
            direction=normalized_direction,
            page=max(page, 1),
            per_page=cls.REPORTS_PER_PAGE,
        )

    @staticmethod
    def get_report(report_id: int) -> Report | None:
        """Return a report by id."""
        return ReportRepository.get_by_id(report_id)

    @classmethod
    def create_report(
        cls,
        name: str,
        report_format: str,
        created_at: str,
    ) -> Report:
        """Create a report."""

        normalized_name, normalized_format = cls._validate_report(
            name,
            report_format,
        )

        report = Report(
            name=normalized_name,
            format=normalized_format,
            created_at=created_at,
        )

        return ReportRepository.create(report)

    @classmethod
    def update_report(
        cls,
        report_id: int,
        name: str,
        report_format: str,
    ) -> Report | None:
        """Update a report."""

        normalized_name, normalized_format = cls._validate_report(
            name,
            report_format,
        )

        report = ReportRepository.get_by_id(report_id)

        if report is None:
            return None

        report.name = normalized_name
        report.format = normalized_format

        ReportRepository.update()

        return report

    @staticmethod
    def delete_report(report_id: int) -> bool:
        """Delete a report."""

        report = ReportRepository.get_by_id(report_id)

        if report is None:
            return False

        ReportRepository.delete(report)

        return True

    @staticmethod
    def total_reports() -> int:
        """Return total reports."""
        return ReportRepository.count()

    @classmethod
    def get_dashboard_metrics(cls) -> dict[str, Any]:
        """Return dashboard metrics."""

        totals = ReportRepository.count_by_format()

        return {
            "total_reports": ReportRepository.count(),

            "excel_reports": totals.get("Excel", 0),

            "pdf_reports": totals.get("PDF", 0),

            "csv_reports": totals.get("CSV", 0),

            "chart_labels": [
                "Excel",
                "PDF",
                "CSV",
            ],

            "chart_values": [
                totals.get("Excel", 0),
                totals.get("PDF", 0),
                totals.get("CSV", 0),
            ],
        }

    @classmethod
    def _validate_report(
        cls,
        name: str,
        report_format: str,
    ) -> tuple[str, str]:
        """Validate report information."""

        normalized_name = name.strip()

        if not normalized_name:
            raise ValueError("El nombre del reporte es obligatorio.")

        if len(normalized_name) > 100:
            raise ValueError(
                "El nombre del reporte no puede exceder los 100 caracteres."
            )

        if report_format not in cls.ALLOWED_FORMATS:
            raise ValueError(
                "Selecciona un formato válido."
            )

        return normalized_name, report_format