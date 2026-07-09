from flask_login import logout_user
from flask_login import login_required



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
    current_user
)

from services.user_service import UserService

auth_bp = Blueprint(
    "auth",
    __name__
)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    # Si el usuario ya inició sesión
    if current_user.is_authenticated:
        return redirect(url_for("home.index"))

    if request.method == "POST":

        email = request.form["email"]

        password = request.form["password"]

        user = UserService.authenticate(email, password)

        if user:

            login_user(user)

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

    logout_user()

    flash(
        "Has cerrado sesión correctamente.",
        "success"
    )

    return redirect(url_for("auth.login"))