from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import get_user_model
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
)
from django.shortcuts import redirect
from django.urls import reverse_lazy

from .forms import SignUpForm

# Create your views here.

User = get_user_model()

class SignUpPage(View):
    template_name = 'accounts/sign-up.html'
    def get(self, request):
        form = SignUpForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password2')
            user = User.objects.create(username=username)
            user.set_password(password)
            user.save()
            return redirect('sign-in')
        return render(request, self.template_name, {'form': form})

class SignInPage(LoginView):
    template_name = 'accounts/sign-in.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('task-list')

class SignOutPage(LogoutView):
    next_page = 'home'