from src.controllers.usercontroller import UserController
import pytest
import unittest.mock as mock
from unittest.mock import patch
from src.util.dao import DAO


@pytest.mark.unit
@pytest.mark.parametrize(
    "input_email, return_value, output_expected",
    [
        (
            "test@email.com",
            [],
            None
        ),
        (
            "test@email.com",
            [{"user object"}],
            {"user object"}
        ),
        (
            "test@email.com",
            [{"user object"}, {"other user object"}],
            {"user object"}
        ),
        (
            "not an email",
            [],
            ValueError('Error: invalid email address')
        ),
    ]
)
def test_get_user_by_email(input_email, return_value, output_expected):
    mockedDAO = mock.MagicMock()
    mockedDAO.find.return_value = return_value

    sut = UserController(dao=mockedDAO)

    try:
        usercontrollerresult = sut.get_user_by_email(email=input_email)
        assert usercontrollerresult == output_expected
    except Exception as e:
        assert str(e) == str(output_expected)

