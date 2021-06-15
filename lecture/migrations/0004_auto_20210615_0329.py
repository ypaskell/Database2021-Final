# Generated by Django 3.1.7 on 2021-06-15 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0003_auto_20210615_0308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_info',
            name='course_max_count',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='lecture.student_class'),
        ),
    ]
