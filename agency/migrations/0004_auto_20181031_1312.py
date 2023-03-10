# Generated by Django 2.1.2 on 2018-10-31 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0003_auto_20181031_1306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statushistory',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='statushistory',
            name='modified_by',
        ),
        migrations.RenameField(
            model_name='statuschange',
            old_name='status',
            new_name='new_status',
        ),
        migrations.RemoveField(
            model_name='statuschange',
            name='date',
        ),
        migrations.RemoveField(
            model_name='statuschange',
            name='status_history',
        ),
        migrations.AddField(
            model_name='agency',
            name='status',
            field=models.CharField(blank=True, choices=[('A', 'Active'), ('D', 'Defaulted'), ('R', 'Revoked'), ('S', 'Reinstated'), ('T', 'Terminated')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='statuschange',
            name='agency',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='status_changes', to='agency.Agency'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statuschange',
            name='old_status',
            field=models.CharField(choices=[('A', 'Active'), ('D', 'Defaulted'), ('R', 'Revoked'), ('S', 'Reinstated'), ('T', 'Terminated')], default=1, max_length=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='StatusHistory',
        ),
    ]
