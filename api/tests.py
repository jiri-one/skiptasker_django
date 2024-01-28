from rest_framework import status
from rest_framework.test import APITestCase
from random import randrange

# from django.db.models.query import QuerySet
from .models import Task


def create_task(task_name: str, task_desc: str) -> Task:
    """Create a task with the given `name` and `description`."""
    return Task.objects.create(name=task_name, description=task_desc)


class TaskModelTests(APITestCase):
    task_name = "test task"
    task_desc = "Test description."

    def test_task_is_created_in_db(self):
        """Task is created in db and checked its content from db."""
        task = create_task(task_name=self.task_name, task_desc=self.task_desc)
        check_this_id = task.id
        self.assertTrue(isinstance(task, Task))
        task_from_db = Task.objects.get(id=check_this_id)
        self.assertEqual(task_from_db.id, check_this_id)
        self.assertEqual(task_from_db.name, self.task_name)
        self.assertEqual(task_from_db.description, self.task_desc)
        self.assertEqual(Task.objects.count(), 1)

    def test_task_is_updated(self):
        """Task is created in db and then updated by PUT method and again checked its content"""
        task = create_task(task_name=self.task_name, task_desc=self.task_desc)
        check_this_id = task.id
        # now update task
        new_name = "some new name"
        response = self.client.put(
            f"/update/{check_this_id}/", {"name": new_name}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().name, new_name)
        self.assertNotEqual(Task.objects.get().name, self.task_name)

    def test_task_status_is_updated(self):
        """Task is created in db and then updated by PUT method and again checked its content. This time we update the status of task too and we will set the status to FINISHED and that's mean-> completion_time should be automatically set."""
        task = create_task(task_name=self.task_name, task_desc=self.task_desc)
        check_this_id = task.id
        self.assertIsNone(Task.objects.get().completion_time)
        # now update the task status to COMPLETED
        response = self.client.put(
            f"/update/{check_this_id}/", {"status": "COMPLETED"}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.get().status, "COMPLETED")
        self.assertIsNotNone(Task.objects.get().completion_time)

    def test_task_completion_time_is_unset(self):
        """Task is created in db and then updated by PUT method to COMPLETED and again opened with set status to INPROGRESS -> completion_time should be automatically UNset."""
        task = create_task(task_name=self.task_name, task_desc=self.task_desc)
        check_this_id = task.id
        self.assertIsNone(Task.objects.get().completion_time)
        # now update the task status to COMPLETED
        response = self.client.put(
            f"/update/{check_this_id}/", {"status": "COMPLETED"}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.get().status, "COMPLETED")
        self.assertIsNotNone(Task.objects.get().completion_time)
        # now update the task status to INPROGRESS
        response = self.client.put(
            f"/update/{check_this_id}/", {"status": "INPROGRESS"}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.get().status, "INPROGRESS")
        self.assertIsNone(Task.objects.get().completion_time)

    def test_task_is_deleted(self):
        """Task is created in db and then try to delete it with DELETE method"""
        task = create_task(task_name=self.task_name, task_desc=self.task_desc)
        check_this_id = task.id
        self.assertEqual(Task.objects.count(), 1)  # one task in db
        # now try to delete task
        response = self.client.delete(f"", {"id": check_this_id}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.count(), 0)  # db is empty now

    def test_task_is_created_from_api(self):
        """Task is created from API with POST method"""
        response = self.client.post(
            f"", {"name": self.task_name, "description": self.task_desc}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        task = Task.objects.get()
        self.assertEqual(Task.objects.count(), 1)  # one task in db
        self.assertEqual(task.name, self.task_name)
        self.assertEqual(task.description, self.task_desc)

    def test_get_method(self):
        """Test if tasks are correctly returned from API with GET method"""
        task_tuples = [("one", "desc"), ("two", "desc2"), ("three", "desc3")]
        task_list = list()
        for name_desc in task_tuples:
            name, desc = name_desc
            created_task = create_task(task_name=name, task_desc=desc)
            task_list.append(created_task)
        response = self.client.get(f"", format="json")
        response_json = response.json()["tasks"]
        for task_from_tuples, task_returned, task_from_response in zip(
            task_tuples, task_list, response_json
        ):
            self.assertTrue(
                task_from_tuples[0] == task_returned.name == task_from_response["name"]
            )

        # this test solution is OK for showcase, but in production we will need care about sorting!

    def test_get_one_task(self):
        """Test if we can get one task from API with GET method"""
        task = create_task(task_name=self.task_name, task_desc=self.task_desc)
        check_this_id = task.id

        response = self.client.get(f"/{check_this_id}/", format="json")
        response_json = response.json()["task"]
        returned_task_name, returned_task_desc = (
            response_json["name"],
            response_json["description"],
        )
        self.assertEqual(
            (self.task_name, self.task_desc), (returned_task_name, returned_task_desc)
        )

    def test_try_to_update_non_existed_task(self):
        # now update task
        response = self.client.put(
            f"/update/{randrange(10)}/", {"name": "new_name"}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


# TODO: write more negative tests
