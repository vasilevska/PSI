# Generated by Django 4.0.4 on 2022-06-02 11:01

from django.db import migrations, models
import django.db.models.deletion
from ..models import *

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('idc', models.AutoField(db_column='IdC', primary_key=True, serialize=False)),
                ('coordinates', models.CharField(blank=True, max_length=20, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('km', models.IntegerField(blank=True, null=True)),
                ('transmision', models.CharField(blank=True, max_length=20, null=True)),
                ('fuel', models.CharField(blank=True, max_length=20, null=True)),
                ('price_per_day', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('images', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('descr', models.CharField(blank=True, max_length=500, null=True)),
                ('type', models.CharField(blank=True, max_length=20, null=True)),
                ('slug', models.SlugField()),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='uploads/')),
            ],
            options={
                'db_table': 'car',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('idman', models.AutoField(db_column='IdMan', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'manufacturer',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('idman', models.OneToOneField(db_column='IdMan', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='cars.manufacturer')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'model',
                'managed': True,
            },
        ),
    ]
