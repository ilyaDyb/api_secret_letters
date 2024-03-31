import re
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import uuid
import json
from api.models import Letters

from users.models import User


@csrf_exempt
def create_letter(request):
    if request.method == "POST":
        text_letter = request.POST.get("text")
        password = request.POST.get("password")
        api_key = request.POST.get("api_key")
        if not text_letter:
            return render(request, "api_response.html", context=
                        {"response": json.dumps([{"status": "error", "warning": 'missing required argument text'}])})
        if not text_letter:
            return render(request, "api_response.html", context=
                        {"response": json.dumps([{"status": "error", "warning": 'missing required argument api_key'}])})
        
        if not User.objects.filter(api_key=api_key).exists():
            return render(request, "api_response.html", context=
                        {"response": json.dumps([{"status": "error", "warning": 'invalid api_key'}])})
        
        id_letter = str(uuid.uuid4())
        Letters.objects.create(letter_id=id_letter, text=text_letter, password=password)

        response = json.dumps([{"status": "success","password":password, "text": text_letter, "id": id_letter}])
        clean_response = re.sub(r'(\w+):', r'"\1":', response)
        

        json_response = json.loads(clean_response)
    
        return render(request, "api_response.html", context={"response": json.dumps(json_response)})
    else:
        return render(request, "api_response.html", context=
                        {"response": json.dumps([{"status": "error", "warning": 'invalid method'}])})


@csrf_exempt
def read_letter(request):
    if request.method == "POST":
        letter_id = request.POST.get("id")
        password = request.POST.get("password")
        print(letter_id, password)
        try:
            letter = Letters.objects.get(letter_id=letter_id, password=password)
            letter_text = letter.text
            if letter.letter_id != "697fae81-569f-42fc-8ea8-87d77a5875c4":
                letter.delete()

            return render(request, "api_response.html", context={"response": json.dumps([{"status": "success", "text": letter_text}])})
        except Exception as e:
            return render(request, "api_response.html", context=
                {"response": json.dumps([{"status": "error", "warning": f'{e}'}])})
    else:
        return render(request, "api_response.html", context=
                {"response": json.dumps([{"status": "error", "warning": 'invalid method'}])})


