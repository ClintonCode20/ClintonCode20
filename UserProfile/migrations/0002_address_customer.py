# Generated by Django 3.2.8 on 2022-02-09 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='customer',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='UserProfile.customer'),
        ),
    ]
