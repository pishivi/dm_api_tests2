from pydantic import BaseModel, StrictStr

# registration_model = {
#     "login": "userjjj",
#     "email": "lala@mail.ru",
#     "password": "kekeek"
# }

class RegistrationModel(BaseModel):
    login: StrictStr
    email: StrictStr
    password: StrictStr


#print(RegistrationModel(**registration_model).model_dump_json()) - посмотреть, как выглядит в формате json