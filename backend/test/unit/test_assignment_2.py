from src.controllers.usercontroller import UserController
import pytest
import unittest.mock as mock


@pytest.mark.unit
@pytest.mark.parametrize(
    "input_email, DAO_return_value, output_expected",
    [
        (
            "test@email.com",
            pytest.raises(Exception),
            Exception
        ),
    ]
)
def test_get_user_by_email_Exception(input_email, DAO_return_value, output_expected):
    mockedDAO = mock.MagicMock()
    mockedDAO.find.side_effect = DAO_return_value
    sut = UserController(dao=mockedDAO)

    with pytest.raises(Exception):
        usercontrollerresult = sut.get_user_by_email(email=input_email)
        assert usercontrollerresult == output_expected

@pytest.mark.unit
@pytest.mark.parametrize(
    "input_email, DAO_return_value, output_expected",
    [
        (
            "test@email.com",
            [{"user object"}],
            {"user object"}
        ),
        (
            "test@email.com",
            [],
            None
        ),
        (
            "test@email.com",
            [{"user object"}, {"other user object"}],
            {"user object"}
        ),
    ]
)
def test_get_user_by_email(input_email, DAO_return_value, output_expected):
    mockedDAO = mock.MagicMock()
    mockedDAO.find.return_value = DAO_return_value
    sut = UserController(dao=mockedDAO)

    usercontrollerresult = sut.get_user_by_email(email=input_email)
    assert usercontrollerresult == output_expected


@pytest.mark.unit
@pytest.mark.parametrize(
    "input_email, DAO_return_value, output_expected",
    [
        (
            "not an email",
            [{"user object"}],
            ValueError('Error: invalid email address')
        ),
        (
            "@.com",
            [{"user object"}],
            ValueError('Error: invalid email address')
        ),
    ]
)
def test_get_user_by_email_ValueError(input_email, DAO_return_value, output_expected):
    mockedDAO = mock.MagicMock()
    mockedDAO.find.return_value = DAO_return_value
    sut = UserController(dao=mockedDAO)

    with pytest.raises(ValueError):
        usercontrollerresult = sut.get_user_by_email(email=input_email)
        assert usercontrollerresult == output_expected

