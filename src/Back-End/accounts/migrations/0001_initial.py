# Generated by Django 3.2.5 on 2022-05-12 07:19

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('identity', models.CharField(choices=[('faculty', 'faculty'), ('student', 'student'), ('admin', 'admin')], default='student', max_length=16)),
                ('has_confirmed', models.BooleanField(default=False)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-c_time'],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userIntro', models.CharField(max_length=400)),
                ('userPhoto', models.ImageField(default='accounts/uploads/default.png', upload_to='accounts/uploads/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.myuser')),
            ],
        ),
        migrations.CreateModel(
            name='ConfirmString',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=256)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.myuser')),
            ],
            options={
                'verbose_name': 'Confirmation_Code',
                'verbose_name_plural': 'Confirmation_Codes',
                'ordering': ['-c_time'],
            },
        ),
    ]
