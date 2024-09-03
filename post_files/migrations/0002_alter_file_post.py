# Generated by Django 5.1 on 2024-09-02 16:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_files', '0001_initial'),
        ('post_module', '0025_alter_postcomment_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='post_module.post'),
        ),
    ]
