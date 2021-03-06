# Generated by Django 3.2.3 on 2021-05-27 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('code', models.CharField(db_index=True, max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('rut', models.CharField(blank=True, max_length=12, null=True, verbose_name='RUT')),
                ('addr_line_1', models.CharField(max_length=40)),
                ('addr_line_2', models.CharField(blank=True, max_length=30, null=True)),
                ('locality', models.CharField(blank=True, max_length=20, null=True)),
                ('city', models.CharField(blank=True, max_length=20, null=True)),
                ('state', models.CharField(blank=True, max_length=20, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=20, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logo')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creacion')),
                ('modification_date', models.DateTimeField(auto_now=True, verbose_name='Fecha Modificacion')),
            ],
            options={
                'verbose_name': 'Warehouse',
                'verbose_name_plural': 'Warehouses',
                'db_table': 'warehouse',
            },
        ),
        migrations.CreateModel(
            name='LocnPrinterMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reserve_locn', models.CharField(max_length=100)),
                ('staging_locn', models.CharField(max_length=100)),
                ('printer_name', models.CharField(max_length=100)),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creacion')),
                ('modification_date', models.DateTimeField(auto_now=True, verbose_name='Fecha Modificacion')),
                ('whse_code', models.ForeignKey(db_column='whse_code', on_delete=django.db.models.deletion.RESTRICT, to='packfromtote.warehouse')),
            ],
            options={
                'verbose_name': 'Locn Printer Map',
                'verbose_name_plural': 'Locn Printer Map',
                'db_table': 'locn_printer_map',
            },
        ),
        migrations.AddConstraint(
            model_name='locnprintermap',
            constraint=models.UniqueConstraint(fields=('whse_code', 'reserve_locn'), name='unique_reserve_locn'),
        ),
        migrations.AddConstraint(
            model_name='locnprintermap',
            constraint=models.UniqueConstraint(fields=('reserve_locn', 'staging_locn'), name='unique_reserve_staging'),
        ),
        migrations.AddConstraint(
            model_name='locnprintermap',
            constraint=models.UniqueConstraint(fields=('reserve_locn', 'printer_name'), name='unique_reserve_locn_printer'),
        ),
    ]
