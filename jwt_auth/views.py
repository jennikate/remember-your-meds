#pylint: disable = no-member
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.conf import settings
from rest_framework.status import HTTP_201_CREATED, HTTP_422_UNPROCESSABLE_ENTITY, HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED

import jwt
from .serializers import UserSerializer, UserPutSerializer
User = get_user_model()


class RegisterView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Registration Successful'})
        return Response(serializer.errors, status=422)


class LoginView(APIView):

    def get_user(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            raise PermissionDenied({'message': 'Invalid Credentilais'})

    def post(self, request):

        email = request.data.get('email')
        password = request.data.get('password')

        user = self.get_user(email)

        if not user.check_password(password):
            raise PermissionDenied({'message': 'Invalid Credentails'})

        token = jwt.encode({'sub': user.id}, settings.SECRET_KEY, algorithm='HS256')

        return Response({'token': token, 'message': f'Welcome back {user.username}'})

class ProfileView(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, request):
        user = User.objects.get(pk=request.user.id)
        serialized_user = UserSerializer(user)
        return Response(serialized_user.data)

    def put(self, request):
        user = User.objects.get(pk=request.user.id)
        updated_user = UserPutSerializer(user, data=request.data)

        if updated_user.is_valid():
            updated_user.save()
            return Response(updated_user.data)
        return Response(updated_user.errors, status=HTTP_422_UNPROCESSABLE_ENTITY)
