from django import forms
from .models import Exercise, User

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = '__all__'
        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'