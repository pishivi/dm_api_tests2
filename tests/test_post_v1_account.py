from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi
import structlog
import time
from dm_api_account.models.registration_model import Registration

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account():
    mailhog = MailhogApi(host="http://5.63.153.31:5025")
    api = DmApiAccount(host="http://5.63.153.31:5051")
    json = Registration(
        login="a11d1f365",
        email="2125m@sdf.ru",
        password="g13g2g5gp"
    )

    response = api.account.post_v1_account(json=json)
    assert response.status_code == 201, f"Код ответа должен быть 201,а не {response.status_code}"
    time.sleep(2)
    token = mailhog.get_token_from_last_email()
    #response = api.account.put_v1_account_token(token=token)
