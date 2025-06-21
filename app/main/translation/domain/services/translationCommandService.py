from abc import ABC, abstractmethod
from app.main.translation.infrastructure.models.translationModel import TranslationModel

class TranslationCommandService(ABC):
    @abstractmethod
    def create_translation(self, user_email: str, text: str) -> TranslationModel:
        pass

    @abstractmethod
    def delete_translation(self, translation_id: int):
        pass

    @abstractmethod
    def update_translation(self, translation_id: int, new_text: str) -> TranslationModel:
        pass
