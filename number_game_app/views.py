from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import random

target = random.randint(1, 100)
turn = 0
success = False

@csrf_exempt
def root(request):
    global target, turn, success
    context = {}
    hint = ''
    guessed_number = None

    if request.method == 'POST' and request.POST.get('guess_number'):
        guessed_number = int(request.POST['guess_number'])
        turn += 1
        if guessed_number == target:
            success = True
        else:
            if(guessed_number > target):
                hint = 'Too high!'
            else:
                hint = 'Too low!'
    else:
        target = random.randint(1, 100)
        turn = 0
        success = False
        guessed_number = None

    context['success'] = success
    context['turn'] = turn
    context['hint'] = hint
    context['guessed_number'] = guessed_number

    return render(request, 'index.html', context)
