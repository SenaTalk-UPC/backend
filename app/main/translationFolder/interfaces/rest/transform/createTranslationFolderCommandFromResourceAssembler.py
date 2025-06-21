from app.main.translationFolder.domain.model.commands.createTranslationFolderCommand import CreateTranslationFolderCommand
from app.main.translationFolder.domain.model.commands.updateTranslationCommand import UpdateTranslationFolderCommand
from app.main.translationFolder.interfaces.rest.resource.createTranslationFolderResource import CreateTranslationFolderResource
from app.main.translationFolder.interfaces.rest.resource.updateTranslationFolderResource import UpdateTranslationFolderResource

class CreateTranslationFolderCommandFromResourceAssembler:

    @staticmethod
    def to_command(resource: CreateTranslationFolderResource) -> CreateTranslationFolderCommand:
        return CreateTranslationFolderCommand(
            name=resource.name,
            description=resource.description,
            translation_ids=resource.translation_ids
        )
    
    @staticmethod
    def to_update_command(folder_id: int, resource: UpdateTranslationFolderResource) -> UpdateTranslationFolderCommand:
        return UpdateTranslationFolderCommand(
            folder_id=folder_id,
            name=resource.name,
            description=resource.description,
            translation_ids=resource.translation_ids
        )
