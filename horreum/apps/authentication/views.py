from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser

from . import models
from .models import User
from .serializers import UserRegistrationSerializer


class SingleUserRegistrationView(generics.CreateAPIView):
    """
    Allows a staff to create single student's account
    Args:
        first_name: the student's first name
        last_name: the student's last name
        username: username that will be indexed by the system
        email: the student's email
        password: The new account password
        role: The user's role either TM,STUDENT, POD_LEADER
    """
    permission_classes = (IsAdminUser,)
    serializer_class = UserRegistrationSerializer

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        message= {
            'message': 'User registered  successfully',
            }
        return Response(message, status= status.HTTP_201_CREATED)
