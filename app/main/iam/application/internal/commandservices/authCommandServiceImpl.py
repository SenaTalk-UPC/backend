from fastapi import HTTPException
from app.main.iam.application.internal.dtos.loginDto import LoginDTO
from app.main.iam.domain.services.authService import AuthService
from app.main.iam.domain.model.aggregates.user import User
from app.main.iam.infrastructure.models.userModel import UserModel
from app.main.iam.infrastructure.security.security import create_access_token
from app.main.translationFolder.infrastructure.repositories.translationFolderRepository import TranslationFolderRepository

class AuthCommandServiceImpl:
    def __init__(self, db):
        self.db = db
        self.auth_service = AuthService(db)

    def register(self, username: str, email: str, password: str) -> bool:
        user = User(id=0, username=username, email=email, password=password)
        return self.auth_service.register(user)

    def login(self, dto: LoginDTO) -> str:
        user = self.auth_service.authenticate(dto.email, dto.password)
        if not user:
            raise HTTPException(status_code=401, detail="Correo o contraseña inválidos")
        token = create_access_token(data={"sub": str(user.id)})
        return token
