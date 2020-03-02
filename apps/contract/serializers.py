from rest_framework import serializers


class UpdateContractApiSer(serializers.Serializer):
    user = serializers.CharField()
    userid_mua = serializers.CharField() #user id mua
    fullname = serializers.CharField()
    number_YCBH = serializers.CharField()
    number_policy = serializers.CharField()
    company = serializers.IntegerField() 
    name_product = serializers.CharField()
    type_product = serializers.IntegerField()
    sumit_date = serializers.DateField()
    release_date = serializers.DateField()
    ack_date = serializers.DateField()
    ack_status = serializers.IntegerField()
    status_policy = serializers.IntegerField()
    premium = serializers.IntegerField()
    bv_premium = serializers.IntegerField()
    status_payment = serializers.IntegerField()
    is_update = serializers.BooleanField()


class InfoUserOrderSerial(serializers.Serializer):
    name = serializers.CharField()
    sotienquybaohiem = serializers.CharField()
    tylephi = serializers.CharField()
    product_type = serializers.CharField()
    company = serializers.CharField()
    sonamhopdong = serializers.IntegerField()
    sonamdongphi = serializers.IntegerField()

    home_age = serializers.IntegerField()
    thanh_pho = serializers.CharField()
    huyen = serializers.CharField()
    address = serializers.CharField()
    phone = serializers.CharField()
    email = serializers.CharField()
    address1 = serializers.CharField()

    ma_hoa_don = serializers.CharField()
    so_tien = serializers.IntegerField()
    loai_san_pham = serializers.CharField() 
    so_dien_thoai = serializers.CharField()
    status1 = serializers.IntegerField()
    created_at = serializers.CharField()
    vnp_TransactionNo = serializers.CharField()
    product_id = serializers.IntegerField()
    order_status = serializers.IntegerField()
    secret = serializers.CharField()
