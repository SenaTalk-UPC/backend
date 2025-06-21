from fastapi import APIRouter, HTTPException
from fastapi import status
from fastapi import Depends
from sqlalchemy.orm import Session
from app.main.config.database import get_db
from app.main.recognition.infrastructure.model.recognitionModelLoader import model, actions
from app.main.recognition.application.internal.commandservices.recognitionCommandServiceImpl import RecognitionCommandServiceImpl
from app.main.recognition.interfaces.rest.resource.recognitionResource import RecognitionResource
from app.main.recognition.interfaces.rest.transform.recognitionCommandFromResourceAssembler import RecognitionCommandFromResourceAssembler
from app.main.recognition.interfaces.rest.transform.recognitionResourceFromEntityAssembler import RecognitionResourceFromEntityAssembler

router = APIRouter(tags=["Recognition"])

@router.post("", status_code=status.HTTP_200_OK)
def recognize(resource: RecognitionResource, db: Session = Depends(get_db)):
    sequence = RecognitionCommandFromResourceAssembler.to_sequence(resource)
    service = RecognitionCommandServiceImpl(model=model, actions=actions)
    entity = service.recognize(sequence)
    result = RecognitionResourceFromEntityAssembler.from_entity(entity)
    return {
        "message": "Prediction generated successfully",
        "status": "success",
        "data": result
    }
