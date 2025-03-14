from controllers.base_controller import BaseController


class TodoController(BaseController):
    def __init__(self, base_url):
        super().__init__(base_url)

    endpoint = 'todos'

    def get_all(self):
        return self.request.get(f'{self.base_url}/{self.endpoint}')

    def get(self, todo_id):
        return self.request.get(f'{self.base_url}/{self.endpoint}/{todo_id}')

    def create(self, body):
        return self.request.post(f'{self.base_url}/{self.endpoint}', self.headers, body)

    def update(self, todo_id, body):
        return self.request.put(f'{self.base_url}/{self.endpoint}/{todo_id}', self.headers, body)

    def delete(self, todo_id):
        return self.request.delete(f'{self.base_url}/{self.endpoint}/{todo_id}')