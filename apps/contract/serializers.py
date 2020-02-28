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