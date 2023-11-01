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


class BbParseMode(Enum):
    COMMON = "Common"
    INFO = "Info"
    POST = "Post"
    CHAT = "Chat"


class InfoBbText(BaseModel):
    value: StrictStr
    parse_mode: BbParseMode

class ColorSchema(Enum):
    MODERN= "Modern"
    PALE = "Pale"
    CLASSIC = "Classic"
    ClASSICPALE = "ClassicPale"
    NIGHT = "Night"

class PagingSettings(BaseModel):
    posts_per_page: int =Field(None, alias="postsPerPage")
    comments_per_page: int = Field(None, alias="commentsPerPage")
    topics_per_page: int = Field(None, alias="topicsPerPage")
    messages_per_page: int =Field(None, alias="messagesPerPage")
    entities_per_page: int = Field(None, alias="entitiesPerPage")


class UserSettings(BaseModel):
    color_schema: ColorSchema
    nanny_greetings_message: Optional[StrictStr] = Field(None, alias="nannyGreetingsMessage")
    paging: PagingSettings

class UserDetails(BaseModel):
    login: StrictStr
    roles: List[Roles]
    medium_picture_url: Optional[StrictStr] = Field(None, alias="mediumPictureUrl")
    small_picture_url: Optional[StrictStr] = Field(None, alias="smallPictureUrl")
    status: Optional[StrictStr] = Field(None)
    rating: Rating
    online: Optional[PastDate] = Field(None)
    name: Optional[StrictStr] = Field(None)
    location: Optional[StrictStr] = Field(None)
    registration: Optional[PastDate] = Field(None)
    icq: Optional[StrictStr] = Field(None)
    skype: Optional[StrictStr] = Field(None)
    original_picture_url: Optional[StrictStr] = Field(None, alias="originalPictureUrl")
    info: Optional[InfoBbText]
    settings: UserSettings


class UserDetailsEnvelop:
    resource: UserDetails
    metadata: Optional[StrictStr] = Field(None)
