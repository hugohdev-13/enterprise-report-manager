"""Authentication routes."""

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    flash,
    url_for
)

from flask_login import (
    login_user,
    logout_user,
    current_user,
    login_required
)

from services.user_service import UserService
from services.activity_service import ActivityService


auth_bp = Blueprint(
    "auth",
    __name__
)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:
        return redirect(url_for("home.index"))

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = UserService.authenticate(email, password)

        if user:

            login_user(user)

            ActivityService.log(
                action="LOGIN",
                description="Inicio de sesión exitoso",
                user=f"{user.first_name} {user.last_name}"
            )

            flash(
                "Bienvenido al sistema.",
                "success"
            )

            return redirect(url_for("home.index"))

        flash(
            "Correo o contraseña incorrectos.",
            "danger"
        )

    return render_template("auth/login.html")


@auth_bp.route("/logout")
@login_required
def logout():

    ActivityService.log(
        action="LOGOUT",
        description="Cierre de sesión",
        user=f"{current_user.first_name} {current_user.last_name}"
    )

    logout_user()

    flash(
        "Sesión cerrada correctamente.",
        "info"
    )

    return redirect(url_for("auth.login"))