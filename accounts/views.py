from django.shortcuts import render
from django.http import HttpRequest,HttpResponse


# Create your views here.
def index(request):
    '''
    请求vos接口，获取详细的账户信息情况，点击首页后自动更新账户信息模型
    '''
    
    return render(request,'accounts/index.html')