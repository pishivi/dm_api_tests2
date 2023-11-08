from services.dm_api_account import DmApiAccount
from dm_api_account.models.change_password_model import ChangePassword


def test_post_v1_account():
    api = DmApiAccount(host="http://5.63.153.31:5051")
    json = ChangePassword(
        login="a1d1f365",
        token="7566c1ca-bed9-466f-af5c-5295a6868582",
        oldPassword="fa111231231",
        newPassword="ho1212phop1"
    )

    response = api.account.put_v1_account_password(json=json)
    print(response)
