from django.contrib.auth import (
    authenticate,
    login,
    logout,
)
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views import View
from users.forms import UserRegisterForm

from django.contrib.auth.forms import AuthenticationForm

class LoginView(View):
    form_class = AuthenticationForm
    template_name = 'home/login.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
        return render(request, self.template_name, {'form': form})
       
class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('login')

class RegisterView(View):
    form_class = UserRegisterForm
    template_name = 'home/register.html' 

    def get(self, request):
        form = self.form_class()
        return render(
            request,
            self.template_name,
            {'form': form}
        )
    
    def post(self, request):
        form=self.form_class(request.POST)
        if form.is_valid():
            user=form.save()
            login (request,user)
            return redirect('index')

        return render(
            request,
            self.template_name,
            {'form': form}
        )

#tiene que estar logeado para entrar si o si, sino vuelve al login

@login_required(login_url='login')
def index_view(request):
    return redirect('vehiculo_list')
