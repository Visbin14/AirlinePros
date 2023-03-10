# Generated by Django 2.1.2 on 2018-11-14 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0017_auto_20181114_0828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agency',
            name='status_iata',
            field=models.CharField(blank=True, choices=[('A', 'Active'), ('D', 'Default Information'), ('R', 'Reviews/Notices of Termination'), ('S', 'Reinstatements'), ('T', 'Terminations And Closures'), ('I', 'Irregularities And Admin Noncompliance')], default='A', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='statuschange',
            name='new_status',
            field=models.CharField(max_length=99),
        ),
        migrations.AlterField(
            model_name='statuschange',
            name='old_status',
            field=models.CharField(max_length=99),
        ),
    ]
