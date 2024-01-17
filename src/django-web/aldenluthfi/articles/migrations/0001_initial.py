# Generated by Django 4.2.6 on 2024-01-08 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash', models.SmallIntegerField(unique=True)),
                ('cover_image', models.FileField(upload_to='')),
                ('title_id', models.CharField(max_length=100, unique=True)),
                ('title_en', models.CharField(max_length=100, unique=True)),
                ('content_id', models.TextField()),
                ('content_en', models.TextField()),
                ('created_at', models.DateTimeField()),
            ],
        ),
    ]
