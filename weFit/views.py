import pkgutil
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from rest_framework import generics

from .serializers import UserSerializer, ExerciseSerializer
from .models import User, Exercise
from .forms import ExerciseForm, UserForm

#from .forms import CategoryForm, WorkoutForm, ExerciseForm

class ExerciseList(generics.ListCreateAPIView):
    serializer_class = ExerciseSerializer
    
    def get_queryset(self):
        queryset = Exercise.objects.all()
        workout = self.request.query_params.get('workout')
        if workout is not None:
            queryset = queryset.filter(exerciseWorkout = workout)
        return queryset
    
class ExerciseDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExerciseSerializer
    queryset = Exercise.objects.all()
    
class UserList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


def signup(request):
    if request.method == "GET":
        form = UserForm()
        return render(request, "auth/signup.html", {'form':form})
    else: 
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
    
    """if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
    else:
        initial_data = {'username':'','email':'','height':'','weight':'','password':'','cpassword':''}
        form = UserCreationForm(initial = initial_data)
    return render(request, 'auth/signup.html',{'form':form})"""

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('home')
    else:
        initial_data = {'username':'','password':''}
        form = AuthenticationForm(initial = initial_data)
    return render(request, 'auth/signin.html',{'form':form})

def profile(request):
    return

def logout_view(request):
    logout(request)
    return redirect('login')



def registration(request): 
    return render(request, "registration.html")

def login_view(request):
    return render(request, "login.html")

def home(request):
    return render(request, "home.html")

def workout(request):
    return render(request, "workout.html")

def administrator(request):
    showall = Exercise.objects.all()
    return render(request, "admin.html", {"data":showall})

def arms(request):
    exercise = Exercise.objects.all()
    return render(request,"arms.html", {'exercises':exercise} )

def stomach(request):
    exercise = Exercise.objects.all()
    return render(request,"stomach.html", {'exercises':exercise} )

def back(request):
    exercise = Exercise.objects.all()
    return render(request,"back.html", {'exercises':exercise} )

def waist(request):
    exercise = Exercise.objects.all()
    return render(request,"waist.html", {'exercises':exercise} )

def buttocks(request):
    exercise = Exercise.objects.all()
    return render(request,"buttocks.html", {'exercises':exercise} )

def thigh(request):
    exercise = Exercise.objects.all()
    return render(request,"thigh.html", {'exercises':exercise} )

def legs(request):
    exercise = Exercise.objects.all()
    return render(request,"legs.html", {'exercises':exercise} )

def full_body(request):
    exercise = Exercise.objects.all()
    return render(request,"full_body.html", {'exercises':exercise} )

"""def exercise(request):
    if request.method=="POST":
        if request.POST.get('exercise_name') and request.POST.get('duration') and request.POST.get('description') and request.POST.get('video_url') and request.POST.get('workout'):
            saverecord = Exercise()
            saverecord.exercise_name = request.POST.get('exercise_name')
            saverecord.duration = request.POST.get('duration')
            saverecord.description = request.POST.get('description')
            saverecord.video_url = request.POST.get('video_url')
            saverecord.workout = request.POST.get('workout')
            saverecord.save()
            messages.success(request, "Exercise "+saverecord.exercise_name+" saved successfully")
            return render(request, "exercise.html")
    else:
            return render(request, "exercise.html")"""
        
def exercise_list(request):
    exercise = Exercise.objects.all()
    return render(request,"exercise_list.html", {'exercises':exercise} )

def exercise_create(request):
    if request.method == "POST":
        form = ExerciseForm(request.POST, request.FILES)
        if form.is_valid():
            exercise = form.save()
            return render("exercise_list.html")
            
    else:
        form = ExerciseForm()
    return render(request, "exercise_form.html", {'form':form})

def exercise_update(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    if request.method == "POST":
        form = ExerciseForm(request.POST, request.FILES, instance=exercise)
        if form.is_valid():
            exercise = form.save()
            return redirect("exercise_list.html", pk=pk)
    else:
        form = ExerciseForm()
    return render(request, "exercise_form.html", {'form':form})

def exercise_delate(request):
    exercise = get_object_or_404(exercise, id=id)
    if request.method == "POST":
        exercise.delete()
        return redirect(exercise_list)
    return render(request, 'exercise_confirm_delete',  {'exercise':exercise} )