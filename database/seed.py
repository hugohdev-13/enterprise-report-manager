"""Initial report data for local development."""

from services import ReportService


def seed():
    """Create the initial reports when the database is empty."""
    if ReportService.total_reports() == 0:
        reports = [
            ("Reporte Ventas", "Excel", "2026-07-07"),
            ("Reporte Clientes", "PDF", "2026-07-07"),
            ("Reporte Inventario", "CSV", "2026-07-07"),
        ]

        for name, report_format, created_at in reports:
            ReportService.create_report(name, report_format, created_at)

        print("Datos iniciales cargados.")
