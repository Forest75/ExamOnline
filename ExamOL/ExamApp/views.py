from django.shortcuts import redirect, render_to_response, get_object_or_404, render
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .app_helper import views_helper
from .models import User, Paper


# Create your views here.


def start_page(request):
    """
    起始页面(跳转到登陆界面)
    """
    return redirect('ExamApp:登录')


@csrf_exempt
@views_helper.is_post_or_get(get_render_html='login.html')
def user_login(request):
    """
    用户登陆页面
    """
    user = views_helper.get_user_or_none(request)
    if user is not None:
        login(request, user)
        if not user.is_teacher:
            return redirect('ExamApp:学生主页', username=user.username)
        else:
            return redirect('ExamApp:老师主页', username=user.username, class_name='all')
    else:
        return render_to_response('login.html', {'error': '密码错误'})


def user_logout(request):
    """
    用户登出后展示页面
    """
    logout(request)
    return redirect('ExamApp:登录')


@views_helper.is_post_or_get(get_render_html='create_user.html')
def create_user(request):
    """
    创建用户界面
    用户(姓名, 学号(用户名)，密码，班级名)
    """
    try:
        user = views_helper.sign_up_user_or_none(request)
        if user is not None:
            #TODO 弹出页面显示:创建用户成功，5秒之后去往主界面
            pass
        else:
            #TODO render渲染，提示用户密码格式不正确
            pass
    except:
        #TODO 提示用户请输入完整信息后再提交
        pass


def page_not_found(request):
    """
    404页面
    """
    return render_to_response('404.html')


@login_required
@csrf_exempt
def commit_bug(request, username: str):
    """
    提交bug页面
    :param request:
    :param username: 用户的学号
    """
    if request.method == 'POST':
        bug_information = request.POST['bug_information']
        # TODO bug信息发送到后台
        return render(request, 'bug.html', {'commit_result': True})
    else:
        user = get_object_or_404(User, username=username)
        return render_to_response('bug.html', {'user': user, 'commit_result': None})


@login_required
def student_home_page(request, username: str):
    """
    学生主页
    :param request
    :param username: 用户的学号
    :return:
    """
    user = get_object_or_404(User, username=username)
    finished_paper_list, unfinished_paper_list = views_helper.get_user_do_and_undo_paper_list(user.uid)
    return render_to_response(
        'student_examlist.html',
        {
            'user': user,
            'finished_paper_list': finished_paper_list,
            'unfinished_paper_list': unfinished_paper_list,
        })


@login_required
@csrf_exempt
def take_exam(request, username: str, paper_id: str):
    """
    学生考试页面
    :param request:
    :param username: 学生的学号
    :param paper_id: 试卷的id
    """
    user = get_object_or_404(User, username=username)
    paper = get_object_or_404(Paper, paper_id=paper_id)
    if request.method == 'POST':
        result = views_helper.save_user_answers(user, paper, request.POST)
        return render_to_response(
            'student_exam.html',
            {
                'user': user,
                'paper': paper,
                'result': result,
            }
        )
    else:
        raw_exam_problems = views_helper.get_exam_problems(user, paper)
        exam_problems = views_helper.add_index_to_problems(raw_exam_problems)
        return render_to_response(
            'student_exam.html',
            {
                'user': user,
                'paper': paper,
                'choice_problems': exam_problems[0],
                'judge_problems': exam_problems[1],
                'fillblank_problems': exam_problems[2],
                'QA_problems': exam_problems[3],
                'operate_problems': exam_problems[4],
            }
        )


@login_required
def teacher_home_page(request, username: str, class_name: str):
    """
    老师主页
    :param request:
    :param username: 老师的工号
    :param class_name: 展示信息班级名
    """
    user = get_object_or_404(User, username=username)
    class_list = views_helper.get_class_list(teacher_id=user.uid)
    student_list = views_helper.get_student_list(user_id=user.uid, class_name=class_name)
    return render_to_response(
        'T_manage_student.html',
        {
            'user': user,
            'student_list': student_list,
            'class_list': class_list,
            'class_name': class_name,
        })


@login_required
def admin_problems(request, username: str, problem_type: str):
    """
    老师管理题库页面
    :param request:
    :param username: 老师的工号
    :param problem_type: 问题的类型(all|choice|judge|fillblank|QA|operate)
    """
    user = get_object_or_404(User, username=username)
    complete_type, problem_list = views_helper.get_problem_list(problem_type)
    return render_to_response(
        'T_manage_problems.html',
        {
            'user': user,
            'problem_list': problem_list,
            'complete_type': complete_type,
        }
    )


@login_required
@csrf_exempt
def create_paper(request, username: str):
    """
    老师创建试卷页面
    :param request
    :param username: 老师的工号
    """
    user = get_object_or_404(User, username=username)
    problem_names = ['选择题', '判断题', '填空题', '问答题', '实际操作题']
    if request.method == 'POST':
        if views_helper.use_info_to_create_paper(teacher_id=user.uid, paper_info=request.POST):
            result = True
        else:
            result = False
        return render_to_response(
            'T_create_paper.html',
            {
                'user': user,
                'problem_names': problem_names,
                'result': result,
            }
        )
    else:
        return render_to_response(
            'T_create_paper.html',
            {
                'user': user,
                'problem_names': problem_names,
            }
        )


@login_required
def mark_scores(request, username: str, paper_id: str, student_id: str):
    """
    老师评分页面
    :param request
    :param username: 老师的工号
    :param paper_id: 试卷id
    :param student_id: 学生的id
    """
    user = get_object_or_404(User, username=username)
    if request.method == 'POST':
        pass
    else:
        paper = views_helper.get_paper(paper_id=paper_id)
        papers = views_helper.get_paper_list(user=user)
        students = views_helper.get_paper_user_list(paper_id=paper_id)
        fillblank_answers, QA_answers, operate_answers = views_helper.get_user_answers(paper_id, student_id)
        return render_to_response(
            'T_grade.html',
            {
                'user': user,
                'paper': paper,
                'papers': papers,
                'students': students,
                'fillblank_answers': [i for i in fillblank_answers],
                'QA_answers': [i for i in QA_answers],
                'operate_answers': [i for i in operate_answers],
            }
        )


@login_required
def analyse(request, username: str, paper_id: str):
    """
    老师查看考试情况页面
    :param request
    :param username: 老师的工号
    :param paper_id: 试卷id
    """
    user = get_object_or_404(User, username=username)
    return render_to_response(
        'T_analyze.html',
        {
            'user': user,
        }
    )
