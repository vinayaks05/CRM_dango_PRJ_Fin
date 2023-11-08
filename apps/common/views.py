from django.shortcuts import render


from django.http import HttpResponse
# Create your views here.
from django.views.generic import TemplateView, CreateView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# import signup form
from .forms import SignUpForm

from django.urls import reverse_lazy

class HomeView(TemplateView):
    template_name = 'common/home.html'

class BaseView(TemplateView):
    template_name = 'common/base.html'

#class DashboardView(TemplateView):
#    template_name = 'common/dashboard.html'

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'common/dashboard.html'
    login_url = reverse_lazy('home')


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('home')
    template_name = 'common/signup.html'

class ContactView(TemplateView):
    template_name = 'common/contacts.html'

class MessageView(TemplateView):
    template_name = 'common/message.html'

def whatsappData(Ph,Message):
    import time
    import webbrowser as web
    import pyautogui as pg
    Phone = "+91" + Ph
    web.open('https://web.whatsapp.com/send?phone='+Phone+'&text='+Message)
    time.sleep(30)
    pg.press('enter')

def SendMessage(request):
    if request.method == 'POST':
        Ph = request.POST['Phone']
        Message = request.POST['Message']
        #print(Ph, Message)
        whatsappData(Ph, Message)
        msg = "Message has been sent"
        return render(request, "commons/message.html", {'msg':msg})
    else:
        return HttpResponse("<h1> 404 not found </h1>")
