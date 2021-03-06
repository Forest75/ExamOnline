# -*- coding: utf-8 -*-
"""
ExamApp的url分发
@file: urls.py
@time: 2018/11/6 20:34
Created by Junyi.
"""
from django.urls import path
from . import views

app_name = 'ExamApp'

urlpatterns = [
    path('', views.start_page, name='起始页'),
    path('login/', views.user_login, name='登录'),
    path('logout/', views.user_logout, name='登出'),
    path('send_bug/<username>/', views.commit_bug, name='报告错误'),
    path('stu_home/<username>/', views.student_home_page, name='学生主页'),
    path('exam/<username>/<paper_id>/', views.take_exam, name='考试页面'),
    path('stu_analyse/<username>/<paper_id>/', views.stu_analyse, name='学生考试情况'),
    path('tea_home/<username>/<class_name>/', views.teacher_home_page, name='老师主页'),
    path('create_student/<username>/', views.create_student, name='创建学生'),
    path('create_many_students/<username>/', views.use_file_to_create_students, name='批量创建学生'),
    path('admin_problems/<username>/<problem_type>/', views.admin_problems, name='管理试题'),
    path('create_problem/<username>/', views.create_problem, name='创建题目'),
    path('create_paper/<username>/', views.create_paper, name='创建试卷'),
    path('mark_scores/<username>/<paper_id>/<student_id>/', views.mark_scores, name='评分'),
    path('analyse/<username>/<paper_id>/', views.analyse, name='考试情况'),
]

handler404 = views.page_not_found
