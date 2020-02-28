from django.utils import timezone
import random
import math
import requests
from django.conf import settings
from apps.contract.models import OderProductPortal


def order_info_api(user_id):
    data = OderProductPortal.objects.get(user_id=user_id)
    url= settings.PORTAL_BIHAMA_RETURN_URL+"insert-order/"
    json_data={
        'user_id':data.userid,
        'userid_mua':data.userid_mua,
        'fullname':data.fullname,
        'number_YCBH':data.number_YCBH,
        'number_policy':data.number_policy,
        'company':data.company,
        'name_product':data.name_product,
        'type_product':data.product_id,
        'sumit_date':data.sumit_date,
        'release_date':data.release_date,
        'ack_date':data.ack_date,
        'ack_status':data.ack_status,
        'status_policy':data.status_policy,
        'premium':data.premium,
        'bv_premium':data.bv_premium,
        'status_payment':data.status_payment,
        'is_update' :data.is_update
    }
    r = requests.post(url, json=json_data)
    return r.status_code