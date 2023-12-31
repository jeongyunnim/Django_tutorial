from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound

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
        result = "Sorry, {} Page not found.".format(topic)
        return (HttpResponseNotFound(result))

def plus_view(request, num1, num2):
    result = ("{} + {} = {}".format(num1, num2, num1 + num2))
    return (HttpResponse(result))