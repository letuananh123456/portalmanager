import binascii
import os
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
# Create your models here.
from django.contrib.auth.models import AbstractUser

TOKEN_LENGTH = 64
RESET_TOKEN_LENGTH = 10
CONFIRM_EMAIL_TOKEN_LENGTH = 128


def generate_access_token(user_id):
    num_bytes = TOKEN_LENGTH // 2
    token = binascii.hexlify(os.urandom(num_bytes)).decode()
    access_token = '{user_id}:{token}'.format(
        user_id=user_id,
        token=token,
    )
    return access_token


class User(AbstractUser):
    GIOITINH = (('0','Nữ'),('1','Nam'))
    hoten = models.CharField(max_length=30,verbose_name='Họ tên',null=True)
    cmnd = models.CharField(max_length=15, verbose_name='CMND/ Thẻ căn cước')
    ngaysinh = models.DateField(verbose_name="Ngày sinh",null=True,)
    gioitinh = models.CharField(max_length=1,choices=GIOITINH, verbose_name="Giới tính")
    phong = models.CharField(max_length=200, verbose_name="Phòng")
    chucvu = models.CharField(max_length=200, verbose_name="Chức vụ")

class Token(models.Model):
    """
    The default authorization token model.
    """
    key = models.CharField(_("Key"), max_length=128, primary_key=True)
    user = models.ForeignKey(
        User, related_name='tokens',
        on_delete=models.CASCADE, verbose_name=_("User")
    )
    created = models.DateTimeField(_("Created"), auto_now_add=True)

    class Meta:
        db_table = 'token'

    def __str__(self):
        return 'Token (user {}): {}'.format(self.user_id, self.key)


class LoginHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(auto_now=True)
    num_date = models.IntegerField(default=1)

    class Meta:
        db_table = 'login_history'


class ResetToken(models.Model):
    reset_token = models.CharField(_("Reset token"), primary_key=True, max_length=RESET_TOKEN_LENGTH)
    user = models.ForeignKey(
        User, related_name='reset_token',
        on_delete=models.CASCADE, verbose_name=_('user')
    )
    created_at = models.DateTimeField(_("Created"), auto_now_add=True)

    class Meta:
        db_table = 'reset_token'

    def save(self, *args, **kwargs):
        if not self.reset_token:
            self.reset_token = self.generate_reset_token()
        return super(ResetToken, self).save(*args, **kwargs)

    def generate_reset_token(self):
        num_bytes = RESET_TOKEN_LENGTH // 2
        return binascii.hexlify(os.urandom(num_bytes)).decode()

    def __str__(self):
        return 'ResetToken (user {}): {}'.format(self.user_id, self.reset_token)


class ConfirmEmailToken(models.Model):
    token = models.CharField(_("token"), primary_key=True, max_length=CONFIRM_EMAIL_TOKEN_LENGTH)
    user = models.ForeignKey(
        User, related_name='confirm_email_token',
        on_delete=models.CASCADE, verbose_name=_('user')
    )
    created_at = models.DateTimeField(_('Created'), auto_now_add=True)

    class Meta:
        db_table = 'confirm_email_token'

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = self.generate_confirm_email_token()
        return super(ConfirmEmailToken, self).save(*args, **kwargs)

    def generate_confirm_email_token(self):
        num_bytes = CONFIRM_EMAIL_TOKEN_LENGTH // 2
        return binascii.hexlify(os.urandom(num_bytes)).decode()

    def __str__(self):
        return 'ConfirmEmailToken (user {}): {}'.format(self.user, self.token)


class Notification(models.Model):
    title = models.TextField(blank=True, default='')
    body = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'notification'
        ordering = ['-created_at']


class UserNotification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE, related_name='user_notifications')
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user_notification'
        ordering = ['-created_at']


class UserCTV(models.Model):

    user_id = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    fullname = models.CharField(max_length=200)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.username




