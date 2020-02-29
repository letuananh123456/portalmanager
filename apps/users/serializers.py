from rest_framework import serializers
from django.contrib.auth.models import User
from .models import LoginHistory


class LoginEmailValidator(serializers.Serializer):
    username = serializers.CharField(required=True, allow_blank=False)
    password = serializers.CharField(required=True, allow_blank=False)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id', 'username', 'email',
        )


class TokenSerializer(serializers.Serializer):
    access_token = serializers.CharField()
    user = UserSerializer(read_only=True)


class LoginHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = LoginHistory
        fields = (
            'start_date', 'end_date', 'num_date',
        )


class UpdateUsertApiSer(serializers.Serializer):
    user_id = serializers.CharField()
    username = serializers.CharField()
    fullname = serializers.CharField()
    phone = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField()


class InfoUserOrderSerial(serializers.Serializer):
    name = serializers.CharField()
    sotienquybaohiem = serializers.CharField()
    tylephi = serializers.CharField()
    product_type = serializers.CharField()
    company = serializers.CharField()
    sonamhopdong = serializers.CharField()
    sonamdongphi = serializers.CharField()

    home_age = serializers.CharField()
    thanh_pho = serializers.CharField()
    huyen = serializers.CharField()
    address = serializers.CharField()
    phone = serializers.CharField()
    email = serializers.CharField()
    address1 = serializers.CharField()

    ma_hoa_don = serializers.CharField()
    so_tien = serializers.CharField()
    loai_san_pham = serializers.CharField() 
    so_dien_thoai = serializers.CharField()
    status1 = serializers.CharField()
    created_at = serializers.CharField()
    vnp_TransactionNo = serializers.CharField()
    product_id = serializers.CharField()
    order_status = serializers.CharField()
    secret = serializers.CharField()
