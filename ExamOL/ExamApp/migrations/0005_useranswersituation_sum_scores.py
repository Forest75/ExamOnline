# Generated by Django 2.1.4 on 2018-12-16 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExamApp', '0004_auto_20181210_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='useranswersituation',
            name='sum_scores',
            field=models.FloatField(default=0, verbose_name='总分'),
        ),
    ]
