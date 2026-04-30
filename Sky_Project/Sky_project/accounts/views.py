# Imports render for showing templates and redirect for moving users after actions.
from django.shortcuts import render, redirect

# Imports Django messages to show success and error feedback.
from django.contrib import messages

# Imports authentication functions for login and logout.
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

# Imports Django's built-in login form.
from django.contrib.auth.forms import AuthenticationForm

# Imports login_required to protect views that need a logged-in user.
from django.contrib.auth.decorators import login_required

# Imports the custom signup form.
from .forms import CustomUserCreationForm


# Handles user signup.
def signup(request):
    # Creates a blank signup form for GET requests.
    form = CustomUserCreationForm()

    if request.method == 'POST':
        # Fills the form with submitted user data.
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            # Saves the new user account.
            form.save()

            # Gets the username to show a success message.
            username = form.cleaned_data.get('username')

            # Shows feedback after successful registration.
            messages.success(request, f'New user "{username}" registered.')

            # Sends the user to the login page after signup.
            return redirect('login')

        # Shows an error if the form is not valid.
        messages.error(request, 'Some issues were found with the information you entered.')

    return render(request, 'accounts/signup.html', {
        'form': form,
    })


# Handles user login.
def login_view(request):
    # Creates a blank login form.
    form = AuthenticationForm()

    if request.method == 'POST':
        # Fills the login form with submitted data.
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            # Checks the username and password.
            user = authenticate(
                request,
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )

            if user is not None:
                # Logs the user into the system.
                auth_login(request, user)

                # Shows a success message after login.
                messages.success(request, f'Welcome back, {user.username}.')

                # Sends the user to the page they originally wanted, or inbox by default.
                next_url = request.GET.get('next', 'messages:inbox')
                return redirect(next_url)

            # Shows an error if authentication fails.
            messages.error(request, 'Username and password do not match.')
        else:
            # Shows an error if the form has validation issues.
            messages.error(request, 'Some issues were found with the information you entered.')

    return render(request, 'accounts/login.html', {
        'form': form,
    })


# Logs the user out.
@login_required
def logout_view(request):
    # Ends the user session.
    auth_logout(request)

    # Shows feedback after logout.
    messages.success(request, 'You have been logged out.')

    # Sends the user back to the login page.
    return redirect('login')