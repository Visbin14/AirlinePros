# Generated by Django 2.1.2 on 2018-11-07 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0006_auto_20181106_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agency',
            name='state',
            field=models.CharField(blank=True, max_length=99, null=True),
        ),
    ]
