# Generated by Django 5.0 on 2023-12-16 17:26

import authentication.models
import authentication.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('phone_number', models.CharField(error_messages={'unique': 'A user with that phone number already exists.'}, help_text='Required. A valid phone number that doesnt excced 15 characters.', max_length=15, unique=True, validators=[authentication.validators.validate_phone_number], verbose_name='user phone number')),
                ('first_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='last name')),
                ('email', models.EmailField(blank=True, error_messages={'unique': 'A user with that email already exists.'}, max_length=254, null=True, unique=True, verbose_name='email address')),
                ('photo', models.ImageField(blank=True, null=True, upload_to=authentication.models.user_photo_upload_path, verbose_name='user photo')),
                ('gender', models.CharField(blank=True, choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('OTHER', 'Other')], default='MALE', max_length=10, null=True, verbose_name='gender')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='date of birth')),
                ('is_active', models.BooleanField(default=False, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.By default the user is inactive', verbose_name='active')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'custom user',
                'verbose_name_plural': 'custom users',
                'ordering': ['-date_joined'],
            },
            managers=[
                ('objects', authentication.models.CustomUserManager()),
            ],
        ),
    ]
