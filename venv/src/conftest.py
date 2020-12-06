import pytest

from helpers.ApiTests import SessionApi


def pytest_addoption(parser):
    parser.addoption("--login", default="",
                     help="enter login")
    parser.addoption("--password", default="",
                     help="enter password")


@pytest.fixture(scope="class")
def api_session(pytestconfig, request):
    session_authorized = SessionApi.get_authorized(pytestconfig.getoption('login'), pytestconfig.getoption('password'))
    request.cls.session_authorized = session_authorized
    return session_authorized
