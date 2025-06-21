from app.main.iam.interfaces.rest.resources.authenticatedUserResource import AuthenticatedUserResource
from app.main.iam.domain.model.aggregates.user import User

class AuthenticatedUserFromEntityAssembler:
    @staticmethod
    def from_user(user: User, token: str) -> AuthenticatedUserResource:
        return AuthenticatedUserResource(email=user.email, token=token)
