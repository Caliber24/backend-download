# Generated by Django 5.1 on 2024-08-28 06:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection_module', '0001_initial'),
        ('post_module', '0019_delete_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='collection',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='collection_module.collection', verbose_name='دسته\u200cبندی'),
        ),
        migrations.DeleteModel(
            name='Collection',
        ),
    ]
