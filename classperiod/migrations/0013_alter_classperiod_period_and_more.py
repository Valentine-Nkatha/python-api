# Generated by Django 5.0.7 on 2024-07-25 04:27

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classperiod', '0012_alter_classperiod_teacherss'),
        ('teachers', '0002_alter_teacher_teachers_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classperiod',
            name='period',
            field=models.IntegerField(),
        ),
        migrations.RemoveField(
            model_name='classperiod',
            name='teacherss',
        ),
        migrations.AddField(
            model_name='classperiod',
            name='teacherss',
            field=models.OneToOneField(default=datetime.datetime(2024, 7, 25, 4, 27, 27, 135712, tzinfo=datetime.timezone.utc), on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to='teachers.teacher'),
            preserve_default=False,
        ),
    ]
