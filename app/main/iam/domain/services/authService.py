import bcrypt
from sqlalchemy.orm import Session
from app.main.iam.infrastructure.repositories.userRepository import UserRepository
from app.main.iam.domain.model.aggregates.user import User

class AuthService:
    def __init__(self, db: Session):
        self.repo = UserRepository(db)

    def authenticate(self, email: str, password: str) -> User | None:
        user = self.repo.get_by_email(email)
        if not user:
            return None
        if not bcrypt.checkpw(password.encode(), user.password.encode()):
            return None
        return user

    def register(self, user: User) -> bool:
        if self.repo.get_by_email(user.email):
            return False
        hashed_pw = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt()).decode()
        self.repo.create_user(email=user.email, hashed_password=hashed_pw)
        return True
