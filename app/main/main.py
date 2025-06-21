from fastapi import FastAPI
from app.main.translation.interfaces.rest.translationController import router as translation_router
from app.main.iam.interfaces.rest.authController import router as auth_router

app = FastAPI(title="Translation API (DDD Example)")

app.include_router(translation_router, prefix="/translation")
app.include_router(auth_router, prefix="/auth")
