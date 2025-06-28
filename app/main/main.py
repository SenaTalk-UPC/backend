from fastapi import FastAPI
from app.main.translation.interfaces.rest.translationController import router as translation_router
from app.main.iam.interfaces.rest.authController import router as auth_router
from app.main.translationFolder.interfaces.rest.translationFolderController import router as translation_folder_router
from app.main.recognition.interfaces.rest.recognitionController import router as recognition_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Translation API (DDD Example)")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(translation_router, prefix="/translation")
app.include_router(auth_router, prefix="/auth")
app.include_router(translation_folder_router, prefix="/folder")
app.include_router(recognition_router, prefix="/recognition")


