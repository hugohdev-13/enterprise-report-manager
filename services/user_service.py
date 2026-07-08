from werkzeug.security import generate_password_hash, check_password_hash

from models import User
from repositories.user_repository import UserRepository


class UserService:

    @staticmethod
    def get_users():
        """Return all users."""
        return UserRepository.get_all()

    @staticmethod
    def get_user(user_id):
        """Return one user by ID."""
        return UserRepository.get(user_id)

    @staticmethod
    def total_users():
        """Return total users."""
        return UserRepository.count()

    @staticmethod
    def create_admin():
        """Create the default administrator if it doesn't exist."""

        if UserRepository.exists():
            return

        admin = User(
            first_name="Admin",
            last_name="System",
            email="admin@enterprise.com",
            password_hash=generate_password_hash("admin123"),
            role="Administrator"
        )

        UserRepository.create(admin)

        print("✔ Usuario administrador creado")

    @staticmethod
    def create_user(first_name, last_name, email, password, role):
        """Create a new user."""

        password_hash = generate_password_hash(password)

        user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password_hash=password_hash,
            role=role
        )

        UserRepository.create(user)

        return user

    @staticmethod
    def update_user(user_id, first_name, last_name, email, role):
        """Update user information."""

        user = UserRepository.get(user_id)

        if user is None:
            return None

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.role = role

        UserRepository.update()

        return user

    @staticmethod
    def delete_user(user_id):
        """Delete a user."""

        user = UserRepository.get(user_id)

        if user:
            UserRepository.delete(user)

    @staticmethod
    def authenticate(email: str, password: str):
        """Authenticate a user."""

        user = UserRepository.get_by_email(email)

        if user is None:
            return None

        if check_password_hash(user.password_hash, password):
            return user

        return None