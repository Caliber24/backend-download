# Generated by Django 5.1 on 2024-08-24 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post_module', '0013_rename_last_update_post_updated_at_post_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='status',
        ),
    ]