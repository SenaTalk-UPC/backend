from fastapi import HTTPException
from app.main.iam.application.internal.dtos.loginDto import LoginDTO
from app.main.iam.domain.services.authService import AuthService
from app.main.iam.domain.model.aggregates.user import User
from app.main.iam.infrastructure.security.security import create_access_token

class AuthCommandServiceImpl:
    def __init__(self, db):
        self.auth_service = AuthService(db)

    def register(self, email: str, password: str) -> bool:
        user = User(email=email, password=password)
        return self.auth_service.register(user)

    def login(self, dto: LoginDTO) -> str:
        user = self.auth_service.authenticate(dto.email, dto.password)
        if not user:
            raise HTTPException(status_code=401, detail="Correo o contraseña inválidos")
        token = create_access_token(data={"sub": user.email})
        return token
