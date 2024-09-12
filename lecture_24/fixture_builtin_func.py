import os.path
import pytest


### REQUEST
@pytest.fixture
def fixture(request):
    test_name = request.node.name
    print("Setup for test:", test_name)

    yield 'data'

    print("Teardown for test:", test_name)


def test_tname(fixture):
    print("test execution")
    assert fixture == 'data'


### tmpdir
def test_create_file_in_tmpdir(tmpdir):
    file_path = tmpdir.join('test_file.txt')
    file_path.write("Test data")

    assert file_path.isfile()
    assert file_path.read() == "Test data"

def test_make_directory_in_tmpdir(tmpdir):
    new_dir = tmpdir.mkdir('test_dir')
    assert new_dir.isdir()

def test_tmpdir_is_removed(tmpdir):
    assert os.path.exists(tmpdir)
    os.rmdir(tmpdir)