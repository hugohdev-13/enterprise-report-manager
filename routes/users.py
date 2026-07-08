from flask import Blueprint, render_template
from services.user_service import UserService
from flask import request, redirect, flash

users_bp = Blueprint(
    "users",
    __name__,
    url_prefix="/users"
)


@users_bp.route("/")
def index():

    users = UserService.get_users()

    return render_template(
        "users/index.html",
        users=users
    )

@users_bp.route("/create", methods=["GET", "POST"])
def create():

    if request.method == "POST":

        UserService.create_user(
            first_name=request.form["first_name"],
            last_name=request.form["last_name"],
            email=request.form["email"],
            password=request.form["password"],
            role=request.form["role"]
        )

        flash("Usuario creado correctamente.", "success")

        return redirect("/users")

    return render_template("users/create.html")