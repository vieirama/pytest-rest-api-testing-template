import pytest

from utils.schema_validation import SchemaValidation

class TestTodos:

    def test_get_all_todos(self, todo_controller):
        response = todo_controller.get_all()

        assert response.status_code == 200
        assert len(response.obj) > 0

        schema_validation = SchemaValidation("get_todos", response.response_json)
        schema_validation.validate_schema()

    @pytest.mark.parametrize("todo_id, expected_user_id, expected_title, expected_completed",
                             [(1, 1, "delectus aut autem", False),
                              (2, 1, "quis ut nam facilis et officia qui", False)])
    def test_get_todo(self, todo_controller,todo_id, expected_user_id, expected_title, expected_completed):
        response = todo_controller.get(todo_id)

        assert response.status_code == 200
        assert response.obj.id == todo_id
        assert response.obj.userId == expected_user_id
        assert response.obj.title == expected_title
        assert response.obj.completed == expected_completed

        schema_validation = SchemaValidation("get_todo", response.response_json)
        schema_validation.validate_schema()
    
    @pytest.mark.parametrize("user_id, title, completed",
                             [(1, "This is a new Todo", False),
                              (2, "This is another Todo", True)])
    def test_create_todo(self, todo_controller, user_id, title, completed):
        body = {'userId': user_id, 'title': title, 'completed': completed}

        response = todo_controller.create(body)

        assert response.status_code == 201
        assert response.obj.userId == user_id
        assert response.obj.title == title
        assert response.obj.completed == completed

    @pytest.mark.parametrize("todo_id, user_id, title, completed",
                             [(1, 1, "This is an updated Todo", True)])
    def test_update_todo(self, todo_controller, todo_id, user_id, title, completed):
        body = {'userId': user_id, 'title': title, 'completed': completed}

        response = todo_controller.update(todo_id, body)

        assert response.status_code == 200
        assert response.obj.userId == user_id
        assert response.obj.title == title
        assert response.obj.completed == completed

    def test_delete_todo(self, todo_controller):
        response = todo_controller.delete(1)

        assert response.status_code == 200
