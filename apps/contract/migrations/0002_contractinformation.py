# Generated by Django 2.2.2 on 2020-03-02 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContractInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer', models.CharField(max_length=200)),
                ('buyer_sex', models.IntegerField(default=0)),
                ('buyer_cmnd', models.CharField(max_length=200)),
                ('buyer_image', models.CharField(max_length=200)),
                ('buyer_birth', models.DateField()),
                ('buyer_phone', models.CharField(max_length=200)),
                ('buyer_email', models.CharField(max_length=200)),
                ('receiver', models.CharField(max_length=200)),
                ('receiver_cmnd', models.CharField(max_length=200)),
                ('receiver_image', models.CharField(max_length=200)),
                ('receiver_birth', models.DateField()),
                ('receiver_sex', models.IntegerField(default=0)),
                ('beneficiary', models.CharField(max_length=200)),
                ('beneficiary_cmnd', models.CharField(max_length=200)),
                ('beneficiary_relationship', models.IntegerField(default=0)),
                ('beneficiary_image', models.CharField(max_length=200)),
                ('beneficiary_birth', models.DateField()),
                ('beneficiary_sex', models.IntegerField(default=0)),
                ('presenter_name', models.CharField(max_length=200)),
                ('presenter_id', models.IntegerField(default=0)),
                ('product_name', models.IntegerField(default=0)),
                ('product_company', models.CharField(max_length=200)),
                ('product_phi', models.IntegerField(max_length=200)),
                ('product_year_contract', models.IntegerField(default=0)),
                ('product_year_phi', models.IntegerField(default=0)),
                ('product_frequency_phi', models.IntegerField(max_length=200)),
                ('product_insurance_money', models.IntegerField(max_length=200)),
                ('supplementary_product_name', models.IntegerField(default=0)),
                ('supplementary_product_company', models.CharField(max_length=200)),
                ('supplementary_product_phi', models.IntegerField(max_length=200)),
                ('supplementary_product_year_contract', models.IntegerField(default=0)),
                ('supplementary_product_year_phi', models.IntegerField(default=0)),
                ('supplementary_product_frequency_phi', models.IntegerField(max_length=200)),
                ('supplementary_product_insurance_money', models.IntegerField(max_length=200)),
                ('pay_main_product', models.IntegerField(default=0)),
                ('pay_phu_product', models.IntegerField(default=0)),
                ('pay_total_phi', models.IntegerField(default=0)),
                ('pay_tax', models.IntegerField(default=0)),
                ('total_payment_amount', models.IntegerField(default=0)),
                ('information_received', models.CharField(max_length=200)),
                ('information_received_name', models.CharField(max_length=200)),
                ('information_received_email', models.CharField(max_length=200)),
                ('information_received_phone', models.CharField(max_length=200)),
                ('information_received_address', models.CharField(max_length=200)),
            ],
        ),
    ]