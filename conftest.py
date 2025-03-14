import pytest
import configparser

from controllers.todo_controller import TodoController

def pytest_addoption(parser):
    parser.addoption("--env",
                     action="store",
                     default="dev",
                     help="Environment option: dev or stg",
                     choices=("dev", "stg"))

@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")

@pytest.fixture(scope="session")
def conf(env):
    config = configparser.ConfigParser()
    config.read('config.ini')

    conf = {
        'env': env,
        'base_url': config[env]['base_url']
    }

    return conf

@pytest.fixture(scope="session")
def todo_controller(conf):
    return TodoController(conf['base_url'])

@pytest.fixture(scope="function")
def create_todo(todo_controller):
    body = {
        'userId': 1,
        'title': 'This is an example Todo',
        'completed': False
    }

    response = todo_controller.create(body)

    assert response.status_code == 201

    return response.obj