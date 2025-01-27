from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.forms import ModelForm
from .models import Profile,Skills

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] 
        labels = {'username': 'Name'}


class ProfileForm(ModelForm):
    class Meta:
        model=Profile
        fields='__all__'

class SkillForm(ModelForm):
    class Meta:
        model=Skills
        fields='__all__'
        exclude=['owner']