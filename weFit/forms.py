from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Exercise, User

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = '__all__'
        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'height', 'weight')

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}))

"""class UserWorkoutForm(forms.ModelForm):
    class Meta:
        model = UserWorkout 
        fields = ['workout','time_spent']

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name','description','level','duration','calory','video']"""