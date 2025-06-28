# app/main/translation/infrastructure/models/translationModel.py
from sqlalchemy import Column, ForeignKey, Integer, String
from app.main.config.database import Base

class TranslationModel(Base):
    __tablename__ = "translations"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    folder_id = Column(Integer, nullable=False)
