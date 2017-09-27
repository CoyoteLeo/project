from django.shortcuts import HttpResponseRedirect, HttpResponse, render
from django.db.models import Q
from django.contrib.auth.views import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.generic import View
from .models import Todolist, History
from .form import Todolistform
from user.models import Profile
import time
import datetime


class todolist(LoginRequiredMixin, View):
    __data = {
        "todolist": {
            "header": 'Todolist',
            "alert": "Not add any events yet."
        },
        "finish": {
            "header": "Finished Events",
            "alert": 'Alert!! Nothing Complete!!'
        },
        "unfinish": {
            "header": "UnFinished Events",
            "alert": 'Congratulation!! All Complete!!'
        },
        "expired": {
            "header": "Expired Events",
            "alert": "Congratulation!! Nothing is expired!!"
        }
    }
    http_method_names = ['get', 'post']

    # http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
    def get(self, request):
        todolist = Todolist.objects.filter(user=request.user)

    def post(selfself, request):
        todolist = Todolist.objects.filter(user=request.user)


@login_required
def todolist(request):
    todolist = Todolist.objects.filter(user=request.user.profile.id)
    alert = 'Not add any events yet.'
    header = 'Todolist'
    event = dict()
    for y in todolist.dates("remind_time", "year").order_by("-remind_time").distinct():
        temp = todolist.filter(remind_time__year=y.year).order_by("-remind_time")
        event[y.year] = dict()
        for m in temp.dates("remind_time", "month").distinct():
            event[y.year][m.month] = temp.filter(remind_time__month=m.month).order_by("-remind_time", )
    return render(request, 'show.html', locals())


@login_required
def add(request):
    form = Todolistform(initial={'user': request.user.profile.id})
    if request.method == 'POST':
        form = Todolistform(request.POST)
        if form.is_valid():
            if 'finish_or_not' in request.POST:
                Todolist(user=Profile.objects.get(id=request.user.profile.id),
                         title=request.POST['title'],
                         content=request.POST['content'],
                         remind_time=request.POST['remind_date'], finish_or_not=True)
                Todolist.save()
            else:
                Todolist.objects.create(user=Profile.objects.get(id=request.user.profile.id),
                                        title=request.POST['title'],
                                        content=request.POST['content'],
                                        remind_time=request.POST['remind_date'],
                                        finish_or_not=False)
            redirect = '/todolist'
            return HttpResponseRedirect(redirect)
    html_title = 'Add'
    header = 'Add New Event'
    return render(request, 'event.html', locals())


@login_required
def delete(request):
    if request.method == 'POST':
        if 'delete_data' in request.POST:
            delete_data = request.POST.getlist('delete_data')
            for event in delete_data:
                Todolist.objects.filter(title=event).delete()
        redirect = '/todolist'
        return HttpResponseRedirect(redirect)
    todolist = Todolist.objects.filter(user=request.user.profile.id)
    return render(request, 'todolist/delete.html', locals())


@login_required
def modify(request, title):
    event_dict = Todolist.objects.get(title=title).__dict__
    event_dict['user'] = request.user.profile.id
    form = Todolistform(initial=event_dict)
    if request.method == 'POST':
        form = Todolistform(request.POST)
        if form.is_valid():
            todolist = Todolist.objects.filter(title=title, user=request.user.profile.id)
            if 'finish_or_not' in request.POST:
                todolist.update(title=request.POST['title'],
                                content=request.POST['content'],
                                remind_time=request.POST['remind_date'],
                                finish_or_not=True)
            else:
                todolist.update(title=request.POST['title'],
                                content=request.POST['content'],
                                remind_time=request.POST['remind_date'],
                                finish_or_not=False)
            redirect = '/todolist'
            return HttpResponseRedirect(redirect)
    html_title = title
    header = title
    return render(request, 'todolist/event.html', locals())


@login_required
def showcomplete(request):
    todolist = Todolist.objects.filter(user=request.user.profile.id, finish_or_not='True')
    header = 'Complete Events'
    alert = 'Alert!! Nothing Complete!!'
    return render(request, 'todolist/show.html', locals())


@login_required
def showuncomplete(request):
    todolist = Todolist.objects.filter(user=request.user.profile.id, finish_or_not='False')
    header = 'UnComplete Events'
    alert = 'Congratulation!! All Complete!!'
    return render(request, 'todolist/show.html', locals())


@login_required
def showmiss(request):
    now_time = datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d")
    todolist = Todolist.objects.filter(
        Q(user=request.user.profile.id) & Q(finish_or_not='False') & Q(remind_time__lte=now_time) & ~Q(remind_time=''))
    header = 'Miss Events'
    alert = 'Congratulation!! Nothing is expired!!'
    return render(request, 'todolist/show.html', locals())


def index(request):
    history = History.objects.all()
    if request.user.is_authenticated:
        now_time = datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d")
        todolist = Todolist.objects.filter(
            Q(user=request.user.profile) & Q(finish_or_not='False') & Q(remind_time__lte=now_time))
    return render(request, 'todolist/index.html', locals())


def meta(request):
    values = request.META.items()  # 將字典的鍵值對抽出成為一個清單
    html = []
    for k, v in values:
        html.append('<tr><td>{0}</td><td>{1}</td></tr>'.format(k, v))
    return HttpResponse('<table>{0}</table>'.format('\n'.join(html)))
