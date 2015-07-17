from django.shortcuts import render, render_to_response, HttpResponse
from django.template import RequestContext
from gpesq.models import Plans
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

def index(request, p_count=None):
    '''main page'''
    plans = Plans.objects.select_related('points').all()
    context = {
        'title': 'G.P. Esquire',
        'plans': plans,
    }
    return render_to_response('home.html', context,
                              context_instance=RequestContext(request))
@csrf_exempt
def add_point(request, method='POST'):
    """takes client call with gps data and saves it to the server db"""
    if request.METHOD == 'POST':
        data = json.loads(request.body)
        #save point
        response = json.dumps({'success': '1', 'error': ''})
        return HttpResponse(response, content_type='application/json')
