from django.shortcuts import render
from .models import Message
from random import choice


# Create your views here.
def index(request):
    if request.method == 'GET':
        context = {"message": "",
                   "is_response": False}
        return render(request, "index.html", context)
    if request.method == 'POST':
        # return random message
        # we do this before saving the user's message
        # to avoid showing their own message
        try:
            pks = Message.objects.values_list('pk', flat=True)
            random_pk = choice(pks)
            random_msg = Message.objects.get(pk=random_pk)
            random_msg = random_msg.message_text
        except IndexError as e:
            random_msg = "You are a special person :)"

        message_text = request.POST.get('message')
        message = Message(message_text=message_text)
        message.save()

        context = {"message": random_msg,
                   "is_response": True}
        return render(request, "index.html", context)
