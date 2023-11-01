from pydantic import BaseModel, StrictStr


class ChangeEmail(BaseModel):
    login: StrictStr
    password: StrictStr
    email: StrictStr


# change_email_model = {
#     "login": "<string>",
#     "password": "<string>",
#     "email": "<string>"
# }