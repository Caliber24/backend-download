# Generated by Django 4.2.6 on 2024-08-14 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/post', verbose_name='تصویر پست')),
                ('description', models.TextField(verbose_name='متن')),
                ('slug', models.SlugField()),
                ('File', models.FileField(blank=True, null=True, upload_to='Files/post', verbose_name='فایل های پست')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'پست',
                'verbose_name_plural': 'پست ها',
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان')),
                ('link', models.CharField(max_length=1000, verbose_name='متن لینک')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post_module.post')),
            ],
            options={
                'verbose_name': 'لینک',
                'verbose_name_plural': 'لینک\u200cها',
            },
        ),
    ]
