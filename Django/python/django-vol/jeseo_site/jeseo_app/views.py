from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect

articles = {
    'sports':"Sports page",
    'politic':"Politic page",
    'finance':"Finance page",
}

def news_view(request, topic):
    try:
        result = articles[topic]
        return (HttpResponse(result))
    except:
        raise (Http404("404 GENERIC ERROR"))

def news_num_view(request, num):
    try:
        topics = list(articles.keys())
        return HttpResponseRedirect(topics[num])
    except:
        raise (Http404("404 GENERIC ERROR"))

def plus_view(request, num1, num2):
    result = ("{} + {} = {}".format(num1, num2, num1 + num2))
    return (HttpResponse(result))