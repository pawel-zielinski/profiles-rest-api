from django.urls import path, include                                           # Include is used for including lists of URLs in the URL pattern and assigning the lists to a secific URL.
from profiles_api import views
from rest_framework.routers import DefaultRouter                                # basename instead of base_name for newer versions of Django (9.11)

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name = 'hello-viewset')# 1st arg - name of the URL, 2nd arg - ViewSet that we want to register to this URL, 3rd arg - base name
                                                                                # (will be used for retrieving the URLs in our router if we ever need to do that using the URL retrieving
                                                                                # function provided by Django).
router.register('profile', views.UserProfileViewSet)                            # 1st arg - the name of the ViewSet, 2nd arg - link this view to UserProfileViewSet from views.py.
                                                                                # Unlike the HelloViewSet that we have registered previously we do not need to specify a base_name argument
                                                                                # and this is because we have in our ViewSet a queryset object. If you provide the queryset then Django REST
                                                                                # Framework can figure out the name from the model that is assigned to it. So you only need to specify the
                                                                                # base_name if you are creating a ViewSet that does not have a queryset or if you want to override
                                                                                # the name of the queryset that is associated to it.
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),                                             # The reaseon we specify '' as 1st arg in path func. is that we do not want to put prefix to this URL.
]                                                                               # After we browse our server with "/api/hello-view/" views.HelloApiView.as_view()) it will
                                                                                # call get function from HelloApiView class at views.py (check urls.py from profiles_project).
