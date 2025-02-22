from locust import task, HttpUser
import random


class ApiUser(HttpUser):
    obj_id = None

    # для вставки в ui host = 'http://167.172.172.115:52353'

    def on_start(self):
        body = {
            "data": {
                "color": "test color",
                "size": "test size"
            },
            "name": f"Test name {random.randint(1, 100)}"
        }
        headers = {'Content-Type': 'application/json'}
        response = self.client.post(
            '/object',
            json=body,
            headers=headers
        )
        self.obj_id = response.json()['id']

    @task(2)
    def get_all_objects(self):
        self.client.get(
            "/object",
            headers={'Content-Type': 'application/json'}
        )

    @task(3)
    def get_one_objects(self):
        self.client.get(
            f"/object/{self.obj_id}",
            headers={'Content-Type': 'application/json'}
        )

    @task(1)
    def update_object(self):
        self.client.patch(
            f"/object/{self.obj_id}",
            json={"name": f"Updated name {random.randint(1, 100)}"},
        )

    def on_stop(self):
        self.client.delete(
            f'/object/{self.obj_id}'
        )
