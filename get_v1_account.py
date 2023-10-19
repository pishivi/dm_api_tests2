import requests


def get_v1_account():
    """
    get current user
    :return:
    """
    url = "http://5.63.153.31:5051/v1/account"

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


response = get_v1_account()
