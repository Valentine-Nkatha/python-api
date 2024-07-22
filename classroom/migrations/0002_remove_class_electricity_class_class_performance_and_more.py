# Generated by Django 5.0.7 on 2024-07-21 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='electricity',
        ),
        migrations.AddField(
            model_name='class',
            name='class_performance',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='class',
            name='class_lecturer',
            field=models.CharField(default='John', max_length=20),
        ),
        migrations.AlterField(
            model_name='class',
            name='class_name',
            field=models.CharField(default='Adalab', max_length=20),
        ),
        migrations.AlterField(
            model_name='class',
            name='class_rep',
            field=models.CharField(default='Nancy', max_length=20),
        ),
    ]
