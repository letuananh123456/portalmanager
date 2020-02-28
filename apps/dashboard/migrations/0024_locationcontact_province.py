# Generated by Django 2.1.7 on 2019-04-04 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0023_daycontact'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocationContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_customer', models.IntegerField(default=0)),
                ('created_time', models.DateTimeField(null=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Channel')),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name_province', models.CharField(max_length=200)),
            ],
        ),
    ]
