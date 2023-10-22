import requests
from requests import session, Response
from ..models.login_credentials_model import login_credential_model


class LoginApi:
    def __init__(self, host, headers):
        self.host = host
        self.session = session()
        if headers:
            self.session.headers.update(headers)

    def post_v1_account_login(self, json: login_credential_model, **kwargs) -> Response:
        """
    Authenticate via credentials
        :return:
        """

        response = self.session.post(
            url=f"{self.host}/v1/account/login",
            json=json
            **kwargs
        )
        return response

    def del_v1_account_login(self, **kwargs):
        """
        logout as current user
        :return:
        """

        response = self.session.delete(
            url=f"{self.host}/v1/account/login",
            # json=payload
            **kwargs
        )
        return response

    def del_v1_account_login_all(self, **kwargs):
        """
        logout from every device
        :return:
        """

        response = self.session.delete(

            url=f"{self.host}/v1/account/login/all",
            # json=payload
            **kwargs
        )
        return response
