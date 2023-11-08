from __future__ import annotations
from typing import Optional

from pydantic import BaseModel, StrictStr, Extra, Field

class Registration(BaseModel):
    class Config:
        extra = Extra.forbid

    login: Optional[StrictStr] = Field(None, description='Login')
    email: Optional[StrictStr] = Field(None, description='Email')
    password: Optional[StrictStr] = Field(None, description='Password')

#print(RegistrationModel(**registration_model).model_dump_json()) - посмотреть, как выглядит в формате json