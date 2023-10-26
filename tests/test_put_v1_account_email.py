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

login = "15a12sd34as"
email = "ch1s12dfsdfgm@sdf.ru"
password = "ho2pgghdfop"
def test_post_v1_account_email():
    mailhog = MailhogApi(host="http://5.63.153.31:5025")
    api = DmApiAccount(host="http://5.63.153.31:5051")
    json = {
        "login": login,
        "password": password,
        "email": email
    }

    response = api.account.put_v1_account_email(json=json)
    assert response.status_code == 200, f"Код ответа должен быть 200,а не {response.status_code}"
    time.sleep(2)
    token = mailhog.get_token_from_last_email()
    response = api.account.put_v1_account_token(token=token)

