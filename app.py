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
# Activity Activity 
from routes.activity import activity_bp

from datetime import datetime
from services.activity_service import ActivityService
from routes.profile import profile_bp
from flask import render_template




app = Flask(__name__)

# ==========================================
# CONFIGURATION
# ==========================================

@app.context_processor
def inject_globals():

    return {

        "today": datetime.now(),

        "notifications": ActivityService.get_notifications(5)

    }
@app.context_processor
def inject_globals():

    return {
        "today": datetime.now()
    }

app.register_blueprint(activity_bp)
app.config["SECRET_KEY"] = os.getenv(
    "SECRET_KEY",
    "development-secret-key"
)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///enterprise.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
@app.errorhandler(403)
def forbidden(error):

    return render_template(
        "errors/403.html"
    ), 403


@app.errorhandler(404)
def not_found(error):

    return render_template(
        "errors/404.html"
    ), 404


@app.errorhandler(500)
def internal_error(error):

    return render_template(
        "errors/500.html"
    ), 500
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
app.register_blueprint(profile_bp)



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