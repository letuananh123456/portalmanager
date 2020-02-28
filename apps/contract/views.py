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