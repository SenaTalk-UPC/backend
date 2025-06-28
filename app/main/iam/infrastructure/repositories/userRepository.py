from app.main.iam.infrastructure.models.userModel import UserModel

class UserRepository:
    def __init__(self, db):
        self.db = db

    def get_by_email(self, email: str) -> UserModel | None:
        return self.db.query(UserModel).filter(UserModel.email == email).first()

    def create_user(self, username: str, email: str, hashed_password: str) -> UserModel:
        user = UserModel(username=username,email=email, password=hashed_password)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
