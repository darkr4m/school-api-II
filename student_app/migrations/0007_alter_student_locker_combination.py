# Generated by Django 5.1.7 on 2025-03-24 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0006_alter_student_locker_combination_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='locker_combination',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
