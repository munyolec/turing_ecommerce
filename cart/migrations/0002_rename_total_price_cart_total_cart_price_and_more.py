# Generated by Django 4.0.1 on 2022-01-19 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='total_price',
            new_name='total_cart_price',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='cart',
        ),
        migrations.AddField(
            model_name='entry',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
