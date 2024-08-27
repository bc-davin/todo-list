from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from .models import Task
from .serializers import TaskSerializer
from rest_framework.decorators import api_view
@api_view(['GET'])
def homePage(request: Request) -> Response:
    response = "Welcome to the Task Manager API"
    return Response(data=response, status=status.HTTP_200_OK)
class TaskListCreateView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get(self, request: Request, *args, **kwargs) -> Response:
        return self.list(request)

    def post(self, request: Request, *args, **kwargs) -> Response:
        return self.create(request)
    
class TaskRetrieveUpdateDestroyView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get(self, request: Request, *args, **kwargs) -> Response:
        return self.retrieve(request, *args, **kwargs)

    def put(self, request: Request, *args, **kwargs) -> Response:
        return self.update(request, *args, **kwargs)

    def delete(self, request: Request, *args, **kwargs) -> Response:
        return self.destroy(request, *args, **kwargs)
