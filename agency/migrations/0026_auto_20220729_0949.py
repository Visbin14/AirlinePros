# Generated by Django 2.1.2 on 2022-07-29 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0025_auto_20220417_0835'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agency',
            options={'permissions': (('download_agencylist', 'Can download agency list'),)},
        ),
    ]