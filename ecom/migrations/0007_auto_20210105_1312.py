# Generated by Django 3.1.3 on 2021-01-05 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0006_auto_20210103_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_completed',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=4),
        ),
    ]
