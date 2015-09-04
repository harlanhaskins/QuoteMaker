from .models import *
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse

def quote(request, path):
    character = get_object_or_404(Homestarkov, path=path)
    count = request.GET.get('count', '1')
    if not count.isdigit():
        return HttpResponse({'message', 'count must be a number'}, 412)
    count = min(str(count), 100)
    quotes = []
    for i in range(count):
        quotes.append(character.new_string())
    return JsonResponse({'quotes': quotes})
