# Generated by Django 3.1.3 on 2021-01-05 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0007_auto_20210105_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=300),
        ),
    ]
