import os

from flask import Flask
from flask_login import LoginManager

# Database
from database.db import db
from database.seed import seed

# Models
from models import User

# Routes
from routes.auth import auth_bp
from routes.home import home
from routes.reports import reports_bp
from routes.users import users_bp

# Services
from services.user_service import UserService


app = Flask(__name__)

# ==========================================
# CONFIGURATION
# ==========================================

app.config["SECRET_KEY"] = os.getenv(
    "SECRET_KEY",
    "development-secret-key"
)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///enterprise.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# ==========================================
# DATABASE
# ==========================================

db.init_app(app)

# ==========================================
# LOGIN MANAGER
# ==========================================

login_manager = LoginManager()

login_manager.init_app(app)

login_manager.login_view = "auth.login"

login_manager.login_message = "Debes iniciar sesión para acceder."

login_manager.login_message_category = "warning"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# ==========================================
# BLUEPRINTS
# ==========================================

app.register_blueprint(auth_bp)

app.register_blueprint(home)

app.register_blueprint(reports_bp)

app.register_blueprint(users_bp)

# ==========================================
# DATABASE INITIALIZATION
# ==========================================

with app.app_context():

    db.create_all()

    seed()

    UserService.create_admin()

# ==========================================
# START APPLICATION
# ==========================================

if __name__ == "__main__":

    app.run(debug=True)