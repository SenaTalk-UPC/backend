# app/main/translation/infrastructure/models/translationModel.py
from sqlalchemy import Column, Integer, String
from app.main.config.database import Base

class TranslationModel(Base):
    __tablename__ = "translations"

    id = Column(Integer, primary_key=True, index=True)
    user_email = Column(String, nullable=False)
    text = Column(String, nullable=False)
