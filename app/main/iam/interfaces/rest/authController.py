from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.main.config.database import get_db
from app.main.iam.application.internal.commandservices.authCommandServiceImpl import AuthCommandServiceImpl

from app.main.iam.interfaces.rest.resources.signInResource import SignInResource
from app.main.iam.interfaces.rest.resources.signUpResource import SignUpResource
from app.main.iam.interfaces.rest.transform.signInCommandFromResourceAssembler import SignInCommandFromResourceAssembler
from app.main.iam.interfaces.rest.transform.signUpCommandFromResourceAssembler import SignUpCommandFromResourceAssembler

router = APIRouter(tags=["Auth"])

@router.post("/login")
def login(sign_in_resource: SignInResource, db: Session = Depends(get_db)):
    service = AuthCommandServiceImpl(db)
    command = SignInCommandFromResourceAssembler.to_command(sign_in_resource)
    try:
        token = service.login(command)
        return {
            "success": True,
            "message": "Inicio de sesión exitoso",
            "data": {
                "access_token": token,
                "token_type": "bearer"
            }
        }
    except HTTPException as e:
        raise e

@router.post("/register")
def register(sign_up_resource: SignUpResource, db: Session = Depends(get_db)):
    service = AuthCommandServiceImpl(db)
    username, email, password = SignUpCommandFromResourceAssembler.to_values(sign_up_resource)
    success = service.register(username, email, password)
    if not success:
        raise HTTPException(status_code=400, detail="El correo ya está registrado")
    return {
        "success": True,
        "message": "Usuario registrado correctamente"
    }
