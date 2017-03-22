from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import Score

# Create your views here.
def index(request):
    scores = Score.objects.order_by("-score")[0:10]
    return render(request, 'highscore/index.html', {"scores":scores})

def submit(request):
    if request.method != 'POST':
        return redirect('/')
    else:
        submit_score = Score.objects.validate(request.POST)
        if "errors" in submit_score:
            for error in submit_score["errors"]:
                messages.info(request, error)
        return redirect('/api/scores')

def scoresJson(request):
    scores = Score.objects.order_by("-score").values('initials','score')[0:10]
    return JsonResponse(list(scores), safe=False)

def byRank(request, rank):
    score = Score.objects.order_by("-score").values('initials','score')[int(rank)-1]
    return JsonResponse(score, safe=False)
