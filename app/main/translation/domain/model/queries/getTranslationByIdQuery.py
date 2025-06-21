from dataclasses import dataclass
from uuid import UUID

@dataclass(frozen=True, slots=True)
class GetTranslationById:
    translation_id: UUID
