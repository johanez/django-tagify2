# Generated by Django 5.1.5 on 2025-01-30 10:06

import tagify.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='test',
            field=tagify.models.TagField(blank=True),
        ),
    ]
