from __future__ import annotations
from pydantic import BaseModel, StrictStr, Extra, Field
from typing import Optional, Dict, List


class ChangeEmail(BaseModel):
    class Config:
        extra = Extra.forbid

    login: Optional[StrictStr] = Field(None, description='User login')
    password: Optional[StrictStr] = Field(None, description='User password')
    email: Optional[StrictStr] = Field(None, description='New user email')