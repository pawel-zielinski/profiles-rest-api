from django.urls import path, include                                           # Include is used for including lists of URLs in the URL pattern and assigning the lists to a secific URL.
from profiles_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name = 'hello-viewset')# 1st arg - name of the URL, 2nd arg - ViewSet that we want to register to this URL, 3rd arg - base name
                                                                                # (will be used for retrieving the URLs in our router if we ever need to do that using the URL retrieving
                                                                                # function provided by Django).

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls)),                                             # The reaseon we specify '' as 1st arg in path func. is that we do not want to put prefix to this URL.
]                                                                               # After we browse our server with "/api/hello-view/" views.HelloApiView.as_view()) it will
                                                                                # call get function from HelloApiView class at views.py (check urls.py from profiles_project).
