import pytest


@pytest.fixture()
def database_connection():
    print('\nSetup: Connection to the DB')
    connection = 'ConnectionObject'
    yield connection
    print('Teardown: Close connection to the DB')
    del connection


def test_database_ops(database_connection):
    print('\nPerform test steps')
    assert database_connection == 'ConnectionObject'