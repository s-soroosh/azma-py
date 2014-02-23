from django.shortcuts import render
from rest_framework import viewsets
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



# it's not nice but i spend a lot of time for it :-|
# i can't use django methods like extra or select_related very well yet but i will keep trying :)
@csrf_exempt
def tech(request):
    if('island' in request.POST):  # # load Technologies by Islands
        t = list(Technology.objects.raw('SELECT * FROM wage_meter_technology WHERE island_id=%s',[request.POST["island"]]))
    elif('tech' in request.POST):  # # load Technologies by related Technologies
        t = list(Technology.objects.
        raw('SELECT * FROM `wage_meter_technology` WHERE `id` in (SELECT `to_technology_id` from `wage_meter_technology_parent` where `from_technology_id` = %s)',
            [request.POST["tech"]]))
    else: return HttpResponseBadRequest()
    s = TechnologySerializer(t, many=True)
    response_obj = HttpResponse(s.data)
    response_obj['Content-Type'] = 'application/json'
    return response_obj
