from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ConvertProduct(models.Model):
    """
    Thông  tin cấu hình loại sản phẩm phải đồng bộ theo bên sàn 
    xem ở README.MD ở code sàn thương mại
    """
    TU_KY = 1
    SUC_KHOE = 2
    DU_LICH = 3
    O_TO = 4
    DAU_TU = 5
    LOAI_PRODUCT = [
        (TU_KY, 'Tử kỳ'),
        (SUC_KHOE, 'Sức khoẻ'),
        (DU_LICH, 'Du lịch'),
        (O_TO, 'Ô tô'),
        (DAU_TU, 'Đầu tư')
    ]

    product_id = models.IntegerField(default=0)
    type_product = models.IntegerField(default=0, choices=LOAI_PRODUCT)
    company = models.IntegerField(default=0)
    conversion_rate = models.FloatField(default=0.0)
    commission_rate = models.FloatField(default=0.0)
    is_nhan_tho = models.BooleanField(default=True)


class OderProductPortal(models.Model):
    ACK_STATUS = [
        (0, 'Chưa ACK'),
        (1, 'Đã ACK')
    ]
    CONG_TY_BAO_HIEM = [
        (1, 'Bảo Việt'),
        (2, 'Cathay')
    ]  
    TRANG_THAI_THANH_TOAN = [
        (0, 'Chưa thanh toán'),
        (1, 'Đã Thanh Toán'),
        (2, 'Thanh Toán Thất Bại')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE) #sponser
    userid_mua = models.CharField(max_length=200) #user id mua
    fullname = models.CharField(max_length=200)
    number_YCBH = models.CharField(max_length=200)
    number_policy = models.CharField(max_length=200)
    company = models.IntegerField(choices=CONG_TY_BAO_HIEM) 
    name_product = models.CharField(max_length=200)
    type_product = models.ForeignKey(ConvertProduct, default=None, null=True, on_delete=models.SET_NULL)
    sumit_date = models.DateField()
    release_date = models.DateField()
    ack_date = models.DateField()
    ack_status = models.IntegerField(default=0,choices=ACK_STATUS) # trạng thái ack
    status_policy = models.IntegerField(default=0)
    premium = models.IntegerField(default=0) # số tiền của hợp đồng
    bv_premium = models.IntegerField(default=0)
    status_payment = models.IntegerField(default=0, choices=TRANG_THAI_THANH_TOAN)
    is_update = models.BooleanField(default=False)


class OderProductHomeModel(models.Model):
    name = models.CharField(max_length=200)
    sotienquybaohiem = models.CharField(max_length=200)
    tylephi = models.CharField(max_length=200)
    product_type = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    sonamhopdong = models.IntegerField(default=0)
    sonamdongphi = models.IntegerField(default=0)

    home_age = models.IntegerField(default=0)
    thanh_pho = models.CharField(max_length=200)
    huyen = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address1 = models.CharField(max_length=200)

    ma_hoa_don = models.CharField(max_length=200)
    so_tien = models.IntegerField(default=0)
    loai_san_pham = models.CharField(default='',max_length=200) 
    so_dien_thoai = models.CharField(max_length=200)
    status1 = models.IntegerField(default=0)
    created_at = models.CharField(max_length=200)
    vnp_TransactionNo = models.CharField(max_length=200)
    product_id = models.IntegerField(default=0)
    order_status = models.IntegerField(default=0)
    secret = models.CharField(max_length=200)
