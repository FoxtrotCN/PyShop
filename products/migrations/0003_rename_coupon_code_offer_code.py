# Generated by Django 4.0.5 on 2022-06-20 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_offer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offer',
            old_name='coupon_code',
            new_name='code',
        ),
    ]
