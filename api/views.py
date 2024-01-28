from rest_framework import status
from rest_framework.views import APIView, Response
from django.core.exceptions import ObjectDoesNotExist
from .models import Task
from .serializers import TaskSerializer


class TasksAPI(APIView):

    def get(self, request):
        tasks = Task.objects.all()
        tasks_data = TaskSerializer(tasks, many=True).data
        response_data = {"tasks": tasks_data}
        return Response(response_data, status=status.HTTP_200_OK)

    def post(self, request):
        """POST method is here only for creating tasks."""
        name = request.data.get("name")
        description = request.data.get("description")
        task = Task.objects.create(name=name, description=description)
        response_data = {"response": f"Task created, its id is {task.id}"}
        return Response(response_data, status=status.HTTP_201_CREATED)

    def put(self, request, id):
        """PUT method is here only for updating tasks."""
        name = request.data.get("name")
        description = request.data.get("description")
        task_status = request.data.get("status")
        # better is to use update method here, but for now let it this way
        try:
            task = Task.objects.get(id=id)
        except ObjectDoesNotExist:
            response_data = {"response": "Task doesn't exist"}
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)
        # We've got it covered by exception, but we'll cover that option as well.
        if not task:
            response_data = {"response": "Task doesn't exist"}
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)
        if name:
            task.name = name
        if description:
            task.description = description
        if task_status:
            task.status = task_status
        task.save()
        response_data = {"response": "Task updated"}
        return Response(response_data, status=status.HTTP_200_OK)

    def delete(self, request):
        id = request.data.get("id")
        task = Task.objects.get(id=id)
        if task is None:
            response_data = {"response": "Task doesn't exist"}
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)

        task.delete()
        response_data = {"response": "task was deleted"}
        return Response(response_data, status=status.HTTP_200_OK)


class OneTaskAPI(APIView):

    def get(self, request, id):
        task = Task.objects.get(id=id)
        task_data = TaskSerializer(task, many=False).data
        response_data = {"task": task_data}
        return Response(response_data, status=status.HTTP_200_OK)


# TODO: allow update a delete from OneTaskAPI too
