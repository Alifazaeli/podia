__author__ = 'ali'

from project.factory import login_manager
from project.models.user import get_user

@login_manager.user_loader
def load_user(user_id):
    return get_user(user_id)