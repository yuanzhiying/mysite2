from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
# Create your views here.


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
    return HttpResponse("You're looking at the results of question %s" % question_id)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        select_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question})
    else:
        select_choice.votes += 1
        select_choice.save()
        return HttpResponseRedirect(reverse('pools:results', args=(question_id,)))
