from trace import Trace

import pytest


@pytest.fixture(scope='class')
def database_prep():
    print('Preparing database')
    yield
    print("Database rollback")


@pytest.fixture(scope='class')
def config_prep():
    print('Preparing configuration')
    yield
    print("Cleaning configuration")
