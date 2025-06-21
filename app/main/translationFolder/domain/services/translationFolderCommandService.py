from abc import ABC, abstractmethod
from app.main.translationFolder.domain.model.commands.createTranslationFolderCommand import CreateTranslationFolderCommand
from app.main.translationFolder.domain.model.commands.updateTranslationCommand import UpdateTranslationFolderCommand
from app.main.translationFolder.domain.model.aggregates.translationFolder import TranslationFolder

class TranslationFolderCommandService(ABC):

    @abstractmethod
    def create_folder(self, command: CreateTranslationFolderCommand) -> TranslationFolder:
        pass

    @abstractmethod
    def update_folder(self, command: UpdateTranslationFolderCommand) -> TranslationFolder:
        pass

    @abstractmethod
    def delete_folder(self, folder_id: int) -> None:
        pass
