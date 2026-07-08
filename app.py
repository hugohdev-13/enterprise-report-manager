import os

from flask import Flask

from routes.home import home
from routes.reports import reports_bp

from database.db import db
from database.seed import seed

app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv(
    "SECRET_KEY",
    "development-secret-key",
)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///enterprise.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(home)
app.register_blueprint(reports_bp)

with app.app_context():
    db.create_all()
    seed()

if __name__ == "__main__":
    app.run(debug=True)
