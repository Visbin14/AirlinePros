# Generated by Django 2.1.2 on 2018-10-29 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_country_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='code',
            field=models.CharField(default='US', max_length=2),
            preserve_default=False,
        ),
    ]
