# Generated by Django 2.1.2 on 2019-02-11 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_auto_20190206_1250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='airline',
            name='gsa_commision',
        ),
        migrations.RemoveField(
            model_name='airline',
            name='iata_coordination_fee',
        ),
        migrations.RemoveField(
            model_name='airline',
            name='max_commission_rate',
        ),
    ]
