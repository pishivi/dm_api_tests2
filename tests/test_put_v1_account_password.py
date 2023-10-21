
from services.dm_api_account import DmApiAccount


def test_post_v1_account():
    api = DmApiAccount(host="http://5.63.153.31:5051")
    json = {
        "login": "opaopa",
        "token": "58d69534-3f1e-4f37-a024-6a339b56bf1f",
        "oldPassword": "hophop",
        "newPassword": "hophop1"
    }


    response = api.account.put_v1_account_password(
        json=json
    )
    print(response)
