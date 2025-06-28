from app.main.recognition.interfaces.rest.resource.recognitionResource import RecognitionResource

class RecognitionCommandFromResourceAssembler:
    @staticmethod
    def to_base64(resource: RecognitionResource) -> str:
        return resource.image_base64
