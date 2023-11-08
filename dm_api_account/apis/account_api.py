from pydantic import BaseModel
from requests import Response
from restclient.restclient import Restclient
from ..models import *
from ..utilities import validate_request_json


class AccountApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.client = Restclient(host=host, headers=headers)
        if headers:
            self.client.session.headers.update(headers)

    def post_v1_account(self, json: Registration, **kwargs) -> Response:
        """
        Register new user
        :param json registration_model
        :return:
        """

        response = self.client.post(
            path=f"/v1/account",
            json=json.model_dump(),
            **kwargs
        )
        return response

    def post_v1_account_password(self, json: ResetPassword, **kwargs) -> Response:
        """
        Reset registered user password
        :param json reset_password_model
        :return:
        """

        response = self.client.post(
            path=f"/v1/account/password",
            json=json.model_dump(),
            **kwargs
        )
        UserEnvelope(**response.json())
        return response

    def put_v1_account_email(self, json: ChangeEmail, **kwargs) -> Response:
        """
        Change registered user email
        :param json change_email_model
        :return:
        """

        response = self.client.put(
            path=f"/v1/account/email",
            json=json.model_dump(),
            **kwargs
        )
        UserEnvelope(**response.json())
        return response

    def put_v1_account_password(self, json: ChangePassword, **kwargs) -> Response:
        """
        Change registered user password
        :param json change_password_model
        :return:
        """

        response = self.client.put(
            path=f"/v1/account/password",
            json=validate_request_json(json),
            **kwargs
        )
        UserEnvelope(**response.json())
        return response

    def put_v1_account_token(self, token: str, **kwargs):
        """
      Activate registered user
        :return:
        """

        response = self.client.put(
            path=f"/v1/account/{token}",
            **kwargs
        )
        UserEnvelope(**response.json())
        return response

    def get_v1_account(self, **kwargs):
        """
        Get current user
        :return:
        """
        response = self.client.get(
            path=f"/v1/account",
            **kwargs
        )
        UserDetailsEnvelope(**response.json())

        return response
