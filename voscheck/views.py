from django.shortcuts import render
from django.views import generic

# class IndexView(generic.FormView):
#     template_name = 'voscheck/index.html'
def index(request):
    print('hello')
    return render(request, 'voscheck/index.html')