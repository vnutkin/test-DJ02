from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'test_app/index.html')
def nic_1(request):
    data ={'card_img':'nic1.jpg', 'card_name':'Николай I (Николай Павлович)',
           'card_life':'25 июня (6 июля) 1796 г. - 18 февраля (2 марта) 1855 г.',
           'card_imp':'1825–1855 гг.',
           'card_cur':'Консервативный правитель, укрепивший самодержавие и бюрократический аппарат. Подавил восстание декабристов и усилил цензуру. При нем проведена кодификация законов (Свод законов Российской империи). Неудачи: поражение в Крымской войне (1853–1856), выявившее отсталость России.'
}
    render(request, 'test_app/nic_1.html', data)
def alex_2(request):
    render(request, 'test_app/alex_2.html')
def alex_3(request):
    render(request, 'test_app/alex_3.html')
def nic_2(request):
    render(request, 'test_app/nic_2.html')


