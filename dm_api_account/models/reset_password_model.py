from __future__ import annotations
from pydantic import BaseModel, StrictStr, Extra, Field
from typing import Optional, Dict, List



class ResetPassword(BaseModel):
    class Config:
        extra = Extra.forbid

    login: Optional[StrictStr] = Field(None, description='Login')
    email: Optional[StrictStr] = Field(None, description='Email')