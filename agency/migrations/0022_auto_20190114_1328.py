# Generated by Django 2.1.2 on 2019-01-14 13:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0024_airline_accepts_uatp'),
        ('agency', '0021_auto_20181220_0631'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgencyCollection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=300, null=True)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='agencycollections', to='main.Country')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agencycollection_createdby', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agencycollection_modifiedby', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='agency',
            name='agency_collection',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='collection_agencies', to='agency.AgencyCollection'),
        ),
        migrations.AlterUniqueTogether(
            name='agencycollection',
            unique_together={('name', 'country')},
        ),
    ]
