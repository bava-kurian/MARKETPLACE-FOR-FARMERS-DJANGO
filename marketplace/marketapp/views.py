from django.shortcuts import render,redirect
from . import models
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

class BaseView(TemplateView):
    
    template_name='base.html'
    
'''class FarmerLoginView(CreateView):
    
    model=models.User
    template_name='farmer_login.html'
    '''

def IndexView(request):
    return render(request,"index.html");

class UserRegisterView(FormView):
    template_name='registration/user_registration.html'
    form_class=UserCreationForm
    redirect_authenticated_user=True
    success_url=reverse_lazy('index')
    
    def form_valid(self, form):
        user=form.save()
        if user is not None:
            login(self.request,user)
        return super(UserRegisterView,self).form_valid(form)
    def get(self,*args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        return super(UserRegisterView,self).get(*args,**kwargs)
@login_required
def UserLogoutConfirm(request):
    return render(request,'registration/logout_confirm.html');


