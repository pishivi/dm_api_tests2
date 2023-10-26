import time
from pprint import pprint

import structlog
from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False
                                          )
    ]
)

login = "sjkdf"
password = "kjabsdf"
email = "kjslbf@mail.ru"


def test_post_v1_account_login():
    mailhog = MailhogApi(host="http://5.63.153.31:5025")
    api = DmApiAccount(host="http://5.63.153.31:5051")
    json = {
        "login": login,
        "email": email,
        "password": password,
    }

    response = api.account.post_v1_account(json=json)
    assert response.status_code == 201, f"Код ответа должен быть 201,а не {response.status_code}"
    time.sleep(2)
    token = mailhog.get_token_from_last_email()
    response = api.account.put_v1_account_token(token=token)

    json = {
        "login": login,
        "password": password,
        "rememberMe": True
    }
    response = api.login.post_v1_account_login(json=json)
    assert response.status_code == 200, f"Код ответа должен быть 200,а не {response.status_code}"
