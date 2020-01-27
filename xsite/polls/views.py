from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question, Choice
# Create your views here.
def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    output = ", ".join(q.question_text for q in latest_questions)
    #template = loader.get_template('polls/index.html')
    context = {
        'latest_questions': latest_questions
    }
    return render(request, 'polls/index.html', context)
    #return HttpResponse(template.render(context))
    #return HttpResponse(output)

def detail(request, question_id):
    #question = Question.objects.get(pk = question_id)
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/detail.html', {'question': question})
    #return HttpResponse("This is a detail view of the question: %s" % question_id)

def results(request, question_id):
    return HttpResponse("These are the results of the question: %s" % question_id)

def vote(request, question_id):
    return HttpResponse("Vote on question: %s" % question_id)