from django.urls import path
from profiles_api import views

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),                          # After we browse our server with "/api/hello-view/" views.HelloApiView.as_view()) it will
]                                                                               # call get function from HelloApiView class at views.py (check urls.py from profiles_project).
