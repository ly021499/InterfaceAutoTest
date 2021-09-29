import pytest
from core import loader
import os
import config


@pytest.fixture(scope='session')
def load_yaml():
    yaml_path = os.path.join(config.DATA_DIR, '')
    yaml_content = loader.load_yaml(yaml_path)
    yield yaml_content


@pytest.fixture(scope='session', autouse=True)
def login():
    token = 'jack'
    yield token
