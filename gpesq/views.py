from django.shortcuts import render, render_to_response, HttpResponse
from django.template import RequestContext
from gpesq.models import Plans, Points
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.core.exceptions import ValidationError
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
    if request.method == 'POST':
        data = json.loads(request.body)
        plan_id = data.pop('plan_id')
        plan = Plans.objects.get(id=plan_id)
        p = Points(plan_id=plan, **data)
        p.save()
        response = json.dumps({'success': '1', 'error': ''})
        return HttpResponse(response, content_type='application/json')

    else:
        # for testing in browser
        data_dict = {'lat': '37.123456', 'lon': '-86.345345', 'plan_id': 1, 'meters_error': '3.0'}
        plan_id = data_dict.pop('plan_id')
        plan = Plans.objects.get(id=plan_id)
        p = Points(plan_id=plan, **data_dict)
        try:
            p.full_clean()
            p.save()
            response = json.dumps({'success': '1', 'error': ''})
        except ValidationError:
            response = json.dumps({'success': '1', 'error': 'Invalid field values'})

        return HttpResponse(response, content_type='application/json')
