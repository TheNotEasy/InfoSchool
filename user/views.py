from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import RegisterForm, LoginForm, SchoolRegisterForm
from .models import School, StudentMeta, TeacherMeta, ParentMeta

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

import uuid


def auth_func(form_type):
    def decorator(func):
        def inner(request):
            if request.user.is_authenticated:
                return redirect('/', permanent=True)

            if request.POST:
                if form_type == RegisterForm:
                    form = form_type(request.POST)
                else:
                    form = form_type(data=request.POST)

                if form.is_valid():
                    user = None
                    if isinstance(form, RegisterForm):
                        user = form.save()
                    elif isinstance(form, AuthenticationForm):
                        user = form.get_user()

                    if user:
                        login(request, user)
                        return redirect('/')
            else:
                form = form_type()

            return func(request, form)

        return inner

    return decorator


@auth_func(AuthenticationForm)
def login_view(request, form):
    return render(request, 'login.html', {'form': form, 'title': 'Вход'})


@auth_func(RegisterForm)
def register(request, form):
    return render(request, 'login.html', {'form': form, 'title': 'Регистрация'})


def logout_view(request):
    logout(request)
    return redirect('/')


def main(request):
    return render(request, 'base.html')


def reg_school(request):
    if request.POST:
        form = SchoolRegisterForm(data=request.POST)

        if form.is_valid():
            user = form.save()
            request.session['school-registration'] = user.id
            return redirect('/user/reg/school/add-students')
    else:
        form = SchoolRegisterForm()
    return render(request, 'regschool.html', {'form': form})


def add_students(request):
    school: int = request.session.get('school-registration')

    # if not school:
    #     return redirect('/user/reg/school')

    if request.POST:
        school: School = School.objects.get(id=school)
        metas = {StudentMeta: (request.POST.get('studentsname'),
                               request.POST.get('studentsgrade'),
                               request.POST.get('studentscode')),
                 TeacherMeta: (request.POST.get('teachersname'),
                               request.POST.get('teacherssubject'),
                               request.POST.get('teacherscode')),
                 ParentMeta: (request.POST.get('parentsname'),
                              request.POST.get('parentsstudent'),
                              request.POST.get('parentscode'))}
        for meta, data in metas.items():
            cleaned_data = []
            for j in data:
                if isinstance(j, str):
                    cleaned_data.append([j])
                else:
                    cleaned_data.append(j)
            for name, i, code in zip(*cleaned_data):
                if name is None:
                    break
                second, first, last = name.split()
                kwargs = {}
                if meta == TeacherMeta:
                    kwargs['subjects'] = i
                elif meta == ParentMeta:
                    kwargs['student'] = StudentMeta.objects.get(code=i)
                else:
                    kwargs['grade'] = i
                meta.objects.create(
                    code=code,
                    first_name=first,
                    second_name=second,
                    last_name=last,
                    school=school,
                    **kwargs
                )

    return render(request, 'addstudents.html')


def get_random_code(request):
    return HttpResponse(str(uuid.uuid4()))
