# Generated by Django 4.0.4 on 2022-06-02 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('idd', models.AutoField(db_column='IdD', primary_key=True, serialize=False)),
                ('issuing_date', models.DateField(blank=True, null=True)),
                ('valid_date', models.DateField(blank=True, null=True)),
                ('issuing_place', models.CharField(blank=True, max_length=50, null=True)),
                ('reg_number', models.CharField(blank=True, max_length=20, null=True)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='documents/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='documents/')),
            ],
            options={
                'db_table': 'document',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.CharField(max_length=50, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('avatar', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='avatars/')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='thumbnails/')),
                ('email_verified', models.IntegerField(blank=True, null=True)),
                ('tel', models.CharField(blank=True, max_length=20, null=True)),
                ('bio', models.CharField(blank=True, max_length=256, null=True)),
                ('doc_verified', models.BooleanField(default=False)),
                ('is_djiler', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('idd', models.ForeignKey(blank=True, db_column='IdD', null=True, on_delete=django.db.models.deletion.CASCADE, to='users.document')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'user',
                'managed': True,
            },
        ),
    ]
