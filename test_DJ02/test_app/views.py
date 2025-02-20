from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'test_app/index.html')
def nic_1(request):
    render(request, 'test_app/nic_1.html')
def alex_2(request):
    render(request, 'test_app/alex_2.html')
def alex_3(request):
    render(request, 'test_app/alex_3.html')
def nic_2(request):
    render(request, 'test_app/nic_2.html')


