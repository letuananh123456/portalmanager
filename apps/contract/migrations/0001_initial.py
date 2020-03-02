# Generated by Django 2.2.2 on 2020-02-29 09:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ConvertProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField(default=0)),
                ('type_product', models.IntegerField(choices=[(1, 'Tử kỳ'), (2, 'Sức khoẻ'), (3, 'Du lịch'), (4, 'Ô tô'), (5, 'Đầu tư')], default=0)),
                ('company', models.IntegerField(default=0)),
                ('conversion_rate', models.FloatField(default=0.0)),
                ('commission_rate', models.FloatField(default=0.0)),
                ('is_nhan_tho', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='OderProductPortal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid_mua', models.CharField(max_length=200)),
                ('fullname', models.CharField(max_length=200)),
                ('number_YCBH', models.CharField(max_length=200)),
                ('number_policy', models.CharField(max_length=200)),
                ('company', models.IntegerField(choices=[(1, 'Bảo Việt'), (2, 'Cathay')])),
                ('name_product', models.CharField(max_length=200)),
                ('sumit_date', models.DateField()),
                ('release_date', models.DateField()),
                ('ack_date', models.DateField()),
                ('ack_status', models.IntegerField(choices=[(0, 'Chưa ACK'), (1, 'Đã ACK')], default=0)),
                ('status_policy', models.IntegerField(default=0)),
                ('premium', models.IntegerField(default=0)),
                ('bv_premium', models.IntegerField(default=0)),
                ('status_payment', models.IntegerField(choices=[(0, 'Chưa thanh toán'), (1, 'Đã Thanh Toán'), (2, 'Thanh Toán Thất Bại')], default=0)),
                ('is_update', models.BooleanField(default=False)),
                ('type_product', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contract.ConvertProduct')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]