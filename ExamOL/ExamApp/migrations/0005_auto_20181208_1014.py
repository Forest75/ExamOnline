# Generated by Django 2.1.3 on 2018-12-08 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExamApp', '0004_auto_20181206_2200'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_id', models.IntegerField(verbose_name='老师编号')),
                ('class_name', models.CharField(max_length=50, verbose_name='班级')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否被删除')),
                ('last_updated_time', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
            ],
            options={
                'verbose_name_plural': '老师与班级的关系',
                'db_table': 'Tea_Class',
                'ordering': ['teacher_id'],
            },
        ),
        migrations.RemoveField(
            model_name='paperuser',
            name='create_time',
        ),
        migrations.RemoveField(
            model_name='teacherstudent',
            name='create_time',
        ),
        migrations.AddField(
            model_name='paperuser',
            name='last_updated_time',
            field=models.DateTimeField(auto_now=True, verbose_name='最后修改时间'),
        ),
        migrations.AddField(
            model_name='teacherstudent',
            name='last_updated_time',
            field=models.DateTimeField(auto_now=True, verbose_name='最后修改时间'),
        ),
        migrations.AlterField(
            model_name='user',
            name='class_name',
            field=models.CharField(blank=True, default='未知', max_length=50, verbose_name='班级'),
        ),
    ]