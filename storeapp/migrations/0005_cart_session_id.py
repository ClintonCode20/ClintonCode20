# Generated by Django 3.2.8 on 2022-02-01 17:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0004_remove_cart_session_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='session_id',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
