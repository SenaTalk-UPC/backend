from typing import List
from app.main.translationFolder.domain.services.translationFolderCommandService import TranslationFolderCommandService
from app.main.translationFolder.domain.model.aggregates.translationFolder import TranslationFolder
from app.main.translationFolder.infrastructure.repositories.translationFolderRepository import TranslationFolderRepository
from app.main.translationFolder.domain.model.commands.createTranslationFolderCommand import CreateTranslationFolderCommand
from app.main.translationFolder.domain.model.commands.updateTranslationCommand import UpdateTranslationFolderCommand

class TranslationFolderCommandServiceImpl(TranslationFolderCommandService):
    def __init__(self, repo: TranslationFolderRepository):
        self.repo = repo

    def create_folder(self, command: CreateTranslationFolderCommand) -> TranslationFolder:
        folder = TranslationFolder(
            id=None,
            name=command.name,
            description=command.description,
            userId=command.userId
        )
        return self.repo.save(folder)

    def update_folder(self, folder_id: int, command: UpdateTranslationFolderCommand) -> TranslationFolder:
        return self.repo.update(folder_id, command.name)

    def delete_folder(self, folder_id: int) -> bool:
        return self.repo.delete(folder_id)

