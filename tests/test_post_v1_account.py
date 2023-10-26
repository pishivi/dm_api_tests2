from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi
import structlog
import time


structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False
                                          )
    ]
)
def test_post_v1_account():
    mailhog = MailhogApi(host="http://5.63.153.31:5025")
    api = DmApiAccount(host="http://5.63.153.31:5051")
    json = {
        "login": "15a122s33d34as",
        "email": "chs2312dfsdfgm@sdf.ru",
        "password": "h2o32pgghdfop"
    }

    response = api.account.post_v1_account(json=json)
    assert response.status_code == 201, f"Код ответа должен быть 201,а не {response.status_code}"
    time.sleep(2)
    token = mailhog.get_token_from_last_email()
    response = api.account.put_v1_account_token(token=token)

