

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
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
                ('images', models.CharField(blank=True, max_length=100, null=True)),
                ('descr', models.CharField(blank=True, max_length=500, null=True)),
                ('type', models.CharField(blank=True, max_length=20, null=True)),
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
                ('slug', models.SlugField()),
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
                ('slug', models.SlugField()),
            ],
            options={
                'db_table': 'model',
                'managed': True,
             'unique_together': {('idman', 'name')},
            },
        ),
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
                ('idu', models.ForeignKey(blank=True, db_column='IdU', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.user')),
                ('idman', models.ForeignKey(blank=True, db_column='IdMan', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='IdMan', to='cars.model')),
                ('model', models.ForeignKey(blank=True, db_column='name', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Model', to='cars.model')),
            ],
            options={
                'db_table': 'car',
                'managed': True,
            },
        ),
    ]
