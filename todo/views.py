from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import get_object_or_404
from todo.serializers import TodoSerializer, TodoCreateSerializer

from todo.models import Todo


class todo_view(APIView):
    def get(self, request):
        todo = Todo.objects.filter(user=request.user)
        serial = TodoSerializer(todo, many=True)
        return Response(serial.data, status=status.HTTP_200_OK)

    def post(self, request):
        serial = TodoCreateSerializer(data=request.data)
        if serial.is_valid():
            serial.save(user=request.user)
            return Response(serial.data, status=status.HTTP_201_CREATED)
        pass


class todo_detail_view(APIView):

    def put(self, request, pk):
        todo = get_object_or_404(Todo, id=pk)
        if request.user == todo.user:
            serializer = TodoCreateSerializer(todo, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("no authority to access", status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, pk):
        todo = get_object_or_404(Todo, id=pk)
        if todo.user == request.user:
            todo.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("no authority to access", status=status.HTTP_403_FORBIDDEN)
        pass
