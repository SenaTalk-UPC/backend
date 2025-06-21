# app/main/translation/application/internal/queryservices/translationQueryServiceImpl.py
from sqlalchemy.orm import Session
from app.main.translation.domain.services.translationQueryService import TranslationQueryService
from app.main.translation.application.internal.dtos.translationDto import TranslationDTO
from app.main.translation.infrastructure.repositories.translationRepository import TranslationRepository

class TranslationQueryServiceImpl(TranslationQueryService):
    def __init__(self, db: Session):
        self.repo = TranslationRepository(db)

    def get_all(self):
        translations = self.repo.get_all()
        return [TranslationDTO(id=t.id, user_email=t.user_email, text=t.text) for t in translations]

    def get_by_translation_id(self, translation_id: int):
        t = self.repo.get_by_id(translation_id)
        if not t:
            return None
        return TranslationDTO(id=t.id, user_email=t.user_email, text=t.text)
