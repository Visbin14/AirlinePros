# Generated by Django 2.1.2 on 2018-11-26 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_country_flag'),
        ('account', '0008_remove_user_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='countries',
            field=models.ManyToManyField(blank=True, null=True, related_name='users', to='main.Country'),
        ),
    ]
