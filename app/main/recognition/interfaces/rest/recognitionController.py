from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from app.main.config.database import get_db

from app.main.recognition.infrastructure.model.recognitionModelLoader import RecognitionModelLoader
from app.main.recognition.application.internal.commandservices.recognitionCommandServiceImpl import RecognitionCommandServiceImpl
from app.main.recognition.interfaces.rest.resource.recognitionResource import RecognitionResource
from app.main.recognition.interfaces.rest.transform.recognitionCommandFromResourceAssembler import RecognitionCommandFromResourceAssembler
from app.main.recognition.interfaces.rest.transform.recognitionResourceFromEntityAssembler import RecognitionResourceFromEntityAssembler

router = APIRouter(tags=["Recognition"])

# Cargamos el modelo y las acciones una sola vez
model = RecognitionModelLoader.load_model()
actions = RecognitionModelLoader.load_actions()

@router.post("", status_code=status.HTTP_200_OK)
def recognize(resource: RecognitionResource, db: Session = Depends(get_db)):
    try:
        sequence = RecognitionCommandFromResourceAssembler.to_sequence(resource)
        service = RecognitionCommandServiceImpl(model=model, actions=actions)
        entity = service.recognize(sequence)
        result = RecognitionResourceFromEntityAssembler.from_entity(entity)
        return {
            "message": "Predicción generada exitosamente",
            "status": "success",
            "data": result
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
