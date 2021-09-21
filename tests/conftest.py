import pytest


@pytest.fixture(scope='session')
def login():
    token = ''
    return token

