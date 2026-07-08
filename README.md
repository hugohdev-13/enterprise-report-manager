# Enterprise Report Manager

Enterprise Report Manager is a Flask web application for organizing and
monitoring operational reports. It provides a responsive dashboard, report
metrics, format distribution charts, and a complete report management workflow.

## Features

- Search reports by name with live filtering.
- Combine search with Excel, PDF, and CSV filters.
- Sort by name, creation date, or format in either direction.
- Browse server-side paginated results (10 records per page).
- Create, edit, and safely delete reports with validation and feedback.
- View live SQLite metrics and Chart.js visualizations.
- Use a responsive Bootstrap 5 interface on desktop and mobile.

## Architecture

The project uses a layered Service + Repository architecture:

```text
Browser / Jinja2
       |
     Routes          HTTP input, redirects, flash messages
       |
    Services         Validation and business use cases
       |
  Repositories       SQLAlchemy queries and persistence
       |
 Models / SQLite     Data model and storage
```

Routes never query SQLAlchemy directly. Business rules are centralized in the
service layer, while database operations remain isolated in repositories.

## Screenshots

### Dashboard

The dashboard presents live totals for all reports and each supported format,
along with a Chart.js distribution chart and the most recent reports.

### Report management

The report directory combines search, format filters, sorting, pagination,
editing, and modal-based deletion in one responsive view.

> Screenshots should be captured from the local environment after startup so
> they reflect the current SQLite data and are not misleading static mockups.

## Technologies

- Python 3.12
- Flask 3
- Flask-SQLAlchemy 3
- SQLAlchemy 2
- SQLite
- Jinja2
- Bootstrap 5
- Bootstrap Icons
- Chart.js

## Installation

1. Clone the repository and open the project directory:

   ```powershell
   git clone <repository-url>
   cd enterprise-report-manager
   ```

2. Create and activate a virtual environment:

   ```powershell
   py -3.12 -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. Install dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

4. Define a secret key for the Flask session:

   ```powershell
   $env:SECRET_KEY = "replace-with-a-secure-random-value"
   ```

5. Start the application:

   ```powershell
   python app.py
   ```

6. Open `http://127.0.0.1:5000` in a browser.

SQLite tables and initial report data are created automatically on first run.

## Project structure

```text
enterprise-report-manager/
|-- app.py
|-- database/
|   |-- db.py
|   `-- seed.py
|-- models/
|   |-- __init__.py
|   `-- report.py
|-- repositories/
|   |-- __init__.py
|   `-- report_repository.py
|-- routes/
|   |-- home.py
|   `-- reports.py
|-- services/
|   |-- __init__.py
|   `-- report_service.py
|-- static/
|   `-- css/style.css
|-- templates/
|   |-- partials/
|   |   |-- navbar.html
|   |   `-- sidebar.html
|   |-- base.html
|   |-- dashboard.html
|   |-- report_form.html
|   `-- reports.html
|-- requirements.txt
`-- README.md
```

## Roadmap

- Add automated unit and integration test suites.
- Add CSRF protection and production-focused security headers.
- Introduce application configuration profiles and an application factory.
- Add authentication and role-based authorization.
- Add report export jobs and an audit trail.
- Add CI checks for formatting, linting, typing, and tests.

## License

See [LICENSE](LICENSE).
