import pytest
from core import loader
import config


@pytest.fixture(scope='session')
def load_all_yaml():
    filepath_list = loader.load_folder(config.DATA_DIR)
    yield filepath_list
