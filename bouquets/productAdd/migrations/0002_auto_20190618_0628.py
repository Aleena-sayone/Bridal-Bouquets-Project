# Generated by Django 2.2.2 on 2019-06-18 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productAdd', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.TextField(max_length=100),
        ),
    ]
