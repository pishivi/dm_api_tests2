from pydantic import BaseModel, StrictStr

class LoginCredentialModel(BaseModel):
    login: StrictStr
    password: StrictStr
    rememberMe: bool

# login_credential_model = {
#     "login": "<string>",
#     "password": "<string>",
#     "rememberMe": "<boolean>"
# }