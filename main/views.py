from django.shortcuts import render

from .models import Dialogue


def index(request):
    if request.method == 'POST':
        context = create_context(request)
        return render(request, 'main/index.html', context)
    else:
        message = Dialogue.objects.all()
        return render(request, 'main/index.html', {'messages': message})


def create_context(request):
    text = request.POST.get('message')

    dialogue = Dialogue()

    dialogue.text = text
    dialogue.author = request.user
    dialogue.save()

    messages = Dialogue.objects.all()

    context = {
        'messages': messages
    }
    return context
