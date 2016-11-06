from django.http import HttpResponse
from .models import Links

def index(request):
    all_links = Links.objects.values_list('id', 'page_id','link')
    output = ','.join( [ q.link for q in all_links] )
    return HttpResponse(output)
