# Generated by Django 3.2.8 on 2022-02-15 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0009_saveditem_added'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saveditem',
            name='added',
        ),
    ]
