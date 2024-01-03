from django.shortcuts import render

def example_view(request):
    return render(request, 'jeseo_app/example.html') 

def variable_view(request):
    return render(request,'jeseo_app/variable.html')