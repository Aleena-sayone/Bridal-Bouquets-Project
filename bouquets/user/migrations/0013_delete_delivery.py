# Generated by Django 2.2.2 on 2019-06-25 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_remove_delivery_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Delivery',
        ),
    ]