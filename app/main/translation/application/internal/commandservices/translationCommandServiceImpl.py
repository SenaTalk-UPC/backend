from app.main.translation.domain.model.commands.createTranslationCommand import CreateTranslationCommand
from app.main.translation.domain.services.translationCommandService import TranslationCommandService
from app.main.translation.infrastructure.repositories.translationRepository import TranslationRepository
from sqlalchemy.orm import Session
from app.main.translation.infrastructure.models.translationModel import TranslationModel

class TranslationCommandServiceImpl(TranslationCommandService):
    def __init__(self, repository: TranslationRepository):
        self.repo = repository

    def create_translation(self, command: CreateTranslationCommand):
        return self.repo.save(user_email=command.user_email, text=command.text)

    def delete_translation(self, translation_id: int):
        self.repo.delete(translation_id)

    def update_translation(self, translation_id: int, new_text: str) -> TranslationModel:
        return self.repo.update(translation_id, new_text)
