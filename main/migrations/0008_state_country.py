# Generated by Django 2.1.2 on 2018-11-08 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_airline_product_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Country'),
        ),
    ]
