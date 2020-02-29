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


class InfoOrderUserApi(APIView):
    """
    API này để lưu cập nhật thông tin user khi có sự thay đổi từ sàn thương mại điện tử
    Cập nhật thành công: 200
    """
    def post(self, request, format=None):
        valid_data = validate_data(user_sers.InfoUserOrderSerial, request.data)

        name = valid_data.get('name')
        sotienquybaohiem = valid_data.get('sotienquybaohiem')
        tylephi = valid_data.get('tylephi')
        product_type = valid_data.get('product_type')
        company = valid_data.get('company')
        sonamhopdong = valid_data.get('sonamhopdong')
        sonamdongphi = valid_data.get('sonamdongphi')

        home_age = valid_data.get('home_age')
        thanh_pho = valid_data.get('thanh_pho')
        huyen = valid_data.get('huyen')
        address = valid_data.get('address')
        phone = valid_data.get('phone')
        email = valid_data.get('email')
        address1 = valid_data.get('address1')

        ma_hoa_don = valid_data.get('ma_hoa_don')
        so_tien = valid_data.get('so_tien')
        loai_san_pham = valid_data.get('loai_san_pham')
        so_dien_thoai = valid_data.get('so_dien_thoai')
        status1 = valid_data.get('status1')
        created_at = valid_data.get('created_at')
        vnp_TransactionNo = valid_data.get('vnp_TransactionNo')
        product_id = valid_data.get('product_id')
        order_status = valid_data.get('order_status')
        secret = valid_data.get('secret')


        data_dict={}
        data_dict['name'] = name
        data_dict['sotienquybaohiem'] = sotienquybaohiem
        data_dict['tylephi'] = tylephi
        data_dict['product_type'] = product_type
        data_dict['company'] = company
        data_dict['sonamhopdong'] = sonamhopdong
        data_dict['sonamdongphi'] = sonamdongphi

        data_dict['home_age'] = home_age
        data_dict['thanh_pho'] = thanh_pho
        data_dict['huyen'] = huyen
        data_dict['address'] = address
        data_dict['phone'] = phone
        data_dict['email'] = email
        data_dict['address1'] = address1

        data_dict['ma_hoa_don'] = ma_hoa_don
        data_dict['so_tien'] = so_tien
        data_dict['loai_san_pham'] = loai_san_pham
        data_dict['so_dien_thoai'] = so_dien_thoai
        data_dict['status1'] = status1
        data_dict['created_at'] = created_at
        data_dict['vnp_TransactionNo'] = vnp_TransactionNo
        data_dict['product_id'] = product_id
        data_dict['order_status'] = order_status
        data_dict['secret'] = secret
        
        if validate_response(data_dict,settings.VNROBOT_API_KEY):
            return Response('', status.HTTP_200_OK)
        else:
            return Response('', status.HTTP_401_UNAUTHORIZED)
