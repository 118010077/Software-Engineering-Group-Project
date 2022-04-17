# Generated by Django 3.2.5 on 2022-04-17 00:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='forumPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=255)),
                ('Content', models.TextField()),
                ('Tag', models.CharField(max_length=255)),
                ('Poster', models.CharField(max_length=255)),
                ('Ctime', models.DateTimeField(auto_now_add=True)),
                ('UpdateTime', models.TimeField()),
            ],
            options={
                'ordering': ['-Tag', '-UpdateTime'],
            },
        ),
        migrations.CreateModel(
            name='forumComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Commenter', models.CharField(max_length=255)),
                ('Content', models.TextField()),
                ('Ctime', models.DateTimeField(auto_now_add=True)),
                ('forumPost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='forum.forumpost')),
            ],
            options={
                'ordering': ['-Ctime'],
            },
        ),
    ]
