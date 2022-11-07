from app.models.user import User
from lib.errors.bad_request import BadRequest


class UserService:
    @classmethod    
    def create(self, data):
        if data["password"] != data["check_password"]:
            raise BadRequest()

        user = User(
                        name=data["name"],
                        email=data["email"],
                        password=data["password"],
                    )
        user.to_hash_password()

        user.full_clean()
        user.save()
        return user
