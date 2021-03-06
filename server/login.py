from flask_login import LoginManager
from .models import User

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.pk == user_id).first()


def register_login(app):
    login_manager.init_app(app)

