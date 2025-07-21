from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Question, Choice

#  this is done to query the database and get the data we need to display in our views

# Create your views here.

# Get questions and display them in the index view

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5] # this queries the database for the latest 5 questions ordered by publication date
    context = {'latest_question_list' : latest_question_list}    # this creates a context dictionary that will be passed to the template}
    return render(request, 'polls/index.html', context)

# Show specific questions and choices 

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

# Get question and display results. 

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question':question})

# Vote for a choice in a question

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form with an error message 
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1  # Increment the vote count for the selected choice
        selected_choice.save()  # Save the updated choice back to the database
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    
 


