# Generated by Django 2.1.2 on 2018-12-20 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20181210_1001'),
        ('agency', '0020_auto_20181212_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='agencytype',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='agencytype', to='main.Country'),
        ),
        migrations.AlterField(
            model_name='agencytype',
            name='name',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='agencytype',
            unique_together={('name', 'country')},
        ),
    ]
