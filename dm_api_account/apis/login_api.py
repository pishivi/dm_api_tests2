from requests import Response
from restclient.restclient import Restclient
from ..models import *  # импортнул все модели из файла models -> __init__.py
from ..utilities import validate_request_json


class LoginApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.client = Restclient(host=host, headers=headers)
        if headers:
            self.client.session.headers.update(headers)

    def post_v1_account_login(self, json: LoginCredentials, **kwargs) -> Response:
        """
    Authenticate via credentials
        :return:
        """

        response = self.client.post(
            path=f"/v1/account/login",
            json=json.model_dump(),
            **kwargs
        )
        UserEnvelope(**response.json())
        return response

    def del_v1_account_login(self, **kwargs):
        """
        logout as current user
        :return:
        """

        response = self.client.delete(
            path=f"/v1/account/login",
            **kwargs
        )
        GeneralError(**response.json())
        return response

    def del_v1_account_login_all(self, **kwargs):
        """
        logout from every device
        :return:
        """

        response = self.client.delete(

            path=f"/v1/account/login/all",
            **kwargs
        )
        GeneralError(**response.json())
        return response
