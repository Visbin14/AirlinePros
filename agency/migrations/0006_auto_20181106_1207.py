# Generated by Django 2.1.2 on 2018-11-06 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0005_auto_20181106_0850'),
    ]

    operations = [
        migrations.AddField(
            model_name='agency',
            name='home_agency',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='agencylistreference',
            name='file',
            field=models.FileField(upload_to='agencyfiles/'),
        ),
    ]
