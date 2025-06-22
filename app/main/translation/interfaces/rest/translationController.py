from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.main.config.database import get_db

# Services
from app.main.translation.application.internal.commandservices.translationCommandServiceImpl import TranslationCommandServiceImpl
from app.main.translation.application.internal.queryservices.translationQueryServiceImpl import TranslationQueryServiceImpl

# Resources
from app.main.translation.infrastructure.repositories.translationRepository import TranslationRepository
from app.main.translation.interfaces.rest.resources.createTranslationResource import CreateTranslationResource
from app.main.translation.interfaces.rest.resources.translationResource import TranslationResource
from app.main.translation.interfaces.rest.resources.updateTranslationResource import UpdateTranslationResource

# Assemblers
from app.main.translation.interfaces.rest.transform.createTranslationCommandFromResourceAssembler import CreateTranslationCommandFromResourceAssembler
from app.main.translation.interfaces.rest.transform.translationResourceFromEntityAssembler import TranslationResourceFromEntityAssembler
from app.main.translation.interfaces.rest.transform.updateTranslationCommandFromResourceAssembler import UpdateTranslationCommandFromResourceAssembler
from app.main.iam.infrastructure.security.security import get_current_user

router = APIRouter(tags=["Translations"])


@router.post("", response_model=dict, status_code=201)
def create_translation(resource: CreateTranslationResource, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    repo = TranslationRepository(db)
    service = TranslationCommandServiceImpl(repo)
    command = CreateTranslationCommandFromResourceAssembler.to_command(resource)
    result = service.create_translation(command)
    resource_out = TranslationResourceFromEntityAssembler.from_entity(result)
    return {
        "message": "Translation created successfully",
        "status": "success",
        "data": resource_out
    }


@router.get("", response_model=dict)
def get_all_translations(db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    service = TranslationQueryServiceImpl(db)
    translations = service.get_all()
    resources = [TranslationResourceFromEntityAssembler.from_entity(t) for t in translations]
    return {
        "message": "Translations retrieved successfully",
        "status": "success",
        "data": resources
    }


@router.get("/{translation_id}", response_model=dict)
def get_translation_by_id(translation_id: int, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    service = TranslationQueryServiceImpl(db)
    translation = service.get_by_translation_id(translation_id)
    resource = TranslationResourceFromEntityAssembler.from_entity(translation)
    return {
        "message": "Translation retrieved successfully",
        "status": "success",
        "data": resource
    }


@router.put("/{translation_id}", response_model=dict)
def update_translation(translation_id: int, resource: UpdateTranslationResource, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    repo = TranslationRepository(db)
    service = TranslationCommandServiceImpl(repo)
    data = UpdateTranslationCommandFromResourceAssembler.to_dict(resource)
    updated_translation = service.update_translation(translation_id, data["text"])
    updated_resource = TranslationResourceFromEntityAssembler.from_entity(updated_translation)
    return {
        "message": "Translation updated successfully",
        "status": "success",
        "data": updated_resource
    }


@router.delete("/{translation_id}", response_model=dict)
def delete_translation(translation_id: int, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    repo = TranslationRepository(db)
    service = TranslationCommandServiceImpl(repo)
    service.delete_translation(translation_id)
    return {
        "message": "Translation deleted successfully",
        "status": "success"
    }
