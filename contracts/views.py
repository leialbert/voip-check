from django.shortcuts import render

# Create your views here.
def index(request):
    '''
    营业执照和合同管理
    '''
    return render(request,'contracts/index.html')