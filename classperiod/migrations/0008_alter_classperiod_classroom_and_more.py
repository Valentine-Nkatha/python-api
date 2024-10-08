# Generated by Django 5.0.7 on 2024-07-17 14:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classperiod', '0007_alter_classperiod_class_id'),
        # ('teacher', '0006_rename_teachers_id_teacher_teachers_national_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classperiod',
            name='classroom',
            field=models.CharField(default='classes', max_length=20),
        ),
        migrations.AlterField(
            model_name='classperiod',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to='teacher.teacher'),
        ),
    ]
