from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm


def signup(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'New user "{username}" registered.')
            return redirect('login')

        messages.error(request, 'Some issues were found with the information you entered.')

    return render(request, 'accounts/signup.html', {
        'form': form,
    })


def login_view(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )

            if user is not None:
                auth_login(request, user)
                messages.success(request, f'Welcome back, {user.username}.')
                next_url = request.GET.get('next', 'messages:inbox')
                return redirect(next_url)

            messages.error(request, 'Username and password do not match.')
        else:
            messages.error(request, 'Some issues were found with the information you entered.')

    return render(request, 'accounts/login.html', {
        'form': form,
    })


@login_required
def logout_view(request):
    auth_logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')