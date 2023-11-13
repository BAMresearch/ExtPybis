import pytest


def pytest_configure(config):
    # register an additional marker
    config.addinivalue_line(
        "markers", "login: mark test to only run when provided with login"
    )


"""
--login and --password command line arguments are username and password for
openBIS (that you use to log in normally)
"""


def pytest_addoption(parser):
    parser.addoption("--login", action="store", default="no_cl_login")
    parser.addoption("--password", action="store", default="no_cl_password")
    parser.addoption("--url", action="store", default="https://localhost:8443/openbis/")
