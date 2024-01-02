from django.shortcuts import render

def example_view(request):
    # 여기에 있는 jeseo_app은 현재 앱 디렉토리를 가리키지 않는다. jeseo_app/templates/jeseo_app/example.html
    return render(request, 'jeseo_app/example.html') 

def variable_view(request):
    my_var = {
        'first_name':'Jeong yun',
        'last_name':'Seo',
        'some_list':[1,2,3],
        'some_dict':{'inside_key':'inside_value'}
    }
    return render(request,'jeseo_app/variable.html', context=my_var)