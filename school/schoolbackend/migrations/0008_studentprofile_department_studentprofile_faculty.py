# Generated by Django 5.1.6 on 2025-02-11 20:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolbackend', '0007_studentprofile_bio_alter_courseenrollment_course_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_department', to='schoolbackend.userdept'),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='faculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_faculty', to='schoolbackend.userfaculty'),
        ),
    ]
