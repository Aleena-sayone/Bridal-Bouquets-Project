# Generated by Django 2.2.2 on 2019-06-22 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productAdd', '0008_auto_20190622_0257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='total',
        ),
        migrations.AddField(
            model_name='cart',
            name='update',
            field=models.BooleanField(null=True),
        ),
    ]
