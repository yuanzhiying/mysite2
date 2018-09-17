from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from django.views import generic
from django.utils import timezone
import datetime
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        # gt_time = timezone.now() - datetime.timedelta(days=1)
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
        # return Question.objects.filter(pub_date__lte=timezone.now()).filter(pub_date__gt=gt_time).order_by('-pub_date')


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

'''
def index(request):
    # get_list_or_404用法 还可以添加filter过滤所取数据
    latest_question_list = get_list_or_404(Question.objects.order_by('-pub_date'))
    # latest_question_list = Question.objects.order_by('-pub_date')
    # context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', {'latest_question_list': latest_question_list})


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
'''


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # request.POST['choice'] 得到提交的值
        select_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question, 'error_message': "You did't select a choice."})
    else:
        select_choice.votes += 1
        select_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
