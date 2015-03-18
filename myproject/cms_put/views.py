from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseNotFound
from models import Page

@csrf_exempt
def processCmsRequests(request, resource):
    if request.method == 'GET':
        try:
            page = Page.objects.get(name = resource)
            return HttpResponse(page.page)
        except Page.DoesNotExist:
            return HttpResponseNotFound("Page not found")
    elif request.method == 'PUT':
        newPage = Page(name = resource, page = request.body)
        newPage.save()
        return HttpResponse("Added to the list")
    else:
        return HttpResponse(status=403)
