from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.utils.timezone import now

def public_api(request):
    data = {
        "email": "neluwah@gmail.com",
        "current_datetime": now().isoformat(),
        "github_url": "https://github.com/nobleenia/hng-api.git"
    }
    return JsonResponse(data)
