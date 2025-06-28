from sqlalchemy.orm import Session
from app.main.translation.application.internal.dtos.translationDto import TranslationDTO
from app.main.translation.infrastructure.models.translationModel import TranslationModel
from typing import List, Optional
from datetime import datetime

class TranslationRepository:
    def __init__(self, db: Session):
        self.db = db

    def save(self, text: str, folder_id: str):
        translation = TranslationModel(text=text, folder_id=folder_id)
        self.db.add(translation)
        self.db.commit()
        self.db.refresh(translation)
        return translation

    def get_all(self):
        return self.db.query(TranslationModel).all()

    def get_by_id(self, translation_id: int):
        return self.db.query(TranslationModel).filter(TranslationModel.id == translation_id).first()
    
    def delete(self, translation_id: int):
        obj = self.db.query(TranslationModel).filter(TranslationModel.id == translation_id).first()
        if obj:
            self.db.delete(obj)
            self.db.commit()

    def update(self, translation_id: int, new_text: str):
        translation = self.db.query(TranslationModel).filter_by(id=translation_id).first()
        if not translation:
            return None
        translation.text = new_text
        self.db.commit()
        self.db.refresh(translation)
        return translation
    
    def get_by_folder_id(self, folder_id: int) -> List[TranslationDTO]:
        records = self.db.query(TranslationModel).filter_by(folder_id=folder_id).all()
        return records