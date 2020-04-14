from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import UnicodeUsernameValidator

from .models import User, UserProfile


class UserCreationForm(forms.ModelForm):
    """A form for creating new users in admin site. Includes all the required fields,
    plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email',)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating user in admin site. Includes all the fields on the
    user, but replaces password field with admin's hashed password
    display field."""
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('username', 'email', 'is_active', 'is_staff', 'is_superuser')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field because the field
        # does not have access to the initial value
        return self.initial["password"]


class UserRegisterForm(forms.Form):

    full_name = forms.CharField(max_length=100, required=True)
    username = forms.CharField(
        max_length=150,
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        validators=[UnicodeUsernameValidator()],
        required=True
    )
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username is already taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("There is already an account "
                                        "associated with this email")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2


class UserLoginForm(forms.Form):

    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class UserProfileUpdateForm(forms.Form):

    full_name = forms.CharField(max_length=100, required=True)
    username = forms.CharField(
        max_length=150,
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        validators=[UnicodeUsernameValidator()],
        required=True
    )
    email = forms.EmailField(required=True)
    avatar = forms.ImageField(label='profile pic', required=False)
    bio = forms.CharField(max_length=200, required=False,
                          widget=forms.Textarea(attrs={'cols': 40,  'rows': 3}))
