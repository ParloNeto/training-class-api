from api.models.user import User
from datetime import datetime

class UserService:

    @staticmethod
    def create_user(data):
        return User(**data).save()

    @staticmethod
    def list_users():
        return list(User.objects.all())