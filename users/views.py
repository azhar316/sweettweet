from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout

from .models import User, UserProfile
from .forms import UserProfileUpdateForm, UserRegisterForm, UserLoginForm


class UserRegisterView(generic.FormView):

    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:user_detail')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('users:user_detail')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password2')
        full_name = form.cleaned_data.get('full_name')
        user, user_profile = UserProfile.objects.create_user_and_profile(full_name=full_name,
                                                                         username=username,
                                                                         email=email,
                                                                         password=password)
        login(self.request, user)
        return super().form_valid(form)


class UserLoginView(generic.FormView):

    form_class = UserLoginForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('users:user_detail')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('users:user_detail')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            error_message = 'username and password do not match'
            return render(self.request, self.template_name,
                          {'form': form, 'error_message': error_message})
        login(self.request, user)
        return super().form_valid(form)


def log_out(request):
    logout(request)
    return redirect('/')


class UserProfileDetailView(LoginRequiredMixin, generic.DetailView):

    template_name = 'users/profile_detail.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return UserProfile.objects.get(user=self.request.user)


class UserProfileUpdateView(LoginRequiredMixin, generic.View):

    form_class = UserProfileUpdateForm
    template_name = 'users/profile_update.html'
    success_url = reverse_lazy('users:user_detail')

    def get(self, *args, **kwargs):
        user = self.request.user
        form = self.form_class(initial={

            'full_name': user.profile.full_name,
            'username': user.username,
            'email': user.email,
            'bio': user.profile.bio
        })
        print(form)
        return render(self.request, self.template_name, {'form': form})

    def post(self, *args, **kwargs):
        user = self.request.user
        form = self.form_class(self.request.POST)
        if form.is_valid():
            user.username = form.cleaned_data.get('username')
            user.email = form.cleaned_data.get('email')
            user.profile.full_name = form.cleaned_data.get('full_name')
            user.profile.bio = form.cleaned_data.get('bio')
            user.profile.avatar = form.cleaned_data.get('avatar')
            user.save()
        else:
            raise ValidationError("Invalid form data")
        return redirect(self.success_url)
