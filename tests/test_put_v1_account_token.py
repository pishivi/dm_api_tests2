import time
import structlog
from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi
from dm_api_account.models.user_envelope_model import UserEnvelopeModel

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False
                                          )
    ]
)


def test_put_v1_account_token():
    mailhog = MailhogApi(host="http://5.63.153.31:5025")
    api = DmApiAccount(host="http://5.63.153.31:5051")
    json = UserEnvelopeModel(
        login= "1d2323e4as",
        email= "chd32fsdfgm@sdf.ru",
        password= "hopagghdfop"
    )
    token = mailhog.get_token_from_last_email()
    response = api.account.put_v1_account_token(token=token)
    assert response.status_code == 200, f"Статус код ответа {response.status_code}, должен быть 200"
    time.sleep(2)
    #token = mailhog.get_token_from_last_email()
