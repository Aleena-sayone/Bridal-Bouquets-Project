# Generated by Django 2.2.2 on 2019-06-24 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productAdd', '0015_auto_20190624_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_date',
            field=models.DateTimeField(null=True),
        ),
    ]
