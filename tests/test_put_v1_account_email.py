
from services.dm_api_account import DmApiAccount


def test_post_v1_account():
    api = DmApiAccount(host="http://5.63.153.31:5051")
    json = {
        "login": "йцукйцук",
        "token": "<uuid>",
        "oldPassword": "<lalala11322",
        "newPassword": "asdfasdfsdf"
    }


    response = api.account.put_v1_account_email(
        json=json
    )
    print(response)
