# Generated by Django 2.2.2 on 2020-03-07 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_hoten'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ngaysinh',
            field=models.DateField(null=True, verbose_name='Ngày sinh'),
        ),
    ]
