from app.main.iam.application.internal.dtos.loginDto import LoginDTO
from app.main.iam.interfaces.rest.resources.signInResource import SignInResource

class SignInCommandFromResourceAssembler:
    @staticmethod
    def to_command(resource: SignInResource) -> LoginDTO:
        return LoginDTO(email=resource.email, password=resource.password)
