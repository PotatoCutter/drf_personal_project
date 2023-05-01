from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework_simplejwt.views import TokenObtainPairView
from users.serializers import UserSerializer, TokenObtainPairSerializer, UserUpdate

from users.models import User


class UserView(APIView):

    def post(self, requast):
        serializer = UserSerializer(data=requast.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "all_good"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, requast, user_id):
        # myuser = get_object_or_404(User, id=user_id)
        # print(myuser.id, user_id, requast.user.id, requast.data)
        myuser = User.objects.get(id=user_id)
        if requast.user.id == myuser.id:
            serializer = UserSerializer(myuser, requast.data)
            # serializer = None
            # print(serializer)
            if serializer.is_valid():
                serializer.save(owner=requast.user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                print(serializer.errors)
                return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "not_authorized"}, status=status.HTTP_401_UNAUTHORIZED)


class UserAPI(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer
