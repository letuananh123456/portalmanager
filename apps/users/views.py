from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from apps.core.utils import validate_data, validate_response
from django.contrib.auth import authenticate
from apps.core.exceptions import HTTP401AuthenticationError, HTTP404NotFoundError, HTTP409ConflictError
from . import models as user_models
from . import utils as user_utils
from . import serializers as user_sers
from rest_framework import status
from .models import LoginHistory
from django.conf import settings
from .models import User



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
    """
    API này để lưu cập nhật thông tin user khi có sự thay đổi từ sàn thương mại điện tử
    Cập nhật thành công: 200
    """
    def post(self, request, format=None):
        valid_data = validate_data(user_sers.UpdateUsertApiSer, request.data)
        user_id = valid_data.get("user_id")
        username = valid_data.get("username")
        fullname = valid_data.get("fullname")
        phone = valid_data.get("phone")
        email = valid_data.get("email")
        password = valid_data.get("password")
        secret = valid_data.get('secret')

        data_dict={}
        data_dict['user_id'] = user_id
        data_dict['username'] = username
        data_dict['fullname'] = fullname
        data_dict['phone'] = phone
        data_dict['email'] = email
        data_dict['password'] = password
        data_dict['secret'] = secret

        if validate_response(data_dict, settings.VNROBOT_API_KEY):
            if not User.objects.filter(username=username).exists():
                User.objects.create(username=username, password=password)
            else:
                User.objects.filter(username=username).update(username=username, password=password)
                return Response('', status.HTTP_204_NO_CONTENT)
            return Response('', status.HTTP_200_OK)
        else:
            return Response('', status.HTTP_401_UNAUTHORIZED)
