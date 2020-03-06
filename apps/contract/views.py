from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status
import json
import requests 
from apps.core.utils import validate_data

# Create your views here.
from . import serializers as contract_sers
from . import models as contract_models
from . import utils as contract_utils
from apps.core.utils import validate_data, validate_response
from apps.core.exceptions import HTTP401AuthenticationError, HTTP404NotFoundError, HTTP409ConflictError
from django.conf import settings

class UpdateContractApi(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        valid_data = validate_data(contract_sers.UpdateContractApiSer, request.data)
        user = valid_data.get('user')
        userid_mua = valid_data.get('userid_mua')
        fullname = valid_data.get('fullname')
        number_YCBH = valid_data.get('number_YCBH')
        number_policy = valid_data.get('number_policy')
        company = valid_data.get('company')
        name_product = valid_data.get('name_product')
        type_product = valid_data.get('type_product')
        sumit_date = valid_data.get('sumit_date')
        release_date = valid_data.get('release_date')
        ack_date = valid_data.get('ack_date')
        ack_status = valid_data.get('ack_status')
        status_policy = valid_data.get('status_policy')
        premium = valid_data.get('premium')
        bv_premium = valid_data.get('bv_premium')
        status_payment = valid_data.get('status_payment')
        is_update = valid_data.get('status_payment')

        OderProductPortal.objects.filter(user=user).update(userid_mua=userid_mua, fullname=fullname, number_YCBH=number_YCBH, number_policy=number_policy, company=company, name_product=name_product,type_product=type_product, sumit_date=sumit_date, release_date=release_date, ack_date=ack_date, ack_status=ack_status, status_policy=status_policy, premium=premium, bv_premium=bv_premium, status_payment=status_payment, is_update=is_update)
        return Response(status=status.HTTP_200_OK)


class InfoOrderHomeUserApi(APIView):
    """
    API này để lưu cập nhật thông tin đơn hàng của user khi có sự thay đổi từ sàn thương mại điện tử
    Cập nhật thành công: 200
    """
    def post(self, request, format=None):
        valid_data = validate_data(contract_sers.InfoUserOrderSerial, request.data)

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
            data=contract_models.OderProductHomeModel.objects.create(
                name=name,sotienquybaohiem=sotienquybaohiem,tylephi=tylephi,product_type=product_type,
                company=company,sonamhopdong=sonamhopdong,sonamdongphi=sonamdongphi,home_age=home_age,
                thanh_pho=thanh_pho,huyen=huyen,address=address,phone=phone,email=email,address1=address1,
                ma_hoa_don=ma_hoa_don,so_tien=so_tien,loai_san_pham=loai_san_pham,so_dien_thoai=so_dien_thoai,
                status1=status1,created_at=created_at,vnp_TransactionNo=vnp_TransactionNo,product_id=product_id,
                order_status=order_status,secret=secret)
            return Response('', status.HTTP_200_OK)
        else:
            return Response('', status.HTTP_401_UNAUTHORIZED)





