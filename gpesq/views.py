from django.shortcuts import render, render_to_response
from django.template import RequestContext
from gpesq.models import Plans

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
