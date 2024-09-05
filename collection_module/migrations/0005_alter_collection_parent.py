# Generated by Django 5.1 on 2024-09-04 16:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection_module', '0004_alter_collection_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_collections', to='collection_module.collection', verbose_name='ابردسته\u200cبندی'),
        ),
    ]
