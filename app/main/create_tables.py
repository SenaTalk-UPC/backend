import sys
import os

# Agrega la raíz del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from app.main.config.database import Base, engine
from app.main.iam.infrastructure.models.userModel import UserModel
from app.main.translation.infrastructure.models.translationModel import TranslationModel
from app.main.translationFolder.infrastructure.models.translationFolderModel import TranslationFolderModel

Base.metadata.create_all(bind=engine)

print("Tablas creadas (si no existían)")