# Imports path to create url routes.
from django.urls import path

# Imports Django's built-in authentication views for password reset.
from django.contrib.auth import views as auth_views

# Imports views from this accounts app.
from . import views

# Url routes for account features.
urlpatterns = [
    path('signup/', views.signup, name='signup'),  # signup page
    path('login/', views.login_view, name='login'),  # login page
    path('logout/', views.logout_view, name='logout'),  # logout action

    # Password reset request page.
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='accounts/password_reset_form.html',
        email_template_name='accounts/password_reset_email.html',
        success_url='/accounts/password-reset/done/'
    ), name='password_reset'),

    # Page shown after the password reset email is sent.
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'
    ), name='password_reset_done'),

    # Page where the user enters a new password using the reset link.
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html',
        success_url='/accounts/reset/done/'
    ), name='password_reset_confirm'),

    # Page shown after the password has been reset successfully.
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'
    ), name='password_reset_complete'),
]