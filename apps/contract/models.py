from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
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


class Collaborators(models.Model):
    user = models.CharField(max_length=200)
    userid_mua = models.CharField(max_length=200) #user id mua
    fullname = models.CharField(max_length=200)
    number_YCBH = models.CharField(max_length=200)
    number_policy = models.CharField(max_length=200)
    company = models.IntegerField(default=0)
    name_product = models.CharField(max_length=200)
    type_product = models.IntegerField(default=0)
    sumit_date = models.DateField()
    release_date = models.DateField()
    ack_date = models.DateField()
    ack_status = models.IntegerField(default=0)
    status_policy = models.IntegerField(default=0)
    premium = models.IntegerField(default=0)
    bv_premium = models.IntegerField(default=0)
    status_payment = models.IntegerField(default=0)
    is_update = models.BooleanField()


class ContractInformation(models.Model):
    buyer = models.CharField(max_length=200)
    buyer_sex = models.IntegerField(default=0)
    buyer_cmnd = models.CharField(max_length=200)
    buyer_image = models.ImageField(upload_to = 'contract/', null=True)
    buyer_birth = models.DateField()
    buyer_phone = models.CharField(max_length=200)
    buyer_email = models.CharField(max_length=200)
    receiver = models.CharField(max_length=200)
    receiver_cmnd = models.CharField(max_length=200)
    receiver_image = models.ImageField(upload_to = 'contract/', null=True)
    receiver_birth = models.DateField()
    receiver_sex = models.IntegerField(default=0)
    beneficiary = models.CharField(max_length=200)
    beneficiary_cmnd = models.CharField(max_length=200)
    beneficiary_relationship = models.IntegerField(default=0)
    beneficiary_image = models.ImageField(upload_to = 'contract/', null=True)
    beneficiary_birth = models.DateField()
    beneficiary_sex = models.IntegerField(default=0)
    presenter_name = models.CharField(max_length=200)
    presenter_id = models.IntegerField(default=0)
    product_name = models.IntegerField(default=0)
    product_company = models.CharField(max_length=200)
    product_phi = models.IntegerField(default=0)
    product_year_contract = models.IntegerField(default=0)
    product_year_phi = models.IntegerField(default=0)
    product_frequency_phi = models.IntegerField(default=0)
    product_insurance_money = models.IntegerField(default=0)
    supplementary_product_name = models.IntegerField(default=0)
    supplementary_product_company = models.CharField(max_length=200)
    supplementary_product_phi = models.IntegerField(default=0)
    supplementary_product_year_contract = models.IntegerField(default=0)
    supplementary_product_year_phi = models.IntegerField(default=0)
    supplementary_product_frequency_phi = models.IntegerField(default=0)
    supplementary_product_insurance_money = models.IntegerField(default=0)
    pay_main_product = models.IntegerField(default=0)
    pay_phu_product = models.IntegerField(default=0)
    pay_total_phi = models.IntegerField(default=0)
    pay_tax = models.IntegerField(default=0)
    total_payment_amount = models.IntegerField(default=0)
    information_received = models.CharField(max_length=200)
    information_received_name = models.CharField(max_length=200)
    information_received_email = models.CharField(max_length=200)
    information_received_phone = models.CharField(max_length=200)
    information_received_address = models.CharField(max_length=200)



