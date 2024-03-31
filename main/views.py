from django.shortcuts import render
import uuid


def index(request):
    return render(request, "main/index.html")


def api_key(request):
    user = request.user

    if user.is_authenticated:
        api_key = user.api_key
        if not api_key:
            user.api_key = uuid.uuid4()
            user.save()
    else:
        api_key = None
    return render(request, "main/api_key.html", context={"api_key": api_key})