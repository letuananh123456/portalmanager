# Generated by Django 2.1.7 on 2019-04-17 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0034_auto_20190417_0459'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite_product_benefit',
            name='benefit',
        ),
        migrations.RemoveField(
            model_name='favorite_product_benefit',
            name='product',
        ),
        migrations.DeleteModel(
            name='Favorite_Product_Benefit',
        ),
        migrations.DeleteModel(
            name='FavoriteBenefit',
        ),
        migrations.DeleteModel(
            name='FavoriteProduct',
        ),
    ]
