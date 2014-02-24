from django.shortcuts import render
from rest_framework import viewsets,renderers
from wage_meter import models
from django.core import serializers
from django.forms.models import model_to_dict
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt  # # @csrf_exempt it can disable CSRF checking for debug purposes
from wage_meter.models import Island,Technology
from wage_meter.serializers import IslandSerializer,TechnologySerializer
from django.template import RequestContext, loader

class IslandViewSet(viewsets.ModelViewSet):
    queryset = Island.objects.all()
    serializer_class = IslandSerializer


def main(request):
    template = loader.get_template('main.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))


@csrf_exempt
def tech(request):
    if 'island' in request.POST:  # # load Technologies by Islands
        t = all_technologies = Technology.objects.all().extra(where=['island_id=%s'], params=[request.POST['island']])
    elif 'tech' in request.POST:  # # load Technologies by related Technologies
        t = Technology.objects.filter(parent__id=request.POST['tech'])
    else: return HttpResponseBadRequest()
    s = TechnologySerializer(t, many=True)
    response_obj = HttpResponse(renderers.JSONRenderer().render(s.data))
    response_obj['Content-Type'] = 'application/json'
    return response_obj
