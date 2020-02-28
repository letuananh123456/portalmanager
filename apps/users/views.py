from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from apps.core.utils import validate_data
from django.contrib.auth import authenticate
# from apps.core.exceptions import HTTP401AuthenticationError, HTTP404NotFoundError, HTTP409ConflictError
from . import models as user_models
from . import utils as user_utils
from . import serializers as user_sers
from rest_framework import status
from .models import LoginHistory



class LoginAPIView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        valid_data = validate_data(user_sers.LoginEmailValidator, request.data)

        username = valid_data.get('username')
        password = valid_data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise HTTP401AuthenticationError('Incorrect email or password')

        access_token = user_models.generate_access_token(user.id)
        token = user_models.Token.objects.create(user=user, key=access_token)
        data = {
            'access_token': token.key,
            'user': user
        }

        user_utils.create_or_update_login_history(user.id)
        serializer = user_sers.TokenSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetUserInfoAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request):
        his = LoginHistory.objects.all()
        ser = user_sers.LoginHistorySerializer(his, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)


class UpdateInfoUserApi(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        valid_data = validate_data(user_sers.UpdateUsertApiSer, request.data)
        user_id = valid_data.get("user_id")
        username = valid_data.get("username")
        fullname = valid_data.get("fullname")
        phone = valid_data.get("phone")
        email = valid_data.get("email")
        password = valid_data.get("password")

        user_models.UpdateUser.objects.filter(user_id = user_id ).update(username=username,fullname=fullname,phone=phone,email=email,password=password)  

        return Response(status=status.HTTP_200_OK)
