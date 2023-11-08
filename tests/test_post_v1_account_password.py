from services.dm_api_account import DmApiAccount
import structlog
from dm_api_account.models.reset_password_model import ResetPassword

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account_password():
    api = DmApiAccount(host="http://5.63.153.31:5051")
    json = ResetPassword(
        login="a1212122sdf122",
        email="e12233663m123l1@mail.ru"
    )

    response = api.account.post_v1_account_password(
        json=json
    )
    print(response)
