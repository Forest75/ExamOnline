# Generated by Django 2.1.3 on 2018-12-09 04:22

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('ExamApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChoiceProblem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_type', models.CharField(default='选择题', max_length=50, verbose_name='题目类型')),
                ('content', models.CharField(max_length=200, verbose_name='题目内容')),
                ('level', models.IntegerField(choices=[(1, '简单'), (2, '中等'), (3, '困难')], default=1, verbose_name='难度系数')),
                ('tag', models.CharField(blank=True, default='数据库', max_length=50, verbose_name='标签')),
                ('author', models.CharField(blank=True, default='未知', max_length=50, verbose_name='作者')),
                ('option_A', models.CharField(max_length=50, verbose_name='A选项')),
                ('option_B', models.CharField(max_length=50, verbose_name='B选项')),
                ('option_C', models.CharField(max_length=50, verbose_name='C选项')),
                ('option_D', models.CharField(max_length=50, verbose_name='D选项')),
                ('answer', models.IntegerField(choices=[(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D')], verbose_name='参考答案')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否被删除')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_updated_time', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
            ],
            options={
                'verbose_name_plural': '选择题',
                'db_table': 'ChoiceProblem',
                'ordering': ['last_updated_time'],
            },
        ),
        migrations.CreateModel(
            name='FillBlankProblem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_type', models.CharField(default='填空题', max_length=50, verbose_name='题目类型')),
                ('content', models.CharField(max_length=200, verbose_name='题目内容')),
                ('level', models.IntegerField(choices=[(1, '简单'), (2, '中等'), (3, '困难')], default=1, verbose_name='难度系数')),
                ('tag', models.CharField(blank=True, default='数据库', max_length=50, verbose_name='标签')),
                ('author', models.CharField(blank=True, default='未知', max_length=50, verbose_name='作者')),
                ('answer', models.CharField(max_length=200, verbose_name='参考答案')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否被删除')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_updated_time', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
            ],
            options={
                'verbose_name_plural': '填空题',
                'db_table': 'FillBlankProblem',
                'ordering': ['last_updated_time'],
            },
        ),
        migrations.CreateModel(
            name='JudgeProblem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_type', models.CharField(default='判断题', max_length=50, verbose_name='题目类型')),
                ('content', models.CharField(max_length=100, verbose_name='题目内容')),
                ('level', models.IntegerField(choices=[(1, '简单'), (2, '中等'), (3, '困难')], default=1, verbose_name='难度系数')),
                ('tag', models.CharField(blank=True, default='数据库', max_length=50, verbose_name='标签')),
                ('author', models.CharField(blank=True, default='未知', max_length=50, verbose_name='作者')),
                ('answer', models.BooleanField(verbose_name='是否正确')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否被删除')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_updated_time', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
            ],
            options={
                'verbose_name_plural': '判断题',
                'db_table': 'JudgeProblem',
                'ordering': ['last_updated_time'],
            },
        ),
        migrations.CreateModel(
            name='OperateProblem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_type', models.CharField(default='实际操作题', max_length=50, verbose_name='题目类型')),
                ('content', models.TextField(verbose_name='题目内容')),
                ('level', models.IntegerField(choices=[(1, '简单'), (2, '中等'), (3, '困难')], default=1, verbose_name='难度系数')),
                ('tag', models.CharField(blank=True, default='数据库', max_length=50, verbose_name='标签')),
                ('author', models.CharField(blank=True, default='未知', max_length=50, verbose_name='作者')),
                ('answer', models.TextField(verbose_name='参考答案')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否被删除')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_updated_time', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
            ],
            options={
                'verbose_name_plural': '实际操作题',
                'db_table': 'OperateProblem',
                'ordering': ['last_updated_time'],
            },
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('paper_id', models.AutoField(primary_key=True, serialize=False, verbose_name='试卷编号')),
                ('owner_id', models.IntegerField(default=0, verbose_name='试卷管理员id')),
                ('level', models.IntegerField(choices=[(1, '简单'), (2, '中等'), (3, '困难')], default=1, verbose_name='难度系数')),
                ('paper_name', models.CharField(max_length=50, verbose_name='试卷名称')),
                ('tag', models.CharField(blank=True, default='数据库', max_length=50, verbose_name='试卷标签')),
                ('author', models.CharField(blank=True, default='未知', max_length=50, verbose_name='作者')),
                ('each_choice_problem_score', models.FloatField(default=0, verbose_name='每道选择题分数')),
                ('each_judge_problem_score', models.FloatField(default=0, verbose_name='每道判断题分数')),
                ('start_time', models.DateTimeField(verbose_name='开始时间')),
                ('end_time', models.DateTimeField(verbose_name='结束时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否被删除')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_updated_time', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
            ],
            options={
                'verbose_name_plural': '试卷',
                'db_table': 'Paper',
                'ordering': ['last_updated_time'],
            },
        ),
        migrations.CreateModel(
            name='PaperProblem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paper_id', models.IntegerField(verbose_name='试卷编号')),
                ('problem_type', models.CharField(max_length=50, verbose_name='题目类型')),
                ('problem_id', models.IntegerField(verbose_name='题目编号')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否被删除')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_updated_time', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
            ],
            options={
                'verbose_name_plural': '试卷与试题关系',
                'db_table': 'Paper_Problem',
                'ordering': ['paper_id'],
            },
        ),
        migrations.CreateModel(
            name='PaperUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paper_id', models.IntegerField(verbose_name='试卷编号')),
                ('uid', models.IntegerField(verbose_name='用户编号')),
                ('is_finished', models.BooleanField(default=False, verbose_name='是否已完成试卷')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否被删除')),
                ('last_updated_time', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
            ],
            options={
                'verbose_name_plural': '试卷与用户关系',
                'db_table': 'Paper_User',
                'ordering': ['paper_id'],
            },
        ),
        migrations.CreateModel(
            name='QAProblem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_type', models.CharField(default='问答题', max_length=50, verbose_name='题目类型')),
                ('content', models.TextField(verbose_name='题目内容')),
                ('level', models.IntegerField(choices=[(1, '简单'), (2, '中等'), (3, '困难')], default=1, verbose_name='难度系数')),
                ('tag', models.CharField(blank=True, default='数据库', max_length=50, verbose_name='标签')),
                ('author', models.CharField(blank=True, default='未知', max_length=50, verbose_name='作者')),
                ('answer', models.TextField(verbose_name='参考答案')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否被删除')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_updated_time', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
            ],
            options={
                'verbose_name_plural': '问答题',
                'db_table': 'QAProblem',
                'ordering': ['last_updated_time'],
            },
        ),
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
        migrations.CreateModel(
            name='TeacherStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_id', models.IntegerField(verbose_name='老师编号')),
                ('student_id', models.IntegerField(verbose_name='学生编号')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否被删除')),
                ('last_updated_time', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
            ],
            options={
                'verbose_name_plural': '老师与学生关系',
                'db_table': 'Tea_Stu',
                'ordering': ['teacher_id'],
            },
        ),
        migrations.CreateModel(
            name='UserAnswerSituation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='答题情况id')),
                ('correct_choice_problem_amount', models.IntegerField(default=0, verbose_name='用户答对的选择题数')),
                ('correct_judge_problem_amount', models.IntegerField(default=0, verbose_name='用户答对的判断题数')),
                ('fill_blank_problem_scores', models.FloatField(default=0, verbose_name='用户填空题总得分')),
                ('QA_problem_scores', models.FloatField(default=0, verbose_name='用户问答题总得分')),
                ('operate_problem_scores', models.FloatField(default=0, verbose_name='用户操作题总得分')),
                ('last_updated_time', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
            ],
            options={
                'verbose_name_plural': '用户答题与得分情况',
                'db_table': 'User_Answer_Situation',
                'ordering': ['last_updated_time'],
            },
        ),
        migrations.CreateModel(
            name='UserChoiceAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paper_id', models.IntegerField(verbose_name='试卷编号')),
                ('uid', models.IntegerField(verbose_name='用户编号')),
                ('problem_id', models.IntegerField(verbose_name='题目编号')),
                ('user_answer', models.IntegerField(verbose_name='用户答案')),
                ('scores', models.IntegerField(default=0, verbose_name='得分')),
                ('last_updated_time', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
            ],
            options={
                'verbose_name_plural': '用户选择题答案',
                'db_table': 'User_Choice_Answer',
                'ordering': ['paper_id', 'last_updated_time'],
            },
        ),
        migrations.CreateModel(
            name='UserJudgeAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paper_id', models.IntegerField(verbose_name='试卷编号')),
                ('uid', models.IntegerField(verbose_name='用户编号')),
                ('problem_id', models.IntegerField(verbose_name='题目编号')),
                ('user_answer', models.BooleanField(verbose_name='用户答案')),
                ('scores', models.IntegerField(default=0, verbose_name='得分')),
                ('last_updated_time', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
            ],
            options={
                'verbose_name_plural': '用户判断题答案',
                'db_table': 'User_Judge_Answer',
                'ordering': ['paper_id', 'last_updated_time'],
            },
        ),
        migrations.CreateModel(
            name='UserTextAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paper_id', models.IntegerField(verbose_name='试卷编号')),
                ('uid', models.IntegerField(verbose_name='用户编号')),
                ('problem_id', models.IntegerField(verbose_name='题目编号')),
                ('problem_type', models.CharField(max_length=50, verbose_name='题目类型')),
                ('user_answer', models.TextField(verbose_name='用户答案')),
                ('scores', models.IntegerField(default=0, verbose_name='得分')),
                ('last_updated_time', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
            ],
            options={
                'verbose_name_plural': '用户非选择判断题答案',
                'db_table': 'User_Text_Answer',
                'ordering': ['paper_id', 'last_updated_time'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('uid', models.AutoField(primary_key=True, serialize=False, verbose_name='用户编号')),
                ('real_name', models.CharField(max_length=30, verbose_name='姓名')),
                ('is_teacher', models.BooleanField(default=False, verbose_name='是否为老师')),
                ('username', models.CharField(max_length=30, unique=True, verbose_name='学号')),
                ('class_name', models.CharField(blank=True, default='未知', max_length=50, verbose_name='班级')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': '用户',
                'ordering': ['class_name'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='paperuser',
            name='answer_situation',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ExamApp.UserAnswerSituation', verbose_name='用户答题情况'),
        ),
    ]
