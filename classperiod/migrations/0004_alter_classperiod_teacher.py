# Generated by Django 5.0.7 on 2024-07-17 13:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classperiod', '0003_alter_classperiod_teacher'),
        # ('teacher', '0002_rename_teachers_id_teacher_teachers_national_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classperiod',
            name='teacher',
            field=models.ForeignKey(default='Python', on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher'),
            preserve_default=False,
        ),
    ]
