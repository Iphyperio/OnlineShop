# Generated by Django 4.2.1 on 2023-05-16 14:15

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='detail',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
