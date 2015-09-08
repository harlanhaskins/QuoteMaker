from .models import *
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from path_maker import *

def quote(request, path):
    quotemaker = get_object_or_404(QuoteMaker, pk=decode_id(path), active=True)
    count = request.GET.get('count', '1')
    if not count.isdigit():
        return HttpResponse({'message', 'count must be a number'}, 412)
    count = min(int(count), 100)
    quotes = []
    for i in range(count):
        quotes.append(quotemaker.new_string())
    return JsonResponse({'quotes': quotes})
