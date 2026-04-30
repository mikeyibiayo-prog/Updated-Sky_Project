# Imports Django form tools.
from django import forms

# Imports Django's built-in form for creating users.
from django.contrib.auth.forms import UserCreationForm

# Imports Django's built-in User model.
from django.contrib.auth.models import User


# Custom signup form used by the signup page.
class CustomUserCreationForm(UserCreationForm):
    # Adds an email field to the normal Django user creation form.
    email = forms.EmailField(required=True)

    class Meta:
        # Tells the form to use Django's User model.
        model = User

        # Fields shown on the signup form.
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        # Runs the original UserCreationForm setup first.
        super().__init__(*args, **kwargs)

        # Adds Bootstrap styling to all form fields.
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control'
            })