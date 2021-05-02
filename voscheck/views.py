from django.shortcuts import render
from django.views import generic

# class IndexView(generic.FormView):
#     template_name = 'voscheck/index.html'
def index(request):
    return render(request, 'voscheck/index.html')

def login(request):
    return render(request, 'voscheck/login.html')

def logout(request):
    if not request.session.get('is_login', None):
        return redirect("login/")
    request.session.flush()
    redirect("login/")