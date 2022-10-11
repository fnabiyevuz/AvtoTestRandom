from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
import random
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required()
def index(request):
    if request.method=="POST":
        quan = int(request.POST['quantity'])
        items = list(Questions.objects.all())
        # change quan to how many random items you want
        random_items = random.sample(items, quan)
        # if you want only a single random item
        # random_item = random.choice(items)
        quiz = Quizs.objects.create(participant=request.user, quantity=quan)
        print(random_items)

        for i in random_items:
            AnswersOfParticipant.objects.create(quiz=quiz, question=i)

        # question = AnswersOfParticipant.objects.filter(quiz=quiz, answer=False)

        # return render(request, 'question.html', {'question':question})
        return redirect('/question/')
    else:
        context = {
            'quizs':Quizs.objects.filter(participant=request.user).order_by('-id'),
            'count':Questions.objects.all().count(),
            'open':Quizs.objects.filter(participant=request.user, is_finished=False)
        }
        return render(request, 'index.html', context)

@login_required()
def question(request):
    
    if request.method == "POST":
        question = request.POST['question']
        answer = request.POST['answer']
        que = AnswersOfParticipant.objects.get(id=question)
        ans = Answers.objects.get(id=answer)
        que.answer=ans
        que.save()
        if ans.status:
            que.quiz.true += 1
        else:
            que.quiz.false += 1
        que.quiz.percentage = (que.quiz.true / que.quiz.quantity)*100
        que.quiz.save()
        return redirect('/question/')
    else:
        question = AnswersOfParticipant.objects.filter(quiz__participant=request.user, answer=None).first()
        if question is not None:
            items = list(question.question.ans_que.all())
            # change 3 to how many random items you want
            random_items = random.sample(items, len(question.question.ans_que.all()))
            # if you want only a single random item
            return render(request, 'question.html', {'question':question, 'answers':random_items, 'quiz':question.quiz})
        else:
            quiz = Quizs.objects.get(participant=request.user, is_finished=False)
            quiz.is_finished=True
            quiz.save()
            return redirect('/')            

@login_required()
def view(request):
    q = request.GET['q']
    try:
        quiz = Quizs.objects.get(id=q)
    except:
        return redirect('/')
    if quiz.participant == request.user:
        ansof = quiz.answer_quizs.all()

        context = {
            'ansof':ansof
        }
        return render(request, 'view.html', context)
    else:
        return redirect('/')


def Login(request):

    if request.method == 'POST':
        r = request.POST
        username = r['username']
        password = r['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/login/')
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        r = request.POST
        username = r['username']
        password = r['password']
        first_name = r['first_name']
        last_name = r['last_name']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/register/')
        else:
            User.objects.create(username=username, password=make_password(password), first_name=first_name, last_name=last_name)
            return redirect('/login/')
    else:
        return render(request, 'register.html')

def LogOut(request):
    logout(request)
    return redirect('/login/')