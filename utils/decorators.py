from functools import wraps

from flask import flash
from flask import redirect
from flask import url_for

from flask_login import current_user


def role_required(*roles):

    def decorator(view):

        @wraps(view)

        def wrapped(*args, **kwargs):

            if current_user.role not in roles:

                flash(
                    "No tienes permisos.",
                    "danger"
                )

                return redirect(
                    url_for("home.index")
                )

            return view(*args, **kwargs)

        return wrapped

    return decorator