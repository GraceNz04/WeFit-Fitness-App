from django.urls import path, include

from . import views

# Namespacing:
# app_name = main
urlpatterns = [
    path("signup/", views.signup, name='signup'),
    path("signin/", views.signin, name='signin'),
    path("login/", views.login_view, name='login'),
    path("logout/", views.logout_view, name='logout'),
    path("signin/", views.profile, name='profile'),
    path("home/", views.home, name="home"),
    path("workout/", views.workout, name="workout"),
    path("exercise_list/", views.exercise_list, name="exercise_list"),
    path("exercise_form/", views.exercise_create, name='exercise_form'),
    path("exercise_update/<int:pk>/", views.exercise_update, name='exercise_update'),
    path("arms/", views.arms, name="arms"),
    path("back/", views.back, name="back"),
    path("stomach/", views.stomach, name="back"),
    path("waist/", views.waist, name="back"),
    path("buttocks/", views.buttocks, name="back"),
    path("thigh/", views.thigh, name="back"),
    path("legs/", views.legs, name="back"),
    path("full_body/", views.full_body, name="back")
]
