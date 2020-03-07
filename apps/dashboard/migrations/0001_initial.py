# Generated by Django 2.2.2 on 2020-03-07 02:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgentTotal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_agent', models.IntegerField(default=0)),
                ('created_time', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name_chanel', models.CharField(max_length=200)),
                ('color', models.TextField(default='rgb(66, 134, 244)')),
            ],
        ),
        migrations.CreateModel(
            name='DayContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_customer', models.IntegerField(default=0)),
                ('created_time', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DaySuccess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_customer', models.IntegerField(default=0)),
                ('number_policy', models.IntegerField(default=0)),
                ('created_time', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteBenefit',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name_benefit', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteProduct',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name_product', models.CharField(max_length=200)),
                ('sa', models.IntegerField(default=0)),
                ('policy_term', models.IntegerField(default=0)),
                ('payment_term', models.IntegerField(default=0)),
                ('ways_to_get_benefit', models.CharField(max_length=200)),
                ('created_time', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MainBenefit',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name_benefit', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MainProduct',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('number_customer', models.IntegerField(default=0)),
                ('name_product', models.CharField(max_length=200)),
                ('created_time', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MonthContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_customer', models.IntegerField(default=0)),
                ('created_time', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MonthSuccess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_customer', models.IntegerField(default=0)),
                ('number_policy', models.IntegerField(default=0)),
                ('created_time', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NewAgent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_agent', models.IntegerField(default=0)),
                ('created_time', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name_province', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SupBenefit',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name_benefit', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SupProduct',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('number_customer', models.IntegerField(default=0)),
                ('name_product', models.CharField(max_length=200)),
                ('created_time', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sup_Product_Benefit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('benefit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.SupBenefit')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.SupProduct')),
            ],
        ),
        migrations.CreateModel(
            name='Main_Product_Benefit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('benefit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.MainBenefit')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.MainProduct')),
            ],
        ),
        migrations.CreateModel(
            name='LocationContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_customer', models.IntegerField(default=0)),
                ('created_time', models.DateTimeField(null=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Province')),
            ],
        ),
        migrations.CreateModel(
            name='Favorite_Product_Benefit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('benefit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.FavoriteBenefit')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.FavoriteProduct')),
            ],
        ),
        migrations.CreateModel(
            name='ChannelSuccess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_customer', models.IntegerField(default=0)),
                ('number_policy', models.IntegerField(default=0)),
                ('created_time', models.DateTimeField(null=True)),
                ('distribution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Channel')),
            ],
        ),
        migrations.CreateModel(
            name='ChannelContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_customer', models.IntegerField(default=0)),
                ('created_time', models.DateTimeField(null=True)),
                ('distribution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Channel')),
            ],
        ),
        migrations.CreateModel(
            name='AgentChannel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_agent', models.IntegerField(default=0)),
                ('created_time', models.DateTimeField(null=True)),
                ('distribution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Channel')),
            ],
        ),
    ]
