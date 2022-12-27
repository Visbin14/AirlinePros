# Generated by Django 2.1.2 on 2022-11-02 06:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agency', '0027_newagents'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0031_commissionhistory_add_yq_yr'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgencyDebitMemo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(null=True)),
                ('allowed_commission_amount', models.FloatField(default=0.0, null=True)),
                ('comment', models.TextField()),
                ('is_acm', models.BooleanField(default=False)),
            ],
            managers=[
                ('csv', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='CarrierDeductions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filedate', models.DateField()),
                ('file', models.FileField(upload_to='deductions')),
                ('imported_at', models.DateTimeField(auto_now_add=True)),
                ('no_bill_items', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Charges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(null=True)),
                ('type', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DailyCreditCardFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('date', models.DateField()),
                ('from_date', models.DateField(blank=True, null=True)),
                ('grand_total', models.FloatField(default=0.0, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Deduction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
                ('amount', models.FloatField(null=True)),
                ('pending', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Disbursement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filedate', models.DateField()),
                ('rundate1', models.DateField()),
                ('rundate2', models.DateField(null=True)),
                ('file1', models.FileField(upload_to='disbursements')),
                ('file2', models.FileField(null=True, upload_to='disbursements')),
                ('bank7', models.FloatField(default=0.0)),
                ('arc_deduction', models.FloatField(default=0.0)),
                ('arc_fees', models.FloatField(default=0.0)),
                ('arc_tot', models.FloatField(default=0.0)),
                ('arc_reversal', models.FloatField(default=0.0)),
                ('arc_net_disb', models.FloatField(default=0.0)),
                ('imported_at', models.DateTimeField(auto_now_add=True)),
                ('pending_deductions', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ExcelReportDownload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(upload_to='excelreports')),
                ('report_type', models.IntegerField(choices=[(1, 'Sales Details'), (2, 'Commission Report'), (3, 'ADM report')], default=1)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Remittance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ped', models.DateField(unique=True)),
                ('remittance', models.DateField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReportFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='reportfile')),
                ('ref_no', models.CharField(max_length=99, null=True)),
                ('imported_at', models.DateTimeField(auto_now_add=True)),
                ('transaction_amount', models.FloatField(null=True)),
                ('fare_amount', models.FloatField(null=True)),
                ('tax', models.FloatField(null=True)),
                ('fandc', models.FloatField(null=True)),
                ('pen', models.FloatField(null=True)),
                ('cobl_amount', models.FloatField(null=True)),
                ('std_comm', models.FloatField(null=True)),
                ('supp_comm', models.FloatField(null=True)),
                ('tax_on_comm', models.FloatField(null=True)),
                ('balance', models.FloatField(null=True)),
                ('acms', models.FloatField(default=0.0, null=True)),
                ('cc', models.FloatField(default=0.0, null=True)),
                ('ca', models.FloatField(default=0.0, null=True)),
                ('airline', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Airline')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='report_files', to='main.Country')),
            ],
            options={
                'permissions': (('view_sales_details', 'Can view sales details report'), ('download_sales_details', 'Can download sales details report'), ('view_sales_summary', 'Can view sales summary report'), ('download_sales_summary', 'Can download sales summary report'), ('view_adm', 'Can view adm report'), ('download_adm', 'Can download adm report'), ('view_sales_by', 'Can view sales by report'), ('download_sales_by', 'Can download sales by report'), ('view_all_sales', 'Can view all sales report'), ('download_all_sales', 'Can download all sales report'), ('view_year_to_year', 'Can view year to year report'), ('download_year_to_years', 'Can download year to year report'), ('view_commission', 'Can view commission report'), ('download_commission', 'Can download commission report'), ('view_sales_comparison', 'Can view sales comparison report'), ('download_sales_comparison', 'Can download sales comparison report'), ('view_top_agency', 'Can view top agency report'), ('download_top_agency', 'Can download top agency report'), ('view_monthly_yoy', 'Can view monthly yoy report'), ('download_monthly_yoy', 'Can download monthly yoy report'), ('view_airline_agency', 'Can view airline agency report'), ('download_airline_agency', 'Can download airline agency report'), ('view_agency_collection_report', 'Can view agency collection report'), ('download_agency_collection_report', 'Can download agency collection report'), ('view_upload_reports', 'Can upload report files'), ('view_upload_calendar', 'Can upload calendar files'), ('view_calendar', 'Can view calendar data'), ('view_disbursement_summary', 'Can view disbursement summary report'), ('download_disbursement_summary', 'Can download disbursement summary report'), ('view_airline_management', 'Can view airline management'), ('change_airline_management', 'Can change airline management'), ('view_weekly_sales_report', 'Can view weekly sales report'), ('download_weekly_sales', 'Can download weekly sales report')),
            },
        ),
        migrations.CreateModel(
            name='ReportPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('month', models.SmallIntegerField()),
                ('week', models.SmallIntegerField()),
                ('ped', models.DateField()),
                ('from_date', models.DateField()),
                ('remittance_date', models.DateField()),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='report_period', to='main.Country')),
            ],
        ),
        migrations.CreateModel(
            name='ReprocessFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('is_done', models.BooleanField(default=False)),
                ('message', models.TextField(blank=True)),
                ('status', models.CharField(blank=True, max_length=100)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('airline', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Airline')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reprocessfile_createdby', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reprocessfile_modifiedby', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Taxes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('type', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(blank=True, max_length=9, null=True)),
                ('ticket_no', models.CharField(blank=True, max_length=99, null=True)),
                ('issue_date', models.DateField(blank=True, null=True)),
                ('transaction_amount', models.FloatField(blank=True, default=0.0, null=True)),
                ('fare_amount', models.FloatField(default=0.0, null=True)),
                ('pen', models.FloatField(default=0.0, null=True)),
                ('pen_type', models.CharField(blank=True, max_length=99, null=True)),
                ('cobl_amount', models.FloatField(default=0.0, null=True)),
                ('std_comm_rate', models.FloatField(null=True)),
                ('std_comm_amount', models.FloatField(default=0.0, null=True)),
                ('sup_comm_rate', models.FloatField(default=0.0, null=True)),
                ('sup_comm_amount', models.FloatField(default=0.0, null=True)),
                ('tax_on_comm', models.FloatField(default=0.0, null=True)),
                ('balance', models.FloatField(default=0.0, null=True)),
                ('cpui', models.CharField(blank=True, max_length=5, null=True)),
                ('stat', models.CharField(blank=True, max_length=5, null=True)),
                ('fop', models.CharField(blank=True, max_length=5, null=True)),
                ('cc', models.FloatField(default=0.0, null=True)),
                ('ca', models.FloatField(default=0.0, null=True)),
                ('ep', models.FloatField(default=0.0, null=True)),
                ('card_type', models.CharField(blank=True, max_length=99, null=True)),
                ('card_code', models.CharField(blank=True, max_length=9, null=True)),
                ('international', models.BooleanField(default=False)),
                ('is_sale', models.BooleanField(default=True)),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agency.Agency')),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.ReportFile')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='taxes',
            name='transaction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='report.Transaction'),
        ),
        migrations.AddField(
            model_name='reportfile',
            name='report_period',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='report.ReportPeriod'),
        ),
        migrations.AddIndex(
            model_name='remittance',
            index=models.Index(fields=['ped'], name='report_remi_ped_6ffaf4_idx'),
        ),
        migrations.AddField(
            model_name='excelreportdownload',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='excelreportdownload_createdby', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='excelreportdownload',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='excelreportdownload_modifiedby', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='disbursement',
            name='airline',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Airline'),
        ),
        migrations.AddField(
            model_name='disbursement',
            name='report_period',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='report.ReportPeriod'),
        ),
        migrations.AddField(
            model_name='deduction',
            name='report',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='report.CarrierDeductions'),
        ),
        migrations.AddField(
            model_name='dailycreditcardfile',
            name='airline',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Airline'),
        ),
        migrations.AddField(
            model_name='dailycreditcardfile',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dailycreditcardfile_createdby', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dailycreditcardfile',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dailycreditcardfile_modifiedby', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='charges',
            name='transaction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='report.Transaction'),
        ),
        migrations.AddField(
            model_name='carrierdeductions',
            name='airline',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Airline'),
        ),
        migrations.AddField(
            model_name='carrierdeductions',
            name='report_period',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='report.ReportPeriod'),
        ),
        migrations.AddField(
            model_name='agencydebitmemo',
            name='transaction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='report.Transaction', unique=True),
        ),
        migrations.AddIndex(
            model_name='transaction',
            index=models.Index(fields=['agency', 'report', 'transaction_type'], name='report_tran_agency__1523b6_idx'),
        ),
        migrations.AddIndex(
            model_name='transaction',
            index=models.Index(fields=['transaction_type', 'ticket_no', 'issue_date', 'transaction_amount', 'fare_amount', 'pen', 'pen_type', 'cobl_amount', 'std_comm_rate', 'std_comm_amount', 'sup_comm_rate', 'sup_comm_amount', 'tax_on_comm', 'balance', 'cpui', 'stat', 'fop', 'cc', 'ca', 'ep', 'card_type', 'card_code', 'international'], name='report_tran_transac_153418_idx'),
        ),
        migrations.AddIndex(
            model_name='taxes',
            index=models.Index(fields=['transaction', 'amount', 'type'], name='report_taxe_transac_f834de_idx'),
        ),
        migrations.AddIndex(
            model_name='reportperiod',
            index=models.Index(fields=['ped', 'year', 'month', 'from_date', 'country'], name='report_repo_ped_c0edb7_idx'),
        ),
        migrations.AddIndex(
            model_name='reportfile',
            index=models.Index(fields=['report_period', 'airline', 'transaction_amount', 'fare_amount', 'tax', 'fandc', 'pen', 'cobl_amount', 'std_comm', 'supp_comm', 'tax_on_comm', 'balance', 'acms', 'cc', 'ca'], name='report_repo_report__3ded25_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='disbursement',
            unique_together={('airline', 'filedate'), ('airline', 'report_period')},
        ),
        migrations.AddIndex(
            model_name='charges',
            index=models.Index(fields=['transaction', 'amount', 'type'], name='report_char_transac_e70e0d_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='carrierdeductions',
            unique_together={('airline', 'report_period')},
        ),
        migrations.AddIndex(
            model_name='agencydebitmemo',
            index=models.Index(fields=['transaction'], name='report_agen_transac_605d2c_idx'),
        ),
    ]