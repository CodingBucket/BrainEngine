from django.http import HttpResponse
from .models import Links

def index(request):
    all_albums = Links.objects.all()
    return HttpResponse(all_albums)