# Generated by Django 2.1.3 on 2018-12-06 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExamApp', '0003_auto_20181206_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='paperuser',
            name='is_finished',
            field=models.BooleanField(default=False, verbose_name='是否已完成试卷'),
        ),
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='用户编号'),
        ),
    ]
