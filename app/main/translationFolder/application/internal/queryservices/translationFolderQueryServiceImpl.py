from typing import List, Optional
from app.main.translationFolder.domain.services.translationFolderQueryService import FolderQueryService
from app.main.translationFolder.domain.model.aggregates.translationFolder import TranslationFolder
from app.main.translationFolder.infrastructure.repositories.translationFolderRepository import TranslationFolderRepository

class TranslationFolderQueryServiceImpl(FolderQueryService):
    def __init__(self, repository: TranslationFolderRepository):
        self.repository = repository

    def get_all_folders(self) -> List[TranslationFolder]:
        return self.repository.get_all()

    def get_folder_by_id(self, folder_id: int) -> Optional[TranslationFolder]:
        return self.repository.get_by_id(folder_id)
