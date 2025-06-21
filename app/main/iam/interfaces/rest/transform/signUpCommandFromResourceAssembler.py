from app.main.iam.interfaces.rest.resources.signUpResource import SignUpResource

class SignUpCommandFromResourceAssembler:
    @staticmethod
    def to_values(resource: SignUpResource) -> tuple[str, str]:
        return resource.email, resource.password
