from django.shortcuts import render, render_to_response
from django.template import RequestContext

# Create your views here.

def index(request, p_count=None):
    '''main page'''

    context = {
        'title': 'G.P. Esquire',
    }
    return render_to_response('home.html', context,
                              context_instance=RequestContext(request))
