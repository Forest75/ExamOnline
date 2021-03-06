from django.contrib import admin
from django.utils.text import capfirst
from django.utils.html import format_html
from django.contrib.auth.admin import UserAdmin
from .models import (User, ChoiceProblem, JudgeProblem, FillBlankProblem,
                     QAProblem, OperateProblem, Paper, PaperProblem,
                     PaperUser, UserAnswerSituation, TeacherStudent,
                     TeacherClass)

# 此段代码意在使在admin页面的Model列表按下面的注册顺序显示


def find_model_index(name):
    count = 0
    for model, model_admin in admin.site._registry.items():
        if capfirst(model._meta.verbose_name_plural) == name:
            return count
        else:
            count += 1
    return count


def index_decorator(func):
    def inner(*args,**kwargs):
        template_response = func(*args,**kwargs)
        for app in template_response.context_data['app_list']:
            app['models'].sort(key=lambda x: find_model_index(x['name']))
        return template_response
    return inner


admin.site.index = index_decorator(admin.site.index)
admin.site.app_index = index_decorator(admin.site.app_index)
admin.site.site_header = "考试平台管理系统"
admin.site.site_title = "考试平台运维"

# Register your models here.


@admin.register(User)
class UserAdmin(UserAdmin):

    def is_teacher(self):
        if self.is_teacher:
            return '老师'
        else:
            return '学生'

    # 自定义管理界面
    is_teacher.short_description = '身份'
    list_display = ['uid', 'username', 'real_name', 'class_name', is_teacher]
    list_filter = ['class_name', 'is_teacher']
    search_fields = ['class_name', 'username', 'real_name']
    list_per_page = 20

    fieldsets = [
        ("用户信息", {"fields": ['real_name', 'username', 'password',
                             'class_name', 'is_superuser', 'is_teacher']}),
    ]


@admin.register(Paper)
class PaperAdmin(admin.ModelAdmin):

    def color_level(self):
        if self.level == 1:
            color_code = 'green'
            text = '简单'
        elif self.level == 2:
            color_code = 'orange'
            text = '中等'
        else:
            color_code = 'red'
            text = '困难'
        return format_html('<span style="color: {};">{}</span>',
                           color_code, text)

    def is_delete(self):
        if not self.is_delete:
            color_code = 'green'
            text = '存在'
        else:
            color_code = 'red'
            text = "不存在"
        return format_html('<span style="color: {};">{}</span>',
                           color_code, text)

    # 自定义管理界面
    color_level.short_description = '难度'
    is_delete.short_description = '是否存在'
    list_display = ['paper_id', 'paper_name', color_level, 'owner_id',
                    'author', 'start_time', 'end_time',
                    'last_updated_time', is_delete]              # 显示在管理界面的列
    list_filter = ['level', 'is_delete', 'last_updated_time']    # 数据过滤字段
    search_fields = ['tag', 'level', 'author']                   # 数据搜索字段
    list_per_page = 20

    # 添加，修改数据项时有分栏目的效果
    fieldsets = [
        ("试卷信息", {"fields": ['paper_name', 'level', 'start_time', 'end_time']}),
        ("其他信息(选填)", {"fields": ['owner_id', 'author', 'tag', 'is_delete']}),
    ]


@admin.register(ChoiceProblem)
class ChoiceProblemAdmin(admin.ModelAdmin):

    def color_level(self):
        if self.level == 1:
            color_code = 'green'
            text = '简单'
        elif self.level == 2:
            color_code = 'orange'
            text = '中等'
        else:
            color_code = 'red'
            text = '困难'
        return format_html('<span style="color: {};">{}</span>',
                           color_code, text)

    def is_delete(self):
        if not self.is_delete:
            color_code = 'green'
            text = '存在'
        else:
            color_code = 'red'
            text = "不存在"
        return format_html('<span style="color: {};">{}</span>',
                           color_code, text)

    # 自定义管理界面
    color_level.short_description = '难度'
    is_delete.short_description = '是否存在'
    list_display = ['tag', color_level, 'author',
                    'last_updated_time', is_delete]              # 显示在管理界面的列
    list_filter = ['level', 'tag', 'is_delete']                  # 数据过滤字段
    search_fields = ['tag', 'level', 'author']                   # 数据搜索字段
    list_per_page = 20

    # 添加，修改数据项时有分栏目的效果
    fieldsets = [
        ("题目信息", {"fields": ['content', 'level', 'option_A', 'option_B',
                             'option_C', 'option_D', 'answer']}),
        ("其他信息(选填)", {"fields": ['author', 'tag', 'is_delete']}),
    ]


@admin.register(JudgeProblem)
class JudgeProblemAdmin(admin.ModelAdmin):

    def color_level(self):
        if self.level == 1:
            color_code = 'green'
            text = '简单'
        elif self.level == 2:
            color_code = 'orange'
            text = '中等'
        else:
            color_code = 'red'
            text = '困难'
        return format_html('<span style="color: {};">{}</span>',
                           color_code, text)

    def answer(self):
        if self.answer:
            color_code = 'green'
            text = '正确'
        else:
            color_code = 'red'
            text = '错误'
        return format_html('<span style="color: {};">{}</span>',
                           color_code, text)

    def is_delete(self):
        if not self.is_delete:
            color_code = 'green'
            text = '存在'
        else:
            color_code = 'red'
            text = "不存在"
        return format_html('<span style="color: {};">{}</span>',
                           color_code, text)

    # 自定义管理界面
    color_level.short_description = '难度'
    is_delete.short_description = '是否存在'
    answer.short_description = '参考答案'
    list_display = ['tag', color_level, 'author', answer,
                    'last_updated_time', is_delete]              # 显示在管理界面的列
    list_filter = ['level', 'tag', 'is_delete']                  # 数据过滤字段
    search_fields = ['tag', 'level', 'author']                   # 数据搜索字段
    list_per_page = 20

    # 添加，修改数据项时有分栏目的效果
    fieldsets = [
        ("题目信息", {"fields": ['content', 'level', 'answer']}),
        ("其他信息(选填)", {"fields": ['author', 'tag', 'is_delete']}),
    ]


@admin.register(FillBlankProblem)
class FillBlankProblemAdmin(admin.ModelAdmin):

    def color_level(self):
        if self.level == 1:
            color_code = 'green'
            text = '简单'
        elif self.level == 2:
            color_code = 'orange'
            text = '中等'
        else:
            color_code = 'red'
            text = '困难'
        return format_html('<span style="color: {};">{}</span>',
                           color_code, text)

    def is_delete(self):
        if not self.is_delete:
            color_code = 'green'
            text = '存在'
        else:
            color_code = 'red'
            text = "不存在"
        return format_html('<span style="color: {};">{}</span>',
                           color_code, text)

    # 自定义管理界面
    color_level.short_description = '难度'
    is_delete.short_description = '是否存在'
    list_display = ['tag', color_level, 'author',
                    'last_updated_time', is_delete]              # 显示在管理界面的列
    list_filter = ['level', 'tag', 'is_delete']                  # 数据过滤字段
    search_fields = ['tag', 'level', 'author']                   # 数据搜索字段
    list_per_page = 20

    # 添加，修改数据项时有分栏目的效果
    fieldsets = [
        ("题目信息", {"fields": ['content', 'level', 'answer']}),
        ("其他信息(选填)", {"fields": ['author', 'tag', 'is_delete']}),
    ]


@admin.register(QAProblem)
class QAProblemAdmin(admin.ModelAdmin):

    def color_level(self):
        if self.level == 1:
            color_code = 'green'
            text = '简单'
        elif self.level == 2:
            color_code = 'orange'
            text = '中等'
        else:
            color_code = 'red'
            text = '困难'
        return format_html('<span style="color: {};">{}</span>',
                           color_code, text)

    def is_delete(self):
        if not self.is_delete:
            color_code = 'green'
            text = '存在'
        else:
            color_code = 'red'
            text =  "不存在"
        return format_html('<span style="color: {};">{}</span>',
                           color_code, text)

    # 自定义管理界面
    color_level.short_description = '难度'
    is_delete.short_description = '是否存在'
    list_display = ['tag', color_level, 'author',
                    'last_updated_time', is_delete]              # 显示在管理界面的列
    list_filter = ['level', 'tag', 'is_delete']                  # 数据过滤字段
    search_fields = ['tag', 'level', 'author']                   # 数据搜索字段
    list_per_page = 20

    # 添加，修改数据项时有分栏目的效果
    fieldsets = [
        ("题目信息", {"fields": ['content', 'level', 'answer']}),
        ("其他信息(选填)", {"fields": ['author', 'tag', 'is_delete']}),
    ]


@admin.register(OperateProblem)
class OperateProblemAdmin(admin.ModelAdmin):

    def color_level(self):
        if self.level == 1:
            color_code = 'green'
            text = '简单'
        elif self.level == 2:
            color_code = 'orange'
            text = '中等'
        else:
            color_code = 'red'
            text = '困难'
        return format_html('<span style="color: {};">{}</span>',
                           color_code, text)

    def is_delete(self):
        if not self.is_delete:
            color_code = 'green'
            text = '存在'
        else:
            color_code = 'red'
            text = "不存在"
        return format_html('<span style="color: {};">{}</span>',
                           color_code, text)

    # 自定义管理界面
    color_level.short_description = '难度'
    is_delete.short_description = '是否存在'
    list_display = ['tag', color_level, 'author',
                    'last_updated_time', is_delete]              # 显示在管理界面的列
    list_filter = ['level', 'tag', 'is_delete']                  # 数据过滤字段
    search_fields = ['tag', 'level', 'author']                   # 数据搜索字段
    list_per_page = 20

    # 添加，修改数据项时有分栏目的效果
    fieldsets = [
        ("题目信息", {"fields": ['content', 'level', 'answer']}),
        ("其他信息(选填)", {"fields": ['author', 'tag', 'is_delete']}),
    ]


@admin.register(PaperProblem)
class PaperProblemAdmin(admin.ModelAdmin):

    def is_delete(self):
        if not self.is_delete:
            color_code = 'green'
            text = '存在'
        else:
            color_code = 'red'
            text = "不存在"
        return format_html('<span style="color: {};">{}</span>',
                           color_code, text)

    # 自定义管理界面
    is_delete.short_description = '是否存在'
    list_display = ['paper_id', 'problem_type', 'problem_id',
                    'last_updated_time', is_delete]              # 显示在管理界面的列
    list_filter = ['paper_id', 'is_delete']                      # 数据过滤字段
    search_fields = ['paper_id']                                 # 数据搜索字段
    list_per_page = 20

    # 添加，修改数据项时有分栏目的效果
    fieldsets = [
        ("试卷与题目的对应关系", {"fields": ['paper_id', 'problem_type',
                                   'problem_id', 'is_delete']}),
    ]


@admin.register(PaperUser)
class PaperUserAdmin(admin.ModelAdmin):

    def is_finished(self):
        if self.is_finished:
            color_code = 'green'
            text = '已完成'
        else:
            color_code = 'red'
            text = "未完成"
        return format_html('<span style="color: {};">{}</span>',
                           color_code, text)

    def is_delete(self):
        if not self.is_delete:
            color_code = 'green'
            text = '存在'
        else:
            color_code = 'red'
            text = "不存在"
        return format_html('<span style="color: {};">{}</span>',
                           color_code, text)

    # 自定义管理界面
    is_delete.short_description = '是否存在'
    list_display = ['paper_id', 'uid', is_finished,
                    'last_updated_time', is_delete]                    # 显示在管理界面的列
    list_filter = ['paper_id', 'uid', 'is_finished', 'is_delete']      # 数据过滤字段
    search_fields = ['paper_id']                                       # 数据搜索字段
    list_per_page = 20

    # 添加，修改数据项时有分栏目的效果
    fieldsets = [
        ("试卷与用户的对应关系", {"fields": ['paper_id', 'uid',
                                   'is_finished', 'is_delete']}),
    ]


@admin.register(TeacherStudent)
class TeacherStudentAdmin(admin.ModelAdmin):

    def is_delete(self):
        if not self.is_delete:
            color_code = 'green'
            text = '存在'
        else:
            color_code = 'red'
            text = "不存在"
        return format_html('<span style="color: {};">{}</span>',
                           color_code, text)

    # 自定义管理界面
    is_delete.short_description = '是否存在'
    list_display = ['teacher_id', 'student_id',
                    'last_updated_time', is_delete]              # 显示在管理界面的列
    list_filter = ['teacher_id', 'is_delete']                    # 数据过滤字段
    search_fields = ['teacher_id']                               # 数据搜索字段
    list_per_page = 20

    # 添加，修改数据项时有分栏目的效果
    fieldsets = [
        ("老师与学生的对应关系", {"fields": ['teacher_id', 'student_id', 'is_delete']}),
    ]


@admin.register(TeacherClass)
class TeacherClassAdmin(admin.ModelAdmin):

    def is_delete(self):
        if not self.is_delete:
            color_code = 'green'
            text = '存在'
        else:
            color_code = 'red'
            text = "不存在"
        return format_html('<span style="color: {};">{}</span>',
                           color_code, text)

    # 自定义管理界面
    is_delete.short_description = '是否存在'
    list_display = ['teacher_id', 'class_name',
                    'last_updated_time', is_delete]              # 显示在管理界面的列
    list_filter = ['teacher_id', 'class_name', 'is_delete']      # 数据过滤字段
    search_fields = ['teacher_id', 'class_name']                 # 数据搜索字段
    list_per_page = 20

    # 添加，修改数据项时有分栏目的效果
    fieldsets = [
        ("老师与班级的对应关系", {"fields": ['teacher_id', 'class_name', 'is_delete']}),
    ]
