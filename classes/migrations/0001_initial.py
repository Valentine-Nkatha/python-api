# Generated by Django 5.0.7 on 2024-07-22 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_lecturer', models.CharField(default='John', max_length=20)),
                ('class_name', models.CharField(default='Adalab', max_length=20)),
                ('class_rep', models.CharField(default='Nancy', max_length=20)),
                ('class_performance', models.FloatField(default=0)),
            ],
        ),
    ]
