# Generated by Django 4.1.7 on 2023-03-10 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_customer_options_alter_order_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=200),
        ),
    ]
