from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, StrictStr, Field, PastDate



class Roles(Enum):
    GUEST = "Guest"
    PLAYER = "Player"
    ADMINISTRATOR = "Administrator"
    NANNY_MODERATOR = "NannyModerator"
    REGULAR_MODERATOR = "RegularModerator"
    SENIOR_MODERATOR = "SeniorModerator"

class Rating(BaseModel):
    enabled: bool
    quality: int
    quantity: int


class User(BaseModel):
    login: StrictStr
    roles: List[Roles]
    medium_picture_url: Optional[StrictStr] = Field(None, alias="mediumPictureUrl")
    small_picture_url: Optional[StrictStr] = Field(None, alias="smallPictureUrl")
    status: Optional[StrictStr] = Field(None)
    rating: Rating
    online: Optional[PastDate]= Field(None)
    name: Optional[StrictStr]= Field(None)
    location: Optional[StrictStr]= Field(None)
    registration: Optional[PastDate]= Field(None)


class UserEnvelopeModel(BaseModel):
    resource: User
    metadata: Optional[StrictStr]= Field(None)
