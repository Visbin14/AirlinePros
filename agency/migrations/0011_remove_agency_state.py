# Generated by Django 2.1.2 on 2018-11-08 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0010_auto_20181107_1050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agency',
            name='state',
        ),
    ]
