from app.main.translation.interfaces.rest.resources.createTranslationResource import CreateTranslationResource
from app.main.translation.domain.model.commands.createTranslationCommand import CreateTranslationCommand

class CreateTranslationCommandFromResourceAssembler:
    @staticmethod
    def to_command(resource: CreateTranslationResource) -> CreateTranslationCommand:
        return CreateTranslationCommand(
            user_email=resource.user_email,
            text=resource.text
        )
