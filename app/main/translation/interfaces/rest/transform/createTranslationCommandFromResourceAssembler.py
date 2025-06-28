from app.main.translation.interfaces.rest.resources.createTranslationResource import CreateTranslationResource
from app.main.translation.domain.model.commands.createTranslationCommand import CreateTranslationCommand

class CreateTranslationCommandFromResourceAssembler:
    @staticmethod
    def to_command(resource: CreateTranslationResource) -> CreateTranslationCommand:
        return CreateTranslationCommand(
            text=resource.text,
            folder_id=resource.folder_id
        )
