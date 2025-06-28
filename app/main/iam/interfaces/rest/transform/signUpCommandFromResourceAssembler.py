from app.main.iam.interfaces.rest.resources.signUpResource import SignUpResource

class SignUpCommandFromResourceAssembler:
    @staticmethod
    def to_values(resource: SignUpResource) -> tuple[str, str, str]:
        return resource.username, resource.email, resource.password
