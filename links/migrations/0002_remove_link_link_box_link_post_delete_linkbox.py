# Generated by Django 4.2 on 2024-08-16 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post_module', '0004_remove_linkbox_post_delete_link_delete_linkbox'),
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='link_box',
        ),
        migrations.AddField(
            model_name='link',
            name='post',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='post_module.post', verbose_name='پست'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='LinkBox',
        ),
    ]
