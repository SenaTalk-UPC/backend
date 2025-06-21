from abc import ABC, abstractmethod
from typing import List, Optional
from app.main.translationFolder.domain.model.aggregates.translationFolder import TranslationFolder

class FolderQueryService(ABC):

    @abstractmethod
    def get_all_folders(self) -> List[TranslationFolder]:
        pass

    @abstractmethod
    def get_folder_by_id(self, folder_id: int) -> Optional[TranslationFolder]:
        pass
