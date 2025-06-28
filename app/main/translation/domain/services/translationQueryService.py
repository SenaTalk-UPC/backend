# app/main/translation/domain/services/queryService/translationQueryService.py
from abc import ABC, abstractmethod
from typing import List
from app.main.translation.application.internal.dtos.translationDto import TranslationDTO

class TranslationQueryService(ABC):
    @abstractmethod
    def get_all(self) -> List[TranslationDTO]:
        pass

    @abstractmethod
    def get_by_translation_id(self, translation_id: int) -> TranslationDTO:
        pass

    @abstractmethod
    def get_by_folder_id(self, folder_id: int) -> List[TranslationDTO]:
        pass