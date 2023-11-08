import time
from pprint import pprint

import structlog

from dm_api_account.models.registration_model import Registration
from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi
from dm_api_account.models.login_credentials_model import LoginCredentials

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False
                                          )
    ]
)


# login = "sjkdf"
# password = "kjabsdf"
# email = "kjslbf@mail.ru"


def test_post_v1_account_login():
    mailhog = MailhogApi(host="http://5.63.153.31:5025")
    api = DmApiAccount(host="http://5.63.153.31:5051")
    json = Registration(
        login="a1212122sdf122",
        email="e12233663m123l1@mail.ru",
        password="fa111231231",
    )

    response = api.account.post_v1_account(json=json)
    assert response.status_code == 201, f"Код ответа должен быть 201,а не {response.status_code}"
    time.sleep(2)
    token = mailhog.get_token_from_last_email()
    response = api.account.put_v1_account_token(token=token)

    json = LoginCredentials(
        login="a1212122sdf122",
        password="fa111231231",
        rememberMe=True
    )
    response = api.login.post_v1_account_login(json=json)
    assert response.status_code == 200, f"Код ответа должен быть 200,а не {response.status_code}"
