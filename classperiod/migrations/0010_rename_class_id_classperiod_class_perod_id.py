# Generated by Django 5.0.7 on 2024-07-17 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classperiod', '0009_rename_classroom_classperiod_classroom_period_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classperiod',
            old_name='class_id',
            new_name='class_perod_id',
        ),
    ]
