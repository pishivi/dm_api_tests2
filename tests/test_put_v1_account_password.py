from services.dm_api_account import DmApiAccount
from dm_api_account.models.change_password_model import ChangePasswordModel


def test_post_v1_account():
    api = DmApiAccount(host="http://5.63.153.31:5051")
    json = ChangePasswordModel(
        login="adf331122335",
        token="962baf7d-26a6-4d10-9310-14a38468ade7",
        oldPassword="g1g2g5gp",
        newPassword="hophop1"
    )

    response = api.account.put_v1_account_password(json=json)
    print(response)
