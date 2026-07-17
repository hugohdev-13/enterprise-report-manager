from flask import Blueprint, render_template
from models import user
from services.user_service import UserService
from services.activity_service import ActivityService
from flask import request, redirect, flash
from flask_login import (
    login_required,
    current_user
)
from utils.decorators import role_required


users_bp = Blueprint(
    "users",
    __name__,
    url_prefix="/users"
)


@users_bp.route("/")
@login_required
@role_required("Administrator")
def index():

    users = UserService.get_users()

    return render_template(
        "users/index.html",
        users=users
    )

@users_bp.route("/create", methods=["GET", "POST"])
@login_required
@role_required("Administrator")

def create():

    if request.method == "POST":
        new_user = UserService.create_user(
            first_name=request.form["first_name"],
            last_name=request.form["last_name"],
            email=request.form["email"],
            password=request.form["password"],
            role=request.form["role"]
        )

        ActivityService.log(
            action="CREATE_USER",
            description=f"Se creó el usuario {new_user.first_name} {new_user.last_name}",
            user=f"{current_user.first_name} {current_user.last_name}"
        )

        flash("Usuario creado correctamente.", "success")

        return redirect("/users")

    return render_template("users/create.html")
@users_bp.route("/edit/<int:user_id>", methods=["GET", "POST"])
@login_required
@role_required("Administrator")
def edit(user_id):

    user = UserService.get_user(user_id)

    if user is None:
        flash("Usuario no encontrado.", "danger")
        return redirect("/users")

    if request.method == "POST":

        ActivityService.log(
            action="UPDATE_USER",
            description=f"Se actualizó el usuario {user.first_name} {user.last_name}",
            user=current_user.email
        )
        return redirect("/users")

    return render_template(
        "users/edit.html",
        user=user
    )
@users_bp.route("/deactivate/<int:user_id>")
@login_required
@role_required("Administrator")
def deactivate(user_id):

    UserService.deactivate_user(user_id)
    user = UserService.get_user(user_id)

    if user:

        ActivityService.log(
            action="DEACTIVATE_USER",
            description=f"Se desactivó el usuario {user.first_name} {user.last_name}",
            user=current_user.email
        )
    return redirect("/users")

@users_bp.route("/activate/<int:user_id>")
@login_required
@role_required("Administrator")
def activate(user_id):

    UserService.activate_user(user_id)
    user = UserService.get_user(user_id)

    if user:

        ActivityService.log(
            action="ACTIVATE_USER",
            description=f"Se activó el usuario {user.first_name} {user.last_name}",
            user=current_user.email
        )
    return redirect("/users")