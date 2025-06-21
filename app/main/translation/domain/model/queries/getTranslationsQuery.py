from dataclasses import dataclass
from uuid import UUID

@dataclass(frozen=True, slots=True)
class GetTranslationsQuery:
    user_id: UUID
    limit: int = 20
