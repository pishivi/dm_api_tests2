import requests


def del_v1_account_login():
    """
    logout as current user
    :return:
    """
    url = "http://5.63.153.31:5051/v1/account/login"

    payload = {}
    headers = {
        'X-Dm-Auth-Token': '<string>',
        'X-Dm-Bb-Render-Mode': '<string>',
        'Accept': 'text/plain'
    }

    response = requests.request(
        method="POST",
        url=url,
        headers=headers,
        json=payload
    )
    return response


response = del_v1_account_login()
