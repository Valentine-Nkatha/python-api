# Generated by Django 5.0.7 on 2024-07-17 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classperiod', '0008_alter_classperiod_classroom_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classperiod',
            old_name='classroom',
            new_name='classroom_period',
        ),
        migrations.RenameField(
            model_name='classperiod',
            old_name='teacher',
            new_name='teachers_period',
        ),
    ]
