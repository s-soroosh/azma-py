from django.shortcuts import render
from wage_meter import models
from django.core import serializers
from django.forms.models import model_to_dict
from django.http import HttpResponse,HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt  # # @csrf_exempt it can disable CSRF checking for debug purposes

def _convert_for_json(objects):
    if(len(objects)>1):
        items = "[ "
        items += objects[0].json_format()
        for obj in objects:
            items += ','
            items += obj.json_format()
        items += " ]"
        return items
    if(len(objects)==1):
        return objects[0].json_format()
    if(len(objects)==0):
        return '{}'

@csrf_exempt
def get_islands(request):
    islands = models.Island.objects.all()
    res = _convert_for_json(islands)
    response_result = HttpResponse("", content_type='application/json; charset=utf-8')
    response_result.write(res)
    response_result['Content-Length'] = len(res)
    return HttpResponse(response_result)


@csrf_exempt
def get_technology_by_island(request):
    selected_island = request.POST['island']
    print(selected_island)
    if selected_island is None:
        return HttpResponseNotFound()
    technologies = models.Technology.objects.filter(island=selected_island)
    res = _convert_for_json(technologies)
    response_result = HttpResponse("", content_type='application/json; charset=utf-8')
    response_result.write(res)
    response_result['Content-Length'] = len(res)
    return HttpResponse(response_result)


@csrf_exempt
def get_technology_by_parent_technology(request):
    selected_technology = request.POST['technology']
    if selected_technology is None:
        return HttpResponseNotFound()
    technologies = models.Technology.objects.filter(parent=selected_technology)
    res = _convert_for_json(technologies)
    response_result = HttpResponse("", content_type='application/json; charset=utf-8')
    response_result.write(res)
    response_result['Content-Length'] = len(res)
    return HttpResponse(response_result)




